"""plan/backlog.json dosyasından proje belgelerini üretir.

Çıktılar:
  docs/03-proje-plani-sprint-ve-kanban.md   (makro plan, sprint planı, kanban)
  docs/06-urun-gereksinimleri.md            (personalar, fonksiyonel ve fonksiyonel olmayan gereksinimler)
Kullanım: python scripts/plan_olustur.py [--bugun YYYY-MM-DD]
"""
import argparse
import json
from datetime import date, timedelta
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
BACKLOG = KOK / "plan" / "backlog.json"
TEKNOLOJI = KOK / "plan" / "teknolojiler.json"
PLAN_MD = KOK / "docs" / "03-proje-plani-sprint-ve-kanban.md"
PRD_MD = KOK / "docs" / "06-urun-gereksinimleri.md"

TIP_AD = {"hikaye": "Kullanıcı hikâyesi", "arastirma": "Ar-Ge araştırması", "gorev": "Görev"}
ONCELIK = {"P1": "Olmazsa olmaz", "P2": "Olmalı", "P3": "Olabilir"}
M_BASVURU = "Hazırlık · Başvuru (23.11–11.12.2026)"
M_DEGER = "Hazırlık · Değerlendirme ve yerleşme (14.12.2026–31.03.2027)"
M_SUREKLI = "Faz 1 · Sürekli işler (Nisan 2027 – Mart 2028)"
M_F2 = "Faz 2 · Yol haritası (2028–2029)"
M_F3 = "Faz 3 · Yol haritası (2029–2030)"


def t(s):
    return date.fromisoformat(s)


def tr(d):
    return d.strftime("%d.%m.%Y")


def yukle():
    v = json.loads(BACKLOG.read_text(encoding="utf-8"))
    v["teknolojiler"] = json.loads(TEKNOLOJI.read_text(encoding="utf-8"))
    return v


def sprintler(v):
    b = t(v["faz1_sprint1"])
    return [{"no": i + 1, "bas": b + timedelta(days=i * v["sprint_gun"]), "bit": b + timedelta(days=i * v["sprint_gun"] + v["sprint_gun"] - 1)}
            for i in range(v["sprint_sayisi"])]


def sprint_ad(s):
    return f"Sprint {s['no']:02d} · {s['bas'].strftime('%d.%m')}–{tr(s['bit'])}"


def hazirla(v):
    """Her öğeye tarih, faz ve milestone bilgisi ekler."""
    sp = sprintler(v)
    ep = {e["id"]: e for e in v["epikler"]}
    for o in v["ogeler"]:
        o["_faz"] = ep[o["epik"]]["faz"]
        if "spr" in o:
            a, b = o["spr"]
            o["_bas"], o["_bit"] = sp[a - 1]["bas"], sp[b - 1]["bit"]
            o["_sprint"] = f"Sprint {a:02d}" + (f" – Sprint {b:02d}" if b != a else "")
            o["_ms"] = sprint_ad(sp[a - 1])
        else:
            o["_bas"], o["_bit"] = t(o["tarih"][0]), t(o["tarih"][1])
            o["_sprint"] = None
            if o.get("surekli"):
                o["_ms"] = M_SUREKLI
            elif o["_faz"] == "F0":
                o["_ms"] = M_BASVURU if o["_bit"] <= date(2026, 12, 11) else M_DEGER
            else:
                o["_ms"] = M_F2 if o["_faz"] == "F2" else M_F3
    return sp


def dogrula(v):
    idx = {o["id"]: o for o in v["ogeler"]}
    uyari = []
    for o in v["ogeler"]:
        for d in o.get("dep", []):
            if d not in idx:
                uyari.append(f"{o['id']}: bilinmeyen bağımlılık {d}")
            elif idx[d]["_bas"] > o["_bas"]:
                uyari.append(f"{o['id']}: bağımlılık {d} bu öğeden sonra başlıyor")
        for k in o["tek"]:
            if k not in v["teknolojiler"]:
                uyari.append(f"{o['id']}: bilinmeyen teknoloji {k}")
    return uyari


