# PROJE DOSYASI · 01 · Problem, Pazar ve Rekabet

Bu bölüm hakem formundaki şu ölçütleri besliyor: **ticarileşme (%15), ithal ikame/ihracat (%15), yenilik (%10), tekniğin bilinen durumu (%6)**.

---

## 1. Problem: kimin, hangi acısı?

### 1.1 Paydaşlar ve sorunları

| Paydaş | Bugünkü durum | Acı noktası | Sonuç |
|---|---|---|---|
| **Öğrenci** | Ders bitince materyal dağınık (PDF, WhatsApp, video kaydı). Soru sormak için bir sonraki dersi ya da eğitmenin mesaj cevabını bekliyor | Soru anında cevapsız kalıyor; genel YZ'ye sorunca **dersle uyumsuz veya uydurma** cevap alıyor | Öğrenme kopukluğu, motivasyon kaybı, kurs bırakma |
| **Eğitmen** | Aynı soruları tekrar tekrar yanıtlıyor; ödevleri tek tek okuyup geri bildirim yazıyor | Zamanının önemli kısmı tekrar eden işlere gidiyor **[VARSAYIM: kendi eğitmenlerimizle ölçülecek, §1.3]** | Geri bildirim gecikiyor ve yüzeysel kalıyor; eğitmen ölçeklenemiyor |
| **Kurum yöneticisi** | 3–5 ayrı araç: video konferans + LMS + dosya paylaşımı + mesajlaşma + ödeme | Dağınık lisans maliyeti (çoğu **döviz bazlı**), veri bütünlüğü yok, öğrenme metriği yok | Yüksek maliyet, KVKK riski, kalite ölçülemiyor |

### 1.2 Genel amaçlı YZ neden çözüm değil?
1. **Kaynağa bağlı değil.** Genel sohbet botları dersin kendi notunu değil, eğitim verisindeki genel bilgiyi kullanıyor. Eğitmenin anlattığı yöntem, notasyon ya da terminolojiyle çelişebiliyor.
2. **Uydurabiliyor.** Kaynağa dayalı sistemlerde bile uydurma ve yanlış reddetme ayrı bir araştırma alanı. Bir 2026 ön çalışmasında, piyasadaki RAG ürünleri arasındaki en büyük farkın doğruluk değil **reddetme davranışı** olduğu bulundu (reddetme oranları %0,2–%11,1) **[LİTERATÜR: arXiv 2608.26385]**.
3. **Öğrenmeyi baltalayabiliyor.** Yaklaşık 1.000 lise öğrencisiyle yapılan randomize kontrollü bir çalışmada, korumasız sohbet botu kullanan öğrenciler alıştırmada daha başarılı olurken **sonraki sınavda daha düşük** puan aldı. Sokratik korumalı sürüm bu kaybı ortadan kaldırdı **[LİTERATÜR: Bastani ve ark., PNAS 2025]**. **Cevap sızıntısını önlemek bir "özellik" değil, pedagojik zorunluluk.**
4. **Veri yurt dışında.** 7499 sayılı Kanun'la değişen KVKK md. 9'a göre yurt dışındaki bulut veya YZ API'sine öğrenci verisi göndermek yurt dışına aktarım sayılıyor. Standart sözleşme ve 5 iş günü içinde Kurul'a bildirim gerekiyor; ihlalde 50.000–1.000.000 TL idari para cezası öngörülüyor **[LİTERATÜR: KVKK rehberi, hukuk yayınları]**.
5. **Ödev puanlamada güvenilirlik düşük.** Hazır büyük dil modellerinin insan puanıyla uyumu ağırlıklı Kappa ile **≈ 0,4–0,7** bandında ve veri setine göre çok değişken. Bir yükseköğretim çalışmasında uyum "düşük ve anlamsız" bulundu **[LİTERATÜR: arXiv 2508.02442; Springer s44163-026-01002-y; ACM 3709026.3709030]**.
6. **Regülasyon baskısı.** AB YZ Yasası Ek III(3)(b), öğrenme çıktısını değerlendiren YZ sistemlerini **yüksek riskli** sayıyor: insan gözetimi, kayıt tutma, veri yönetişimi ve şeffaflık zorunlu. Uygulama tarihi, sonradan yapılan değişiklikle (Digital Omnibus) **02.12.2027**'ye ertelendi **[TEYİT: AB Resmî Gazetesi]**.

