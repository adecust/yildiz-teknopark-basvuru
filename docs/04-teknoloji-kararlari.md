# Teknoloji Kararları ve Karşılaştırmalar

**Proje:** KAYNAK-YZ · **Tarih:** Kasım 2026 · **Durum:** Ön karar (her karar ilgili sprintte deneyle kesinleşir)

Bu belge, projede kullanılacak teknolojilerin alternatifleriyle karşılaştırmasını ve seçim gerekçelerini içerir. Görev ve sprint bazında hangi teknolojinin kullanılacağı [`03-proje-plani-sprint-ve-kanban.md`](03-proje-plani-sprint-ve-kanban.md) belgesinde ve GitHub issue'larında yer alır.

## Karar ilkeleri

Seçimlerde aşağıdaki ölçütler sırasıyla gözetilmiştir:

1. **Veri egemenliği:** Kişisel veri ve modeller yurt içinde barındırılabilmeli; kurum içi kurulum mümkün olmalıdır.
2. **Lisans uygunluğu:** Ticari kullanıma ve kurum içi kurulum lisansı satışına engel olmamalıdır (GPL/AGPL bileşenler dağıtılan pakette kullanılmaz).
3. **Türkçe başarımı:** Türkçe metin ve konuşmada yayımlanmış kanıt bulunmalıdır.
4. **Olgunluk ve sürdürülebilirlik:** Aktif geliştirilen, topluluğu güçlü projeler tercih edilir.
5. **Ekip uyumu:** Tek dil ağırlıklı (Python + TypeScript) küçük bir ekip tarafından yönetilebilir olmalıdır.
6. **Ar-Ge esnekliği:** Araştırma katmanı kara kutu çerçevelere bağlanmamalı; bileşenler deneyle değiştirilebilmelidir.

---

## K-01 · Arka uç çatısı

| Seçenek | Güçlü yön | Zayıf yön | Değerlendirme |
|---|---|---|---|
| **FastAPI (Python)** | YZ ekosistemiyle aynı dil; asenkron; otomatik OpenAPI belgesi | Yönetim paneli hazır gelmez | **Seçildi** |
| Django (Python) | Hazır yönetim paneli, olgun ORM | Asenkron ve API odaklı kullanımda daha ağır | Alternatif |
| NestJS (TypeScript) | Güçlü yapı | YZ servisleri için ikinci dil gerektirir | Elendi |

**Gerekçe:** Platform ve YZ servisleri aynı dilde yazılarak ekip ve bakım yükü azaltılır. **Kesinleşme:** Sprint 01 (G-1501).

## K-02 · Ön yüz

| Seçenek | Güçlü yön | Zayıf yön | Değerlendirme |
|---|---|---|---|
| **Next.js (React, TypeScript)** | Geniş geliştirici havuzu; sunucu tarafı oluşturma (bireysel satış sayfaları için arama motoru görünürlüğü) | Sürüm değişimleri sık | **Seçildi** |
| Nuxt (Vue) | Sade öğrenme eğrisi | Daha küçük ekosistem | Alternatif |
| SvelteKit | Yüksek performans | İşe alım havuzu dar | Elendi |

**Kesinleşme:** Sprint 01 (G-1501).

## K-03 · Veritabanı ve vektör arama

| Seçenek | Güçlü yön | Zayıf yön | Değerlendirme |
|---|---|---|---|
| **PostgreSQL + pgvector** | İlişkisel veri, vektör ve tam metin tek sistemde; satır düzeyi güvenlikle kurum ayrımı; tek yedekleme | Hibrit arama elle kurulur | **Seçildi** |
| Qdrant | Tek konteyner, güçlü filtreleme | İkinci veri sistemi; senkronizasyon yükü | Ölçek eşiği aşılırsa geçiş seçeneği |
| Weaviate | Yerleşik hibrit arama | İkinci veri sistemi | Alternatif |
| Milvus | Çok büyük ölçek | etcd, MinIO ve çok sayıda servis; küçük ölçekte gereksiz | Elendi |

