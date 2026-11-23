# PROJE DOSYASI · 02 · Ar-Ge İçeriği ve Teknik Tasarım

Bu bölüm hakem formundaki şu ölçütleri besliyor: **yenilik (%10), uygulanabilirlik (%6), tekniğin bilinen durumunu aşma (%6), teknolojik bilgi/know-how (%10), ekip uzmanlığı (%6)**. Hakemin "bu bir Ar-Ge projesi mi?" sorusunun cevabı bu belgede.

---

## 1. Bu proje neden Ar-Ge? (Frascati ölçütleri)

OECD Frascati Kılavuzu'na göre bir faaliyetin Ar-Ge sayılması için beş ölçütü sağlaması gerekiyor:

| Ölçüt | Projedeki karşılığı |
|---|---|
| **Yeni (novel)** | Türkçe eğitim içeriğinde kaynağa kilitli üretim + rubrik tabanlı değerlendirme + pedagojik sızıntı kontrolünün **tek sistemde ve ölçülmüş başarımla** birleştirilmesi. Yerli literatürde ve üründe bu birleşim yok (belge 01, §4). |
| **Yaratıcı (creative)** | Türkçe'ye özgü hibrit erişim, cevaplanabilirlik kapısı, iddia düzeyinde doğrulama, çapa tabanlı kalibrasyon gibi özgün yöntem kombinasyonları tasarlanacak; hazır bir kütüphaneyle çözülemiyor. |
| **Belirsiz (uncertain)** | Hedeflerin ulaşılabilirliği **bilinmiyor**. Örneğin literatürde YZ-insan puan uyumu 0,4–0,7 iken ≥ 0,75 hedefi; Türkçe'de sadakat ≥ %95 ve reddetme ≥ %90 hedeflerinin aynı anda sağlanması (birini artırmak diğerini düşürebilir). |
| **Sistematik (systematic)** | Her araştırma sorusu için hipotez, deney tasarımı, test seti, metrik ve istatistiksel analiz önceden tanımlandı (belge 03). |
| **Aktarılabilir / tekrarlanabilir** | Test setleri, değerlendirme protokolü ve sonuçlar belgelenecek; YTÜ ile ortak yayın ve fikri mülkiyet başvurusu hedefleniyor. |

**Ar-Ge olmayan kısım ve ayrımı:** Kayıt, rol yönetimi, takvim, bildirim, ödeme gibi platform işlevleri rutin yazılım geliştirme. Bunlar "test yatağı" olarak yapılıyor ve **toplam eforun ≈ %25–30'u** ile sınırlı tutuluyor. Bu efor proje raporlarında ayrı iş paketinde (İP-2) izleniyor.

---

## 2. Araştırma soruları, hipotezler ve başarı ölçütleri

Her soru için: **H** = hipotez, **Temel çizgi** = bugünkü bilinen durum, **Hedef** = projenin aşmayı amaçladığı değer, **B planı** = hedefe ulaşılamazsa ne yapılacağı.

### AR-1 · Kaynağa sadakat ve doğru reddetme
- **Soru:** Türkçe ders içeriğinde bir dil modeli, cevabını **yalnızca** verilen ders kaynaklarına dayandırabilir mi ve kaynakta cevabı olmayan soruları güvenilir biçimde reddedebilir mi?
- **H1.1:** Cevaplanabilirlik kapısı (erişim skoru + kanıt yeterliliği sınıflandırıcısı) ile iddia düzeyinde doğrulama birlikte kullanıldığında, tek başına "sadece kaynaktan cevap ver" talimatına göre sadakat **en az 10 puan** artar.
- **H1.2:** Reddetme eşiği ceza-duyarlı skorla (doğru cevap +1, yanlış cevap −4, ret 0) kalibre edildiğinde sadakat ≥ %95 ve reddetme doğruluğu ≥ %90 aynı anda sağlanabilir.
- **Temel çizgi [LİTERATÜR]:** Ticari RAG ürünlerinde reddetme oranı %0,2–%11,1 arasında değişiyor ve en büyük kalite farkını yaratıyor (arXiv 2608.26385). Standart sadakat ölçücülerinin reddetmeyi iyi ölçmediği gösterildi (RAGAS/DeepEval karşılaştırması, ResearchGate 399331938).
- **Hedef:** Sadakat ≥ %95 · Kaynak dışı soru reddetme doğruluğu ≥ %90 · Gereksiz reddetme ≤ %8 · Atıf doğruluğu ≥ %95
- **B planı:** Eşik kurum bazında ayarlanabilir hâle getirilir. Belirsiz durumda "kısmi cevap + kaynakta eksik olan kısım" şablonu kullanılır. Hedefin altında kalan ders türleri raporlanır.