### 1.3 Başvurudan önce kendi verimizle kanıt toplama (öneri)
Hakemin "bu sorun gerçek mi?" sorusuna en güçlü cevap kendi verimizdir. Başvurudan önce 1 haftada yapılabilecek bir anket önerisi:

**Eğitmen anketi (tüm eğitmenler):**
1. Haftada kaç saatinizi ödev okumaya ve geri bildirim yazmaya ayırıyorsunuz?
2. Haftada kaç öğrenci sorusunu ders dışında (mesaj, e-posta) yanıtlıyorsunuz? Bunların yüzde kaçı ders notunda cevabı olan sorular?
3. Ödev geri bildirimini ortalama kaç günde iletiyorsunuz?
4. Öğrencilerin ödevlerde YZ kullandığını düşünüyor musunuz? Nasıl tespit ediyorsunuz?

**Öğrenci anketi (son 3 ayın öğrencileri):**
1. Dersten sonra aklınıza gelen bir soruya cevap bulmak ne kadar sürüyor?
2. Ders konusunda ChatGPT veya benzeri araç kullanıyor musunuz? Verdiği cevap ders anlatımıyla çelişti mi?
3. Ödev geri bildirimi size ne zaman ulaşıyor, yeterince açıklayıcı mı?

Sonuçlar sunumdaki "Problem" slaytına rakam olarak girer. Örnek kullanım: "Eğitmenlerimiz haftada ortalama X saat ödev okuyor; ders dışı soruların %Y'sinin cevabı zaten ders notunda".

---

## 2. Neden şimdi?

| Gelişme | Proje için anlamı |
|---|---|
| Açık ağırlıklı **Türkçe** modeller olgunlaştı: YTÜ COSMOS'un Cosmos T1 (Gemma 2 9B tabanlı, 200 milyar+ Türkçe token) ve Turkish-Llama-8B modelleri; turkish-e5-large embedding modeli (MIT lisansı) | Yurt içinde barındırılabilen, ticari kullanıma uygun lisanslı yerli bileşenlerle çalışmak artık mümkün |
| Türkçe değerlendirme altyapısı oluştu: TR-MTEB (EMNLP 2025), TR-TEB, TurkishMMLU (EMNLP 2024), TQuAD, CETVEL | Bilgi erişimi ve model seçimi için kıyaslanabilir ölçütler var |
| Türkçe konuşma tanıma yeterli seviyede: Whisper large-v3, FLEURS Türkçe testinde ≈ %6, Common Voice'ta ≈ %7,7 kelime hata oranı **[LİTERATÜR: arXiv 2611.03605]** | Ders videoları aranabilir ve atıf verilebilir kaynağa dönüşebilir |
| Google, 2026'da Classroom'a NotebookLM ve Gemini'yi entegre etti | Pazar "kaynağa dayalı eğitim YZ'si" kategorisini doğruladı. **Yerli, Türkçe ve yurt içinde çalışan alternatif ihtiyacı belirginleşti** |
| KVKK yurt dışı aktarım rejimi sıkılaştı (2024) ve AB YZ Yasası'nın eğitim yükümlülükleri yaklaşıyor (2027) | Yurt içi barındırma ve uyumlu tasarım satış avantajına dönüşüyor |

---

## 3. Pazar

### 3.1 Pazar büyüklüğü (üst-aşağı)

