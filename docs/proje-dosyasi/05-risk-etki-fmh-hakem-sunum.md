# PROJE DOSYASI · 05 · Risk, Etki, Fikri Mülkiyet ve Hakem Hazırlığı

Bu bölüm hakem formundaki **kalite/standart (%5), verimlilik (%5), maliyet (%6), katma değer (%6)** ölçütlerini besliyor. Ayrıca hakem soru-cevap provasını ve zorunlu "Firma/Proje Sunumu"nun slayt metnini içeriyor.

---

## 1. Risk yönetimi

O = olasılık, E = etki (1–5).

| # | Risk | Tür | O | E | Önlem | B planı | Sahibi |
|---|---|---|---|---|---|---|---|
| R1 | Hakem projeyi "rutin LMS + hazır YZ API'si" olarak görür | Başvuru | 3 | 5 | Ar-Ge çekirdeği başlıkta ve özette; platform %24 efor ile sınırlı; ölçülebilir AR hedefleri; PoC verisi | Revize edip yeniden başvuru (reddedilen proje revizyonla tekrar sunulabilir) | Proje yöneticisi |
| R2 | YTÜ akademisyen eşleştirmesi gecikir | Başvuru | 3 | 3 | TTO talebi ilk hafta; iki ayrı alan için paralel arayış | Formda "planlanıyor"; niyet mektubu detaylı proje dosyasına (Ocak) | Proje yöneticisi |
| R3 | Kıdemli YZ mühendisi işe alınamaz | Organizasyon | 3 | 4 | Erken ilan; rekabetçi teklif; teknopark gelir vergisi istisnası net ücreti artırıyor | Danışman sözleşmeli uzman + akademik danışman desteği; mevcut ekipten yetiştirme | Yönetim |
| R4 | QWK ≥ 0,75 hedefine ulaşılamaz | Teknik | 3 | 3 | E-3 deney kolları; rubrik iyileştirme; kalibrasyon | Asistan modu: kanıt + taslak geri bildirim, puan eğitmende (değer korunur) | Teknik lider |
| R5 | Sadakat ve reddetme hedefleri birlikte sağlanamaz | Teknik | 2 | 4 | Ceza-duyarlı eşik; iddia doğrulama | Kurum bazlı eşik; "kısmi cevap" şablonu | Teknik lider |
| R6 | Yerli açık model kalitesi yetersiz kalır | Teknik | 2 | 3 | Birden çok aday model (E-6); ince ayar | Hibrit: anonimleştirilmiş zor görevler ticari API'de (kurum izniyle) | Teknik lider |
| R7 | GPU maliyeti veya erişimi | Teknik/Mali | 2 | 3 | Yurt içi bulut + nicemleme + önbellek | Satın alma (KDV istisnası) veya alternatif sağlayıcı | DevOps |
| R8 | KVKK ihlali / veri sızıntısı | Hukuki | 1 | 5 | Satır düzeyi güvenlik, şifreleme, sızma testi, yurt içi barındırma | Olay müdahale planı, 72 saat bildirim prosedürü | DevOps + hukuk |
| R9 | AB YZ Yasası takvimi veya yorumu değişir | Regülasyon | 3 | 2 | Tasarım zaten insan gözetimli ve kayıt tutuyor | AB girişini erteleme; Türk dilli pazarlara öncelik | Yönetim |
| R10 | Google ve benzerleri Türkiye'de agresif fiyatlar | Ticari | 4 | 3 | Segment odağı (kurs, kurumsal, kurum içi kurulum); yurt içi veri; ölçülmüş kalite | Kurum içi kurulum ve API kanalına ağırlık | Yönetim |
| R11 | Dış kurum pilotu bulunamaz | Ticari | 2 | 4 | İlk 3 hedef kurum listesi (G-006); Yıldız ağı; ücretsiz pilot teklifi | Kendi şubelerimiz veya ortak kurslar | Yönetim |
| R12 | Faz 2 başvurusu gecikir → 90 gün kuralı | Takvim | 2 | 5 | KT-6 kaydırılamaz; G-014 Kasım 2027'de başlar | Faz 1 ek süre talebi (en fazla %30, bir kez) **ve** Faz 2 erken başvuru | Proje yöneticisi |
| R13 | Eğitim geliri ile Ar-Ge kazancı karışır (vergi denetimi) | Mali | 2 | 4 | Şube muhasebesi, ayrıştırma yöntemi, mali müşavir | YMM görüşü; gerekirse ayrı Ar-Ge şirketi | Mali müşavir |
| R14 | Öğrenci veya eğitmen benimsemesi düşük | Ticari | 2 | 3 | Eğitmen eğitimi; ders içi tanıtım; geri bildirim döngüsü | Özellik önceliklerini pilot verisine göre değiştirme | Proje yöneticisi |
| R15 | 31.12.2028 teşvik süresi uzatılmaz | Mevzuat | 2 | 3 | Mevzuat takibi | Faz 2 iş modeli teşviksiz senaryoya göre de kârlı kurgulanır | Mali müşavir |