def hikaye_cumlesi(o):
    p, i, f = o["as"]
    return f"Bir **{p}** olarak, **{i}** istiyorum; böylece {f}."


def kk_satirlari(o):
    if o["tip"] == "hikaye":
        return [f"**Verilen** {a}, **olduğunda** {b}, **o zaman** {c}." for a, b, c in o["kk"]]
    return list(o["kk"])


def tek_kisa(v, kodlar):
    return ", ".join(v["teknolojiler"][k].split(" (")[0] for k in kodlar)


def plan_belgesi(v, sp, bugun):
    ep = {e["id"]: e for e in v["epikler"]}
    og = v["ogeler"]
    L = []
    a = L.append
    a("# Proje Planı: Makro Plan, Sprintler ve Kanban")
    a("")
    a(f"> Bu belge `plan/backlog.json` dosyasından `scripts/plan_olustur.py` ile üretilir; elle düzenlenmez. Son üretim: {tr(bugun)}.")
    a("")
    a(f"**Proje:** {v['proje']}")
    a("")
    a(f"**Kurum notu:** {v['kurum_notu']}")
    a("")
    a("## 1. Planlama yaklaşımı")
    a("")
    a("- **Makro düzey:** fazlar ve epikler (ürünün işlev alanları ve Ar-Ge iş paketleri).")
    a("- **Mikro düzey:** kullanıcı hikâyeleri, Ar-Ge araştırmaları ve görevler; Faz 1 iki haftalık 26 sprinte bölünmüştür.")
    a("- **Her öğede:** tarih, sorumlu, öncelik, hikâye puanı, kullanılacak teknolojiler ve kabul kriteri bulunur. Kullanıcı hikâyelerinde ayrıca fonksiyonel gereksinimler yer alır (bkz. `docs/06-urun-gereksinimleri.md`).")
    a("- Faz 2 ve Faz 3 makro düzeyde planlanmıştır; sprint planlaması önceki fazın son çeyreğinde yapılacaktır.")
    a("")
    a("## 2. Fazlar")
    a("")
    a("| Faz | Başlangıç | Bitiş | Epik | Öğe |")
    a("|---|---|---|---|---|")
    for k, f in v["fazlar"].items():
        a(f"| {f['ad']} | {tr(t(f['bas']))} | {tr(t(f['bit']))} | {sum(1 for e in v['epikler'] if e['faz'] == k)} | {sum(1 for o in og if o['_faz'] == k)} |")
    a("")
    a("## 3. Epikler")
    a("")
    a("| Epik | Faz | Tarih aralığı | Hikâye | Araştırma | Görev | Puan | Amaç |")
    a("|---|---|---|---|---|---|---|---|")
    for e in v["epikler"]:
        gs = [o for o in og if o["epik"] == e["id"]]
        b, s = min(o["_bas"] for o in gs), max(o["_bit"] for o in gs)
        n = lambda tip: sum(1 for o in gs if o["tip"] == tip)
        a(f"| **{e['id']}** {e['ad']} | {v['fazlar'][e['faz']]['ad'].split(' · ')[0]} | {tr(b)} – {tr(s)} | {n('hikaye')} | {n('arastirma')} | {n('gorev')} | {sum(o.get('sp', 0) for o in gs) or '—'} | {e['amac']} |")
    a("")
    a("## 4. Kanban görünümü")
    a("")
    devam = [o for o in og if o["_bas"] <= bugun <= o["_bit"]]
    yakin = [o for o in og if bugun < o["_bas"] <= bugun + timedelta(days=14)]
    a(f"{tr(bugun)} itibarıyla:")
    a("")
    a("| Sütun | Öğeler |")
    a("|---|---|")
    a(f"| Devam ediyor | {', '.join(o['id'] for o in devam) or '—'} |")
    a(f"| Önümüzdeki 14 gün | {', '.join(o['id'] for o in yakin) or '—'} |")
    a(f"| Yapılacak | {len(og) - len(devam) - len(yakin)} öğe |")
    a("")
    a("GitHub'da durumlar `durum:` etiketleriyle izlenir: yapılacak → bu sprint → devam ediyor → incelemede → kapalı.")
    a("")
    a("## 5. Hazırlık dönemi (Faz 0)")
    a("")
    a("| Öğe | Başlık | Başlangıç | Bitiş | Sorumlu | Teknolojiler |")
    a("|---|---|---|---|---|---|")
    for o in og:
        if o["_faz"] == "F0" and not o.get("surekli"):
            a(f"| {o['id']} | {o['t']} | {tr(o['_bas'])} | {tr(o['_bit'])} | {o['r']} | {tek_kisa(v, o['tek'])} |")
    a("")
    a("## 6. Faz 1 sprint planı")
    a("")
    for s in sp:
        gs = [o for o in og if o.get("spr") and o["spr"][0] == s["no"]]
        if not gs:
            continue
        kod = sorted({k for o in gs for k in o["tek"]}, key=lambda k: list(v["teknolojiler"]).index(k))
        a(f"### {sprint_ad(s)}")
        a("")
        a(f"**Başlayan öğe:** {len(gs)} · **Hikâye puanı:** {sum(o.get('sp', 0) for o in gs)} · **Teknolojiler:** {tek_kisa(v, kod)}")
        a("")
        a("| Öğe | Tür | Başlık | Epik | Süre | Sorumlu | Öncelik | Puan |")
        a("|---|---|---|---|---|---|---|---|")
        for o in gs:
            a(f"| {o['id']} | {TIP_AD[o['tip']]} | {o['t']} | {o['epik']} | {o['_sprint']} | {o['r']} | {ONCELIK[o['on']]} | {o.get('sp', '—')} |")
        a("")
    a("**Faz 1 boyunca sürekli işler:** " + "; ".join(f"{o['id']} {o['t']}" for o in og if o.get("surekli")) + ".")
    a("")
    a("## 7. Faz 2 ve Faz 3 yol haritası")
    a("")
    a("| Öğe | Tür | Başlık | Epik | Başlangıç | Bitiş | Teknolojiler |")
    a("|---|---|---|---|---|---|---|")
    for o in og:
        if o["_faz"] in ("F2", "F3"):
            a(f"| {o['id']} | {TIP_AD[o['tip']]} | {o['t']} | {o['epik']} | {tr(o['_bas'])} | {tr(o['_bit'])} | {tek_kisa(v, o['tek'])} |")
    a("")
    a("## 8. Kritik tarihler")
    a("")
    a("| Tarih | Olay | Kural |")
    a("|---|---|---|")
    for r in [("11.12.2026", "Online aday firma başvurusu", "Eksik veya hatalı beyan başvurunun yok sayılmasına yol açar"),
              ("≤ 09.02.2027", "Aday komisyon sonucu", "En geç 60 gün; itiraz yolu yok"),
              ("01.04.2027", "Faz 1 ve Sprint 01 başlangıcı (tahmini)", "Faaliyet onay yazısının tarihi esas alınır"),
              ("Her ayın 20'si", "Aylık muafiyet raporu", "Gecikme aykırı faaliyet sayılır"),
              ("31.01.2028", "Faz 2 başvurusu son tarihi", "Mevcut proje bitmeden en az 60 gün önce"),
              ("31.03.2028", "Faz 1 bitişi", "90 gün projesiz kalan firma bölgeden çıkarılır"),
              ("31.12.2028", "4691 sayılı Kanun teşvik süresi sonu (mevcut mevzuat)", "Uzatma kararı izlenmelidir")]:
        a(f"| {r[0]} | {r[1]} | {r[2]} |")
    a("")
    a("## 9. Teknoloji kullanımı")
    a("")
    a("Seçim gerekçeleri: [`04-teknoloji-kararlari.md`](04-teknoloji-kararlari.md).")
    a("")
    a("| Teknoloji | Öğe sayısı | İlk kullanıldığı sprint |")
    a("|---|---|---|")
    for k, ad in v["teknolojiler"].items():
        gs = [o for o in og if k in o["tek"]]
        if not gs:
            continue
        ilk = min((o["spr"][0] for o in gs if o.get("spr")), default=None)
        a(f"| {ad} | {len(gs)} | {'Sprint %02d' % ilk if ilk else 'Hazırlık / Faz 2'} |")
    a("")
    PLAN_MD.write_text("\n".join(L) + "\n", encoding="utf-8")


