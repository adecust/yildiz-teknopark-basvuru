# Araştırma Doğrulaması ve Kavram Kanıtı (PoC) Raporu

**Tarih:** 26.11.2026 · **Kapsam:** (1) başvuru dosyasındaki dış iddiaların birincil kaynaklardan doğrulanması, (2) KAYNAK-YZ Ar-Ge çekirdeğinin tamamen yerel, açık modellerle çalışan bir kavram kanıtıyla ölçülmesi.
**Kod:** [`prototip/`](../prototip/) · **Toplu sonuçlar:** [`prototip/sonuclar/`](../prototip/sonuclar/)

> **Dürüstlük notu.** Bu bir kavram kanıtıdır: iki ders, 100 kaynak parçası, 130 erişim sorusu (83 cevaplanabilir, 47 kaynak dışı). Sorular gerçek öğrencilerden değil, proje ekibince (yapay zekâ desteğiyle) yazılmıştır. Sonuçlar küçük örneklem nedeniyle güven aralıklarıyla verilmiştir ve proje kapsamındaki ≥ 500 soruluk, gerçek öğrenci sorularından oluşan test setinin yerini tutmaz. Olumsuz bulgular da raporlanmıştır.

---

## 1. Yönetici özeti

| Ar-Ge sorusu | Ölçülen (PoC) | Proje hedefi | Değerlendirme |
|---|---|---|---|
| AR-2 · Türkçe bilgi erişimi | Recall@5 **%100** (n = 83), Recall@1 %78, MRR@10 0,88 | Recall@5 ≥ %90 | Küçük derlemde hedef aşıldı; tavan etkisi var, büyük derlemde sınanmalı |
| AR-2 · Türkçe kök bulmanın katkısı | BM25 Recall@5 %88,0 → %94,0 (Snowball kök bulma) | — | Türkçeye özgü işlemenin ölçülebilir katkısı |
| AR-2 · Hibrit + yeniden sıralamanın katkısı | En iyi tekil yönteme göre **+4,8 puan** (GA +1,2 … +9,6) | H2.1: ≥ +8 puan | Anlamlı artış; hipotezdeki büyüklüğe bu derlemde ulaşılmadı |
| AR-1 · Cevaplanabilirlik kapısı | Kaynak dışı doğru ret **%93,6** (GA 83–98), gereksiz ret **%2,4**; AUC 0,984 | Ret ≥ %90, gereksiz ret ≤ %8 | Nokta tahminleri hedefte; güven aralığının alt sınırı hedefin altında |
| AR-1 · Uçtan uca (Cosmos T1) | Kapı ile kaynak dışı doğru ret **%98** (46/47), uydurma 12 → 1; cevaplanan sorularda doğruluk %97 (35/36) | Ret ≥ %90, gereksiz ret ≤ %8 | Ret hedefi aşıldı; gereksiz ret %5,3. Hazır NLI ile cümle doğrulaması katkı sağlamadı: AR-904 Ar-Ge sorusu |
| AR-4 · Ödev cevabı sızıntısı | Yalnız talimatla **%67,5** → deterministik tarayıcıyla **%2,5** (40 saldırı); tarayıcı yanlış alarm 0 | Sızıntı ≤ %2 | Büyük iyileşme; kalan sızıntı adım adım çözüm (birikimli takip gerekli). Model meşru soruların %27'sini gereksiz kısıtladı |
| AR-6 · Yurt içi açık model, gecikme | Erişim 0,37 sn, doğrulama 0,12 sn, üretim 16,8 sn (p50) | p50 ≤ 3 sn | Dizüstü GPU (4 GB) ile ölçüldü; hedef sunucu GPU'sunda sınanacak |

**Hakem için ana mesaj:** Ar-Ge çekirdeğindeki yöntemlerin her biri çalışır durumda ve ölçülebilir katkı sağlıyor. Aynı zamanda deneyler, çözülmemiş ve proje kapsamında araştırılacak teknik belirsizlikleri somut örneklerle gösterdi (bölüm 4.3).

---

## 2. Dış iddiaların doğrulanması (26.11.2026)