| Katman | Tanım | Büyüklük | Kaynak / dayanak |
|---|---|---|---|
| **TAM** | Türkiye eğitim teknolojileri pazarı | ≈ 2,2 milyar $ (2024), ≈ 2,45 milyar $ (2025 tahmini); 2033'te > 6 milyar $ | **[LİTERATÜR: IMARC, Ekonomist, Webtures]** |
| (alternatif ölçüm) | Türkiye e-öğrenme ve beceri geliştirme platformları | ≈ 2,2 milyar $ (2025) → ≈ 5,5 milyar $ (2031), yıllık ≈ %15,8 büyüme | **[LİTERATÜR: Ken Research]** |
| **SAM** | Öğrenme platformu + YZ destekli değerlendirme; hedef segmentler: kurslar, etüt merkezleri, özel okullar, üniversite sürekli eğitim merkezleri, kurumsal akademiler, bireysel eğitmenler | TAM'ın ≈ %8–10'u → **≈ 180–250 milyon $** | **[VARSAYIM]**: yazılım/platform payı tahmini; içerik ve donanım hariç |
| **SOM (3. yıl)** | Gerçekçi pazar payı | SAM'ın ≈ %0,5–1'i → **≈ 1–2 milyon $** (≈ 50 milyon TL ölçeği) | Belge 04'teki gelir projeksiyonu ile tutarlı **[VARSAYIM]** |

### 3.2 Aşağı-yukarı doğrulama (segment bazında)

| Segment | Birim sayısı | Kaynak | Ürün için anlamı |
|---|---|---|---|
| Özel okullar | **15.094** (2025–26) | **[LİTERATÜR: MEB 2025–26 istatistikleri]** | Okul sonrası destek ve ödev değerlendirme |
| Özel öğretim kursları, etüt merkezleri, mesleki kurslar | Binlerce **[TEYİT: MEB Özel Öğretim Kurumları GM verisi]** | MEB ÖÖKGM | **Birincil hedef.** Kendi segmentimiz, ihtiyacı birebir biliyoruz |
| Üniversite sürekli eğitim merkezleri (SEM) | ≈ 200 üniversite **[TEYİT]** | YÖK | Sertifika programları; kurum içi kurulum talebi yüksek |
| Kurumsal akademiler (banka, holding, kamu) | Yüzlerce | — | Yurt içi veri ve kurum içi kurulum zorunlu; yüksek bilet |
| Bireysel eğitmenler ve özel ders verenler | On binler **[VARSAYIM]** | — | B2C/B2SMB; kendi kendine kayıt, düşük satış maliyeti |

**İlk 3 hedef kurum tipi** (pilot ve ilk satış): (1) kendi sektörümüzdeki benzer kurslar, (2) Yıldız Teknopark'taki firmaların kurumsal eğitim birimleri, (3) bir üniversite SEM'i (YTÜ SEM ile tanışma fırsatı).

---

## 4. Rekabet analizi

### 4.1 Rakip haritası

| Rakip | Tür | Güçlü yön | Zayıf yön (bizim fırsatımız) |
|---|---|---|---|
| **Google Classroom + Gemini + NotebookLM** | Küresel, ücretsiz/ücretli | 2026'da ders materyalinden not defteri, flashcard, quiz; 30+ öğretmen YZ özelliği; geniş kurulu taban | Veriler yurt dışında (KVKK aktarım yükü); Workspace for Education ekosistemine bağlı; ileri özellikler Education Plus lisansında; rubrik tabanlı **ölçülmüş** puanlama uyumu yok; Türkçe özelleştirme sınırlı; kursların ödeme ve kayıt süreçlerine uygun değil |
| **Moodle / Canvas + YZ eklentileri** | Küresel LMS | Olgun LMS işlevleri; eklenti ekosistemi | YZ sonradan eklenti; kaynağa sadakat ve sızıntı kontrolü eklentiye bağlı; Türkçe kalite belirsiz; kurulum ve bakım yükü yüksek |
| **ChatGPT Edu / genel sohbet botları** | Küresel | Güçlü genel model | Ders kaynağına kilitli değil; pedagojik kontrol yok; LMS değil; veriler yurt dışında; döviz bazlı fiyat |
| **Khanmigo** | Küresel, Sokratik eğitmen | Pedagojik tasarım | Kendi içeriğine bağlı, eğitmenin kendi kaynağını kullanmıyor; Türkçe değil |
| **InfinityLMS** | Yerli kurumsal LMS | 12 YZ aracı, 300+ kurum, 2,5 milyon kullanıcı (firma beyanı) | Kurumsal ve iş güvenliği eğitimine odaklı; kaynağa sadakat ve rubrik uyumu ölçümleri kamuya açık değil |
| **Akademi.Net (GobiAI)** | Yerli LMS | Videodan ve PDF'ten başlık, özet, ön/son test üretimi | İçerik üretimi odaklı; soru-cevapta atıf ve reddetme, rubrikle değerlendirme yok |
| **HeryerOnline** | Yerli; dershane ve kurumlara | Canlı ders, optik okuma, YZ analitiği; Türkiye altyapısı | Sınav ve analitik odaklı; kaynağa dayalı üretken YZ ve ödev değerlendirme değil |
| **Vedubox (ETGİ)** | Yerli LMS + canlı ders | Yerli ve milli konumlandırma; YZ destekli öğrenme yolları | Kaynağa sadakat ve değerlendirme uyumu iddiası yok |
| **Perculus** | Yerli sanal sınıf | 2025'te Constructor Tech tarafından ≈ 5 milyon $'a satın alındı | Canlı ders altyapısı; YZ çekirdeği değil. **Bu satın alma, segmentin yatırımcı ilgisini kanıtlıyor** |

