# Faz 1 · Kanban ve Zaman Planı

> Bu belge `plan/faz1-plan.json` dosyasından `scripts/plan_olustur.py` ile **otomatik üretilir**. Elle düzenlemeyin; JSON'u güncelleyip betiği yeniden çalıştırın. Son üretim: **23.11.2026**.

**Proje:** Türkçe Eğitim İçeriği İçin Kaynağa Dayalı Üretken YZ ile Soru-Cevap ve Rubrik Tabanlı Otomatik Ödev Değerlendirme Platformu

**Faz 1 tahmini süre:** 01.04.2027 → 31.03.2028 (12 ay). Başlangıç, Yıldız'ın değerlendirme sürelerine bağlı bir tahmindir; faaliyet onay yazısının tarihi gerçek başlangıç olur.

## 1. Girdi: firmadan alınan cevaplar ve plana etkisi

| Cevap | Plana etkisi |
|---|---|
| Aylık 200–300 öğrenci (sürekli değişen) | Pilot ve test verisi için yeterli. Ödev veri seti (≥300) 1–2 ayda toplanabilir. Ölçek küçük kaldığı için **dış kurum pilotu (7.3) ticarileşme puanı açısından kritik.** |
| Şirket içinde yazılım ekibi var | Büyük artı; 'Ar-Ge kapasitesi' riski azalır. Yine de **YZ/dil işleme uzmanı** yoksa işe alım (H-07) gerekiyor. |
| Hem bireysel hem kurumsal satış | Gelir modeli: kurumsal abonelik (SaaS) + bireysel abonelik. B2C altyapısı İP-2'ye eklendi (2.7). |
| Mevcut şirketle (şube) girilecek | 3 yıllık bilanço avantajı korunur. **Ana sözleşmede yazılım/Ar-Ge faaliyeti yoksa tadil gerekir** (H-03, D-05); şube tescili kira sonrası (D-07). Eğitim geliri ile yazılım kazancının ayrıştırılması için mali müşavir görüşü şart (H-02). |
| YTÜ'de tanıdık akademisyen yok | **Kritik yol.** Yönerge md. 16.6'ya göre Yıldız TTO, YTÜ akademisyenlerinden akademik danışmanlık hizmeti sağlıyor. Eşleştirme talebi ilk hafta yapılmalı (H-04). |
| En kısa zamanda başvuru | Online başvuru hedefi **11.12.2026**. Detaylı proje dosyası aday komisyon sürecine paralel yazılır (D-02), çünkü hakeme ancak aday komisyon kabulünden sonra gidiyor. |

## 2. Kritik tarihler

| Tarih | Olay | Kural / not |
|---|---|---|
| 27.11.2026 | Yıldız ön görüşmesi + TTO akademisyen talebi | Kritik yolun başı |
| **11.12.2026** | **Online aday firma başvurusu** | Eksik / hatalı beyan → başvuru yok sayılır |
| ≤ 09.02.2027 | Aday komisyon sonucu | Yönerge: en geç 60 gün, itiraz yok |
| ~12.03.2027 | Hakem heyeti sonucu (tahmini) | 21 + 21 gün; salt çoğunluk |
| ~31.03.2027 | Faaliyet onay yazısı | Faaliyet başlangıcı bu yazının tarihi |
| 01.04.2027 | **Faz 1 başlangıcı (tahmini)** | Proje süresi en fazla 12 ay |
| Her ayın 20'si | Aylık muafiyet raporu | Gecikme = aykırı faaliyet |
| **31.01.2028** | **Faz 2 başvurusu son tarihi** | Mevcut proje bitmeden ≥60 gün önce; hedef 14.01.2028 |
| 29.02.2028 | Revizyon başvurusu için son gün | Bitişe <30 gün kala revizyon yapılamaz |
| 31.03.2028 | Faz 1 bitişi | 90 gün projesiz kalan firma ihraç edilir |
| 31.05.2028 | 2027 yıllık faaliyet raporu | SMMM/YMM onaylı |
| 31.12.2028 | 4691 teşvik süresi sonu (mevcut mevzuat) | Faz 2 bu tarihi aşıyor; uzatma yapılıp yapılmadığı izlenmeli |

## 3. Kanban panosu

### ✅ Tamamlandı
- **[R-01]** Yıldız Teknopark detaylı araştırması → `docs/01-yildiz-teknopark-arastirma-raporu.md`
- **[R-02]** Faz yapısının güncellenmesi ve kabul analizi → `docs/02-faz-yapisi-ve-kabul-analizi.md`

### 🔄 Devam ediyor (0)
- —

### 🔥 Bu hafta başlayacak (7)
- **[H-01]** Yıldız Teknopark ile ön görüşme (Kurumsal Kiralama) — 24.11.2026 → 27.11.2026 · _Yönetim_ `kritik` `yildiz`
- **[H-02]** Mali müşavir görüşü: teknopark şubesi, kazanç ayrıştırma, KDV istisnası — 24.11.2026 → 02.12.2026 · _Mali Müşavir_ `kritik` `mali`
- **[H-03]** Ana sözleşme amaç-konu kontrolü (yazılım/Ar-Ge faaliyeti var mı?) — 24.11.2026 → 04.12.2026 · _Mali Müşavir_ `mali` `evrak`
- **[H-04]** Yıldız TTO'ya akademik danışman eşleştirme talebi — 24.11.2026 → 27.11.2026 · _Proje Yöneticisi_ `kritik` `akademik`
- **[H-06]** Mevcut yazılım ekibi envanteri ve Ar-Ge personeli haritası — 24.11.2026 → 02.12.2026 · _Proje Yöneticisi_ `ekip`
- **[H-09]** Literatür, patent taraması ve rakip (SOTA) tablosu — 25.11.2026 → 04.12.2026 · _Proje Yöneticisi_ `ar-ge`
- **[H-10]** Pazar ve ticarileşme analizi (B2B + B2C, fiyatlama, ihracat) — 25.11.2026 → 04.12.2026 · _Yönetim_ `ticari`

