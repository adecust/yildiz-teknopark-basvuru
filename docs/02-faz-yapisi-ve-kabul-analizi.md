# Güncellenmiş Faz Yapısı ve Kabul Analizi

**Tarih:** 23.11.2026
**Dayanak:** `docs/01-yildiz-teknopark-arastirma-raporu.md` (değerlendirme ölçütleri, hakem formu ağırlıkları, Yıldız yönergesi kuralları)

> **Varsayımlar** (henüz cevaplanmadı, cevaplara göre güncellenecek): mevcut yazılım ekibi yok ya da küçük; eğitimler çeşitli alanlarda; platform ileride başka kurumlara da satılabilir.

---

## 1. Yeni faz yapısı

| | Eski | Yeni |
|---|---|---|
| **Faz 1** | Eğitim platformu (LMS) | **Eğitim platformu + kaynağa dayalı YZ** (eski Faz 1 ve Faz 2 birleşti) |
| **Faz 2** | Kaynağa dayalı YZ (ödev kontrolü, soru-cevap) | **Avatarlı sanal sınıf + sınıf içi YZ asistanı** (eski Faz 3) |
| **Faz 3** | Sanal sınıf | — (yerine ileride öğrenme analitiği/kişiselleştirme projesi önerilebilir; bkz. bölüm 7) |

Teknopark kurallarına göre her faz **ayrı bir TGB projesi** olarak başvurulacak. Her proje en az 6, en fazla 12 ay sürüyor. Bir sonraki proje, mevcut proje bitmeden en az 60 gün önce başvurulmalı. 90 gün projesiz kalan firma ihraç ediliyor.

```
Ay:     1    2    3    4    5    6    7    8    9   10   11   12 | 13 ...  24
Faz 1:  [========= Platform + Kaynağa Dayalı YZ (12 ay) =========] |
Faz 2:                                    hazırlık ─► başvuru ─► [==== Sanal Sınıf (12 ay) ====]
                                          (Ay 8-9)   (Ay 10)      (Ay 13'te başlar)
```

---

## 2. FAZ 1: Eğitim platformu + kaynağa dayalı eğitim YZ'si

### 2.1 Hakeme sunulacak proje adı (öneri)
**"Türkçe Eğitim İçeriği İçin Kaynağa Dayalı (Grounded) Üretken Yapay Zekâ ile Soru-Cevap ve Rubrik Tabanlı Otomatik Ödev Değerlendirme Platformu"**

Başlıkta "platform" kelimesi en sonda yer alıyor. Hakem ilk olarak YZ'yi, yani Ar-Ge çekirdeğini görmeli.

### 2.2 Kapsam: iki katman

**A) Platform katmanı ("test yatağı")**
Bu katman Ar-Ge değil, ama YZ'nin çalışacağı ve ölçüleceği zemin. Toplam iş yükünün **en fazla %25–30'u** olmalı ve dosyada kısa anlatılmalı.

- Kullanıcı ve rol yönetimi: öğrenci, eğitmen, kurum yöneticisi; kurumlar birbirinden tamamen ayrı (çok kiracılı)
- Ders alanları: her ders için ayrı bölüm, kayıt ve davet
- Kaynak yükleme: ders notu, PDF, slayt, video
- Ödev ve proje yükleme, teslim tarihleri
- Takvim, duyuru ve bildirimler
- Canlı ders: hazır altyapı entegrasyonu (BigBlueButton, Jitsi veya Google Meet/Zoom API). **Sıfırdan video altyapısı yazılmamalı.**
- Ders kayıtları ve otomatik transkript (YZ'nin kaynağına dönüşüyor; aşağıda AR-5)
- Mobil uyumlu web arayüzü

**B) Ar-Ge katmanı: projenin asıl değeri**
Her araştırma sorusu ölçülebilir bir hedefle birlikte yazılmalı:

| # | Araştırma sorusu / teknik belirsizlik | Ölçülebilir hedef (öneri) |
|---|---|---|
| **AR-1** | **Kaynağa sadakat:** YZ yalnızca o derse yüklenen kaynaklardan cevap verebilir mi, kaynakta olmayanı uydurmadan "bu kaynaklarda yok" diyebilir mi? | Cevapların kaynağa sadakati ≥ %95; kaynak dışı soruları doğru reddetme ≥ %90; her cevapta sayfa/slayt atfı |
| **AR-2** | **Türkçe bilgi erişimi:** Türkçe eğitim içeriğinde (sondan eklemeli dil, terim karışıklığı, formül, tablo) doğru parçayı bulma | Türkçe test setinde ilk 5 sonuçta doğru kaynak (Recall@5) ≥ %90 |
| **AR-3** | **Rubrik tabanlı otomatik ödev değerlendirme:** YZ, eğitmenin rubriğine göre insan eğitmene yakın puan ve gerekçeli geri bildirim verebilir mi? | Eğitmen puanıyla uyum (Ağırlıklı Kappa) ≥ 0,75; geri bildirimlerin eğitmen tarafından "kullanılabilir" bulunma oranı ≥ %80 |
| **AR-4** | **Pedagojik sınırlar:** Öğrenciye ödevin cevabını doğrudan vermeyip yönlendiren (Sokratik) davranış; manipülasyona ("jailbreak") direnç | Ödev cevabı sızdırma oranı ≤ %2; saldırı test setinde direnç ≥ %95 |
| **AR-5** | **Çok kaynaklı içerik işleme:** PDF, slayt, görsel ve ders video transkriptinin tek bilgi tabanında birleşmesi | Transkriptte Türkçe kelime hata oranı ≤ %10; görsel ve tablo içeriğinden doğru cevap ≥ %85 |
| **AR-6** | **Ölçeklenebilirlik ve veri egemenliği:** KVKK uyumlu, yurt içinde barındırılan ve açık ağırlıklı model seçeneğiyle düşük maliyet ve gecikme | Yanıt süresi ≤ 3 sn; öğrenci başı aylık YZ maliyeti hedefi; yurt içinde çalışan model ile ticari model arasındaki kalite farkı ≤ %5 |
| AR-7 *(opsiyonel)* | Ödevlerde intihal ve YZ ile yazılmış metin tespiti | Türkçe metinde tespit doğruluğu ≥ %85 |

**Başlangıç ve hedef teknoloji hazırlık seviyesi:** Başlangıç TRL 2–3 (kavram ve literatür), hedef TRL 6–7 (gerçek ortamda, sizin öğrencilerinizle pilot).

### 2.3 Tekniğin bilinen durumu ve farkımız
Bu tablo hakemin "tekniğin bilinen durumunu aşıyor mu?" sorusunu (%6) ve "yenilik" sorusunu (%10) cevaplıyor:

| Rakip | Ne yapıyor | Eksik kaldığı nokta (bizim farkımız) |
|---|---|---|
| Moodle, Canvas, Google Classroom | LMS | YZ sonradan eklenti olarak geliyor; kaynağa kilitli değil; Türkçe zayıf |
| ChatGPT Edu, Gemini for Education | Genel YZ asistanı | Ders kaynağıyla sınırlı değil, uydurabiliyor; rubrikle ödev puanlamıyor; veriler yurt dışında |
| NotebookLM | Kaynağa dayalı soru-cevap | LMS değil; ödev değerlendirme ve pedagojik sınır yok; kurumsal sınıf yapısı yok |
| Khanmigo | Sokratik öğretmen asistanı | Kendi içeriğine bağlı; eğitmenin kendi kaynağını kullanmıyor; Türkçe yok |
| Yerli LMS'ler | Uzaktan eğitim altyapısı | Üretken YZ ve otomatik değerlendirme yok ya da sınırlı |

**Konumlandırma cümlesi:** "Eğitmenin kendi kaynağına kilitlenen, Türkçe için optimize edilmiş, rubriğe göre ödev değerlendirebilen ve verisi yurt içinde kalan ilk entegre eğitim platformu."