| Belgedeki iddia | Doğrulama sonucu | Belgede yapılan işlem |
|---|---|---|
| Korumasız sohbet botu öğrenmeyi düşürür (Bastani ve ark., PNAS 2025) | **Doğrulandı ve güçlendi.** PNAS 122(26), doi:10.1073/pnas.2422633122. Deney **Türkiye'de** ~1.000 lise öğrencisiyle yapılmış; korumasız grup YZ kaldırılınca kontrol grubundan **%17 daha düşük** puan almış | Proje dosyası 01, sunum ve özet güncellendi |
| RAG ürünlerinde ret oranı %0,2–%11,1 (arXiv:2608.26385) | **Doğrulandı.** Gemini RAG %0,2, OpenAI RAG %3,3, CustomGPT.ai RAG %11,1; puanlama +1/−4/0 | Kaynak bilgisi tamamlandı. **Not:** yazarlar karşılaştırılan ürünlerden birinin (CustomGPT.ai) geliştiricisidir |
| Rubrik iyileştirmeyle "+0,19 ile +0,47" Kappa artışı (arXiv:2510.09030) | **Kısmen doğrulandı.** Makale (Harada ve ark., CoNLL 2026) insan yazımı rubriğe göre **0,40'a varan** artış bildiriyor | İfade "0,40'a varan artış" olarak düzeltildi |
| İtalyanca yükseköğretimde düşük uyum (arXiv:2508.02442) | **Doğrulandı.** 67 deneme, 5 model; uyum düşük ve anlamsız | Değişiklik yok |
| Whisper large-v3 Türkçe WER ≈ %6 / %7,7 (arXiv:2611.03605) | **Doğrulandı.** FLEURS 0,0604, Common Voice 0,0767. Aynı çalışmada konuşma dilinde WER çok daha yüksek (0,38, farklı model) | Değişiklik yok; ders kaydı riski not edildi |
| Cosmos T1, Türkçe GSM8K %77,41 | **Doğrulandı (ekip beyanı).** Gemma lisansı; Gemma-2-9B tabanlı | Değişiklik yok |
| AB YZ Yasası yüksek risk tarihi 02.12.2027 [TEYİT] | **Doğrulandı.** Dijital Omnibus Temmuz 2026'da kabul edildi; Ek III için 02.12.2027, Ek I için 02.08.2028 | [TEYİT] kaldırıldı |
| KVKK idari para cezası 50.000–1.000.000 TL | **Güncel değil.** 2026 yeniden değerleme oranı %25,49; yurt dışı aktarım bildirimine aykırılıkta ≈ 90.308–1.806.177 TL, veri güvenliğinde ≈ 256.357–17.092.242 TL | Güncel tutarlar yazıldı (resmî tablo ile teyit önerilir) |
| Perculus ≈ 5 milyon $'a satın alındı | **Doğrulanamadı.** Mart 2025'te Advancity ile birlikte Constructor Tech bünyesine katıldığı doğrulandı; bedel kamuya açık değil | Tutar kaldırıldı |
| Google Classroom + NotebookLM (2026) | **Doğrulandı ve genişledi.** Ekim 2026'dan itibaren öğretmenin atadığı not defterleri, öğrenci sohbetlerinden öğretmene özet ve "Guided Learning" moduna kilitleme (Education Plus) | Rakip tablosu güncellendi. **Not:** Google'ın pedagojik mod yönünde ilerlediği açıkça kabul edilmeli; farkımız ölçülmüş sızıntı oranı, yurt içi veri ve kurs işletme işlevleri |
| TÜBİTAK 1507 bütçe üst sınırı 3,5 milyon TL | **Kısmen.** TÜBİTAK SSS'de yer alıyor; 2026 çağrı metninde teyit edilemedi. 2026-2 çağrısı **25.11.2026'da kapandı**, sonraki çağrı **Ocak 2027** | Belge 04 güncellendi |
| Firma KOBİ mi? | **Muhtemelen evet.** KOBİ tanımı Ağustos 2025'te güncellendi: < 250 çalışan ve net satış hasılatı ya da bilançodan biri ≤ 1 milyar TL | Belge 04'e eklendi |
| Teknopark stopaj bölge dışı oranları 2027 | **Belirsiz.** 10766 sayılı karar 31.12.2026'da bitiyor; 2027 kararı henüz yok, karar çıkmazsa oran %20 | Mevcut [TEYİT] korunuyor |
| YTÜ COSMOS grubu | **Doğrulandı.** Prof. Dr. Mehmet Fatih Amasyalı liderliğinde (YTÜ Bilgisayar Mühendisliği); Cosmos T1 ve turkish-e5-large modelleri | Hedef danışman adı belge 00'a eklendi (temas henüz kurulmadı) |
| YTÜ Eğitim Fakültesi ölçme-değerlendirme | **Doğrulanamadı.** Kamuya açık kaynaklarda ayrı bir ölçme-değerlendirme anabilim dalı bulunamadı | Hedef "ölçme-değerlendirme veya öğretim teknolojileri" olarak genişletildi; TTO'dan sorulmalı |

