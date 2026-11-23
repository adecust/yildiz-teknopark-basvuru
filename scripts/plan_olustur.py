"""plan/faz1-plan.json dosyasından docs/03-faz1-kanban-ve-zaman-plani.md belgesini üretir.

Kullanım:  python scripts/plan_olustur.py [--bugun YYYY-MM-DD]
"""
import argparse
import json
from datetime import date, timedelta
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
PLAN = KOK / "plan" / "faz1-plan.json"
CIKTI = KOK / "docs" / "03-faz1-kanban-ve-zaman-plani.md"

AYLAR = ["Oca", "Şub", "Mar", "Nis", "May", "Haz", "Tem", "Ağu", "Eyl", "Eki", "Kas", "Ara"]


def tarih(s):
    return date.fromisoformat(s)


def tr(d):
    return d.strftime("%d.%m.%Y")


def ay_listesi(bas, bit):
    y, m = bas.year, bas.month
    sonuc = []
    while (y, m) <= (bit.year, bit.month):
        sonuc.append((y, m))
        m += 1
        if m == 13:
            y, m = y + 1, 1
    return sonuc


def dogrula(gorevler):
    idx = {g["id"]: g for g in gorevler}
    uyarilar = []
    for g in gorevler:
        if tarih(g["e"]) < tarih(g["s"]):
            uyarilar.append(f"{g['id']}: bitiş başlangıçtan önce")
        for d in g["dep"]:
            if d not in idx:
                uyarilar.append(f"{g['id']}: bilinmeyen bağımlılık {d}")
            elif tarih(idx[d]["e"]) > tarih(g["e"]):
                uyarilar.append(f"{g['id']}: bağımlılık {d} bu görevden sonra bitiyor")
    return uyarilar


def kart(g):
    etiket = " ".join(f"`{x}`" for x in g["l"])
    return f"- **[{g['id']}]** {g['t']} — {tr(tarih(g['s']))} → {tr(tarih(g['e']))} · _{g['r']}_ {etiket}"