### AR-2 · Türkçe için hibrit bilgi erişimi
- **Soru:** Sondan eklemeli Türkçe'de (ör. "türevlerinin", "türevini aldığımızda") ve teknik terim karışık eğitim içeriğinde, doğru kaynak parçasını ilk 5 sonuç içinde bulmak için hangi parçalama, embedding ve sıralama birleşimi en iyisi?
- **H2.1:** Yoğun (dense) + seyrek (Türkçe kök bulmalı BM25) hibrit erişim ve ardından çapraz kodlayıcıyla yeniden sıralama, en iyi tek yöntemden Recall@5'te en az 8 puan daha iyidir.
- **H2.2:** Yapı-farkındalıklı parçalama (başlık hiyerarşisi, slayt birimi, video konu segmenti), sabit uzunluklu parçalamadan daha iyidir.
- **Temel çizgi [LİTERATÜR]:** Türkçe gömme modeli karşılaştırmalarında sıralama karışık. TR-TEB'de BGE-M3 63,76 ile önde; TR-MTEB'de (EMNLP 2025) multilingual-e5-base en tutarlı; bir 2026 çalışmasında embeddinggemma-300m 65,42 ile en yüksek. **Eğitim içeriği için hangisinin en iyi olduğu bilinmiyor; bu projenin deneysel sorusu.** Uzun metinlerde 8K bağlamlı modellerin 512 tokenlı modellerden daha iyi olduğu raporlandı (TR-TEB).
- **Hedef:** Recall@5 ≥ %90 · MRR@10 ≥ 0,75 (kendi Türkçe eğitim test setimizde)
- **B planı:** Ders bazında terim sözlüğü ile sorgu genişletme; gerekirse turkish-e5 / bge-m3 üzerinde alan uyarlamalı ince ayar (kendi veri setiyle).