*Kaynaklar: Google Workspace Updates (Nisan ve Ağustos 2026), Google blog (BETT ve ISTE 2026), firma web siteleri, KPMG Türkiye Startup Yatırımları 2025 Ç1. Rakip iddiaları firma beyanıdır, bağımsız doğrulanmamıştır.*

### 4.2 Özellik karşılaştırma matrisi

| Özellik | Google Classroom+NotebookLM | Moodle/Canvas+eklenti | ChatGPT Edu | Yerli LMS'ler | **KAYNAK-YZ (hedef)** |
|---|---|---|---|---|---|
| Ders kaynağına kilitli soru-cevap | ✓ | ~ (eklentiye bağlı) | ✗ | ~ | ✓ |
| Sayfa / slayt / **video dakikası** atfı | ~ | ✗ | ✗ | ✗ | ✓ |
| Kaynak dışı soruyu ölçülmüş biçimde reddetme | ? | ✗ | ✗ | ✗ | ✓ (hedef ≥ %90) |
| Ödev cevabı sızıntı kontrolü (Sokratik mod) | ~ | ✗ | ~ | ✗ | ✓ (hedef ≤ %2) |
| Rubrik tabanlı, **ölçülmüş uyumlu** ön-değerlendirme | ~ (yalnızca öneri) | ~ | ✗ | ✗ | ✓ (hedef Kappa ≥ 0,75) |
| Türkçe için optimize bilgi erişimi | ~ | ✗ | ~ | ~ | ✓ |
| **Yurt içinde barındırma / kurum içi kurulum** | ✗ | ✓ (kurum içi kurulum) | ✗ | ✓ | ✓ |
| Açık ağırlıklı yerli model seçeneği | ✗ | ✗ | ✗ | ✗ | ✓ |
| AB YZ Yasası yüksek risk gereklerine göre tasarım | ? | ✗ | ? | ✗ | ✓ |
| Kurs işletmesi işlevleri (kayıt, ödeme, B2C) | ✗ | ~ | ✗ | ✓ | ✓ |

✓ var · ~ kısmen · ✗ yok · ? kamuya açık bilgi yok

### 4.3 Google gibi devlerle nasıl rekabet ederiz?
Doğrudan değil, **odaklanarak**:
1. **Segment.** Google'ın odağı okullar ve Workspace kurumları. Bizim odağımız kurslar, kurumsal akademiler, SEM'ler ve bireysel eğitmenler; bunların kayıt, ödeme ve satış ihtiyaçları da var.
2. **Veri egemenliği.** Yurt içi barındırma ve kurum içi kurulum. Kamu, banka ve savunma akademileri için **zorunlu**.
3. **Ölçülmüş güvenilirlik.** Sadakat, reddetme, sızıntı ve puan uyumu metriklerini her kuruma **şeffaf panoda** göstermek. Rakiplerin hiçbiri bunu yapmıyor.
4. **Türkçe derinlik.** Türkçe bilgi erişimi ve yerli model; Türk dilli pazarlara aktarılabilir.
5. **Uyumluluk.** AB YZ Yasası ve KVKK uyumlu tasarım, AB ve kurumsal satışta giriş bileti.