---

## 2. Etkiler

| Hakem ölçütü | Etki | Ölçüm |
|---|---|---|
| **Kalite / standart (%5)** | Kaynağa dayalı, atıflı ve doğrulanmış YZ yanıtları; **AB YZ Yasası yüksek risk gereklerine** (insan gözetimi, kayıt, şeffaflık) göre tasarım; WCAG 2.2 AA erişilebilirlik; OWASP ASVS L2; ISO/IEC 27001 hazırlığı (36 ay hedefi) | Kalite panosu metrikleri; sızma testi raporu; erişilebilirlik denetimi |
| **Verimlilik (%5)** | Eğitmenin ödev değerlendirme süresinde ≥ %40 azalma; ders dışı tekrar eden soruların YZ'ye kayması; ders kayıtlarının aranabilir hâle gelmesi | Pilot denek içi süre ölçümü; soru dağılımı |
| **Maliyet (%6)** | Kurumlar için 3–5 ayrı (çoğu döviz bazlı) aracın tek yerli platformda birleşmesi; yurt içi açık modelle öğrenci başı YZ maliyetinin ticari modele göre ≥ %60 düşmesi (hedef) | E-6 maliyet karşılaştırması; pilot kurum maliyet anketi |
| **Katma değer (%6)** | Yüksek nitelikli istihdam (YZ, yazılım); yerli dil modellerinin ticari kullanımı (YTÜ çıktılarının sanayiye aktarımı); ihracat edilebilir yazılım ürünü; Türkçe eğitim YZ veri setleri | İstihdam, ihracat ve yayın göstergeleri (belge 04, §5.4) |
| **Teknolojik bilgi (%10)** | Belge 02, §7'deki yöntemler, veri setleri ve raporlar | Çıktı listesi; yayın ve patent başvuruları |
| **Üniversite-sanayi (%10)** | YTÜ Bilgisayar Müh. (Türkçe dil modelleri) + Eğitim Fakültesi (ölçme-değerlendirme) danışmanlığı; stajyer ve tez öğrencileri; YTÜ modellerinin ticari ortamda sınanması; ortak yayın | Danışmanlık sözleşmeleri; yayın; stajyer sayısı |
| **Sosyal** | 7/24 ders desteği ile fırsat eşitliği (özel ders alamayan öğrenciler); Sokratik tasarımla "kopya aracı" değil öğrenme aracı; erişilebilirlik | Pilot memnuniyet ve kullanım dağılımı |
| **Çevresel / sürdürülebilirlik** | Görev bazlı küçük model kullanımı ve önbellekle enerji verimliliği; basılı materyal ihtiyacının azalması. Yıldız'ın "Sustainable Development Zone" hedefiyle uyumlu | 1.000 soru başına GPU-saat |

---

## 3. Fikri mülkiyet stratejisi

| Varlık | Koruma yolu | Not |
|---|---|---|
| Kaynak kod | FSEK eser koruması (kendiliğinden doğar); isteğe bağlı kayıt-tescil (Kültür ve Turizm Bakanlığı Telif Hakları GM) | Commit geçmişi ve sürüm arşivi = yaratım tarihi kanıtı |
| **Teknik yöntemler** | **Patent** ön değerlendirmesi (Yıldız TTO + patent vekili) | SMK'ya göre bilgisayar programları "tek başına" buluş sayılmaz; teknik etki doğuran yöntemler değerlendirilebilir **[TEYİT: patent vekili]**. Faydalı model usulleri kapsamadığı için yöntemler için uygun değil |
| Model ağırlıkları, istemler, kalibrasyon verisi | **Ticari sır** | Erişim kontrolü, gizlilik sözleşmeleri |
| Veri setleri | Ticari sır; anonim alt kümesi akademik yayında (YTÜ ile) | Rıza kapsamına göre |
| Ürün adı ve logo | **Marka** tescili (TÜRKPATENT; ihracat için Madrid sistemi) | Başvuru öncesi marka araştırması |