### AR-3 · Rubrik tabanlı otomatik ödev değerlendirme
- **Soru:** Bir dil modeli, eğitmenin rubriğine göre açık uçlu Türkçe ödevleri **insan eğitmenle uyumlu**, tutarlı ve kanıtlı biçimde ön-değerlendirebilir mi?
- **H3.1:** Kriter başına kanıt çıkarımı + eğitmen puanlı çapa örnekleri + çoklu örnekleme birleşimi, doğrudan "bu ödevi puanla" yaklaşımına göre ağırlıklı Kappa'yı en az 0,15 artırır.
- **H3.2:** Belirsizliği yüksek ödevleri (örnekler arası anlaşmazlık) eğitmene yönlendirmek, otomatik değerlendirilen kısımda uyumu ≥ 0,80'e çıkarır; bu sırada eğitmen iş yükü ≥ %40 azalır.
- **Temel çizgi [LİTERATÜR]:** Hazır modellerde insanla uyum ≈ 0,4–0,7 (gpt-3.5 ile 0,68; Gemini ile ASAP'ta 0,45; İtalyanca yükseköğretim çalışmasında düşük ve anlamsız). Rubriğin yinelemeli iyileştirilmesiyle +0,19 ile +0,47 arası Kappa artışı raporlandı (arXiv 2510.09030). Kapalı modellerin argüman netliği gibi üst düzey kriterlerde zayıf olduğu bulundu (EssayJudge).
- **Hedef:** Ağırlıklı Kappa ≥ 0,75 (tüm set) · ≥ 0,80 (otomatik değerlendirilen alt küme) · Aynı ödevin tekrar puanlanmasında tutarlılık ≥ 0,90 · Geri bildirimin eğitmenlerce "kullanılabilir" bulunması ≥ %80
- **B planı:** Sistem "otomatik puanlayıcı" yerine "eğitmen asistanı" konumunda kalır: kanıt çıkarımı ve geri bildirim taslağı üretir, puanı eğitmen verir. Ürün değeri korunur; zaten AB YZ Yasası insan gözetimini zorunlu kılıyor.

### AR-4 · Pedagojik sınırlar ve cevap sızıntısı
- **Soru:** Öğrenci ödevin cevabını doğrudan istediğinde ya da manipülasyonla almaya çalıştığında sistem cevabı vermeden, öğrenmeyi destekleyen ipuçlarıyla yönlendirebilir mi?
- **H4.1:** Niyet sınıflandırma + ödev eşleme + deterministik sızıntı tarayıcısı + ipucu merdiveni birleşimi, yalnızca talimata (prompt) dayalı korumaya göre sızıntıyı en az %70 azaltır.
- **Temel çizgi [LİTERATÜR]:** Korumasız sohbet botu sonraki sınav başarısını düşürürken Sokratik koruma bu kaybı kaldırdı (Bastani ve ark., PNAS 2025). Deterministik ön tarama, sızıntıyı azaltmada en etkili tek aşama olarak raporlandı (SocraGate, Applied Sciences 2026).
- **Hedef:** Sızıntı oranı ≤ %2 · Saldırı (jailbreak) test setinde direnç ≥ %95 · Meşru kavram sorularında gereksiz kısıtlama ≤ %5
- **B planı:** Eğitmen bazında "kapalı mod" (ödev süresince sohbet yalnızca kavram açıklar). Kritik ödevler için cevap anahtarı yüklemesi zorunlu tutulur.

### AR-5 · Çok kipli içerik işleme
- **Soru:** PDF, slayt (görsel, tablo ve formül dahil) ve ders videosundan, atıf verilebilir tek bir bilgi tabanı oluşturulabilir mi?
- **H5.1:** Zaman damgalı transkript ve slayt hizalaması ile videodan gelen cevapların atıf doğruluğu ≥ %90 olur.
- **Temel çizgi [LİTERATÜR]:** Whisper large-v3 Türkçe kelime hata oranı FLEURS'ta ≈ %6, Common Voice'ta ≈ %7,7 (arXiv 2611.03605). Gerçek sınıf kayıtlarında (gürültü, terim, konuşma dili) daha yüksek olması bekleniyor.
- **Hedef:** Ders kaydı kelime hata oranı ≤ %10 · Tablo ve görsel kaynaklı sorularda doğru cevap ≥ %85 · Video atıf doğruluğu ≥ %90
- **B planı:** Ders bazında terim sözlüğüyle konuşma tanıma düzeltmesi (ör. ilk istem / sonradan düzeltme); görsel içerikte eğitmen onaylı açıklama.

### AR-6 · Yurt içi açık model, maliyet ve veri egemenliği
- **Soru:** Yurt içinde barındırılan açık ağırlıklı (tercihen Türkçe odaklı) modeller, ticari büyük modellere yakın kalite ile, öğrenci başına sürdürülebilir maliyette çalışabilir mi?
- **H6.1:** Görev bazlı model yönlendirme (sınıflandırma ve doğrulama için küçük model, üretim için orta model) ve 4-bit nicemleme ile, ticari modele göre kalite kaybı ≤ %5 iken maliyet ≥ %60 düşer.
- **Temel çizgi [LİTERATÜR]:** Cosmos T1 (9B), Türkçe GSM8K'da %77,41 doğruluk; ekibin beyanına göre Llama-3.1-70B (%66,13) ve Gemma-2-9B'nin (%63,10) önünde. Bağımsız doğrulama yok; **bu proje kendi görevlerimizde ölçecek.**
- **Hedef:** Yanıt süresi p50 ≤ 3 sn, p95 ≤ 6 sn · Kalite farkı ≤ %5 (AR-1 ve AR-3 metriklerinde) · Öğrenci başı aylık YZ maliyeti hedef fiyatın ≤ %20'si
- **B planı:** Hibrit model: hassas veri yurt içi modelde, anonimleştirilmiş zor görevler ticari API'de (kurum izniyle, KVKK standart sözleşmesiyle).

### AR-7 · (Opsiyonel) Türkçe YZ ile yazılmış metin ve intihal tespiti
- **Hedef:** Türkçe ödevlerde tespit doğruluğu ≥ %85, yanlış suçlama ≤ %5. Yanlış suçlamanın etik maliyeti yüksek olduğundan çıktı yalnızca eğitmene "inceleme önerisi" olarak gösterilir.
- **Not:** Bu alanın güvenilirliği literatürde tartışmalı. Hedefe ulaşılamazsa kapsamdan çıkarılır (İP-5, görev 5.6).

---

## 3. Sistem mimarisi

### 3.1 Katmanlı görünüm

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│  İSTEMCİLER   Web (Next.js, PWA, mobil uyumlu)  ·  Eğitmen paneli  ·  Kurum paneli  │
└──────────────────────────────┬───────────────────────────────────────────────────┘
                               │ HTTPS (TLS 1.3)
┌──────────────────────────────▼───────────────────────────────────────────────────┐
│  API GEÇİDİ  kimlik doğrulama (OIDC/JWT) · hız sınırlama · kiracı (tenant) çözümü │
└───────┬───────────────────────┬──────────────────────────┬───────────────────────┘
        │                       │                          │
┌───────▼────────┐   ┌──────────▼───────────┐   ┌──────────▼──────────────────────┐
│ PLATFORM       │   │ YZ ORKESTRASYON      │   │ İÇERİK İŞLEME HATTI (asenkron)  │
│ SERVİSİ        │   │ SERVİSİ              │   │                                 │
│ • Kurum/ders   │   │ • Niyet & politika   │   │ • Belge ayrıştırma (PDF/PPTX)   │
│ • Kayıt/rol    │   │ • Sorgu işleme       │   │ • OCR · görsel açıklama         │
│ • Ödev teslim  │   │ • Hibrit erişim      │   │ • Konuşma tanıma (video)        │
│ • Takvim/bild. │   │ • Cevaplanabilirlik  │   │ • Parçalama · gömme · indeks    │
│ • Canlı ders   │   │ • Üretim + atıf      │   │                                 │
│ • Ödeme (B2C)  │   │ • İddia doğrulama    │   │ Kuyruk: Redis + işçi süreçleri  │
│                │   │ • Rubrik değerlend.  │   │                                 │
└───────┬────────┘   └──────────┬───────────┘   └──────────┬──────────────────────┘
        │                       │                          │
┌───────▼───────────────────────▼──────────────────────────▼───────────────────────┐
│ VERİ KATMANI                                                                       │
│ PostgreSQL 16+ (satır düzeyi güvenlik, pgvector, tam metin 'turkish')              │
│ Nesne deposu (S3 uyumlu, yurt içi)  ·  Redis (önbellek, kuyruk)                    │
└───────────────────────────────────────┬──────────────────────────────────────────┘
                                        │
┌───────────────────────────────────────▼──────────────────────────────────────────┐
│ MODEL SERVİS KATMANI (yurt içi GPU)                                                │
│ vLLM: üretim modeli (ör. Cosmos T1 / Turkish-Gemma / Qwen ailesi — deneyle seçilir)│
│ Gömme modeli (bge-m3 / turkish-e5-large / embeddinggemma — deneyle seçilir)        │
│ Yeniden sıralayıcı (bge-reranker-v2-m3) · Konuşma tanıma (faster-whisper large-v3) │
│ Model yönlendirici → (isteğe bağlı, anonimleştirilmiş) ticari API                  │
└──────────────────────────────────────────────────────────────────────────────────┘
   Yan sistemler: BigBlueButton (canlı ders, yurt içi) · Langfuse (LLM izleme, yurt içi)
                  Değerlendirme düzeneği (CI'da regresyon testi) · Prometheus/Grafana
```

### 3.2 Teknoloji yığını ve gerekçeler

| Katman | Seçim | Gerekçe | Alternatif | Lisans |
|---|---|---|---|---|
| Ön yüz | Next.js (React, TypeScript), PWA | Mobil uyumlu, SEO (B2C), geniş geliştirici havuzu | Vue/Nuxt | MIT |
| Platform API | Python FastAPI (modüler monolit) | YZ servisleriyle aynı dil; hızlı geliştirme; tek ekip | NestJS | MIT |
| YZ orkestrasyon | Python, sade iç kütüphane (gerekirse LlamaIndex/LangGraph parçaları) | Ar-Ge'nin kendisi bu katmanda; kara kutu çerçeveye bağımlı olmamak | LangChain | — |
| Veritabanı | PostgreSQL + pgvector + `turkish` tam metin yapılandırması | Tek veritabanında ilişkisel + vektör + BM25 benzeri arama; satır düzeyi güvenlik ile kiracı ayrımı | Qdrant + OpenSearch (ölçek gerekirse) | PostgreSQL / Apache-2.0 |
| Kuyruk | Redis + Arq/Celery | Asenkron içerik işleme | RabbitMQ | BSD |
| Nesne deposu | S3 uyumlu (yurt içi bulut veya MinIO) | Yurt içi veri | — | AGPL (MinIO) / ticari |
| Canlı ders | **BigBlueButton** (kendi sunucumuzda) | Açık kaynak; kayıt, beyaz tahta, eğitim odaklı; veri yurt içinde | Jitsi; Zoom/Meet API (müşteri talebiyle) | LGPL |
| Üretim modeli | vLLM üzerinde açık ağırlıklı model; **aday:** Cosmos T1 (Gemma lisansı), Turkish-Llama-8B, Qwen/Gemma aileleri | Yurt içi, ticari kullanım uygun lisanslar; Türkçe başarımı | Ticari API (anonimleştirilmiş) | Model lisansına göre |
| Gömme | **Aday:** bge-m3, turkish-e5-large (YTÜ COSMOS), multilingual-e5-large, embeddinggemma-300m | Türkçe karşılaştırmalarda öne çıkanlar; seçim İP-3 deneyiyle | — | MIT / Apache |
| Yeniden sıralama | bge-reranker-v2-m3 | Çok dilli çapraz kodlayıcı | Türkçe ince ayarlı reranker (Ar-Ge çıktısı olabilir) | Apache-2.0 |
| Belge ayrıştırma | Docling / marker + Tesseract (`tur`) / PaddleOCR | Tablo ve başlık yapısını koruyor; Türkçe OCR | Ticari OCR | MIT / Apache |
| Konuşma tanıma | faster-whisper (large-v3), gerekirse Türkçe ince ayarlı sürüm | Türkçe başarımı iyi; yurt içinde çalışır | Ticari konuşma tanıma API'si | MIT |
| LLM izleme | Langfuse (kendi sunucumuzda) | İzleme, istem sürümleme, değerlendirme kayıtları (AB YZ Yasası kayıt tutma) | — | MIT |
| Ödeme (B2C) | iyzico / PayTR | Yerli ödeme kuruluşları | Stripe (yurt dışı satış için) | Ticari |
| Altyapı | Docker + Kubernetes (k3s/RKE2), Terraform, GitHub Actions | Taşınabilirlik; kurum içi kurulum paketi | — | Apache |

**İlke:** Projenin Ar-Ge katmanı (YZ orkestrasyon ve değerlendirme) kendi kodumuz; çerçeveye kilitlenmiyoruz. Platform katmanı ise olgun, hazır bileşenlerle hızlı kuruluyor.

---

## 4. Veri akışları ve algoritmalar

### 4.1 İçerik alım hattı (eğitmen kaynak yüklediğinde)

```
Yükleme ─► Tür tespiti ─┬─ PDF/DOCX ─► yapı-farkındalıklı ayrıştırma (başlık, paragraf, tablo, sayfa no)
                        ├─ PPTX ─────► slayt metni + konuşmacı notu + slayt görseli ─► görsel açıklama (VLM)
                        ├─ Görsel/taranmış ─► OCR (Türkçe) ─► düzen kurtarma
                        └─ Video/ses ─► konuşma tanıma (zaman damgalı) ─► konu segmentasyonu ─► (ops.) slayt hizalama
        ─► Türkçe normalizasyon ─► parçalama ─► meta veri ekleme ─► gömme + tam metin indeksleme ─► "hazır"
```

**Türkçe normalizasyon:**
- Unicode NFC; **Türkçe'ye özgü büyük-küçük harf dönüşümü** (İ↔i, I↔ı). Standart `lower()` "İSTANBUL"u yanlış dönüştürüyor; bu Türkçe erişimde klasik bir hata kaynağı.
- Şapka ve noktasız yazımlara karşı ikinci bir "sade" indeks alanı ("kâr/kar", öğrencinin "ogrenci" yazması gibi)
- Kök bulma: PostgreSQL `turkish` Snowball sözlüğü (temel çizgi); Zemberek tabanlı biçimbirimsel çözümleme (deney kolu)
- Ders bazında **terim sözlüğü**: eğitmenin tanımladığı eş anlamlılar ve kısaltmalar (ör. "TYT", "türev = derivative")

**Parçalama stratejisi (H2.2 deneyi):**
| Kaynak | Birim | Hedef boyut | Bağlam |
|---|---|---|---|
| PDF/DOCX | Başlık altı bölüm → paragraf grupları | 300–500 token, %10–15 örtüşme | Üst-alt (parent-child): küçük parça erişim için, üst bölüm üretime bağlam olarak |
| Slayt | 1 slayt = 1 parça (+ konuşmacı notu + görsel açıklaması) | Değişken | Komşu slaytlar bağlam |
| Video | Konu segmenti (60–180 sn), zaman damgalı | 200–400 token | Segment başlığı (otomatik özet) |

Her parçanın meta verisi: `kurum_id, ders_id, kaynak_id, tür, sayfa/slayt/zaman_aralığı, hafta, başlık_yolu, eğitmen_onay_durumu, sürüm`.

### 4.2 Soru-cevap hattı (öğrenci soru sorduğunda)

```
Soru
 │
 ├─► [1] Niyet ve politika sınıflandırma ──► kapsam dışı / zararlı ─► kibar ret + yönlendirme
 │        (kavram sorusu · ödev çözüm talebi · sınav sorusu · platform yardımı · sohbet)
 │                 └─► ödev çözüm talebi ─► PEDAGOJİK MOD (§4.3)
 │
 ├─► [2] Sorgu işleme: konuşma geçmişinden bağımsız soru üretme · çok parçalı soruyu bölme
 │        · Türkçe normalizasyon · terim sözlüğü genişletme
 │
 ├─► [3] Hibrit erişim: yoğun (pgvector HNSW, k=40) + seyrek (tam metin 'turkish', k=40)
 │        ─► Karşılıklı Sıra Birleştirme (RRF, k=60) ─► yeniden sıralama (top-20 → top-5)
 │        Filtre: kurum_id + ders_id (satır düzeyi güvenlik) + eğitmenin yayımladığı kaynaklar
 │
 ├─► [4] CEVAPLANABİLİRLİK KAPISI
 │        özellikler: en iyi reranker skoru, skor dağılımı, kanıt kapsama sınıflandırıcısı
 │        ─► eşik altı ─► RET: "Bu sorunun cevabı ders kaynaklarında yok. Eğitmenine sor / ilgili
 │                         olabilecek bölümler: …" (+ eğitmene 'cevapsız soru' raporu)
 │
 ├─► [5] Kısıtlı üretim: yalnızca seçilen kanıt parçaları; her cümle [K1]..[K5] atfı zorunlu;
 │        düşük sıcaklık; Türkçe pedagojik üslup; uzunluk sınırı
 │
 ├─► [6] İDDİA DÜZEYİNDE DOĞRULAMA
 │        cevap ─► atomik iddialara ayır ─► her iddia için atıf verilen parçayla çıkarım kontrolü
 │        ─► desteklenmeyen iddia: (a) çıkar, (b) yeniden üret (1 kez), (c) hâlâ yoksa RET
 │        ─► atıf doğruluğu kontrolü (atıf verilen parça gerçekten destekliyor mu?)
 │
 └─► [7] Yanıt + tıklanabilir atıflar (PDF sayfası / slayt / video dakikası) + "yararlı mı?" geri bildirimi
          Kayıt: istek, erişilen parçalar, skorlar, model sürümü, karar (AB YZ Yasası kayıt tutma)
```

**Ceza-duyarlı eşik kalibrasyonu (H1.2):** Doğrulama setinde eşik değeri taranır ve beklenen fayda `F = (+1)·doğru − 4·yanlış + 0·ret` en büyük olan eşik seçilir. Ceza katsayısı (4) eğitimde yanlış bilginin maliyetini yansıtıyor; kurum bazında 2–8 arası ayarlanabilir.

### 4.3 Pedagojik mod ve sızıntı kontrolü

**Ödev eşleme:** Öğrencinin sorusu, aktif ödevlerin metniyle (ve varsa eğitmenin işaretlediği "korumalı sorular"la) anlamsal olarak karşılaştırılır. Benzerlik eşiği aşılırsa pedagojik mod devreye girer.

**İpucu merdiveni:**
| Seviye | Ne verir | Örnek |
|---|---|---|
| L0 | İlgili kavramın kaynaktaki yerini hatırlatma | "Bu, Hafta 4 notundaki zincir kuralıyla ilgili (s. 12)." |
| L1 | Yönlendirici soru | "Dış fonksiyon ve iç fonksiyon hangileri sence?" |
| L2 | İlk adımı gösterme (cevap değil) | "İlk adımda dış fonksiyonun türevini alıyoruz…" |
| L3 | **Benzer ama farklı** çözülmüş örnek (kaynaktan) | "Kaynaktaki Örnek 4.3'e bak; aynı yöntemle…" |
| — | **Asla:** ödevin nihai cevabı, tam çözümü, teslim edilebilir metin | — |

Öğrenci her seviyede kendi girişimini yazınca sistem **onun adımını değerlendirir** ("bu adım doğru / şurada hata var"). Böylece öğrenci üretim yaparak ilerler.

**Deterministik sızıntı tarayıcısı (çıktı kapısı):** Üretilen yanıt, eğitmenin cevap anahtarı (varsa) ve ödev çözüm kalıplarıyla n-gram ve anlamsal benzerlik açısından taranır. Eşik aşılırsa yanıt engellenir ve bir alt seviyeden yeniden üretilir.

**Saldırı direnci (test kategorileri):** rol yapma ("öğretmen modundasın"), sahte yetki ("hocam izin verdi"), parçalı sorma (cevabı adım adım sızdırma), dil değiştirme (İngilizce sorma), biçim hilesi ("kod bloğu olarak yaz"), dolaylı istem enjeksiyonu (yüklenen ödev dosyasına gizlenmiş talimat).

**Eğitmen kontrolü (ders/ödev bazında):** `serbest` (kavram + çözüm açıklaması) · `sokratik` (varsayılan) · `kapalı` (ödev süresince yalnızca kavram hatırlatma).

### 4.4 Rubrik tabanlı ödev değerlendirme hattı

**Rubrik şeması (örnek):**
```json
{
  "rubrik_id": "R-2027-ANALIZ-04",
  "olcek": "0-4",
  "kriterler": [
    {"id": "K1", "ad": "Kavramsal doğruluk", "agirlik": 0.40,
     "seviyeler": {"4": "Tüm kavramlar doğru ve kaynaktaki tanımlarla uyumlu", "3": "...", "2": "...", "1": "...", "0": "Yok / tamamen hatalı"}},
    {"id": "K2", "ad": "Yöntem ve adımlar", "agirlik": 0.30, "seviyeler": {"...": "..."}},
    {"id": "K3", "ad": "Gerekçelendirme", "agirlik": 0.20, "seviyeler": {"...": "..."}},
    {"id": "K4", "ad": "Sunum ve dil", "agirlik": 0.10, "seviyeler": {"...": "..."}}
  ],
  "capa_ornekler": ["odev_id_A (eğitmen puanı: K1=4,K2=3…)", "odev_id_B (…)", "odev_id_C (…)"],
  "kaynak_baglami": ["ders_id/hafta_4", "ders_id/hafta_5"]
}
```

**Hat:**
```
Teslim ─► ön işleme (PDF/DOCX → yapılandırılmış metin; dolaylı istem enjeksiyonu temizliği)
  ─► [1] Kriter başına KANIT ÇIKARIMI: ödevden alıntı + konum (paragraf/satır)
  ─► [2] Kriter başına SEVİYE TAHMİNİ: rubrik betimleyicileri + eğitmen puanlı çapa örnekler
         (karşılaştırmalı: "bu kanıt, çapa A ile çapa B arasında mı?") + ilgili ders kaynağı
  ─► [3] ÇOKLU ÖRNEKLEME (n = 3–5) ─► dağılım ─► belirsizlik skoru
  ─► [4] KALİBRASYON: ders bazında eğitmen puanlarıyla eğitilen sıralı (ordinal) düzeltme modeli
         (girdi: örnek puanları, belirsizlik, uzunluk vb.; uzunluk yanlılığı kontrolü)
  ─► [5] KARAR: belirsizlik > eşik ─► "eğitmen incelemesi gerekli" işareti
  ─► [6] GERİ BİLDİRİM: kriter başına güçlü yön / geliştirme önerisi, ödevden alıntı ve
         ders kaynağına atıfla ("Hafta 4 notu s. 12'deki tanımı tekrar oku")
  ─► [7] EĞİTMEN ONAY EKRANI: puanı onayla / düzelt (düzeltmeler kalibrasyon verisine döner)
```

**Rubrik iyileştirme döngüsü:** Eğitmen düzeltmelerinin yoğunlaştığı kriterlerde sistem, betimleyicinin belirsiz olduğu yerleri işaretler ve eğitmene daha net ifade önerir (yansıt-düzelt yaklaşımı; arXiv 2510.09030).

**Adalet kontrolleri:** puanın ödev uzunluğu, yazım hataları ve ağız/üslup farklılıklarıyla korelasyonu izlenir. Anlamlı yanlılık bulunursa raporlanır ve kalibrasyonda düzeltilir.

**Faz 1 ödev türleri:** açık uçlu metin cevapları, rapor ve kompozisyonlar (PDF/DOCX), kısa cevaplı sorular. **Kapsam dışı:** el yazısı ve fotoğraf ödevler (Faz 3+). Kod ödevleri kurum eğitim alanına göre opsiyonel.

### 4.5 Model servis ve yönlendirme

| Görev | Model sınıfı | Not |
|---|---|---|
| Niyet sınıflandırma, ödev eşleme | Küçük kodlayıcı / küçük LLM | Düşük gecikme |
| Gömme, yeniden sıralama | Gömme + çapraz kodlayıcı | GPU paylaşımlı |
| Cevap üretimi, geri bildirim | Orta boy (≈ 8–14B) açık model, 4-bit nicemleme | vLLM, sürekli toplu işleme (continuous batching) |
| İddia doğrulama | Küçük-orta model veya NLI modeli | Paralel çalıştırma |
| Zor ve uzun bağlam görevleri | (İsteğe bağlı) ticari API | Kurum izni + kişisel veri maskeleme + KVKK standart sözleşmesi |

**Kapasite kaba hesabı (Faz 1 pilot):** 300 öğrenci, en yoğun saatte %10 eşzamanlı = 30 kullanıcı, kullanıcı başına dakikada ≈ 1 soru → dakikada ≈ 30 istek. Tek bir 48 GB'lık GPU'da (ör. L40S sınıfı) 4-bit 8–9B model + gömme + reranker bu yükü karşılayabilir **[VARSAYIM: İP-6 yük testiyle doğrulanacak]**. Dış kurum ölçeğinde (10.000 öğrenci) yatay ölçekleme ve kurum bazlı kota uygulanır.

**Anlamsal önbellek:** Aynı derste sık sorulan sorular için doğrulanmış cevaplar önbelleğe alınır (kaynak sürümü değişince geçersiz olur). Maliyeti ve gecikmeyi düşürür.

---

## 5. Platform (test yatağı) tasarımı

### 5.1 Modüller
| Modül | İşlevler |
|---|---|
| Kurum ve kullanıcı | Çok kiracılı yapı; roller: **sistem yöneticisi, kurum yöneticisi, eğitmen, asistan eğitmen, öğrenci, bireysel eğitmen (B2C)**; davet bağlantısı veya sınıf kodu ile katılım; toplu içe aktarma (CSV) |
| Ders alanı | Ders, şube ve dönem; haftalık yapı; kaynak kütüphanesi (yayımla/taslak); duyurular |
| Canlı ders | BigBlueButton oturumu oluşturma ve katılma; kayıtların otomatik olarak ders kaynağına eklenmesi (→ transkript hattı); yoklama |
| Ödev | Ödev oluşturma (rubrik bağlama, korumalı soru işaretleme, cevap anahtarı); teslim (çoklu dosya); geç teslim kuralları; eğitmen değerlendirme ekranı (YZ önerisi + onay) |
| YZ asistanı | Ders sayfasında sohbet; atıf önizleme; "yararlı mı?" geri bildirimi; eğitmen için "cevapsız sorular" ve "sık sorulanlar" raporu |
| Takvim ve bildirim | Ders, ödev ve canlı ders takvimi; iCal dışa aktarma; e-posta ve uygulama içi bildirim |
| Ölçüm ve analitik | Kullanım metrikleri; YZ kalite panosu (sadakat, reddetme, eğitmen düzeltme oranı) |
| Ticari | B2C abonelik ve ödeme; kurum faturalama (öğrenci başı); kota yönetimi |

### 5.2 Yetki matrisi (özet)
| İşlem | Öğrenci | Eğitmen | Kurum yön. | Sistem yön. |
|---|---|---|---|---|
| Ders kaynağı yükle / yayımla | — | ✓ (kendi dersi) | ✓ | — |
| YZ'ye soru sor | ✓ | ✓ | — | — |
| Ödev teslim et | ✓ | — | — | — |
| YZ önerisini onayla / not ver | — | ✓ | — | — |
| Kurum genelinde rapor | — | — | ✓ | — |
| Pedagojik mod ayarı | — | ✓ | ✓ (varsayılan) | — |
| Kişisel veri dışa aktarma / silme talebi | ✓ (kendi verisi) | — | ✓ (işleme) | ✓ |

### 5.3 Çekirdek veri modeli (özet)
```
kurum(id, ad, plan, veri_konumu, ayarlar)
kullanici(id, kurum_id, rol, ad, eposta, kvkk_riza_surumu, olusturma)
ders(id, kurum_id, ad, donem, pedagojik_mod, terim_sozlugu_json)
ders_uyelik(ders_id, kullanici_id, rol)
kaynak(id, ders_id, tur, dosya_yolu, surum, durum[taslak/yayinda], isleme_durumu)
parca(id, kaynak_id, ders_id, kurum_id, metin, konum_json, hafta, embedding vector, tsv tsvector)
odev(id, ders_id, baslik, aciklama, rubrik_id, son_tarih, korumali_sorular_json, cevap_anahtari_yolu)
teslim(id, odev_id, ogrenci_id, dosya_yolu, metin, teslim_zamani)
degerlendirme(id, teslim_id, kaynak[yz/egitmen], kriter_puanlari_json, belirsizlik, geri_bildirim, onay_durumu, model_surumu)
rubrik(id, ders_id, sema_json, capa_teslimler)
sohbet(id, ders_id, kullanici_id) · mesaj(id, sohbet_id, rol, metin, atiflar_json, karar[cevap/ret/pedagojik], skorlar_json, model_surumu)
canli_ders(id, ders_id, bbb_oturum_id, kayit_kaynak_id, baslangic, bitis)
denetim_kaydi(id, kurum_id, aktor, eylem, nesne, zaman, ayrinti_json)   -- AB YZ Yasası / KVKK
```
Tüm tablolarda `kurum_id` ile **satır düzeyi güvenlik**: bir kurumun verisine başka kurumdan sorgu atılamaz.

### 5.4 API taslağı (seçme uç noktalar)
```
POST /api/v1/dersler/{ders_id}/kaynaklar            # yükle → işleme kuyruğu
GET  /api/v1/kaynaklar/{id}/durum                     # işleme ilerlemesi
POST /api/v1/dersler/{ders_id}/asistan/sor           # {soru, sohbet_id} → {cevap, atiflar[], karar}
POST /api/v1/odevler/{odev_id}/teslimler              # öğrenci teslimi
POST /api/v1/teslimler/{id}/yz-degerlendir            # rubrik tabanlı ön değerlendirme (asenkron)
PUT  /api/v1/degerlendirmeler/{id}/onay               # eğitmen onay/düzeltme
GET  /api/v1/dersler/{ders_id}/raporlar/cevapsiz-sorular
GET  /api/v1/kurum/kalite-panosu                      # sadakat, ret, düzeltme oranları
POST /api/v1/canli-dersler/{id}/webhook/kayit         # BBB kaydı hazır → transkript hattı
```

---

## 6. Güvenlik, KVKK ve AB YZ Yasası uyumu (tasarımın parçası)

| Gereksinim | Tasarım kararı |
|---|---|
| **Veri konumu** | Varsayılan: tüm veri ve modeller **yurt içi** veri merkezinde. Kurum içi kurulum seçeneği var. |
| **Yurt dışı aktarım (KVKK md. 9)** | Ticari API yalnızca kurum açıkça izin verirse; kişisel veri maskeleme (ad, e-posta, T.C. kimlik no, telefon); standart sözleşme ve Kurul'a bildirim süreci. |
| **Şifreleme** | Aktarımda TLS 1.3; durağan veride AES-256; anahtar yönetimi (KMS). |
| **Kiracı ayrımı** | PostgreSQL satır düzeyi güvenlik + uygulama katmanı kontrolü + otomatik sızma testleri. |
| **Açık rıza ve aydınlatma** | Öğrenci ve eğitmenlere YZ işleme için ayrı aydınlatma; **18 yaş altı için veli onayı**; VERBİS kaydı. |
| **Model eğitimi** | Öğrenci verisi varsayılan olarak model eğitiminde **kullanılmaz**. Kalibrasyon ve ince ayar yalnızca anonimleştirilmiş ve rızası alınmış veriyle yapılır. |
| **Saklama ve silme** | Kurum politikasına göre saklama süresi; silme talebi uç noktası; yedeklerde silme. |
| **AB YZ Yasası, yüksek risk (Ek III-3b)** | **İnsan gözetimi:** not kararı eğitmende. **Kayıt tutma:** her YZ kararının girdi, kanıt ve model sürümü kaydı. **Şeffaflık:** kullanıcıya YZ ile etkileşimde olduğu ve puanın "öneri" olduğu açıkça gösteriliyor. **Veri yönetişimi:** test setleri ve yanlılık analizi. **Teknik dokümantasyon:** bu belge + model kartları. |
| **Erişilebilirlik** | WCAG 2.2 AA hedefi (klavye, ekran okuyucu, kontrast). |
| **Güvenli yazılım geliştirme** | OWASP ASVS L2; bağımlılık taraması; Faz 1 sonunda bağımsız sızma testi. |

---

## 7. Projenin üreteceği teknolojik bilgi ve know-how (ölçüt 12, %10)

| Çıktı | Tür | Aktarılabilirlik |
|---|---|---|
| Türkçe eğitim soru-cevap test seti (≥ 500 soru, ≥ %20 kaynak dışı) | Veri seti | Anonimleştirilmiş sürümü YTÜ ile akademik yayında paylaşılabilir |
| Türkçe ödev değerlendirme veri seti (≥ 300 ödev, rubrik, çoklu eğitmen puanı) | Veri seti | Rıza kapsamına göre |
| Türkçe eğitim içeriği için gömme ve parçalama karşılaştırma raporu | Teknik rapor / makale | Yayın |
| Cevaplanabilirlik kapısı + iddia düzeyinde doğrulama yöntemi | Yöntem | Patent ön değerlendirmesi |
| Çapa tabanlı rubrik kalibrasyon yöntemi | Yöntem | Patent ön değerlendirmesi / makale |
| Pedagojik sızıntı tarayıcısı ve Türkçe saldırı test seti | Yöntem + veri seti | Ürün özelliği; makale |
| (Ops.) alan uyarlamalı Türkçe reranker / gömme | Model | Ticari sır veya açık lisans kararı |
| Değerlendirme düzeneği (eval harness) | Yazılım | Sürekli kalite güvencesi; Faz 2 ve 3'te yeniden kullanım |