**Gerekçe:** 2026 karşılaştırmalarında küçük-orta ölçekte motorların erişim doğruluğu eşit bulunmuştur; fark işletme kolaylığındadır. Projenin ilk yıllardaki hacmi (milyonun altında parça) pgvector için uygundur. **Geçiş eşiği:** 10 milyon vektör veya p95 arama süresinin 300 ms'yi aşması. **Kesinleşme:** Sprint 09 (AR-806, AR-807).

## K-04 · Türkçe tam metin arama ve kök bulma

| Seçenek | Güçlü yön | Zayıf yön | Değerlendirme |
|---|---|---|---|
| **PostgreSQL 'turkish' sözlüğü (Snowball)** | Ek sistem gerektirmez | Kural tabanlı, sınırlı biçimbirim çözümleme | **Temel çizgi** |
| **Zemberek-NLP** | Türkçe biçimbirim çözümlemesi | Java tabanlı; ayrı servis | **Deney kolu** |
| OpenSearch (Türkçe analizör) | Güçlü arama motoru | Ek altyapı | Gerekirse |

**Ön bulgu (PoC, 26.11.2026):** BM25'te Snowball Türkçe kök bulma Recall@5'i ham sözcüğe göre %88,0'dan %94,0'a çıkardı; 5 harflik önek %92,8 verdi (docs/07). **Kesinleşme:** Sprint 06 (AR-803), E-2 deneyiyle.

## K-05 · Belge ayrıştırma

| Seçenek | Lisans | Güçlü yön | Zayıf yön | Değerlendirme |
|---|---|---|---|---|
| **Docling** | MIT | İç içe tablolarda güçlü; lisans sorunu yok | Büyük dosyalarda zaman aşımı bildirilmiş | **Seçildi** |
| Marker | GPL-3.0 | Satır içi formüllerde güçlü | GPL lisansı kurum içi kurulum paketinde dağıtılamaz; GPU gerektirir | **Yalnızca karşılaştırma kolu** |
| Unstructured (açık kaynak) | Apache-2.0 | Güvenilirlik ve çok biçim desteği | Tablo yapısında daha zayıf | Yedek seçenek |

**Gerekçe:** Bağımsız ve üretici karşılaştırmalarında Docling ile Marker basit tablolarda yakın, iç içe tablolarda Docling daha güçlü bulunmuştur. Lisans, kurum içi kurulum satışı için belirleyicidir. **Kesinleşme:** Sprint 06 (AR-801).

## K-06 · Optik karakter tanıma

**Seçim:** Tesseract (Türkçe dil paketi) temel çizgi; PaddleOCR deney kolu. Taranmış ders notlarında karakter doğruluğu ölçülerek seçilir. **Kesinleşme:** Sprint 06 (AR-801).

## K-07 · Konuşma tanıma (ders kayıtları)

| Seçenek | Güçlü yön | Zayıf yön | Değerlendirme |
|---|---|---|---|
| **faster-whisper (Whisper large-v3)** | Türkçe FLEURS testinde ≈ %6, Common Voice'ta ≈ %7,7 kelime hata oranı; yurt içinde çalışır | GPU gerektirir | **Seçildi** |
| Whisper large-v3-turbo | Daha hızlı | Türkçe ince ayarlı sürümde daha yüksek hata raporlanmış | Hız kolu |
| Ticari konuşma tanıma API'leri | Kurulum gerektirmez | Ses verisi yurt dışına çıkar | Elendi |

**Kesinleşme:** Sprint 06–08 (AR-804), en az 5 saatlik gerçek ders kaydıyla.

## K-08 · Gömme (embedding) modeli

| Aday | Lisans | Kanıt | Not |
|---|---|---|---|
| bge-m3 | MIT | TR-TEB'de 63,76 ile önde; 8K bağlam | Çok dilli, ihracat için avantaj |
| turkish-e5-large (YTÜ COSMOS) | MIT | Türkçeye özgü | Akademik iş birliğiyle uyumlu |
| multilingual-e5-large / base | MIT | TR-MTEB'de en tutarlı model (base) | Güçlü temel çizgi |
| embeddinggemma-300m | Gemma | Bir 2026 çalışmasında Türkçe MTEB'de 65,42 | Küçük ve hızlı |