### 2.4 İş paketleri (12 ay, üst seviye)
Ayrıntılı kanban sonraki belgede çıkarılacak.

| İP | Ad | Ay | Ana çıktı |
|---|---|---|---|
| İP-0 | Proje yönetimi, teknopark raporlaması | 1–12 | Aylık muafiyet ve proje izleme raporları |
| İP-1 | Gereksinim analizi, literatür ve patent taraması, **Türkçe test veri setlerinin oluşturulması** | 1–2 | SOTA raporu; soru-cevap ve ödev test setleri (kendi derslerinizden) |
| İP-2 | Platform çekirdeği (test yatağı) | 1–4 | Rol yönetimi, ders alanları, kaynak ve ödev yükleme, takvim, canlı ders entegrasyonu |
| İP-3 | İçerik işleme ve Türkçe bilgi erişimi (AR-2, AR-5) | 2–5 | Parçalama, vektörleme, transkript hattı; Recall@5 ölçümü |
| İP-4 | Kaynağa dayalı soru-cevap motoru ve pedagojik sınırlar (AR-1, AR-4) | 4–7 | Atıflı chatbot, kaynak dışını reddetme, saldırı testleri |
| İP-5 | Rubrik tabanlı otomatik ödev değerlendirme (AR-3) | 5–9 | Puanlama ve geri bildirim modülü; eğitmen uyum ölçümü |
| İP-6 | Ölçeklenebilirlik, KVKK, yurt içi model (AR-6) | 6–9 | Maliyet ve gecikme optimizasyonu, model karşılaştırması |
| İP-7 | **Pilot:** kendi öğrencilerinizle gerçek ortam testi | 8–11 | Pilot raporu, kullanıcı metrikleri |
| İP-8 | Fikri mülkiyet, ticarileşme hazırlığı, **Faz 2 başvurusu** | 9–12 | Yazılım tescili, patent/faydalı model ön başvurusu, B2B satış paketi; Faz 2 dosyası **Ay 10'da teslim** |

### 2.5 Faz 1 ekibi (minimum öneri)
| Rol | Sayı | Not |
|---|---|---|
| Proje yöneticisi / ürün sahibi | 1 | Siz ya da teknik bir yönetici |
| YZ / dil işleme mühendisi | 2 | Ar-Ge çekirdeği; en az biri yüksek lisans ya da deneyimli olmalı |
| Backend geliştirici | 1–2 | Platform ve YZ servisleri |
| Frontend / mobil geliştirici | 1 | |
| DevOps / güvenlik (yarı zamanlı) | 0,5 | KVKK, barındırma |
| Eğitim tasarımcısı / alan uzmanı | 1 | Destek personeli; rubrik ve test seti hazırlığı. Sizin eğitmenlerinizden biri olabilir |
| **YTÜ akademik danışman** | 2 | Biri Bilgisayar Mühendisliği'nden (dil işleme/YZ), biri Eğitim Fakültesi'nden (ölçme-değerlendirme) |
| Stajyer / tez öğrencisi | 1–2 | YTÜ'den. Hem KPI hem üniversite iş birliği puanı sağlar |

Kurallar hatırlatması: destek personeli Ar-Ge personelinin yaklaşık %10'unu, kapsam dışı personel %15'ini geçmemeli.

---

## 3. FAZ 1 KABUL ANALİZİ

### 3.1 1. kapı: Aday Girişimci Değerlendirme Komisyonu