**Patent adayı yöntemler** (patentlenebilirlik görüşü alınacak):
1. Eğitim içeriğinde **ceza-duyarlı cevaplanabilirlik kapısı ve iddia düzeyinde atıf doğrulamayla** kaynağa kilitli yanıt üretme yöntemi
2. **Çapa tabanlı karşılaştırmalı rubrik değerlendirme, belirsizlik ölçümü ve eğitmene seçici yönlendirme** yöntemi
3. **Konuşma düzeyinde birikimli pedagojik sızıntı takibi** ve deterministik çıktı kapısı

**Yayın politikası:** Önce patent başvurusu, sonra yayın. Yayın, başvuru tarihinden sonra yapılmalı; aksi hâlde yenilik kaybolur.

---

## 4. Hakem soru-cevap provası (en olası 15 soru)

**S1. "Bu bir RAG uygulaması; ChatGPT'ye belge yükleyip soru sormaktan farkı ne? Ar-Ge nerede?"**
C: Ar-Ge, modelin kendisinde değil, **güvenilirlik katmanında**. Hazır sistemlerin ölçülmemiş üç sorunu var: kaynak dışı soruda uydurma, ödev cevabını sızdırma ve insanla uyumsuz puanlama. Bizim hedeflerimiz literatürdeki temel çizginin ötesinde ve ölçülebilir: sadakat ≥ %95 + reddetme ≥ %90 aynı anda; sızıntı ≤ %2; QWK ≥ 0,75 (literatür 0,4–0,7). Bunlara hangi yöntemle ulaşılacağı belirsiz. Bu yüzden altı deney koluyla (E-1…E-6) sistematik olarak araştırıyoruz. Sonuçlar, Türkçe eğitim için daha önce olmayan test setleriyle ölçülecek. Başvuru öncesi kavram kanıtımız bunu somutlaştırdı: cevaplanabilirlik kapısı kaynak dışı sorulardaki uydurmayı 47 soruda 12'den 1'e indirdi; buna karşılık hazır çok dilli doğrulama modeli Türkçe sayısal cümlelerde başarısız oldu. Yani sorun gerçek ve hazır bileşenlerle çözülmüyor (docs/07).

**S2. "Google artık Classroom'da NotebookLM ve Gemini'yi veriyor. Neden sizi seçsinler?"**
C: (1) Veri yurt içinde ya da kurumun kendi sunucusunda. Kamu, banka ve savunma akademileri için zorunlu; KVKK md. 9 aktarım yükünü kaldırıyor. (2) Segmentimiz Workspace okulları değil; kurslar, SEM'ler, kurumsal akademiler ve bireysel eğitmenler. Bunların kayıt, ödeme ve canlı ders ihtiyacını da karşılıyoruz. (3) Ölçülmüş güvenilirlik: sadakat, reddetme, sızıntı ve puan uyumunu kuruma şeffaf panoda gösteriyoruz. (4) Türkçe derinlik ve yerli model. (5) AB YZ Yasası uyumlu insan gözetimli değerlendirme.

**S3. "Siz bir eğitim firmasısınız. YZ geliştirme kapasiteniz var mı?"**
C: Şirket içinde yazılım ekibimiz var (platform kısmını o yürütüyor). YZ çekirdeği için kıdemli bir YZ/dil işleme mühendisi işe alıyoruz [durum]. YTÜ'den iki akademik danışmanla çalışıyoruz [isimler]. En önemlisi, rakiplerin sahip olmadığı şeye sahibiz: **gerçek öğrenciler, gerçek ders içeriği ve gerçek eğitmen puanları**. Değerlendirme Ar-Ge'si bu veri olmadan yapılamaz.

**S4. "QWK 0,75 gerçekçi mi?"**
C: Bilmiyoruz; Ar-Ge'nin konusu bu. Literatürde hazır modellerle 0,4–0,7 raporlanıyor. Rubriğin yinelemeli iyileştirilmesiyle QWK'de 0,40'a varan artış gösteren çalışmalar var (arXiv 2510.09030). Biz kriter başına kanıt çıkarımı, çapa örnekleri, çoklu örnekleme ve ders bazında kalibrasyonla hedefliyoruz. Ulaşılamazsa B planımız hazır: sistem asistan modunda kalır ve eğitmen süresini yine ≥ %40 azaltır. Bu da ürün değerini korur.

**S5. "12 ay yeter mi?"**
C: Platform hazır bileşenlerle (canlı ders için BigBlueButton, PostgreSQL) kuruluyor ve efor payı %24. Ar-Ge iş paketleri paralel ilerliyor. 7 kilometre taşı ve her birinde devam/dur kriteri var. Opsiyonel kapsam (YZ metni tespiti) baştan ayrıldı.