**Gerekçe:** Türkçe karşılaştırmalarda sıralama çalışmaya göre değişmektedir; eğitim içeriği için en iyisi bilinmemektedir. Seçim, projenin kendi Türkçe test setinde yapılacaktır. **Ön bulgu (PoC, 26.11.2026):** tek başına bge-m3 (Recall@1 0,71) turkish-e5-large'dan (0,61) iyi; BM25 ile hibritte turkish-e5-large daha yüksek Recall@5 verdi (0,976'ya karşı 0,964). Model seçimi yöntemle etkileşimli (docs/07). **Kesinleşme:** Sprint 09 (AR-806).

## K-09 · Yeniden sıralama

**Seçim:** bge-reranker-v2-m3 (çok dilli çapraz kodlayıcı). Gerekirse kendi verimizle Türkçe ince ayar yapılır. **Kesinleşme:** Sprint 11 (AR-807).

## K-10 · Üretim (dil) modeli

| Aday | Lisans | Güçlü yön | Not |
|---|---|---|---|
| **Cosmos T1 / Turkish-Gemma-9b-T1 (YTÜ COSMOS)** | Gemma lisansı (ticari kullanım, kullanım politikasına uyum) | 200 milyar+ Türkçe token; Türkçe muhakeme | Yerli model; akademik iş birliğiyle uyumlu |
| Turkish-Llama-8b (YTÜ COSMOS) | Llama lisansı | Türkçe ince ayarlı | Lisans koşulları incelenecek |
| Qwen ailesi | Çoğunlukla Apache-2.0 | Güçlü çok dilli başarım | Boyut seçenekleri geniş |
| Ticari model API'si | Ticari | En yüksek genel başarım | Yalnızca karşılaştırma ve anonim veriyle |

**Gerekçe:** Veri egemenliği ve maliyet hedefi (AR-6) nedeniyle varsayılan seçenek yurt içinde barındırılan açık ağırlıklı modeldir. Kalite farkı (hedef ≤ %5) deneyle ölçülür. **Kesinleşme:** Sprint 16 (AR-1506) ve Sprint 18 (AR-1507).

## K-11 · Model servis sunucusu

| Seçenek | Durum (2026) | Güçlü yön | Değerlendirme |
|---|---|---|---|
| **vLLM** | Aktif | Olgun ekosistem; kolay dağıtım; sürekli toplu işleme | **Seçildi** |
| SGLang | Aktif | Ortak önek tekrarının yüksek olduğu iş yüklerinde daha yüksek hız (aynı ders bağlamı) | **Karşılaştırma kolu** |
| Hugging Face TGI | Bakım modunda | Düşük tek kullanıcı gecikmesi | Yeni kurulum için önerilmiyor |
| Ollama / llama.cpp | Aktif | Kolay yerel kullanım | Çok kullanıcılı üretim için uygun değil |

**Kesinleşme:** Sprint 16 (AR-1506) ve Sprint 18 (AR-1507).

## K-12 · YZ orkestrasyon katmanı

| Seçenek | Değerlendirme |
|---|---|
| **İnce, kendi kodumuz** (gerektiğinde kütüphanelerden parça) | **Seçildi.** Ar-Ge çekirdeği bu katmandadır; deney kollarının tam denetimi ve fikri mülkiyet için gereklidir |
| LangChain / LangGraph / LlamaIndex | Hızlı başlangıç sağlar ancak soyutlama katmanları deney denetimini ve bakımı zorlaştırır; yalnızca yardımcı parçalar kullanılabilir |

## K-13 · İzleme ve değerlendirme