| Ölçüt (Yönerge md. 10.1) | Durum | Açıklama |
|---|---|---|
| TGB misyonuna uygunluk | 🟢 | EdTech + üretken YZ; formda EdTech seçeneği var; Yıldız'ın YILDIZ TECH dizisinin ilki eğitim teknolojileriydi |
| Milli sanayiye/teknolojiye katkı | 🟢 | Yerli LMS ve yerli eğitim YZ'si; veri egemenliği; yabancı lisansların (Canvas, Zoom, ChatGPT Edu) ikamesi |
| Projenin niteliği | 🟡 → 🟢 | Ar-Ge çekirdeği öne çıkarılırsa güçlü. LMS ağırlıklı anlatılırsa zayıf |
| Ticarileşme açısından nicelik | 🟢 | Aylık ~20 milyon TL gelir, hazır öğrenci kitlesi, pilot sahası |
| Firmanın Ar-Ge kapasitesi | 🔴 → 🟡 | **En büyük soru işareti.** Bir eğitim firmasının yazılım ve YZ geliştirme yetkinliği sorgulanacak. Çözüm: ekip planı, işe alım takvimi, YTÜ danışmanları |
| "Mevcut iş taşınıyor" algısı | 🟡 | Eğitim hizmeti teknopark dışında kalmalı; teknoparkta yalnızca yazılım ve Ar-Ge yapılacağı açık yazılmalı |

### 3.2 2. kapı: Hakem heyeti, puan simülasyonu

> **Uyarı:** Bu bir **simülasyon**. İTÜ'nün Bakanlık onaylı form ağırlıkları kullanıldı; Yıldız'ın formu yayımlanmamış. 1–5 arası puanlar benim tahminim. Amaç, hangi kalemlerin puanı belirlediğini görmek.

Puan = ağırlık × (verilen puan / 5)

| # | Ölçüt | Ağırlık | **Eski Faz 1** (yalnız LMS) | **Yeni Faz 1, zayıf hazırlık** | **Yeni Faz 1, güçlü hazırlık** |
|---|---|---|---|---|---|
| 4 | Yenilik | 10 | 1 → 2,0 | 2 → 4,0 | 4 → 8,0 |
| 5 | Uygulanabilirlik | 6 | 5 → 6,0 | 4 → 4,8 | 4 → 4,8 |
| 6 | Tekniğin bilinen durumunu aşma | 6 | 1 → 1,2 | 2 → 2,4 | 3 → 3,6 |
| 7 | Ticarileşme | 15 | 3 → 9,0 | 3 → 9,0 | 5 → 15,0 |
| 8 | İthal ikame / ihracat | 15 | 2 → 6,0 | 3 → 9,0 | 4 → 12,0 |
| 9 | Kalite / standart | 5 | 2 → 2,0 | 3 → 3,0 | 4 → 4,0 |
| 10 | Verimlilik | 5 | 3 → 3,0 | 4 → 4,0 | 5 → 5,0 |
| 11 | Maliyet iyileştirme | 6 | 3 → 3,6 | 3 → 3,6 | 4 → 4,8 |
| 12 | Teknolojik bilgi / know-how | 10 | 1 → 2,0 | 2 → 4,0 | 4 → 8,0 |
| 13 | Katma değer | 6 | 2 → 2,4 | 3 → 3,6 | 4 → 4,8 |
| 14 | Üniversite-sanayi iş birliği | 10 | 1 → 2,0 | 1 → 2,0 | 5 → 10,0 |
| 15 | Ekip uzmanlığı | 6 | 3 → 3,6 | 2 → 2,4 | 3 → 3,6 |
| | **TOPLAM / 100** | | **≈ 43** ❌ | **≈ 52** ❌ | **≈ 84** ✅ |

İTÜ'de eşik 70/100. Yıldız'da 3 hakemden 2'sinin olumlu oyu yeterli.

**Sonuç:** Aynı fikir, hazırlığa göre ya ~52 ile reddedilir ya da ~84 ile rahat geçer. **Fark fikirde değil; dosyanın nasıl kurulduğunda.**

"Zayıf" ile "güçlü" hazırlık arasındaki farkı yaratan 5 kalem (toplam ~32 puan):
1. **İsimli YTÜ akademisyen danışman** → +8 puan (ölçüt 14)
2. **B2B SaaS ticarileşme planı** (başka kurs, okul ve kurumlara satış) + somut fiyatlama → +6 (ölçüt 7)
3. **Ölçülebilir Ar-Ge hedefleri ve SOTA tablosu** → yenilik, know-how ve teknik ölçütlerde toplam +9
4. **İhracat hedefi** (Türk cumhuriyetleri, Arapça/İngilizce sürüm yol haritası) + ithal ikame anlatısı → +3 (ölçüt 8)
5. Kalite, verimlilik ve maliyet kalemlerinin **rakamla** yazılması (örneğin "eğitmenin ödev okuma süresinde %60 azalma") → +4