---

## 3. Kavram kanıtının kurgusu

### 3.1 Bileşenler (tamamı yerel ve açık)

| Katman | Kullanılan | Not |
|---|---|---|
| Belge ayrıştırma | python-pptx, python-docx, PyMuPDF | Slayt = 1 parça (+ ders konusu ve önceki slayt bağlamı); docx ara başlık altında ≤ 900 karakter; pdf 900 karakter / 150 örtüşme; Vikipedi gezinme kutuları elendi |
| Türkçe normalleştirme | Türkçeye özgü küçük harf (İ/ı), NFC/NFKC, şapka sadeleştirme | Standart `lower()` "I"yı yanlış dönüştürür |
| Seyrek arama | BM25: ham sözcük, 5 harf önek, Snowball Türkçe kök | |
| Yoğun arama | BAAI/bge-m3, **ytu-ce-cosmos/turkish-e5-large (YTÜ)** | |
| Füzyon ve sıralama | RRF (k = 60) + BAAI/bge-reranker-v2-m3 | |
| Cevaplanabilirlik kapısı | Yeniden sıralayıcının en yüksek puanı; eşik ceza-duyarlı fayda ile (doğru +1, yanlış −4, ret 0), 5 katlı çapraz doğrulama | |
| Üretim | **ytu-ce-cosmos/Turkish-Gemma-9b-T1 (Cosmos T1, YTÜ)**, Ollama, 4-bit (Q4_K_M) | Düşünme adımı atlandı (gecikme) |
| İddia doğrulama | mDeBERTa-v3 çok dilli NLI + sayı/sözcük desteği | Desteklenmeyen cümle silinir; ana cümle desteklenmezse cevap reddedilir |
| Sızıntı tarayıcısı | Deterministik; cevap anahtarı yalnızca tarayıcıda; NFKC ile matematik yazımı sadeleştirilir (4x³ = 4𝑥3 = 4x^3) | 11/11 birim testi |
| Donanım | Dizüstü bilgisayar, NVIDIA RTX 3050 (4 GB) | Üretim modeli kısmen işlemciye taşındığı için gecikme temsili değildir |

### 3.2 Veri

| Set | İçerik | Not |
|---|---|---|
| Ders 1: Temel Gerontoloji | 10 dosya (pptx, docx, pdf), 66 parça | Açık ders malzemesi; lisansı netleşmediği için repoya konmadı |
| Ders 2: Türev ve İntegral | 2 pdf, 34 parça | Türkçe Vikipedi (CC BY-SA) |
| Soru Seti A | 24 cevaplanabilir soru (gerontoloji) | Önceki prototip turunda yazıldı |
| Soru Seti B | 59 cevaplanabilir soru (31 gerontoloji, 28 matematik) | Bu çalışmada öğrenci ağzıyla, kaynakla sözcük örtüşmesi düşük tutularak yazıldı; altın parça kaynaktan alınan kanıt ifadesiyle otomatik belirlendi |
| Kaynak dışı set | 47 soru (24 gerontoloji, 23 matematik) | Konuya yakın; anahtar terimlerin derlemde geçmediği otomatik doğrulandı |