| Seçenek | Lisans | Değerlendirme |
|---|---|---|
| **Langfuse (kendi sunucumuzda)** | MIT | **Seçildi.** İstek izleme, istem sürümleme, değerlendirme kayıtları; AB YZ Yasası kayıt tutma gereğini destekler |
| Arize Phoenix | Elastic / açık kaynak | Alternatif |
| **RAGAS + kendi değerlendirme düzeneğimiz** | Apache-2.0 | **Seçildi.** Standart ölçücüler reddetme davranışını iyi ölçmediğinden reddetme, sızıntı ve puan uyumu metrikleri kendi düzeneğimizde uygulanır |

## K-14 · Canlı ders altyapısı

| Seçenek | Güçlü yön | Zayıf yön | Değerlendirme |
|---|---|---|---|
| **BigBlueButton (kendi sunucumuzda)** | Eğitim odaklı; beyaz tahta, sunum, kayıt; Moodle/Canvas ile doğrudan entegrasyon | Üretimde en az 16 GB RAM; uçtan uca şifreleme yok | **Faz 1 için seçildi** |
| Jitsi Meet | Genel amaçlı; uçtan uca şifreleme | Eğitim araçları zayıf | Alternatif |
| **LiveKit** | Geliştiriciye yönelik gerçek zamanlı altyapı; özel deneyim kurulabilir | Hazır sınıf uygulaması değildir | **Faz 2 (sanal sınıf) için seçildi** |

**Kesinleşme:** Sprint 07 (US-501).

## K-15 · Kimlik yönetimi

| Seçenek | Değerlendirme |
|---|---|
| **Keycloak** | **Seçildi.** OIDC ve SAML; kurumların kendi kimlik sistemleriyle tek oturum açma talebini karşılar; kurum içi kurulumda paketlenebilir |
| Zitadel | Alternatif |
| Auth.js (uygulama içi) | Kurumsal tek oturum açma için yetersiz |

## K-16 · Ödeme (bireysel abonelik)

