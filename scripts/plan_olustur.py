"""plan/proje-plani.json dosyasından proje planı belgesini üretir.

Çıktı: docs/03-proje-plani-sprint-ve-kanban.md
Kullanım: python scripts/plan_olustur.py [--bugun YYYY-MM-DD]
"""
import argparse
import json
from datetime import date, timedelta
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
PLAN = KOK / "plan" / "proje-plani.json"
CIKTI = KOK / "docs" / "03-proje-plani-sprint-ve-kanban.md"


def t(s):
    return date.fromisoformat(s)


def tr(d):
    return d.strftime("%d.%m.%Y")


def yukle():
    return json.loads(PLAN.read_text(encoding="utf-8"))


def sprintler(v):
    bas, son, gun = t(v["sprint_baslangic"]), t(v["sprint_son"]), v["sprint_gun"]
    liste, i = [], 1
    while bas <= son:
        liste.append({"no": i, "bas": bas, "bit": bas + timedelta(days=gun - 1)})
        bas += timedelta(days=gun)
        i += 1
    return liste


def sprint_bul(sp, gun):
    for s in sp:
        if s["bas"] <= gun <= s["bit"]:
            return s
    return None


def sprint_ad(s):
    return f"Sprint {s['no']:02d} · {tr(s['bas'])}–{tr(s['bit'])}"


def dogrula(v):
    idx = {g["id"]: g for g in v["gorevler"]}
    uyari = []
    for g in v["gorevler"]:
        if t(g["e"]) < t(g["s"]):
            uyari.append(f"{g['id']}: bitiş başlangıçtan önce")
        for d in g["dep"]:
            if d not in idx:
                uyari.append(f"{g['id']}: bilinmeyen bağımlılık {d}")
            elif t(idx[d]["e"]) > t(g["e"]):
                uyari.append(f"{g['id']}: bağımlılık {d} bu görevden sonra bitiyor")
    return uyari