### ⏭ Sıradaki 30 gün (10)
- **[H-05]** Akademisyen görüşmeleri ve niyet mektubu — 30.11.2026 → 09.12.2026 · _Proje Yöneticisi_ `kritik` `akademik`
- **[H-07]** YZ / doğal dil işleme mühendisi işe alım süreci — 30.11.2026 → 29.01.2027 · _Yönetim_ `ekip`
- **[H-08]** Zorunlu evrakların OCR'lı PDF olarak hazırlanması — 30.11.2026 → 09.12.2026 · _Mali Müşavir_ `evrak`
- **[H-11]** Proje özeti (≥1200 karakter) ve form metinleri — 02.12.2026 → 07.12.2026 · _Proje Yöneticisi_ `dosya`
- **[H-12]** Firma / proje sunumu (13 slayt) — 02.12.2026 → 09.12.2026 · _Proje Yöneticisi_ `dosya` `kritik`
- **[H-13]** İç hakem simülasyonu (15 soru) ve revizyon — 09.12.2026 → 10.12.2026 · _Proje Yöneticisi_ `dosya`
- **[H-14]** Online aday firma başvurusunun gönderilmesi — 11.12.2026 → 11.12.2026 · _Proje Yöneticisi_ `kritik` `yildiz`
- **[D-01]** Aday Girişimci Değerlendirme Komisyonu sürecinin takibi — 14.12.2026 → 15.01.2027 · _Proje Yöneticisi_ `yildiz`
- **[D-02]** Detaylı proje dosyası (17 bölüm, hakem heyeti için) — 07.12.2026 → 15.01.2027 · _Proje Yöneticisi_ `dosya` `kritik`
- **[D-05]** Ana sözleşme tadili (gerekirse) ve tescil — 07.12.2026 → 29.01.2027 · _Mali Müşavir_ `mali` `evrak`

### 📋 Backlog (56)

<details><summary><b>M1 · Değerlendirme ve Yerleşme</b> (7 görev)</summary>

- **[D-03]** ARGEPORTAL entegrasyonu, proje dosyasının yüklenmesi, başvuru ücreti — 18.01.2027 → 29.01.2027 · _Proje Yöneticisi_ `yildiz`
- **[D-04]** Hakem heyeti süreci ve sunum / soru-cevap provası — 01.02.2027 → 12.03.2027 · _Proje Yöneticisi_ `yildiz` `kritik`
- **[D-06]** Kira müzakeresi, sözleşme ve 3 aylık güvence bedeli — 08.03.2027 → 19.03.2027 · _Yönetim_ `yildiz` `mali`
- **[D-07]** Teknopark şubesinin ticaret sicil tescili ve vergi dairesi kaydı — 15.03.2027 → 26.03.2027 · _Mali Müşavir_ `mali` `evrak`
- **[D-08]** Faaliyet Onay Yazısı ve vergi dairesi / SGK bildirimleri — 22.03.2027 → 31.03.2027 · _Mali Müşavir_ `yildiz` `kritik`
- **[D-09]** Personel onayları, dijital giriş kartları, ofis kurulumu — 22.03.2027 → 31.03.2027 · _Proje Yöneticisi_ `ekip`
- **[D-10]** Akademisyen görevlendirme yazısının Yıldız onayı — 01.03.2027 → 31.03.2027 · _Proje Yöneticisi_ `akademik`

</details>

<details><summary><b>İP-0 · Proje Yönetimi ve Teknopark Raporlaması</b> (2 görev)</summary>