**S6. "Test verisi nereden, KVKK?"**
C: Kendi kurumumuzun anonimleştirilmiş ders içerikleri ve ödevleri; öğrenci ve eğitmenlerden açık rıza; 18 yaş altı için veli onayı; yurt içi barındırma. Öğrenci verisi varsayılan olarak model eğitiminde kullanılmıyor.

**S7. "Neden yerli/açık model? Ticari model daha iyi değil mi?"**
C: Üç neden: veri egemenliği, döviz bazlı maliyetin düşmesi ve kurum içi kurulum. Kalite farkı (hedef ≤ %5) bizim deneyimizin konusu (E-6). Mimari model bağımsız; kurum isterse ticari model de kullanılabiliyor.

**S8. "Kim satın alacak? Rakam verin."**
C: Belge 04, §5: kurum başı öğrenci başına 60–85 TL/ay; bireysel eğitmene 499–999 TL/ay; kurum içi kurulum lisansı. Temkinli senaryoda 2030'da ≈ 54 milyon TL. İlk müşteri kendi kurumumuz; ikincisi pilot dış kurum. [Varsa: "X kurumdan niyet mektubu aldık."]

**S9. "İthal ikame nerede?"**
C: Kurumların dövizle ödediği LMS, video konferans ve YZ aboneliklerinin yerini alıyor; yabancı YZ API'lerine bağımlılığı yerli modelle azaltıyor. İhracat önce Türk dilli ülkelere.

**S10. "Üniversite iş birliği kâğıt üstünde mi?"**
C: Danışmanlar deney tasarımını ve analizini denetliyor (çeyreklik değerlendirme). Ortak yayın hedefi var; stajyer ve tez öğrencileri projede çalışıyor; YTÜ'de geliştirilen Türkçe modeller gerçek ürün ortamında sınanıyor. YTÜ için de sanayiye aktarım çıktısı.

**S11. "Platform kısmı rutin yazılım değil mi?"**
C: Evet, öyle ve bunu ayrıştırıyoruz. Platform, YZ'nin gerçek kullanıcılarla ölçüleceği test yatağı (efor %24). Ar-Ge iddiamız YZ katmanında.

**S12. "Başarısız olursanız?"**
C: Her araştırma sorusu için B planı var (belge 02). Olumsuz sonuçlar da raporlanacak; bu, Ar-Ge'nin doğası. Ürün, asistan modu ve kurum bazlı eşiklerle değer üretmeye devam eder.

**S13. "Faz 2 nedir, neden ayrı proje?"**
C: Avatarlı, web tabanlı sanal sınıf ve içinde Faz 1 YZ'sinin bağlam farkındalıklı asistan olarak çalışması. Ayrı teknik belirsizlikler var: gerçek zamanlı çok kullanıcılı senkronizasyon, düşük bant genişliği, çok konuşmacılı bağlam. Faz 1'in pilot verisiyle tasarlanacak.

**S14. "Öğrenciler bunu kopya için kullanmaz mı?"**
C: Tam tersine; tasarımın merkezinde bu var. Sokratik mod, ipucu merdiveni, deterministik sızıntı tarayıcısı ve eğitmen kontrolü. Randomize kontrollü çalışmalar korumasız sohbet botunun öğrenmeyi düşürdüğünü, korumalı olanın düşürmediğini gösteriyor (PNAS 2025).

**S15. "Bölge dışı çalışma talebiniz var mı?"**
C: Pilot dönemindeki saha çalışmaları (kurum ziyaretleri, eğitmen eğitimleri) dışında Ar-Ge teknoparkta yürütülecek. Uzaktan çalışma talebi mevzuattaki oranlar içinde ve gerekçeli **[güncel orana göre doldurun]**.

---

## 5. Hakem formuna göre öz değerlendirme (iç simülasyon)