### 3.3 Faz 1 için risk tablosu

| Risk | Olasılık | Etki | Önlem |
|---|---|---|---|
| Hakem projeyi "rutin LMS + hazır YZ API'si" olarak görür | Orta | **Çok yüksek** | Ar-Ge çekirdeğini başlığa ve özete taşımak; platformu "test yatağı" olarak kısa anlatmak; AR-1…AR-6 hedeflerini ölçülebilir yazmak |
| "Sadece OpenAI/Gemini API'si çağırıyorlar" eleştirisi | Yüksek | Yüksek | Ar-Ge'nin modelin kendisinde değil, **erişim, doğrulama, sadakat kontrolü, rubrik hizalama, Türkçe uyarlama ve yurt içi model ince ayarında** olduğunu göstermek; model karşılaştırma deneyleri |
| Firmanın Ar-Ge kapasitesi zayıf görünür | Yüksek | Yüksek | Ekibin özgeçmişleri; teknik lider; YTÜ danışmanları; gerekirse deneyimli bir teknik ortak |
| 12 aya sığmama | Orta | Orta | Platformda hazır bileşenler (canlı ders entegrasyonu, açık kaynak modüller); AR-7'nin opsiyonel tutulması |
| Eğitim geliri ile Ar-Ge kazancının karışması | Orta | Orta (vergi) | Ayrı teknopark şubesi ya da Ar-Ge şirketi; platform lisansının eğitim şirketine **bedelle** verilmesi (transfer fiyatlandırması); mali müşavir görüşü |
| KVKK: öğrenci verisi ve ödevler YZ'ye gidiyor | Orta | Yüksek | Yurt içi barındırma, açık rıza, anonimleştirme; AR-6 zaten bunu Ar-Ge kalemi yapıyor |

### 3.4 Faz 1 kabul değerlendirmesi

| Senaryo | Değerlendirme |
|---|---|
| Eski Faz 1 (yalnız LMS) | **Düşük.** Ar-Ge niteliği yok; büyük olasılıkla ret |
| Yeni Faz 1, ama LMS ağırlıklı anlatım, akademisyen yok, yalnızca kendi kullanımı | **Düşük–orta.** Komisyondan geçebilir, hakemde zorlanır |
| **Yeni Faz 1 + bölüm 5'teki 7 zorunlu şart** | **Yüksek.** Güçlü bir aday profili |

---

## 4. FAZ 2: Avatarlı sanal sınıf + sınıf içi YZ asistanı

### 4.1 Önerilen proje adı
**"Web Tabanlı, Ölçeklenebilir Çok Kullanıcılı Sanal Sınıf Ortamında Kaynağa Dayalı YZ Öğretmen Asistanı ve Etkileşim Analitiği"**

### 4.2 Kapsam
- Avatar oluşturma (kişiselleştirilebilir, düşük donanımda çalışan)
- 3B ya da 2,5B sanal sınıflar, çalışma odaları, ortak beyaz tahta ve dosya paylaşımı
- **Mekânsal ses:** yakındaki kişiyi duyma, grup çalışması
- Öğretmene soru sorma, söz isteme, sınıf içi anket ve quiz
- **Faz 1 YZ'sinin sınıfa "asistan karakter" olarak girmesi:** öğrencilerin sorularını o dersin kaynağıyla yanıtlayan ve öğretmene özet veren bir ajan
- Sınıf içi etkileşim analitiği (katılım, grup dinamiği; KVKK sınırları içinde)

### 4.3 Ar-Ge soruları ve hedefleri