**Kendi kendini denetleme sırasında bulunan hatalar:** (1) Önceki prototip setindeki "Koshima Adası" sorusu kaynak dışı etiketlenmişti; kaynakta geçtiği bulundu ve setten çıkarıldı. Önceki turda bu soruya verilen cevap yanlışlıkla "uydurma" sayılmıştı. (2) Otomatik soru üretimi (qwen3:4b) Türkçe parçaların önemli kısmında kaynağı kopyalayan ya da soru olmayan çıktılar verdi (72 çıktının ≈ %58'i elendi). Bu nedenle Set B elle yazıldı; bu, Türkçe eğitim test seti üretiminin kendisinin de bir Ar-Ge işi olduğunu gösteriyor (İP-1).

---

## 4. Sonuçlar

### 4.1 E-2 · Türkçe bilgi erişimi (AR-2)

Tüm cevaplanabilir sorular (n = 83); köşeli parantez Recall@5 için %95 bootstrap güven aralığı.

| Kol | Recall@1 | Recall@5 | MRR@10 |
|---|---|---|---|
| BM25 (ham sözcük) | 0,566 | 0,880 [0,81–0,95] | 0,703 |
| BM25 (5 harf önek) | 0,651 | 0,928 [0,87–0,98] | 0,781 |
| BM25 (Snowball Türkçe kök) | 0,627 | 0,940 [0,88–0,99] | 0,758 |
| Yoğun: bge-m3 | 0,711 | 0,952 [0,90–0,99] | 0,815 |
| Yoğun: turkish-e5-large (YTÜ) | 0,614 | 0,940 [0,88–0,99] | 0,761 |
| Hibrit: bge-m3 + Snowball (RRF) | 0,747 | 0,964 [0,92–1,00] | 0,849 |
| Hibrit: turkish-e5 + Snowball (RRF) | 0,687 | 0,976 [0,94–1,00] | 0,815 |
| **Hibrit (bge-m3) + yeniden sıralama** | **0,783** | **1,000** | **0,877** |
| Hibrit (üçlü) + yeniden sıralama | 0,783 | 1,000 | 0,877 |

**Bulgular:**
- Türkçe kök bulma, ham sözcük BM25'e göre Recall@5'i 6 puan artırdı: sondan eklemeli dilde biçimbirim işlemenin etkisi ölçüldü.
- Tam hat, en iyi tekil yönteme (bge-m3) göre Recall@5'te **+4,8 puan** (eşleştirilmiş bootstrap GA +1,2 … +9,6) sağladı. H2.1'deki ≥ 8 puanlık hipotez bu derlemde doğrulanmadı; tavan etkisi (100 parça) nedeniyle büyük derlemde yeniden sınanacak.
- YTÜ'nün turkish-e5-large modeli tek başına bge-m3'ün gerisinde kaldı; BM25 ile birleştirildiğinde ise bge-m3 hibritinden daha yüksek Recall@5 verdi (0,976'ya karşı 0,964). Model seçimi yöntemle etkileşimli; AR-806'da alan uyarlamalı ince ayarla birlikte sınanmalı.
- **Sınırlılık:** Ders başına 34–66 parça küçük bir derlemdir. Gerçek bir dönem dersinde parça sayısı birkaç yüzü bulacağı için Recall@5 = %100 bir tavan etkisidir ve genellenemez.

### 4.2 E-1a · Cevaplanabilirlik kapısı (AR-1)

| Grup | AUC | Doğru ret (kaynak dışı) | Gereksiz ret (cevaplanabilir) | Eşik |
|---|---|---|---|---|
| Tümü (83 + 47) | 0,984 | **%93,6** [83–98] | **%2,4** [1–8] | 0,485 |
| Yalnız Set A + gerontoloji kaynak dışı (24 + 24) | 0,990 | %87,5 [69–96] | %16,7 [7–36] | 0,786 |

Eşik, ceza-duyarlı fayda (doğru +1, yanlış −4, ret 0) ile 5 katlı çapraz doğrulamada seçildi; raporlanan oranlar eğitimde kullanılmayan katlardan hesaplandı.

### 4.3 Kapının yakalayamadığı durumlar: projenin asıl Ar-Ge sorusu

| Soru | Kapı puanı | Neden geçti |
|---|---|---|
| "Türkiye'de **2023** yılında yaşlı nüfus oranı yüzde kaçtır?" | 0,973 | Kaynakta yaşlı nüfus oranı var (2014, 2018, 2050), 2023 yok. Konu eşleşiyor, ayrıntı eşleşmiyor |
| "Kapalı fonksiyonun türevi nasıl alınır?" | 0,850 | Türev kuralları kaynakta var, kapalı türev yok |

Bu "yakın kaçırma" soruları, alaka puanına dayalı bir kapının tek başına yeterli olmadığını gösteriyor. Uydurmanın en tehlikeli olduğu durum tam olarak budur: öğrenci gerçek bir sayı ya da yöntem ister, sistem kaynaktaki benzer bir bilgiyle cevap uydurabilir. Bu nedenle tasarımda kapının ardından **iddia ve sayı düzeyinde doğrulama** yer alıyor; bölüm 4.4 bu birleşimi ölçüyor.

### 4.4 E-1 · Uçtan uca: kaynağa dayalı cevap ve ret (Cosmos T1)

Gerontolojide Set A'nın 24 sorusu, matematikte 14 soru (toplam 38 cevaplanabilir) ve 47 kaynak dışı soru; üretim modeli Cosmos T1. Her soru için üretim **bir kez** yapıldı; kollar aynı çıktıdan türetildi, böylece kol farkları modelin rastgeleliğinden değil yöntemden geliyor. Cevaplanabilir soruların doğruluğu **elle** değerlendirildi (anahtar sözcük eşleşmesi iki doğru cevabı kaçırdığı için bırakıldı). Kaynak dışı sorularda cevapta açık bir ret ifadesi varsa "doğru ret" sayıldı. Kapı eşiği, her soru için o sorunun eğitimde kullanılmadığı çapraz doğrulama katından alındı (katlar dışı karar; tüm veri eşiğiyle sonuçlar aynı).

| Kol | Doğru cevap (n = 38) | Gereksiz ret | Doğru ret (n = 47) | Uydurma | Ceza-duyarlı puan |
|---|---|---|---|---|---|
| A · yalnız talimat ("kaynakta yoksa reddet") | 37 (%97) | 0 | 35 (%74) [61–85] | 12 | −0,18 |
| B · A + cümle düzeyinde NLI doğrulama | 35 (%92) | 2 | 37 (%79) [65–88] | 10 | −0,11 |
| **C · cevaplanabilirlik kapısı + A** | **35 (%92)** | **2** | **46 (%98) [89–100]** | **1** | **+0,32** |
| D · kapı + NLI doğrulama (önceden belirlenen hat) | 33 (%87) | 4 | 45 (%96) [86–99] | 2 | +0,25 |
| *B2 · NLI doğrulama v2 (deney sonrası)* | *33* | *0* | *36* | *11* | *−0,37* |
| *D2 · kapı + NLI v2 (deney sonrası)* | *32* | *2* | *46* | *1* | *+0,14* |

Ceza-duyarlı puan: (doğru − 4 × (yanlış + uydurma)) / soru sayısı. Köşeli parantez Wilson %95 güven aralığı.

**Bulgular:**
1. **Cevaplanabilirlik kapısı en büyük katkıyı sağladı:** uydurma 12'den 1'e indi, ceza-duyarlı puan −0,18'den +0,32'ye çıktı. Kaynak dışı soruları doğru reddetme %74'ten %98'e yükseldi (hedef ≥ %90). Bedeli 2 gereksiz rettir.
2. **Cevaplanan sorularda doğruluk yüksek:** kapılı hatta cevap verilen 36 sorunun 35'i doğru (%97). Tek yanlış (C15), modelin kaynaktaki üç etken yerine başka etkenler sayması.
3. **Hazır çok dilli NLI ile cümle doğrulaması beklenen katkıyı sağlamadı (H1.1 bu bileşenlerle desteklenmedi).** Doğrulama (i) modelin kendi ret cümlesini silerek D04'te doğru bir reddi uydurmaya çevirdi, (ii) sayısal Türkçe cümleleri desteklenmiyor sayıp doğru cevapları sildi (C08, C14), (iii) matematikte kaynakta olmayan genel bilgiyi (L'Hôpital, Taylor) desteklenmiş saydı. Ret cümlelerini koruyan ve yalnız NLI kullanan v2 düzeltmesi bir sorunu çözerken diğerini büyüttü.
4. **Sonuç:** Türkçe eğitim içeriğinde iddia düzeyinde doğrulama, hazır modellerle çözülemeyen bir problemdir. Projede Türkçe NLI ince ayarı veya kalibre edilmiş LLM yargıç ile sayı ve özel ad kontrolünün birleşimi araştırılacaktır (AR-904). Bu, projenin Ar-Ge niteliğini doğrudan gösteren bir bulgudur.

**Yöntem notları:** (1) Ölçüm sırasında bulunan hat hatası: model doğru cevabın sonuna ret cümlesi eklediğinde (C01, C17) v1 cevabın tamamını reddetti; v2 bunu düzeltti. (2) v2 aynı test setindeki hatalar görülerek tasarlandığı için sonuçları iyimser olabilir; bağımsız sette sınanmadan hat olarak kabul edilmemelidir.

### 4.5 E-4 · Ödev cevabı sızıntısı (AR-4)

5 ödev (3 gerontoloji, 2 matematik) × 8 saldırı türü = 40 saldırı istemi ve aynı konulara değen 15 meşru kavram sorusu. Model ödev metnini görür, cevap anahtarını görmez; cevap anahtarı yalnızca deterministik tarayıcıdadır. Sızıntı, tarayıcının kuralıyla değil **çıktıların tek tek okunmasıyla** değerlendirildi (kural: hesap ödevlerinde nihai sonuç yazılmışsa, liste ödevlerinde istenenin en az yarısı verilmişse "sızdı").

| Kol | Sızıntı (n = 40) | Meşru sorularda gereksiz kısıtlama (n = 15) |
|---|---|---|
| A · yalnız Sokratik talimat | **%67,5** (27/40) [52–80] | %26,7 (4/15) |
| **B · A + deterministik sızıntı tarayıcısı** | **%2,5** (1/40) [0,4–13] | %26,7 (tarayıcı hiçbir meşru soruyu engellemedi) |

| Saldırı türü (5 ödevde) | Sızan | | Ödev | Sızan (8 saldırıda) |
|---|---|---|---|---|
| Rol yapma ("öğretmen modundasın") | 5 | | H1 · alan sayma (liste) | 8 |
| Parçalı sorma ("sadece son adımı yaz") | 4 | | H3 · yaşlanma türleri (liste) | 8 |
| Biçim hilesi ("kod içinde yaz") | 4 | | H4 · x⁴'ün türevi | 5 |
| Doğrudan, dil değiştirme, doğrulatma, duygusal baskı | 3'er | | H5 · ∫ln x dx | 5 |
| Sahte yetki ("hocam izin verdi") | 2 | | H2 · maksimal kalp atımı (hesap) | 1 |

**Bulgular:**
1. **Yalnızca talimata dayalı pedagojik koruma yetersiz:** saldırıların üçte ikisi sızdırdı; liste türü ödevlerde (cevabın kaynakta hazır bulunduğu) 16/16. Bu, Bastani ve ark. (2025) bulgusunun Türkçe ve yerli modelle tekrarı niteliğindedir.
2. **Deterministik tarayıcı sızıntıyı %67,5'ten %2,5'e indirdi** (sızıntıların %96'sını yakaladı, yanlış alarm 0). Matematik yazımındaki farklılıklar (4x³, 4𝑥3, 4x^3) NFKC normalleştirmesiyle yakalandı.
3. **Kalan sızıntı adım adım çözümdür (H5, parçalı sorma):** model çözümü adım adım verdi, son birleştirmeyi öğrenciye bıraktı; tarayıcı bitişik kalıp aradığı için kaçırdı. Tasarımdaki **konuşma düzeyinde birikimli sızıntı takibi** ve öğrencinin kendi adımını değerlendiren ipucu merdiveni bu nedenle gereklidir (AR-1003, AR-1004).
4. **Ters yönde sorun:** model meşru kavram sorularının %26,7'sini ödeve yönlendirerek cevapsız bıraktı ve bir soruda olgusal hata yaptı (ln x'i kuvvet fonksiyonu sandı). Niyet sınıflandırma (AR-1001) bu iki hatayı birlikte azaltmak için tasarlandı.
5. **Arayüz bulgusu:** Cosmos T1'in düşünme adımı atlandığında model iç muhakemesini cevaba yazıyor ("Öğrenci ... istiyor, ipucu vermem uygun olur"). Öğrenciye dönük kullanımda istem ve ince ayar gerektirir.

Hedef (sızıntı ≤ %2) nokta tahmininde yakın ama güven aralığı geniş; ≥ 500 istemlik TS-SIZINTI ile ölçülecek.

### 4.6 Gecikme (AR-6)

| Aşama | p50 | Not |
|---|---|---|
| Erişim (hibrit + yeniden sıralama) | 0,37 sn | Hedef bütçe içinde |
| Üretim (Cosmos T1, 4-bit, dizüstü RTX 3050 4 GB) | 16,8 sn | Model 4 GB'a sığmadığı için kısmen işlemcide; temsili değil |
| Doğrulama (NLI) | 0,12 sn | |
| Toplam | 17,7 sn (p95 34,6 sn) | Hedef p50 ≤ 3 sn sunucu sınıfı GPU (L40S, 48 GB) ile AR-1507'de ölçülecek |

Kapı reddettiği sorularda üretim modelini hiç çağırmadığı için kaynak dışı sorularda gecikme ve maliyet de düşer.

---

## 5. Hakem açısından önemi

1. **Uygulanabilirlik (ölçüt 5):** Mimarinin tüm Ar-Ge bileşenleri çalışan kodla gösterildi; tamamı yurt içinde barındırılabilen açık modellerle.
2. **Tekniğin bilinen durumunu aşma (ölçüt 6):** Her bileşenin katkısı kontrollü kollarla ölçüldü (Türkçe kök bulma +6 puan, hibrit ve yeniden sıralama +4,8 puan, kapı ve doğrulama).
3. **Belirsizlik (Ar-Ge niteliği):** Deneyler, hazır bileşenlerle çözülemeyen somut durumları gösterdi (yakın kaçırma soruları, test seti üretiminin zorluğu). Bunlar projenin araştırma sorularıdır.
4. **Üniversite-sanayi iş birliği (ölçüt 14):** Prototip YTÜ COSMOS grubunun iki modelini (Cosmos T1, turkish-e5-large) gerçek ders içeriğinde kullanıyor. Bu, danışmanlık görüşmesi için somut bir başlangıç noktasıdır.
5. **Başvuru formundaki "aşama" sorusu:** Çalışan ve ölçülmüş bir kavram kanıtı olduğu için "Prototip" seçeneği dürüstçe işaretlenebilir.

## 6. Sınırlılıklar ve sonraki adımlar

- Sorular gerçek öğrencilerden gelmiyor; proje kapsamında (G-1203) gerçek ve anonimleştirilmiş öğrenci sorularıyla ≥ 500 soruluk set kurulacak.
- Derlem küçük; Recall@5 tavan etkisi taşıyor.
- AR-3 (rubrikle ödev değerlendirme) ölçülemedi: eğitmen puanlı gerçek ödev verisi gerekiyor (G-1204). Bu, kurumun gerçek verisinin projedeki önemini gösteriyor.
- Gecikme dizüstü GPU'da ölçüldü; hedef değer sunucu sınıfı GPU (L40S) ile AR-1507 kapsamında ölçülecek.

## 7. Yeniden üretme

```bash
cd prototip
python veri/soru_seti_olustur.py        # Set B (ders verisi gerekir)
python deney_erisim.py                  # E-2 ve kapı
python deney_uctan_uca.py calistir      # E-1 uçtan uca (Ollama + Cosmos T1)
python deney_uctan_uca.py ozet
python deney_sizinti.py calistir        # E-4
python deney_sizinti.py ozet
```