**Seçim:** iyzico (abonelik API'si, yerli ödeme kuruluşu). **Alternatif:** PayTR. Yurt dışı bireysel satış başladığında uluslararası ödeme sağlayıcısı değerlendirilecektir. **Kesinleşme:** Sprint 08 (US-1302).

## K-17 · Altyapı ve barındırma

| Seçenek | Güçlü yön | Zayıf yön | Değerlendirme |
|---|---|---|---|
| **Yurt içi GPU bulutu (kiralama)** | Hızlı başlangıç; veri yurt içinde; ihtiyaca göre ölçek | Uzun vadede maliyet | **Faz 1 için seçildi** |
| GPU sunucusu satın alma | 24+ ayda daha düşük maliyet; 4691 kapsamında makine-teçhizat KDV istisnası | Peşin yatırım; bakım | Faz 1 sonunda AR-1507 maliyet raporuyla yeniden değerlendirilecek |
| Yurt dışı büyük bulut | Geniş hizmet yelpazesi | KVKK yurt dışı aktarım yükü | Elendi |

**Sağlayıcı adayları:** Türkiye veri merkezlerinden L40S ve H100 sunan sağlayıcılar (ör. Cloud4U Türkiye, vMind) ve diğer yerli bulut sağlayıcıları; teklif alınarak seçilecektir. **Orkestrasyon:** Docker, Kubernetes (k3s/RKE2), Helm ve Terraform; kurum içi kurulum paketi de aynı yapıyla hazırlanır.

## K-18 · Veri etiketleme

**Seçim:** Label Studio (kendi sunucumuzda). Soru-cevap, ödev puanı ve sızıntı test setlerinin etiketlenmesi ve etiketleyiciler arası uyumun ölçülmesi için kullanılır. **Alternatif:** Argilla.

## K-19 · Test ve kalite güvencesi

| Alan | Araç |
|---|---|
| Birim ve entegrasyon testi | pytest |
| Uçtan uca test | Playwright |
| Yük testi | k6 |
| Güvenlik | OWASP ZAP + bağımsız sızma testi |
| Erişilebilirlik | axe-core (WCAG 2.2 AA) |
| YZ regresyon | Kendi değerlendirme düzeneğimiz (sürekli entegrasyonda kalite kapısı) |
| Sürekli entegrasyon | GitHub Actions |

## K-20 · Faz 2 (sanal sınıf) ön kararları

| Konu | Seçim | Alternatif | Not |
|---|---|---|---|
| 3B istemci | Three.js / React Three Fiber | Babylon.js, PlayCanvas | Web tabanlı, kurulum gerektirmez |
| Ses ve görüntü | LiveKit | — | Mekânsal ses istemci tarafında geliştirilecek |
| Oda ve durum senkronizasyonu | Colyseus | Kendi WebSocket katmanı | Deneyle kesinleşir |
| Ortak beyaz tahta | Yjs (CRDT) | — | Çevrimdışı uyumlu |
| Avatar | Açık VRM/GLB formatı (VRoid Studio, Avatar SDK değerlendirmesi) | — | Ready Player Me 31.01.2026 itibarıyla hizmetlerini sonlandırmıştır; kapalı bir platforma bağımlılıktan kaçınılır |

**Kesinleşme:** Faz 2 başlangıcı (US-2001).

---

## Kaynaklar

- [LLM inference engines compared 2026 (vLLM, SGLang, TGI)](https://dev.to/jangwook_kim_e31e7291ad98/llm-inference-engines-compared-2026-vllm-vs-sglang-vs-tgi-vs-max-4fpo) · [Prem AI: LLM inference servers compared 2026](https://blog.premai.io/llm-inference-servers-compared-vllm-vs-tgi-vs-sglang-vs-triton-2026) · [vLLM ve TGI karşılaştırmalı çalışma (arXiv 2511.17593)](https://arxiv.org/html/2511.17593v1)
- [Docling, Marker, MarkItDown karşılaştırması](https://dev.to/dmaxdev/markitdown-vs-docling-vs-marker-pdf-to-markdown-for-llms-571o) · [opendataloader-bench](https://github.com/opendataloader-project/opendataloader-bench) · [Unstructured benchmark](https://unstructured.io/benchmarks)
- [Vector databases in 2026](https://buttondown.com/ultradune/archive/eval-002-vector-databases-in-2026-qdrant-vs) · [AIMultiple açık kaynak vektör veritabanları](https://aimultiple.com/open-source-vector-databases) · [pgvector vs Qdrant vs Milvus 2026](https://dev.to/linou518/choosing-the-foundation-for-your-rag-system-pgvector-vs-qdrant-vs-milvus-2026-4i5o)
- [Jitsi ve BigBlueButton 2026](https://ossalt.com/guides/jitsi-vs-bigbluebutton-2026) · [Self-hosted video conferencing 2026](https://selfhosting.sh/best/video-conferencing/) · [LiveKit alternatifleri](https://getstream.io/blog/livekit-alternatives/)
- [Cloud4U Türkiye yapay zekâ altyapısı](https://www.cloud4u.com/news/cloud4u-ai-infrastructure-turkey/) · [vMind white paper](https://www.vmind.com.tr/pdf/white%20paper_rev.pdf)
- [Ready Player Me kapanışı (Frame VR)](https://learn.framevr.io/blog/rpm-closure) · [TechCrunch: Netflix acquires Ready Player Me](https://techcrunch.com/2025/12/19/netflix-acquires-gaming-avatar-maker-ready-player-me/) · [Avatar platformları 2026](https://avatarsdk.com/blog/2026/08/31/avatar-platforms-2026-whos-alive-whos-gone/)
- [YTÜ COSMOS Hugging Face](https://huggingface.co/ytu-ce-cosmos/models) · [TR-MTEB (EMNLP 2025)](https://aclanthology.org/2025.findings-emnlp.471.pdf) · [TR-TEB](https://www.researchgate.net/publication/407438143_TR-TEB_Turkish_Text_Embedding_Benchmark) · [Mecellem (arXiv 2601.16018)](https://arxiv.org/html/2601.16018v1) · [Türkçe konuşma tanıma (arXiv 2611.03605)](https://arxiv.org/abs/2611.03605)