| # | Teknik belirsizlik | Ölçülebilir hedef (öneri) |
|---|---|---|
| AR-1 | Kurulum gerektirmeyen tarayıcı tabanlı, çok kullanıcılı gerçek zamanlı senkronizasyon | Sınıf başı ≥ 50 eş zamanlı kullanıcı; durum senkron gecikmesi ≤ 150 ms |
| AR-2 | Düşük bant genişliği ve düşük donanımda çalışma (Türkiye ve hedef ihracat ülkeleri koşulları) | 2 Mbps bağlantıda ve orta seviye telefonda ≥ 30 FPS |
| AR-3 | Mekânsal ses ve grup çalışmasının ölçeklenmesi | Ses gecikmesi ≤ 200 ms; 10 paralel çalışma odası |
| AR-4 | Çok katılımcılı ortamda YZ ajanının bağlamı anlaması (kim sordu, hangi konuşma, hangi ders) | Doğru bağlam atfı ≥ %90; Faz 1 sadakat hedeflerinin korunması |
| AR-5 | Gizliliği koruyan etkileşim analitiği | Kişisel veri işlemeden grup düzeyinde katılım metrikleri; öğretmen faydalılık puanı ≥ 4/5 |

### 4.4 Faz 2 kabul analizi
Faz 2'de teknoparka zaten kiracı olarak bakılacak, ama **proje yine aynı hakem sürecinden geçecek** (Yönerge md. 10.2.1).

| # | Ölçüt | Ağırlık | Tahmini puan |
|---|---|---|---|
| 4 | Yenilik | 10 | 4 → 8,0 |
| 5 | Uygulanabilirlik | 6 | 3 → 3,6 *(kullanıcı benimsemesi ve donanım belirsizliği)* |
| 6 | Tekniğin bilinen durumunu aşma | 6 | 3 → 3,6 |
| 7 | Ticarileşme | 15 | 3–4 → 9,0–12,0 |
| 8 | İthal ikame / ihracat | 15 | 3–4 → 9,0–12,0 |
| 9 | Kalite / standart | 5 | 3 → 3,0 |
| 10 | Verimlilik | 5 | 3 → 3,0 |
| 11 | Maliyet | 6 | 3 → 3,6 |
| 12 | Know-how | 10 | 4 → 8,0 |
| 13 | Katma değer | 6 | 4 → 4,8 |
| 14 | Üniversite-sanayi | 10 | 4 → 8,0 |
| 15 | Ekip | 6 | 3–4 → 3,6–4,8 |
| | **TOPLAM** | | **≈ 71–78** 🟡 |

**Değerlendirme: Orta–yüksek, sınırda.** Teknik yenilik güçlü, ama hakemler şunları soracak:
- "Sanal sınıfı öğrenciler gerçekten kullanır mı?" Bunun cevabı **Faz 1 pilotundan gelen gerçek kullanım verisi** olacak.
- "Gather, Spatial, Frame VR'dan farkı ne?" Fark, **YZ asistanının ders kaynağına kilitli olması ve Faz 1 platformuyla tam entegrasyon**.

**Faz 2'nin kabulünü güçlendirecekler:**
1. Faz 1 pilot metrikleri: aktif kullanıcı, memnuniyet, eğitmenin kazandığı zaman. **Bunun için Faz 1'de ölçüm altyapısı baştan kurulmalı.**
2. Faz 1'den en az bir **ödeme yapan dış kurum müşterisi**. Ticarileşme puanını 3'ten 5'e çıkarır.
3. Faz 1'den çıkan fikri mülkiyet (yazılım tescili, patent başvurusu). Know-how kanıtı olur.
4. Yıldız'ın **Gametech** dikeyine ve YTÜ'nün oyun/simülasyon tarafındaki akademisyenlerine bağlanmak.
5. Gerekirse Faz 2'yi ikiye bölmek. Örneğin 2a: sanal sınıf altyapısı, 2b: YZ ajanı ve analitik. Her biri 12 ay sınırına rahat sığar, zincir de uzar.

---