---

## 5. Değer önerisi (segment bazında)

| Segment | Mesaj | Ölçülebilir vaat (pilot sonrası doğrulanacak) |
|---|---|---|
| Kurs / etüt merkezi | "Öğrencin gece 11'de bile senin anlattığın gibi cevap alsın; ödevleri yarı sürede değerlendir." | Eğitmenin ödev okuma süresinde ≥ %40 azalma **[hedef]** |
| Kurumsal akademi | "Eğitim içeriğin ve çalışan verin şirketten çıkmadan YZ asistanı." | Kurum içi kurulum; veri yurt dışına çıkmıyor |
| Üniversite SEM | "Sertifika programlarında ölçeklenebilir, kanıtlı geri bildirim." | Geri bildirim süresinin günlerden saatlere inmesi **[hedef]** |
| Bireysel eğitmen | "Kendi dersini aç, öğrencilerine 7/24 asistan ver." | Aylık sabit fiyat, 10 dakikada kurulum |
| Öğrenci | "Sorduğun soruya dersin notundan, sayfa numarasıyla cevap." | Soru başına ortalama yanıt ≤ 3 sn |

---

## 6. İthal ikame ve ihracat

### 6.1 İthal ikame (ölçüt 8, %15)
| İkame edilen yabancı ürün/hizmet | Tipik maliyet kalemi | KAYNAK-YZ karşılığı |
|---|---|---|
| Zoom / Teams / Google Meet lisansları | Kullanıcı başı aylık $ | Yurt içi barındırılan açık kaynak canlı ders (BigBlueButton) entegrasyonu |
| Canvas / Moodle Workplace / yabancı LMS abonelikleri | Kullanıcı başı yıllık $ | Yerli platform |
| ChatGPT / Gemini / Claude kurumsal YZ abonelikleri ve API'leri | Kullanıcı başı aylık $ veya token başı $ | Yurt içinde barındırılan açık ağırlıklı model (ör. Cosmos T1 / Turkish-Gemma); ticari API yalnızca isteğe bağlı |
| Yabancı otomatik değerlendirme ve intihal araçları | Lisans $ | Rubrik tabanlı değerlendirme + (opsiyonel) Türkçe YZ metni tespiti |

**Döviz etkisi (örnek hesap şablonu):** 200 öğrencili bir kurumun yabancı LMS + video konferans + YZ aboneliği için ödediği aylık $ tutar × 12 = yıllık döviz çıkışı. Pilot kurumlardan gerçek veriyle doldurulacak **[VARSAYIM]**.

### 6.2 İhracat yol haritası
| Dönem | Pazar | Neden | Giriş yolu |
|---|---|---|---|
| 2028 | **Azerbaycan, KKTC** | Dil yakınlığı (Azerbaycan Türkçesi), kültürel yakınlık, Türk eğitim kurumlarının varlığı | Türk kurs zincirlerinin şubeleri, HİB, Yıldız UTPO |
| 2028–29 | **Kazakistan, Özbekistan** | Türk dilli; hızla dijitalleşen eğitim pazarları | Yerel distribütör + StarCamp / Yıldız yurt dışı ofisleri |
| 2029+ | **Almanya / AB** (Türk diasporası eğitim kurumları ile başlayarak) | Büyük pazar; AB YZ Yasası uyumu giriş bariyeri, bizim için avantaj | AB YZ Yasası uyumluluk dokümantasyonu + yerel ortak |
| 2029+ | Körfez / MENA (Arapça) | Büyük özel eğitim pazarı | Arapça dil uyarlaması (Faz 3 sonrası) |

**Teknik hazırlık:** Dil bağımsız mimari (Türkçe'ye özgü bileşenler eklenti olarak), çok dilli embedding modelleri (bge-m3 100+ dil), arayüz yerelleştirmesi (i18n) Faz 1'de baştan kuruluyor.