def uret(bugun):
    v = yukle()
    sp = sprintler(v)
    fazlar = {f["key"]: f for f in v["fazlar"]}
    epikler = {e["id"]: e for e in v["epikler"]}
    tek = v["teknolojiler"]
    gt = v["gorev_teknoloji"]
    gorevler = v["gorevler"]
    for g in gorevler:
        g["_faz"] = epikler[g["epik"]]["faz"]
        g["_sp"] = None if fazlar[g["_faz"]].get("makro") else sprint_bul(sp, t(g["s"]))

    L = []
    a = L.append
    a("# Proje Planı: Makro Plan, Sprintler ve Kanban")
    a("")
    a(f"> Bu belge `plan/proje-plani.json` dosyasından `scripts/plan_olustur.py` ile üretilir. Elle düzenlenmez; plan dosyası güncellenip betik yeniden çalıştırılır. Son üretim: {tr(bugun)}.")
    a("")
    a(f"**Proje:** {v['proje']}")
    a("")
    a(f"**Kurum notu:** {v['kurum_notu']}")
    a("")
    a("**Planlama yaklaşımı:** Proje üç düzeyde planlanmıştır. Makro düzeyde fazlar ve epikler (iş paketleri), mikro düzeyde iki haftalık sprintlere yerleştirilmiş görevler. Faz 0 ve Faz 1 sprint düzeyinde ayrıntılandırılmıştır. Faz 2 ve Faz 3 makro düzeyde planlanmış olup sprint planlaması bir önceki fazın son çeyreğinde yapılacaktır.")
    a("")

    a("## 1. Makro plan: fazlar")
    a("")
    a("| Faz | Başlangıç | Bitiş | Epik | Görev | Planlama düzeyi |")
    a("|---|---|---|---|---|---|")
    for k, f in fazlar.items():
        ep = [e for e in epikler.values() if e["faz"] == k]
        gs = [g for g in gorevler if g["_faz"] == k]
        a(f"| {f['ad']} | {tr(t(f['bas']))} | {tr(t(f['bit']))} | {len(ep)} | {len(gs)} | {'Makro' if f.get('makro') else 'Sprint (mikro)'} |")
    a("")

    a("## 2. Epikler (iş paketleri)")
    a("")
    a("| Epik | Faz | Tarih aralığı | Sprintler | Görev | Amaç |")
    a("|---|---|---|---|---|---|")
    for e in epikler.values():
        gs = [g for g in gorevler if g["epik"] == e["id"]]
        b, s = min(t(g["s"]) for g in gs), max(t(g["e"]) for g in gs)
        sps = sorted({g["_sp"]["no"] for g in gs if g["_sp"]})
        spt = f"S{sps[0]:02d}–S{sps[-1]:02d}" if sps else "Makro"
        a(f"| {e['id']} · {e['ad']} | {fazlar[e['faz']]['ad'].split(' · ')[0]} | {tr(b)} – {tr(s)} | {spt} | {len(gs)} | {e['amac']} |")
    a("")

    a("## 3. Kanban görünümü")
    a("")
    a(f"Görevlerin {tr(bugun)} tarihine göre durumu. GitHub'da aynı durumlar `durum:` etiketleriyle izlenir.")
    a("")
    aktif = sprint_bul(sp, bugun)
    sonraki = sp[aktif["no"]] if aktif and aktif["no"] < len(sp) else None
    devam = [g for g in gorevler if t(g["s"]) <= bugun <= t(g["e"])]
    bu = [g for g in gorevler if aktif and g["_sp"] and g["_sp"]["no"] == aktif["no"] and g not in devam]
    son = [g for g in gorevler if sonraki and g["_sp"] and g["_sp"]["no"] == sonraki["no"]]
    a("| Sütun | Görevler |")
    a("|---|---|")
    a("| Tamamlandı | Araştırma raporu, faz yapısı ve kabul analizi, proje dosyası, sunum ve özet belgesi |")
    a(f"| Devam ediyor | {', '.join(g['id'] for g in devam) or '—'} |")
    a(f"| Bu sprint ({sprint_ad(aktif) if aktif else '—'}) | {', '.join(g['id'] for g in bu) or '—'} |")
    a(f"| Sonraki sprint ({sprint_ad(sonraki) if sonraki else '—'}) | {', '.join(g['id'] for g in son) or '—'} |")
    kalan = len(gorevler) - len(devam) - len(bu) - len(son)
    a(f"| Yapılacak (sonraki sprintler ve makro fazlar) | {kalan} görev |")
    a("")

    a("## 4. Sprint planı (mikro düzey)")
    a("")
    for s in sp:
        gs = [g for g in gorevler if g["_sp"] and g["_sp"]["no"] == s["no"]]
        if not gs:
            continue
        kodlar = sorted({k for g in gs for k in gt[g["id"]]}, key=lambda k: list(tek).index(k))
        a(f"### {sprint_ad(s)}")
        a("")
        a(f"**Başlayan görev:** {len(gs)} · **Kullanılacak teknolojiler:** {'; '.join(tek[k] for k in kodlar)}")
        a("")
        a("| Görev | Epik | Başlangıç | Bitiş | Sorumlu | Teknolojiler | Kabul kriteri |")
        a("|---|---|---|---|---|---|---|")
        for g in gs:
            a(f"| **{g['id']}** {g['t']} | {g['epik']} | {tr(t(g['s']))} | {tr(t(g['e']))} | {g['r']} | {', '.join(tek[k].split(' (')[0] for k in gt[g['id']])} | {g['k']} |")
        a("")

    a("## 5. Faz 2 ve Faz 3 makro görevleri")
    a("")
    a("| Görev | Epik | Başlangıç | Bitiş | Sorumlu | Teknolojiler | Kabul kriteri |")
    a("|---|---|---|---|---|---|---|")
    for g in gorevler:
        if g["_sp"] is None:
            a(f"| **{g['id']}** {g['t']} | {g['epik']} | {tr(t(g['s']))} | {tr(t(g['e']))} | {g['r']} | {', '.join(tek[k].split(' (')[0] for k in gt[g['id']])} | {g['k']} |")
    a("")

    a("## 6. Kritik tarihler")
    a("")
    a("| Tarih | Olay | Kural |")
    a("|---|---|---|")
    for satir in [
        ("11.12.2026", "Online aday firma başvurusu", "Eksik veya hatalı beyan başvurunun yok sayılmasına yol açar"),
        ("≤ 09.02.2027", "Aday komisyon sonucu", "En geç 60 gün; itiraz yolu yok"),
        ("~12.03.2027", "Hakem heyeti sonucu (tahmini)", "21 + 21 gün; salt çoğunluk"),
        ("01.04.2027", "Faz 1 başlangıcı (tahmini)", "Faaliyet onay yazısının tarihi esas alınır"),
        ("Her ayın 20'si", "Aylık muafiyet raporu", "Gecikme aykırı faaliyet sayılır"),
        ("31.01.2028", "Faz 2 başvurusu son tarihi", "Mevcut proje bitmeden en az 60 gün önce"),
        ("29.02.2028", "Revizyon başvurusu için son gün", "Bitişe 30 günden az kala revizyon yapılamaz"),
        ("31.03.2028", "Faz 1 bitişi", "90 gün projesiz kalan firma bölgeden çıkarılır"),
        ("31.05.2028", "2027 yıllık faaliyet raporu", "Mali müşavir onaylı"),
        ("31.12.2028", "4691 sayılı Kanun teşvik süresi sonu (mevcut mevzuat)", "Uzatma kararı izlenmelidir"),
    ]:
        a(f"| {satir[0]} | {satir[1]} | {satir[2]} |")
    a("")

    a("## 7. Teknoloji kataloğu ve kullanım yoğunluğu")
    a("")
    a("Teknoloji seçimlerinin alternatiflerle karşılaştırması ve gerekçeleri: [`docs/04-teknoloji-kararlari.md`](04-teknoloji-kararlari.md).")
    a("")
    a("| Kod | Teknoloji | Görev sayısı | Kullanıldığı ilk sprint |")
    a("|---|---|---|---|")
    for k, ad in tek.items():
        gs = [g for g in gorevler if k in gt[g["id"]]]
        ilk = min((g["_sp"]["no"] for g in gs if g["_sp"]), default=None)
        a(f"| {k} | {ad} | {len(gs)} | {'S%02d' % ilk if ilk else 'Faz 2'} |")
    a("")

    a("## 8. Çalışma kuralları")
    a("")
    for m in [
        "Her görev GitHub'da bir issue'dur; her issue bir epiğe (alt iş olarak) ve bir sprint milestone'una bağlıdır.",
        "Durum etiketleri: `durum: yapılacak` → `durum: bu sprint` → `durum: devam ediyor` → `durum: incelemede` → kapalı.",
        "Bir görev ancak kabul kriteri sağlandığında kapatılır. Sayısal kriterlerde ölçüm sonucu issue'ya yorum olarak eklenir; bu kayıtlar hakem ve denetim için kanıttır.",
        "Sprint başında sprint planlama, sprint sonunda gözden geçirme yapılır; kayan görev bir sonraki sprinte taşınır ve plan dosyası güncellenir.",
        "Kritik yol: ön görüşme ve TTO talebi → başvuru → aday komisyon → hakem → kira → faaliyet onayı → Faz 1 → Faz 2 başvurusu.",
    ]:
        a(f"- {m}")
    a("")
    CIKTI.write_text("\n".join(L) + "\n", encoding="utf-8")
    return len(gorevler), dogrula(v)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--bugun", default=date.today().isoformat())
    a = ap.parse_args()
    n, uyari = uret(t(a.bugun))
    print(f"{n} görev yazıldı -> {CIKTI}")
    for u in uyari:
        print("UYARI:", u)