## 5. Kabul için 7 zorunlu şart (başvurudan önce tamamlanmalı)

| # | Şart | Neden | Etkilediği yer |
|---|---|---|---|
| 1 | **Ar-Ge çekirdeğini başlığa, özete ve sunumun ilk slaytlarına taşımak**; platformu "test yatağı" olarak konumlamak | En sık red nedeni "rutin yazılım" | Aday komisyon + ölçüt 4, 6, 12 |
| 2 | **YTÜ'den isimli 2 akademik danışman** (Bilgisayar Mühendisliği + Eğitim Fakültesi), niyet mektubuyla | %10 ağırlık; iki hakem de akademisyen | Ölçüt 14 + formdaki zorunlu soru |
| 3 | **B2B SaaS ticarileşme planı:** başka kurslar, okullar, üniversiteler, kurumsal eğitim birimleri; fiyatlama; ilk 3 hedef müşteri | Ticarileşme %15; ayrıca eğitim hizmeti geliri vergi istisnasına girmiyor | Ölçüt 7 + vergi |
| 4 | **AR-1…AR-6 için ölçülebilir hedefler** ve **SOTA karşılaştırma tablosu** | "Tekniğin bilinen durumunu aşma" ancak rakamla kanıtlanır | Ölçüt 4, 6, 12 |
| 5 | **Ekip planı:** en az 1 deneyimli YZ/dil işleme mühendisi isimle; işe alım takvimi | "Eğitim firmasının Ar-Ge kapasitesi" sorusu | Aday komisyon + ölçüt 15 |
| 6 | **İhracat ve ithal ikame anlatısı:** ikame edilen yabancı ürünler, döviz etkisi, hedef ülkeler ve dil sürümleri | %15 ağırlık; Yıldız'ın "global" vurgusu | Ölçüt 8 |
| 7 | **Yapısal ayrım:** teknopark şubesi ya da ayrı Ar-Ge şirketi kararı; eğitim hizmetinin teknopark dışında kalması; ana sözleşme kontrolü | "Mevcut iş taşınıyor" algısı ve vergi uyumu | Aday komisyon + mali yapı |

---

## 6. Genel sonuç

| Faz | Eski yapı | Yeni yapı (+ 7 şart) |
|---|---|---|
| **Faz 1** | Düşük (≈43/100, ret) | **Yüksek (≈84/100)** |
| **Faz 2** | — | **Orta–yüksek (≈71–78/100)**; Faz 1 pilot verisi ve ilk dış müşteriyle güçlenir |

**Faz birleştirme kararı doğru.** Kabulü Ar-Ge'si en güçlü olan YZ belirleyecek; platform da onun etrafında kurulacak. Kalan risk büyük ölçüde **ekip ve akademik iş birliği** tarafında. İkisi de başvurudan önce çözülebilir.

---

## 7. İleriye dönük not: zincirin devamı (Faz 3 adayı)

90 gün projesiz kalmamak için Faz 2 bitmeden yeni bir proje gerekecek. Faz 1 ve 2'nin doğal devamı olarak:
- **Uyarlanabilir öğrenme ve öğrenci modelleme:** öğrencinin hangi kavramı bilmediğini tahmin etme (bilgi izleme), kişisel çalışma rotası, kaynaktan otomatik soru üretme, ders bırakma riski için erken uyarı.

Bu proje, Faz 1 ve Faz 2'de toplanan verileri kullanacağı için Ar-Ge kanıtı en güçlü olan proje olur.

---

## 8. Netleşmesi gerekenler (cevaplara göre bu belge güncellenecek)

1. Öğrenci ve eğitmen sayısı; eğitim alanları (YZ test setleri bunlara göre hazırlanacak)
2. Şirket içinde yazılım ekibi var mı?
3. Platformun dış kurumlara satışı: hedef müşteri tipi
4. Şube mi, ayrı Ar-Ge şirketi mi? (Mali müşavir görüşü)
5. YTÜ'de tanıdık bir akademisyen var mı?
6. Hedeflenen başvuru tarihi