def uret(bugun):
    veri = json.loads(PLAN.read_text(encoding="utf-8"))
    gorevler = veri["gorevler"]
    ms = {m["key"]: m for m in veri["milestones"]}
    uyarilar = dogrula(gorevler)

    hafta_sonu = bugun + timedelta(days=6)
    otuz = bugun + timedelta(days=30)
    devam = [g for g in gorevler if tarih(g["s"]) <= bugun <= tarih(g["e"])]
    bu_hafta = [g for g in gorevler if bugun < tarih(g["s"]) <= hafta_sonu]
    sirada = [g for g in gorevler if hafta_sonu < tarih(g["s"]) <= otuz]
    backlog = [g for g in gorevler if tarih(g["s"]) > otuz]

    L = []
    L.append("# Faz 1 · Kanban ve Zaman Planı")
    L.append("")
    L.append(f"> Bu belge `plan/faz1-plan.json` dosyasından `scripts/plan_olustur.py` ile **otomatik üretilir**. "
             f"Elle düzenlemeyin; JSON'u güncelleyip betiği yeniden çalıştırın. Son üretim: **{tr(bugun)}**.")
    L.append("")
    L.append(f"**Proje:** {veri['proje']}")
    L.append("")
    L.append(f"**Faz 1 tahmini süre:** {tr(tarih(veri['faz1_baslangic_tahmini']))} → {tr(tarih(veri['faz1_bitis_tahmini']))} (12 ay). "
             "Başlangıç, Yıldız'ın değerlendirme sürelerine bağlı bir tahmindir; faaliyet onay yazısının tarihi gerçek başlangıç olur.")
    L.append("")
    L.append("## 1. Girdi: firmadan alınan cevaplar ve plana etkisi")
    L.append("")
    L.append("| Cevap | Plana etkisi |")
    L.append("|---|---|")
    L.append("| Aylık 200–300 öğrenci (sürekli değişen) | Pilot ve test verisi için yeterli. Ödev veri seti (≥300) 1–2 ayda toplanabilir. Ölçek küçük kaldığı için **dış kurum pilotu (7.3) ticarileşme puanı açısından kritik.** |")
    L.append("| Şirket içinde yazılım ekibi var | Büyük artı; 'Ar-Ge kapasitesi' riski azalır. Yine de **YZ/dil işleme uzmanı** yoksa işe alım (H-07) gerekiyor. |")
    L.append("| Hem bireysel hem kurumsal satış | Gelir modeli: kurumsal abonelik (SaaS) + bireysel abonelik. B2C altyapısı İP-2'ye eklendi (2.7). |")
    L.append("| Mevcut şirketle (şube) girilecek | 3 yıllık bilanço avantajı korunur. **Ana sözleşmede yazılım/Ar-Ge faaliyeti yoksa tadil gerekir** (H-03, D-05); şube tescili kira sonrası (D-07). Eğitim geliri ile yazılım kazancının ayrıştırılması için mali müşavir görüşü şart (H-02). |")
    L.append("| YTÜ'de tanıdık akademisyen yok | **Kritik yol.** Yönerge md. 16.6'ya göre Yıldız TTO, YTÜ akademisyenlerinden akademik danışmanlık hizmeti sağlıyor. Eşleştirme talebi ilk hafta yapılmalı (H-04). |")
    L.append("| En kısa zamanda başvuru | Online başvuru hedefi **11.12.2026**. Detaylı proje dosyası aday komisyon sürecine paralel yazılır (D-02), çünkü hakeme ancak aday komisyon kabulünden sonra gidiyor. |")
    L.append("")

    L.append("## 2. Kritik tarihler")
    L.append("")
    L.append("| Tarih | Olay | Kural / not |")
    L.append("|---|---|---|")
    L.append("| 27.11.2026 | Yıldız ön görüşmesi + TTO akademisyen talebi | Kritik yolun başı |")
    L.append("| **11.12.2026** | **Online aday firma başvurusu** | Eksik / hatalı beyan → başvuru yok sayılır |")
    L.append("| ≤ 09.02.2027 | Aday komisyon sonucu | Yönerge: en geç 60 gün, itiraz yok |")
    L.append("| ~12.03.2027 | Hakem heyeti sonucu (tahmini) | 21 + 21 gün; salt çoğunluk |")
    L.append("| ~31.03.2027 | Faaliyet onay yazısı | Faaliyet başlangıcı bu yazının tarihi |")
    L.append("| 01.04.2027 | **Faz 1 başlangıcı (tahmini)** | Proje süresi en fazla 12 ay |")
    L.append("| Her ayın 20'si | Aylık muafiyet raporu | Gecikme = aykırı faaliyet |")
    L.append("| **31.01.2028** | **Faz 2 başvurusu son tarihi** | Mevcut proje bitmeden ≥60 gün önce; hedef 14.01.2028 |")
    L.append("| 29.02.2028 | Revizyon başvurusu için son gün | Bitişe <30 gün kala revizyon yapılamaz |")
    L.append("| 31.03.2028 | Faz 1 bitişi | 90 gün projesiz kalan firma ihraç edilir |")
    L.append("| 31.05.2028 | 2027 yıllık faaliyet raporu | SMMM/YMM onaylı |")
    L.append("| 31.12.2028 | 4691 teşvik süresi sonu (mevcut mevzuat) | Faz 2 bu tarihi aşıyor; uzatma yapılıp yapılmadığı izlenmeli |")
    L.append("")

    L.append("## 3. Kanban panosu")
    L.append("")
    L.append("### ✅ Tamamlandı")
    for t in veri["tamamlanan"]:
        L.append(f"- **[{t['id']}]** {t['t']} → `{t['doc']}`")
    L.append("")
    for baslik, grup in [("🔄 Devam ediyor", devam), ("🔥 Bu hafta başlayacak", bu_hafta), ("⏭ Sıradaki 30 gün", sirada)]:
        L.append(f"### {baslik} ({len(grup)})")
        if grup:
            L.extend(kart(g) for g in grup)
        else:
            L.append("- —")
        L.append("")
    L.append(f"### 📋 Backlog ({len(backlog)})")
    L.append("")
    for key, m in ms.items():
        grup = [g for g in backlog if g["m"] == key]
        if grup:
            L.append(f"<details><summary><b>{m['title']}</b> ({len(grup)} görev)</summary>")
            L.append("")
            L.extend(kart(g) for g in grup)
            L.append("")
            L.append("</details>")
            L.append("")

    L.append("## 4. Zaman çizelgesi (aylık)")
    L.append("")
    bas = min(tarih(g["s"]) for g in gorevler)
    bit = max(tarih(g["e"]) for g in gorevler)
    aylar = ay_listesi(bas, bit)
    L.append("| İş paketi | " + " | ".join(f"{AYLAR[m-1]} {str(y)[2:]}" for y, m in aylar) + " |")
    L.append("|---|" + "---|" * len(aylar))
    for key, m in ms.items():
        grup = [g for g in gorevler if g["m"] == key]
        hucre = []
        for y, a in aylar:
            ay_bas = date(y, a, 1)
            ay_bit = date(y + (a == 12), a % 12 + 1, 1) - timedelta(days=1)
            aktif = any(tarih(g["s"]) <= ay_bit and tarih(g["e"]) >= ay_bas for g in grup)
            hucre.append("█" if aktif else "")
        L.append(f"| {m['title']} | " + " | ".join(hucre) + " |")
    L.append("")

    L.append("## 5. Milestone bazında görev listesi")
    L.append("")
    for key, m in ms.items():
        grup = [g for g in gorevler if g["m"] == key]
        L.append(f"### {m['title']}")
        L.append("")
        L.append(f"_Son tarih: {tr(tarih(m['due']))} · {m['desc']}_")
        L.append("")
        L.append("| ID | Görev | Başlangıç | Bitiş | Rol | Bağımlılık | Kabul kriteri |")
        L.append("|---|---|---|---|---|---|---|")
        for g in grup:
            L.append(f"| {g['id']} | {g['t']} | {tr(tarih(g['s']))} | {tr(tarih(g['e']))} | {g['r']} | "
                     f"{', '.join(g['dep']) or '—'} | {g['k']} |")
        L.append("")

    L.append("## 6. Kanban kuralları")
    L.append("")
    L.append("- Kolonlar: **Backlog → Bu hafta → Devam ediyor → İncelemede → Tamamlandı.** GitHub'da her görev bir issue; kolon durumu `durum:*` etiketiyle izlenir.")
    L.append("- Bir görev ancak **kabul kriteri** sağlandığında kapatılır. Kriter rakamsa (ör. Recall@5 ≥ %90) ölçüm sonucu issue'ya yorum olarak eklenir. Bu kayıtlar ileride hakem ve Bakanlık denetimi için kanıt olur.")
    L.append("- `kritik` etiketli görevlerdeki gecikme haftalık toplantıda ele alınır; kritik yol: **H-04 → H-05 → H-14 → D-01 → D-03 → D-04 → D-06 → D-08 → Faz 1 başlangıcı.**")
    L.append("- Tarih değişirse önce `plan/faz1-plan.json` güncellenir, sonra belge yeniden üretilir ve issue tarihleri eşitlenir.")
    L.append("")

    CIKTI.write_text("\n".join(L) + "\n", encoding="utf-8")
    return len(gorevler), uyarilar


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--bugun", default=date.today().isoformat())
    a = ap.parse_args()
    n, uyarilar = uret(tarih(a.bugun))
    print(f"{n} görev yazıldı -> {CIKTI}")
    for u in uyarilar:
        print("UYARI:", u)