- **[0.1]** Aylık muafiyet raporu + SGK / personel / proje izleme formları (her ayın 20'sine kadar) — 01.05.2027 → 20.04.2028 · _Proje Yöneticisi_ `tekrarlayan` `yildiz`
- **[0.2]** Çeyreklik ilerleme ve risk gözden geçirmesi (akademik danışmanlarla) — 28.06.2027 → 31.03.2028 · _Proje Yöneticisi_ `tekrarlayan`

</details>

<details><summary><b>İP-1 · Gereksinim, Literatür ve Türkçe Test Setleri</b> (5 görev)</summary>

- **[1.1]** Gereksinim analizi ve sistem mimarisi dokümanı — 01.04.2027 → 16.04.2027 · _Proje Yöneticisi_ `ar-ge`
- **[1.2]** Güncel SOTA raporu (kaynağa dayalı üretim, otomatik değerlendirme) — 01.04.2027 → 23.04.2027 · _YZ Mühendisi_ `ar-ge`
- **[1.3]** Türkçe soru-cevap test seti (≥500 soru, eğitmen etiketli) — 12.04.2027 → 21.05.2027 · _Eğitim Tasarımcısı_ `ar-ge` `veri`
- **[1.4]** Ödev değerlendirme veri seti (≥300 ödev, rubrik, eğitmen puanı) — 12.04.2027 → 28.05.2027 · _Eğitim Tasarımcısı_ `ar-ge` `veri` `kvkk`
- **[1.5]** Değerlendirme metodolojisi ve metrik protokolü — 19.04.2027 → 07.05.2027 · _Akademik Danışman_ `ar-ge` `akademik`

</details>

<details><summary><b>İP-2 · Platform Çekirdeği (Test Yatağı)</b> (8 görev)</summary>

- **[2.1]** Çok kiracılı veri modeli, kimlik doğrulama ve rol yönetimi — 01.04.2027 → 23.04.2027 · _Backend_ `platform`
- **[2.2]** Ders alanları, kayıt ve davet akışı — 19.04.2027 → 14.05.2027 · _Backend_ `platform`
- **[2.3]** Ders kaynağı yükleme ve depolama — 03.05.2027 → 28.05.2027 · _Backend_ `platform`
- **[2.4]** Ödev / proje teslim modülü — 17.05.2027 → 11.06.2027 · _Backend_ `platform`
- **[2.5]** Takvim, duyuru ve bildirimler — 31.05.2027 → 25.06.2027 · _Frontend_ `platform`
- **[2.6]** Canlı ders entegrasyonu ve ders kaydı — 07.06.2027 → 09.07.2027 · _Backend_ `platform`
- **[2.7]** Bireysel (B2C) kayıt, abonelik ve ödeme altyapısı — 21.06.2027 → 23.07.2027 · _Backend_ `platform` `ticari`
- **[2.8]** Platform MVP iç testi (mobil uyum dahil) — 12.07.2027 → 30.07.2027 · _Frontend_ `platform` `test`

</details>

<details><summary><b>İP-3 · İçerik İşleme ve Türkçe Bilgi Erişimi (AR-2, AR-5)</b> (5 görev)</summary>

- **[3.1]** Doküman ayrıştırma: PDF, slayt, görsel, tablo, OCR — 03.05.2027 → 28.05.2027 · _YZ Mühendisi_ `ar-ge`
- **[3.2]** Türkçe ders transkript hattı ve kelime hata oranı ölçümü — 17.05.2027 → 18.06.2027 · _YZ Mühendisi_ `ar-ge`
- **[3.3]** Türkçe parçalama stratejileri ve embedding modeli karşılaştırması — 31.05.2027 → 02.07.2027 · _YZ Mühendisi_ `ar-ge`
- **[3.4]** Hibrit arama + yeniden sıralama (hedef Recall@5 ≥ %90) — 21.06.2027 → 13.08.2027 · _YZ Mühendisi_ `ar-ge` `kritik`
- **[3.5]** İP-3 ara teknik raporu — 16.08.2027 → 31.08.2027 · _YZ Mühendisi_ `ar-ge` `rapor`

</details>

<details><summary><b>İP-4 · Kaynağa Dayalı Soru-Cevap ve Pedagojik Sınırlar (AR-1, AR-4)</b> (7 görev)</summary>

- **[4.1]** Atıflı (kaynak gösteren) cevap üretimi — 01.07.2027 → 30.07.2027 · _YZ Mühendisi_ `ar-ge`
- **[4.2]** Kaynak dışı soruları reddetme ve belirsizlik tespiti — 19.07.2027 → 27.08.2027 · _YZ Mühendisi_ `ar-ge` `kritik`
- **[4.3]** Cevap-kaynak sadakat doğrulayıcı — 09.08.2027 → 17.09.2027 · _YZ Mühendisi_ `ar-ge` `kritik`
- **[4.4]** Sokratik mod ve ödev cevabı sızıntısını önleme — 23.08.2027 → 30.09.2027 · _YZ Mühendisi_ `ar-ge`
- **[4.5]** Saldırı (jailbreak) test seti ve dayanıklılık — 13.09.2027 → 15.10.2027 · _YZ Mühendisi_ `ar-ge` `test`
- **[4.6]** Chatbot arayüzünün platforma entegrasyonu — 30.08.2027 → 08.10.2027 · _Frontend_ `platform`
- **[4.7]** İP-4 değerlendirme raporu — 11.10.2027 → 29.10.2027 · _YZ Mühendisi_ `ar-ge` `rapor`

</details>

<details><summary><b>İP-5 · Rubrik Tabanlı Otomatik Ödev Değerlendirme (AR-3)</b> (7 görev)</summary>

- **[5.1]** Rubrik tanımlama arayüzü — 02.08.2027 → 27.08.2027 · _Frontend_ `platform`
- **[5.2]** Rubrik tabanlı puanlama motoru v1 — 16.08.2027 → 30.09.2027 · _YZ Mühendisi_ `ar-ge` `kritik`
- **[5.3]** Gerekçeli ve kaynağa dayalı geri bildirim üretimi — 13.09.2027 → 22.10.2027 · _YZ Mühendisi_ `ar-ge`
- **[5.4]** Eğitmen-YZ puan uyumu kalibrasyonu (hedef ağırlıklı Kappa ≥ 0,75) — 11.10.2027 → 19.11.2027 · _YZ Mühendisi_ `ar-ge` `kritik` `akademik`
- **[5.5]** Eğitmen onay akışı (YZ önerir, eğitmen onaylar) — 01.11.2027 → 26.11.2027 · _Backend_ `platform`
- **[5.6]** (Opsiyonel) Türkçe intihal ve YZ ile yazılmış metin tespiti — 08.11.2027 → 17.12.2027 · _YZ Mühendisi_ `ar-ge` `opsiyonel`
- **[5.7]** İP-5 değerlendirme raporu — 13.12.2027 → 24.12.2027 · _YZ Mühendisi_ `ar-ge` `rapor`

</details>

<details><summary><b>İP-6 · Ölçeklenebilirlik, KVKK ve Yurt İçi Model (AR-6)</b> (5 görev)</summary>

- **[6.1]** KVKK: veri envanteri, aydınlatma, açık rıza, anonimleştirme — 01.09.2027 → 24.09.2027 · _DevOps_ `kvkk`
- **[6.2]** Açık ağırlıklı modelin yurt içinde barındırılması ve ince ayar denemeleri — 13.09.2027 → 12.11.2027 · _YZ Mühendisi_ `ar-ge`
- **[6.3]** Yurt içi model ile ticari model kalite karşılaştırması — 01.11.2027 → 03.12.2027 · _YZ Mühendisi_ `ar-ge`
- **[6.4]** Maliyet ve gecikme optimizasyonu (yanıt ≤ 3 sn) — 15.11.2027 → 17.12.2027 · _DevOps_ `ar-ge`
- **[6.5]** Yük testi — 06.12.2027 → 24.12.2027 · _DevOps_ `test`

</details>

<details><summary><b>İP-7 · Pilot Uygulama</b> (4 görev)</summary>

- **[7.1]** Pilot planı ve kullanım ölçüm altyapısı — 04.10.2027 → 29.10.2027 · _Proje Yöneticisi_ `pilot`
- **[7.2]** Pilot 1: kendi öğrencilerimizle gerçek ortam testi — 01.11.2027 → 24.12.2027 · _Proje Yöneticisi_ `pilot` `kritik`
- **[7.3]** Pilot 2: en az 1 dış kurum (ücretli ya da sözleşmeli) — 03.01.2028 → 25.02.2028 · _Yönetim_ `pilot` `ticari` `kritik`
- **[7.4]** Pilot raporu — 21.02.2028 → 10.03.2028 · _Proje Yöneticisi_ `pilot` `rapor`

</details>

<details><summary><b>İP-8 · Fikri Mülkiyet, Ticarileşme ve Faz 2 Başvurusu</b> (6 görev)</summary>

- **[8.1]** Faz 2 (sanal sınıf) proje dosyasının hazırlanması — 15.11.2027 → 31.12.2027 · _Proje Yöneticisi_ `faz-2` `dosya` `kritik`
- **[8.2]** Faz 2 başvurusunun Yıldız'a teslimi (son tarih 31.01.2028) — 03.01.2028 → 14.01.2028 · _Proje Yöneticisi_ `faz-2` `kritik` `yildiz`
- **[8.3]** Yazılım eser tescili ve patent / faydalı model ön değerlendirmesi (Yıldız TTO) — 01.12.2027 → 28.01.2028 · _Proje Yöneticisi_ `fmh` `akademik`
- **[8.4]** B2B ve B2C satış paketi, fiyatlama, sözleşme şablonları — 13.12.2027 → 11.02.2028 · _Yönetim_ `ticari`
- **[8.5]** Faz 1 proje sonuç raporu — 01.03.2028 → 17.03.2028 · _Proje Yöneticisi_ `rapor`
- **[8.6]** Proje bitirme belgesi başvurusu — 13.03.2028 → 31.03.2028 · _Proje Yöneticisi_ `yildiz`

</details>

## 4. Zaman çizelgesi (aylık)

| İş paketi | Kas 26 | Ara 26 | Oca 27 | Şub 27 | Mar 27 | Nis 27 | May 27 | Haz 27 | Tem 27 | Ağu 27 | Eyl 27 | Eki 27 | Kas 27 | Ara 27 | Oca 28 | Şub 28 | Mar 28 | Nis 28 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M0 · Başvuru Hazırlığı | █ | █ | █ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| M1 · Değerlendirme ve Yerleşme |  | █ | █ | █ | █ |  |  |  |  |  |  |  |  |  |  |  |  |  |
| İP-0 · Proje Yönetimi ve Teknopark Raporlaması |  |  |  |  |  |  | █ | █ | █ | █ | █ | █ | █ | █ | █ | █ | █ | █ |
| İP-1 · Gereksinim, Literatür ve Türkçe Test Setleri |  |  |  |  |  | █ | █ |  |  |  |  |  |  |  |  |  |  |  |
| İP-2 · Platform Çekirdeği (Test Yatağı) |  |  |  |  |  | █ | █ | █ | █ |  |  |  |  |  |  |  |  |  |
| İP-3 · İçerik İşleme ve Türkçe Bilgi Erişimi (AR-2, AR-5) |  |  |  |  |  |  | █ | █ | █ | █ |  |  |  |  |  |  |  |  |
| İP-4 · Kaynağa Dayalı Soru-Cevap ve Pedagojik Sınırlar (AR-1, AR-4) |  |  |  |  |  |  |  |  | █ | █ | █ | █ |  |  |  |  |  |  |
| İP-5 · Rubrik Tabanlı Otomatik Ödev Değerlendirme (AR-3) |  |  |  |  |  |  |  |  |  | █ | █ | █ | █ | █ |  |  |  |  |
| İP-6 · Ölçeklenebilirlik, KVKK ve Yurt İçi Model (AR-6) |  |  |  |  |  |  |  |  |  |  | █ | █ | █ | █ |  |  |  |  |
| İP-7 · Pilot Uygulama |  |  |  |  |  |  |  |  |  |  |  | █ | █ | █ | █ | █ | █ |  |
| İP-8 · Fikri Mülkiyet, Ticarileşme ve Faz 2 Başvurusu |  |  |  |  |  |  |  |  |  |  |  |  | █ | █ | █ | █ | █ |  |

## 5. Milestone bazında görev listesi

### M0 · Başvuru Hazırlığı

_Son tarih: 11.12.2026 · Yıldız Teknopark online aday firma başvurusunun eksiksiz gönderilmesi._

| ID | Görev | Başlangıç | Bitiş | Rol | Bağımlılık | Kabul kriteri |
|---|---|---|---|---|---|---|
| H-01 | Yıldız Teknopark ile ön görüşme (Kurumsal Kiralama) | 24.11.2026 | 27.11.2026 | Yönetim | — | Görüşme yapıldı; raporun 10. bölümündeki 9 teyit sorusu (ücret, m², boş alan, sunum var mı, destekli proje muafiyeti, süre, şube, takvim) yanıtlandı ve not alındı. |
| H-02 | Mali müşavir görüşü: teknopark şubesi, kazanç ayrıştırma, KDV istisnası | 24.11.2026 | 02.12.2026 | Mali Müşavir | — | Yazılı görüş: şube yapısı, eğitim geliri ile Ar-Ge/yazılım kazancının ayrıştırılması, platform satışında KDV istisnası uygunluğu. |
| H-03 | Ana sözleşme amaç-konu kontrolü (yazılım/Ar-Ge faaliyeti var mı?) | 24.11.2026 | 04.12.2026 | Mali Müşavir | — | Ana sözleşmede yazılım geliştirme ve Ar-Ge faaliyetleri yer alıyor ya da tadil kararı alındı (bkz. D-05). |
| H-04 | Yıldız TTO'ya akademik danışman eşleştirme talebi | 24.11.2026 | 27.11.2026 | Proje Yöneticisi | — | Yıldız TTO'ya yazılı talep iletildi: (1) Bilgisayar Müh. – doğal dil işleme / üretken YZ, (2) Eğitim Fakültesi – ölçme ve değerlendirme. |
| H-05 | Akademisyen görüşmeleri ve niyet mektubu | 30.11.2026 | 09.12.2026 | Proje Yöneticisi | H-04 | En az 1 (hedef 2) YTÜ öğretim üyesi ile görüşüldü; danışmanlık niyet mektubu ya da e-posta teyidi alındı. |
| H-06 | Mevcut yazılım ekibi envanteri ve Ar-Ge personeli haritası | 24.11.2026 | 02.12.2026 | Proje Yöneticisi | — | Her kişi için diploma, unvan, deneyim, olası rol (Ar-Ge / destek / kapsam dışı) tablosu; destek ≤%10 ve kapsam dışı ≤%15 kontrolü. |
| H-07 | YZ / doğal dil işleme mühendisi işe alım süreci | 30.11.2026 | 29.01.2027 | Yönetim | H-06 | İlan yayında; en az 1 deneyimli YZ mühendisi ile anlaşma ya da teklif aşaması (başvuru dosyasında isimle gösterilebilir). |
| H-08 | Zorunlu evrakların OCR'lı PDF olarak hazırlanması | 30.11.2026 | 09.12.2026 | Mali Müşavir | — | Vergi levhası, TTSG, son 3 yıl gelir tablosu-bilanço (KV beyannamesi), borç yoktur (vergi dairesi), borç yoktur (SGK); hepsi metni seçilebilir PDF. Borç yoktur yazıları başvurudan en fazla birkaç gün önce alınmış. |
| H-09 | Literatür, patent taraması ve rakip (SOTA) tablosu | 25.11.2026 | 04.12.2026 | Proje Yöneticisi | — | Rakip tablosu (Moodle/Canvas, ChatGPT Edu, NotebookLM, Khanmigo, yerli LMS'ler) + akademik kaynak listesi + TÜRKPATENT/Google Patents taraması özeti. |
| H-10 | Pazar ve ticarileşme analizi (B2B + B2C, fiyatlama, ihracat) | 25.11.2026 | 04.12.2026 | Yönetim | — | TAM/SAM/SOM; bireysel ve kurumsal fiyat modeli; ilk 3 hedef kurum; ithal ikame edilen ürünler; hedef ihracat ülkeleri; 3 yıllık gelir projeksiyonu. |
| H-11 | Proje özeti (≥1200 karakter) ve form metinleri | 02.12.2026 | 07.12.2026 | Proje Yöneticisi | H-09, H-10 | Formun tüm metin alanları taslakta; özet ≥1200 karakter ve problem → yenilik → yöntem → çıktı → pazar akışında. |
| H-12 | Firma / proje sunumu (13 slayt) | 02.12.2026 | 09.12.2026 | Proje Yöneticisi | H-09, H-10 | Rapordaki 7.2 akışına göre 13 slayt; KPI tablosu (şimdi / 12 ay / 36 ay) dahil. |
| H-13 | İç hakem simülasyonu (15 soru) ve revizyon | 09.12.2026 | 10.12.2026 | Proje Yöneticisi | H-11, H-12 | Dosya, hakem formunun 15 sorusuna göre puanlandı; 70'in altındaki her kalem için düzeltme yapıldı. |
| H-14 | Online aday firma başvurusunun gönderilmesi | 11.12.2026 | 11.12.2026 | Proje Yöneticisi | H-08, H-13 | Form gönderildi; başvuru teyidi alındı; tüm belgeler OCR'lı PDF. |

### M1 · Değerlendirme ve Yerleşme

_Son tarih: 31.03.2027 · Aday komisyon (≤60 gün), hakem heyeti (21+21 gün), kira, şube tescili, faaliyet onayı. Tarihler Yıldız'ın sürelerine bağlı tahminlerdir._

| ID | Görev | Başlangıç | Bitiş | Rol | Bağımlılık | Kabul kriteri |
|---|---|---|---|---|---|---|
| D-01 | Aday Girişimci Değerlendirme Komisyonu sürecinin takibi | 14.12.2026 | 15.01.2027 | Proje Yöneticisi | H-14 | Komisyon sonucu alındı. Planlanan hedef 15.01.2027; yönergeye göre en geç 60 gün (09.02.2027). Geç gelirse M1'in kalan tarihleri aynı oranda kayar. |
| D-02 | Detaylı proje dosyası (17 bölüm, hakem heyeti için) | 07.12.2026 | 15.01.2027 | Proje Yöneticisi | H-09 | Rapor 7.1'deki 17 bölüm tamam; AR-1…AR-6 ölçülebilir hedefler; İP'ler ve Gantt; ekip-İP matrisi; akademisyen rolleri. |
| D-03 | ARGEPORTAL entegrasyonu, proje dosyasının yüklenmesi, başvuru ücreti | 18.01.2027 | 29.01.2027 | Proje Yöneticisi | D-01, D-02 | Proje dosyası sistemde; ücret dekontu yüklendi. |
| D-04 | Hakem heyeti süreci ve sunum / soru-cevap provası | 01.02.2027 | 12.03.2027 | Proje Yöneticisi | D-03 | Hakem sonucu alındı (21 + 21 gün). Sözlü sunum istenirse prova yapıldı. |
| D-05 | Ana sözleşme tadili (gerekirse) ve tescil | 07.12.2026 | 29.01.2027 | Mali Müşavir | H-03 | Tadil TTSG'de yayımlandı ya da gerek olmadığı teyit edildi. |
| D-06 | Kira müzakeresi, sözleşme ve 3 aylık güvence bedeli | 08.03.2027 | 19.03.2027 | Yönetim | D-04 | Kira sözleşmesi imzalandı; güvence bedeli 3 gün içinde ödendi; alan teslim alındı. |
| D-07 | Teknopark şubesinin ticaret sicil tescili ve vergi dairesi kaydı | 15.03.2027 | 26.03.2027 | Mali Müşavir | D-06 | Şube tescil edildi; vergi levhası ve imza sirküleri hazır. |
| D-08 | Faaliyet Onay Yazısı ve vergi dairesi / SGK bildirimleri | 22.03.2027 | 31.03.2027 | Mali Müşavir | D-07 | E-imzalı faaliyet onay yazısı alındı; vergi dairesi ve SGK'ya ibraz edildi; ilk 10 gün belgeleri teslim edildi. |
| D-09 | Personel onayları, dijital giriş kartları, ofis kurulumu | 22.03.2027 | 31.03.2027 | Proje Yöneticisi | D-06 | Tüm personel işe başlamadan önce sistemde onaylı; kartlar aktif; ofis kullanıma hazır. |
| D-10 | Akademisyen görevlendirme yazısının Yıldız onayı | 01.03.2027 | 31.03.2027 | Proje Yöneticisi | H-05 | Üniversite görevlendirme yazısı alındı ve yönetici şirket tarafından onaylandı (Yönerge 16.1). |

### İP-0 · Proje Yönetimi ve Teknopark Raporlaması

_Son tarih: 20.04.2028 · Aylık muafiyet raporları, çeyreklik gözden geçirmeler._

| ID | Görev | Başlangıç | Bitiş | Rol | Bağımlılık | Kabul kriteri |
|---|---|---|---|---|---|---|
| 0.1 | Aylık muafiyet raporu + SGK / personel / proje izleme formları (her ayın 20'sine kadar) | 01.05.2027 | 20.04.2028 | Proje Yöneticisi | D-08 | 12 ayın tamamı zamanında e-imza ile onaya sunuldu (Nisan 2027 → Mart 2028). |
| 0.2 | Çeyreklik ilerleme ve risk gözden geçirmesi (akademik danışmanlarla) | 28.06.2027 | 31.03.2028 | Proje Yöneticisi | — | Haziran, Eylül, Aralık, Mart toplantı notları; risk tablosu güncel. |

### İP-1 · Gereksinim, Literatür ve Türkçe Test Setleri

_Son tarih: 28.05.2027 · Ay 1-2_

| ID | Görev | Başlangıç | Bitiş | Rol | Bağımlılık | Kabul kriteri |
|---|---|---|---|---|---|---|
| 1.1 | Gereksinim analizi ve sistem mimarisi dokümanı | 01.04.2027 | 16.04.2027 | Proje Yöneticisi | — | Onaylı gereksinim listesi ve mimari diyagram. |
| 1.2 | Güncel SOTA raporu (kaynağa dayalı üretim, otomatik değerlendirme) | 01.04.2027 | 23.04.2027 | YZ Mühendisi | — | Literatür raporu; seçilen yöntemlerin gerekçesi. |
| 1.3 | Türkçe soru-cevap test seti (≥500 soru, eğitmen etiketli) | 12.04.2027 | 21.05.2027 | Eğitim Tasarımcısı | 1.1 | ≥500 soru; her birine kaynak referansı; ≥%20'si kaynak dışı (red testi için). |
| 1.4 | Ödev değerlendirme veri seti (≥300 ödev, rubrik, eğitmen puanı) | 12.04.2027 | 28.05.2027 | Eğitim Tasarımcısı | 1.1 | ≥300 anonimleştirilmiş ödev; açık rıza alındı; her ödevde en az 1 eğitmen puanı (≥%20'sinde 2 eğitmen). |
| 1.5 | Değerlendirme metodolojisi ve metrik protokolü | 19.04.2027 | 07.05.2027 | Akademik Danışman | 1.2 | Sadakat, red doğruluğu, Recall@5, ağırlıklı Kappa, WER ölçüm protokolü yazıldı. |

### İP-2 · Platform Çekirdeği (Test Yatağı)

_Son tarih: 30.07.2027 · Ay 1-4_

| ID | Görev | Başlangıç | Bitiş | Rol | Bağımlılık | Kabul kriteri |
|---|---|---|---|---|---|---|
| 2.1 | Çok kiracılı veri modeli, kimlik doğrulama ve rol yönetimi | 01.04.2027 | 23.04.2027 | Backend | — | Öğrenci / eğitmen / kurum yöneticisi / bireysel kullanıcı rolleri; kurumlar arası veri yalıtımı testli. |
| 2.2 | Ders alanları, kayıt ve davet akışı | 19.04.2027 | 14.05.2027 | Backend | 2.1 | Eğitmen ders açar; öğrenci davet/kod ile katılır; her derse ayrı alan. |
| 2.3 | Ders kaynağı yükleme ve depolama | 03.05.2027 | 28.05.2027 | Backend | 2.2 | PDF, slayt, görsel, video yüklenir; sürümlenir; YZ hattına olay gönderir. |
| 2.4 | Ödev / proje teslim modülü | 17.05.2027 | 11.06.2027 | Backend | 2.2 | Teslim tarihi, geç teslim, dosya yükleme, eğitmen puanlama ekranı. |
| 2.5 | Takvim, duyuru ve bildirimler | 31.05.2027 | 25.06.2027 | Frontend | 2.2 | Ders takvimi, ödev tarihleri, e-posta / uygulama içi bildirim. |
| 2.6 | Canlı ders entegrasyonu ve ders kaydı | 07.06.2027 | 09.07.2027 | Backend | 2.2 | Hazır altyapı (BBB/Jitsi/Meet/Zoom) entegre; kayıtlar ders kaynağına otomatik eklenir. |
| 2.7 | Bireysel (B2C) kayıt, abonelik ve ödeme altyapısı | 21.06.2027 | 23.07.2027 | Backend | 2.1 | Bireysel kullanıcı kendi dersini açabilir; abonelik planları; ödeme sağlayıcı entegrasyonu. |
| 2.8 | Platform MVP iç testi (mobil uyum dahil) | 12.07.2027 | 30.07.2027 | Frontend | 2.3, 2.4, 2.5, 2.6 | Kritik akışlar test edildi; mobil tarayıcıda çalışıyor; hata listesi kapandı. |

### İP-3 · İçerik İşleme ve Türkçe Bilgi Erişimi (AR-2, AR-5)

_Son tarih: 31.08.2027 · Ay 2-5_

| ID | Görev | Başlangıç | Bitiş | Rol | Bağımlılık | Kabul kriteri |
|---|---|---|---|---|---|---|
| 3.1 | Doküman ayrıştırma: PDF, slayt, görsel, tablo, OCR | 03.05.2027 | 28.05.2027 | YZ Mühendisi | 1.1 | Tablo ve görsel içeriği metne dönüştürülüyor; örnek setlerde doğruluk ölçüldü. |
| 3.2 | Türkçe ders transkript hattı ve kelime hata oranı ölçümü | 17.05.2027 | 18.06.2027 | YZ Mühendisi | 1.5 | Kelime hata oranı (WER) ≤ %10 hedefi ölçüldü ve raporlandı. |
| 3.3 | Türkçe parçalama stratejileri ve embedding modeli karşılaştırması | 31.05.2027 | 02.07.2027 | YZ Mühendisi | 1.3, 3.1 | ≥3 embedding modeli × ≥3 parçalama stratejisi karşılaştırma tablosu. |
| 3.4 | Hibrit arama + yeniden sıralama (hedef Recall@5 ≥ %90) | 21.06.2027 | 13.08.2027 | YZ Mühendisi | 3.3 | Test setinde Recall@5 ≥ %90 ya da sapma gerekçesi raporlandı. |
| 3.5 | İP-3 ara teknik raporu | 16.08.2027 | 31.08.2027 | YZ Mühendisi | 3.4, 3.2 | Deney sonuçları, seçilen yapı, öğrenilenler. |

### İP-4 · Kaynağa Dayalı Soru-Cevap ve Pedagojik Sınırlar (AR-1, AR-4)

_Son tarih: 29.10.2027 · Ay 4-7_

| ID | Görev | Başlangıç | Bitiş | Rol | Bağımlılık | Kabul kriteri |
|---|---|---|---|---|---|---|
| 4.1 | Atıflı (kaynak gösteren) cevap üretimi | 01.07.2027 | 30.07.2027 | YZ Mühendisi | 3.3 | Her cevapta sayfa / slayt / zaman damgası atfı. |
| 4.2 | Kaynak dışı soruları reddetme ve belirsizlik tespiti | 19.07.2027 | 27.08.2027 | YZ Mühendisi | 4.1 | Kaynak dışı soru reddetme doğruluğu ≥ %90. |
| 4.3 | Cevap-kaynak sadakat doğrulayıcı | 09.08.2027 | 17.09.2027 | YZ Mühendisi | 4.1 | Sadakat ≥ %95 (test setinde); uydurma cevaplar yakalanıp düzeltiliyor. |
| 4.4 | Sokratik mod ve ödev cevabı sızıntısını önleme | 23.08.2027 | 30.09.2027 | YZ Mühendisi | 4.1 | Ödev cevabı sızdırma oranı ≤ %2. |
| 4.5 | Saldırı (jailbreak) test seti ve dayanıklılık | 13.09.2027 | 15.10.2027 | YZ Mühendisi | 4.4 | ≥200 saldırı senaryosu; direnç ≥ %95. |
| 4.6 | Chatbot arayüzünün platforma entegrasyonu | 30.08.2027 | 08.10.2027 | Frontend | 4.1, 2.8 | Her ders sayfasında chatbot; atıflar tıklanınca kaynağa gidiyor. |
| 4.7 | İP-4 değerlendirme raporu | 11.10.2027 | 29.10.2027 | YZ Mühendisi | 4.2, 4.3, 4.4, 4.5 | AR-1 ve AR-4 hedeflerine karşı ölçüm sonuçları. |

### İP-5 · Rubrik Tabanlı Otomatik Ödev Değerlendirme (AR-3)

_Son tarih: 24.12.2027 · Ay 5-9_

| ID | Görev | Başlangıç | Bitiş | Rol | Bağımlılık | Kabul kriteri |
|---|---|---|---|---|---|---|
| 5.1 | Rubrik tanımlama arayüzü | 02.08.2027 | 27.08.2027 | Frontend | 2.4 | Eğitmen kriter, ağırlık ve seviye tanımlayabiliyor; şablon rubrikler. |
| 5.2 | Rubrik tabanlı puanlama motoru v1 | 16.08.2027 | 30.09.2027 | YZ Mühendisi | 1.4, 5.1 | Ödev → kriter bazında puan + kanıt alıntısı. |
| 5.3 | Gerekçeli ve kaynağa dayalı geri bildirim üretimi | 13.09.2027 | 22.10.2027 | YZ Mühendisi | 5.2 | Geri bildirimlerin eğitmenlerce 'kullanılabilir' bulunma oranı ≥ %80. |
| 5.4 | Eğitmen-YZ puan uyumu kalibrasyonu (hedef ağırlıklı Kappa ≥ 0,75) | 11.10.2027 | 19.11.2027 | YZ Mühendisi | 5.2 | Ağırlıklı Kappa ≥ 0,75 ya da sapma analizi; Eğitim Fakültesi danışmanıyla değerlendirildi. |
| 5.5 | Eğitmen onay akışı (YZ önerir, eğitmen onaylar) | 01.11.2027 | 26.11.2027 | Backend | 5.2 | Eğitmen YZ puanını onaylar / düzeltir; düzeltmeler kalibrasyon verisine eklenir. |
| 5.6 | (Opsiyonel) Türkçe intihal ve YZ ile yazılmış metin tespiti | 08.11.2027 | 17.12.2027 | YZ Mühendisi | 5.2 | Tespit doğruluğu ≥ %85 ya da opsiyonel kapsamdan çıkarma kararı. |
| 5.7 | İP-5 değerlendirme raporu | 13.12.2027 | 24.12.2027 | YZ Mühendisi | 5.4 | AR-3 hedeflerine karşı sonuçlar. |

### İP-6 · Ölçeklenebilirlik, KVKK ve Yurt İçi Model (AR-6)

_Son tarih: 24.12.2027 · Ay 6-9_

| ID | Görev | Başlangıç | Bitiş | Rol | Bağımlılık | Kabul kriteri |
|---|---|---|---|---|---|---|
| 6.1 | KVKK: veri envanteri, aydınlatma, açık rıza, anonimleştirme | 01.09.2027 | 24.09.2027 | DevOps | — | VERBİS ve aydınlatma metinleri güncel; öğrenci verisi anonimleştirme hattı. |
| 6.2 | Açık ağırlıklı modelin yurt içinde barındırılması ve ince ayar denemeleri | 13.09.2027 | 12.11.2027 | YZ Mühendisi | 4.1 | Yurt içi model çalışıyor; ≥2 ince ayar deneyi raporlandı. |
| 6.3 | Yurt içi model ile ticari model kalite karşılaştırması | 01.11.2027 | 03.12.2027 | YZ Mühendisi | 6.2, 4.7 | Kalite farkı ≤ %5 hedefine karşı ölçüm. |
| 6.4 | Maliyet ve gecikme optimizasyonu (yanıt ≤ 3 sn) | 15.11.2027 | 17.12.2027 | DevOps | 6.2 | Ortalama yanıt ≤ 3 sn; öğrenci başı aylık YZ maliyeti hesaplandı. |
| 6.5 | Yük testi | 06.12.2027 | 24.12.2027 | DevOps | 6.4 | Hedef eş zamanlı kullanıcı yükünde performans raporu. |

### İP-7 · Pilot Uygulama

_Son tarih: 10.03.2028 · Ay 7-12_

| ID | Görev | Başlangıç | Bitiş | Rol | Bağımlılık | Kabul kriteri |
|---|---|---|---|---|---|---|
| 7.1 | Pilot planı ve kullanım ölçüm altyapısı | 04.10.2027 | 29.10.2027 | Proje Yöneticisi | 2.8 | Aktif kullanıcı, kullanım sıklığı, memnuniyet, eğitmenin kazandığı süre ölçülüyor (Faz 2 için kanıt). |
| 7.2 | Pilot 1: kendi öğrencilerimizle gerçek ortam testi | 01.11.2027 | 24.12.2027 | Proje Yöneticisi | 7.1, 4.7 | Aylık 200-300 öğrencinin en az %50'si platformu kullandı; metrikler toplandı. |
| 7.3 | Pilot 2: en az 1 dış kurum (ücretli ya da sözleşmeli) | 03.01.2028 | 25.02.2028 | Yönetim | 7.2 | En az 1 dış kurum aktif kullanıyor; tercihen ücretli sözleşme. |
| 7.4 | Pilot raporu | 21.02.2028 | 10.03.2028 | Proje Yöneticisi | 7.3 | Kullanım ve öğrenme etkisi metrikleri, kullanıcı geri bildirimi. |

### İP-8 · Fikri Mülkiyet, Ticarileşme ve Faz 2 Başvurusu

_Son tarih: 31.03.2028 · Ay 8-12. Faz 2 başvurusu en geç 31.01.2028 (bitişten ≥60 gün önce)._

| ID | Görev | Başlangıç | Bitiş | Rol | Bağımlılık | Kabul kriteri |
|---|---|---|---|---|---|---|
| 8.1 | Faz 2 (sanal sınıf) proje dosyasının hazırlanması | 15.11.2027 | 31.12.2027 | Proje Yöneticisi | 4.7 | Faz 2 dosyası, Faz 1 pilot verileriyle hazır. |
| 8.2 | Faz 2 başvurusunun Yıldız'a teslimi (son tarih 31.01.2028) | 03.01.2028 | 14.01.2028 | Proje Yöneticisi | 8.1 | Başvuru teslim edildi. 60 gün kuralı ve 90 gün projesiz kalma riski kapatıldı. |
| 8.3 | Yazılım eser tescili ve patent / faydalı model ön değerlendirmesi (Yıldız TTO) | 01.12.2027 | 28.01.2028 | Proje Yöneticisi | 4.7 | En az 1 tescil başvurusu; patentlenebilirlik görüşü alındı. |
| 8.4 | B2B ve B2C satış paketi, fiyatlama, sözleşme şablonları | 13.12.2027 | 11.02.2028 | Yönetim | 7.2 | Fiyat listesi, kurumsal sözleşme şablonu, KVKK eki, tanıtım materyali. |
| 8.5 | Faz 1 proje sonuç raporu | 01.03.2028 | 17.03.2028 | Proje Yöneticisi | 7.4 | Tüm AR hedeflerine karşı sonuçlar, çıktılar, ticarileşme durumu. |
| 8.6 | Proje bitirme belgesi başvurusu | 13.03.2028 | 31.03.2028 | Proje Yöneticisi | 8.5 | Başvuru yapıldı (süreç ortalama 30 gün). |

## 6. Kanban kuralları

- Kolonlar: **Backlog → Bu hafta → Devam ediyor → İncelemede → Tamamlandı.** GitHub'da her görev bir issue; kolon durumu `durum:*` etiketiyle izlenir.
- Bir görev ancak **kabul kriteri** sağlandığında kapatılır. Kriter rakamsa (ör. Recall@5 ≥ %90) ölçüm sonucu issue'ya yorum olarak eklenir. Bu kayıtlar ileride hakem ve Bakanlık denetimi için kanıt olur.
- `kritik` etiketli görevlerdeki gecikme haftalık toplantıda ele alınır; kritik yol: **H-04 → H-05 → H-14 → D-01 → D-03 → D-04 → D-06 → D-08 → Faz 1 başlangıcı.**
- Tarih değişirse önce `plan/faz1-plan.json` güncellenir, sonra belge yeniden üretilir ve issue tarihleri eşitlenir.