| # | Ölçüt | Ağırlık | Kanıt (belge) | Öz puan (1–5) |
|---|---|---|---|---|
| 4 | Yenilik | 10 | 01 §4.2, 02 §1–2 | 4 |
| 5 | Uygulanabilirlik | 6 | 02 §3–5, 04 §2–3, docs/07 (ölçülmüş PoC) | 5 |
| 6 | Tekniğin bilinen durumunu aşma | 6 | 02 §2 temel çizgi ↔ hedef | 4 |
| 7 | Ticarileşme | 15 | 04 §5, 01 §3, §5 | 4–5 |
| 8 | İthal ikame / ihracat | 15 | 01 §6 | 4 |
| 9 | Kalite / standart | 5 | 05 §2, 02 §6 | 4 |
| 10 | Verimlilik | 5 | 05 §2, 03 §9 | 4 |
| 11 | Maliyet | 6 | 05 §2, 02 AR-6 | 4 |
| 12 | Know-how | 10 | 02 §7, 05 §3 | 4 |
| 13 | Katma değer | 6 | 05 §2, 04 §5.4 | 4 |
| 14 | Üniversite-sanayi | 10 | 04 §3.1, 05 §2 | **5 (niyet mektubu varsa) / 2–3 (yoksa)** |
| 15 | Ekip | 6 | 04 §3 | 3–4 (YZ mühendisi isimle gösterilirse 4) |
| | **Tahmini toplam** | | | **≈ 80–86 / 100** (akademisyensiz ≈ 72–78) |

---

## 6. Zorunlu "Firma / Proje Sunumu"

Güncel sunum `teslim/KAYNAK-YZ_Firma_Proje_Sunumu.pdf` (düzenlenebilir hâli `.pptx`) dosyasındadır; konuşmacı notları her slayta eklenmiştir. Slayt akışı:

| # | Slayt | Ana mesaj |
|---|---|---|
| 1 | Kapak | Eğitimi güçlendiren, kaynağa dayalı Türkçe yapay zekâ |
| 2 | Sunum akışı | Dokuz bölüm |
| 3 | Kurum profili | Asıl faaliyet alanı eğitim; gelir, öğrenci ve ekip göstergeleri |
| 4 | Projenin kurumumuz için anlamı | Pedagoji öncelikli; ilk kullanıcı kurumun kendisi; ardından sektör |
| 5 | Sorun tanımı | Öğrenci, eğitmen ve kurum açısından ihtiyaç; randomize kontrollü çalışma kanıtı |
| 6 | Genel amaçlı YZ araçlarının sınırlılıkları | Kaynağa bağlılık, öğrenme, veri ve puanlama sorunları |
| 7 | Tekniğin bilinen durumu ve boşluk | Rakip karşılaştırma matrisi |
| 8 | Önerilen çözüm | Beş adımlı akış ve test yatağı platformu |
| 9 | Ar-Ge içeriği ve ölçülebilir hedefler | AR-1–AR-6: bugünkü durum ve hedef |
| 10 | Sistem mimarisi | Katmanlar ve soru-cevap hattı |
| 11 | Teknoloji altyapısı ve seçim gerekçeleri | Katman bazında seçim, gerekçe ve alternatif |
| 12 | Doğrulama yaklaşımı | Test setleri ve yöntem |
| 13 | **Kavram kanıtı: ilk ölçümler** | Gerçek ders içeriğinde ölçülen sonuçlar ve Ar-Ge için öğrenilenler (docs/07) |
| 14 | Uygulama takvimi | Faz 1 Gantt şeması ve kilometre taşları |
| 15 | Proje ekibi ve üniversite-sanayi iş birliği | Roller ve YTÜ danışmanları |
| 16 | Pazar ve ticarileşme | Pazar büyüklüğü, fiyatlama, gelir projeksiyonu |
| 17 | İthal ikame, ihracat ve mevzuata uyum | İkame edilen ürünler, ihracat yol haritası, KVKK ve AB YZ Yasası |
| 18 | Riskler ve B planları | Altı temel risk, önlem ve B planı |
| 19 | Bütçe ve finansman | ≈ 17,6 milyon TL; öz kaynak |
| 20 | Sonuç | Faz zinciri ve Yıldız Teknopark'a katkı göstergeleri |

## 7. Başvuru günü son kontrol listesi
- [ ] Form metinleri belge 00 §3'ten; özet ≥ 1200 karakter
- [ ] Aşama sorusu dürüstçe (PoC yapıldıysa "Prototip")
- [ ] Akademik iş birliği alanları güncel durumla dolduruldu
- [ ] Rakamlar form, sunum ve proje dosyasında **birebir aynı** (personel 7, bütçe, tarihler)
- [ ] 5 zorunlu evrak + sunum, OCR'lı PDF
- [ ] Sunum: `teslim/KAYNAK-YZ_Firma_Proje_Sunumu.pdf` (20 slayt); ‹…› ile işaretli tüm alanlar dolduruldu
- [ ] Başvuru teyidi kaydedildi; G-009 issue'su kapatıldı