def prd_belgesi(v):
    og = v["ogeler"]
    L = []
    a = L.append
    a("# Ürün Gereksinimleri Belgesi")
    a("")
    a("> Bu belge `plan/backlog.json` dosyasından üretilir. Fonksiyonel gereksinim numaraları kullanıcı hikâyesi numarasından türetilir (ör. US-101 → FR-101.1).")
    a("")
    a(f"**Ürün:** {v['proje']}")
    a("")
    a(f"**Amaç:** {v['kurum_notu']}")
    a("")
    a("## 1. Personalar")
    a("")
    a("| Persona | Tanım |")
    a("|---|---|")
    for p in v["personalar"]:
        a(f"| {p['ad']} | {p['tanim']} |")
    a("")
    a("## 2. Fonksiyonel olmayan gereksinimler")
    a("")
    a("| No | Alan | Gereksinim |")
    a("|---|---|---|")
    for n in v["nfr"]:
        a(f"| {n[0]} | {n[1]} | {n[2]} |")
    a("")
    a("## 3. Epik bazında fonksiyonel gereksinimler ve kabul kriterleri")
    a("")
    for e in v["epikler"]:
        gs = [o for o in og if o["epik"] == e["id"] and o["tip"] in ("hikaye", "arastirma")]
        if not gs:
            continue
        a(f"### {e['id']} · {e['ad']}")
        a("")
        a(f"_{e['amac']}_")
        a("")
        for o in gs:
            a(f"#### {o['id']} · {o['t']}")
            a("")
            a(f"Tür: {TIP_AD[o['tip']]} · Öncelik: {ONCELIK[o['on']]} · Puan: {o.get('sp', '—')} · Planlanan: {o['_sprint'] or tr(o['_bas']) + ' – ' + tr(o['_bit'])}")
            a("")
            if o["tip"] == "hikaye":
                a(hikaye_cumlesi(o))
                a("")
                a("**Fonksiyonel gereksinimler**")
                a("")
                num = o["id"].split("-")[1]
                for i, g in enumerate(o["gr"], 1):
                    a(f"- FR-{num}.{i}: {g}")
                a("")
            else:
                a(f"**Hipotez ve ölçüt:** {o['hedef']}")
                a("")
            a("**Kabul kriterleri**")
            a("")
            for k in kk_satirlari(o):
                a(f"- {k}")
            a("")
    PRD_MD.write_text("\n".join(L) + "\n", encoding="utf-8")


def uret(bugun):
    v = yukle()
    sp = hazirla(v)
    plan_belgesi(v, sp, bugun)
    prd_belgesi(v)
    return v, dogrula(v)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--bugun", default=date.today().isoformat())
    a = ap.parse_args()
    v, uyari = uret(t(a.bugun))
    tipler = {k: sum(1 for o in v["ogeler"] if o["tip"] == k) for k in TIP_AD}
    print(f"{len(v['epikler'])} epik, {len(v['ogeler'])} öğe {tipler} -> {PLAN_MD.name}, {PRD_MD.name}")
    for u in uyari:
        print("UYARI:", u)
