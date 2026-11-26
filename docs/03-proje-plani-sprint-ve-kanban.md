# Proje Planı: Makro Plan, Sprintler ve Kanban

> Bu belge `plan/backlog.json` dosyasından `scripts/plan_olustur.py` ile üretilir; elle düzenlenmez. Son üretim: 26.11.2026.

**Proje:** KAYNAK-YZ: Türkçe Eğitim İçeriği İçin Kaynağa Dayalı Üretken Yapay Zekâ ile Soru-Cevap ve Rubrik Tabanlı Otomatik Ödev Değerlendirme Platformu

**Kurum notu:** Başvuran kurumun asıl faaliyet alanı eğitimdir. Yapay zekâ, kurumun eğitim hizmetini güçlendirmek amacıyla geliştirilmektedir; ilk kullanıcı kurumun kendisidir.

## 1. Planlama yaklaşımı

- **Makro düzey:** fazlar ve epikler (ürünün işlev alanları ve Ar-Ge iş paketleri).
- **Mikro düzey:** kullanıcı hikâyeleri, Ar-Ge araştırmaları ve görevler; Faz 1 iki haftalık 26 sprinte bölünmüştür.
- **Her öğede:** tarih, sorumlu, öncelik, hikâye puanı, kullanılacak teknolojiler ve kabul kriteri bulunur. Kullanıcı hikâyelerinde ayrıca fonksiyonel gereksinimler yer alır (bkz. `docs/06-urun-gereksinimleri.md`).
- Faz 2 ve Faz 3 makro düzeyde planlanmıştır; sprint planlaması önceki fazın son çeyreğinde yapılacaktır.

## 2. Fazlar

| Faz | Başlangıç | Bitiş | Epik | Öğe |
|---|---|---|---|---|
| Faz 0 · Başvuru ve yerleşme | 23.11.2026 | 31.03.2027 | 1 | 16 |
| Faz 1 · Platform ve kaynağa dayalı eğitim YZ'si | 01.04.2027 | 31.03.2028 | 16 | 85 |
| Faz 2 · Sanal sınıf ve sınıf içi YZ asistanı | 01.04.2028 | 31.03.2029 | 4 | 7 |
| Faz 3 · Uyarlanabilir öğrenme | 01.04.2029 | 31.03.2030 | 1 | 1 |

## 3. Epikler

| Epik | Faz | Tarih aralığı | Hikâye | Araştırma | Görev | Puan | Amaç |
|---|---|---|---|---|---|---|---|
| **EP-00** Teknopark başvurusu ve proje yönetimi | Faz 0 | 24.11.2026 – 20.04.2028 | 0 | 0 | 16 | — | Başvurunun tamamlanması, yerleşme işlemleri ve proje süresince teknopark yükümlülüklerinin yerine getirilmesi. |
| **EP-01** Kimlik doğrulama ve hesap yönetimi | Faz 1 | 01.04.2027 – 18.08.2027 | 7 | 0 | 0 | 39 | Kullanıcıların güvenli biçimde giriş yapması, hesap oluşturması ve rollerine göre yetkilendirilmesi. |
| **EP-02** Kurum ve kullanıcı yönetimi | Faz 1 | 01.04.2027 – 26.05.2027 | 4 | 0 | 0 | 23 | Kurumların ayrı alanlarda yönetilmesi ve kullanıcıların toplu olarak eklenip yönetilmesi. |
| **EP-03** Ders yönetimi | Faz 1 | 29.04.2027 – 23.06.2027 | 4 | 0 | 0 | 16 | Eğitmenlerin ders açması ve öğrencilerin derslere katılıp derslerini tek yerden izlemesi. |
| **EP-04** Ders kaynakları | Faz 1 | 13.05.2027 – 23.06.2027 | 3 | 0 | 0 | 18 | Ders notu, sunum ve kayıtların yüklenmesi, sürümlenmesi ve öğrenciye sunulması. |
| **EP-05** Canlı ders | Faz 1 | 10.06.2027 – 21.07.2027 | 4 | 0 | 0 | 19 | Yurt içinde barındırılan canlı ders altyapısının platforma entegrasyonu. |
| **EP-06** Ödev ve teslim | Faz 1 | 27.05.2027 – 21.07.2027 | 4 | 0 | 0 | 18 | Ödev verilmesi, teslim alınması ve değerlendirilmesi. |
| **EP-07** Takvim ve bildirimler | Faz 1 | 24.06.2027 – 21.07.2027 | 2 | 0 | 0 | 10 | Ders, canlı ders ve ödev tarihlerinin takibi ve hatırlatılması. |
| **EP-08** İçerik işleme ve Türkçe bilgi erişimi (Ar-Ge) | Faz 1 | 27.05.2027 – 01.09.2027 | 1 | 7 | 0 | 47 | AR-2 ve AR-5: ders kaynaklarının aranabilir bilgi tabanına dönüştürülmesi; Recall@5 ≥ %90, ders kaydı WER ≤ %10. |
| **EP-09** YZ ders asistanı (Ar-Ge) | Faz 1 | 08.07.2027 – 15.09.2027 | 5 | 2 | 0 | 46 | AR-1: öğrencinin sorusunu yalnızca ders kaynağından, atıflı yanıtlaması; sadakat ≥ %95, ret ≥ %90. |
| **EP-10** Pedagojik mod (Ar-Ge) | Faz 1 | 22.07.2027 – 13.10.2027 | 1 | 4 | 0 | 32 | AR-4: ödev sorularında yanıt yerine yönlendirme; sızıntı ≤ %2. |
| **EP-11** Rubrik ve YZ destekli ödev değerlendirme (Ar-Ge) | Faz 1 | 05.08.2027 – 22.12.2027 | 4 | 4 | 0 | 66 | AR-3: rubriğe göre kanıtlı ön-değerlendirme; eğitmenle uyum (Kappa) ≥ 0,75. |
| **EP-12** Test setleri ve değerlendirme düzeneği | Faz 1 | 01.04.2027 – 23.06.2027 | 0 | 0 | 6 | — | Ar-Ge hedeflerinin ölçülmesi için Türkçe test setleri ve otomatik ölçüm altyapısı. |
| **EP-13** Bireysel abonelik ve faturalama | Faz 1 | 24.06.2027 – 08.12.2027 | 4 | 0 | 0 | 23 | Bireysel eğitmenlerin kendi kendine kayıt olması, abonelik ve kurum faturalaması. |
| **EP-14** Raporlama ve kalite panosu | Faz 1 | 30.09.2027 – 27.10.2027 | 3 | 0 | 0 | 18 | Kullanım ve YZ kalite metriklerinin kurum ve eğitmene gösterilmesi. |
| **EP-15** Altyapı, güvenlik, KVKK ve yurt içi model (Ar-Ge) | Faz 1 | 01.04.2027 – 22.12.2027 | 0 | 2 | 7 | 21 | AR-6: yurt içi barındırma, güvenlik, KVKK uyumu; yurt içi modelle kalite farkı ≤ %5, p50 ≤ 3 sn. |
| **EP-16** Pilot uygulama ve yaygınlaştırma | Faz 1 | 16.09.2027 – 15.03.2028 | 0 | 0 | 7 | — | Kurumumuzda ve en az bir dış kurumda gerçek ortam doğrulaması; satışa hazırlık. |
| **EP-20** Sanal sınıf altyapısı | Faz 2 | 03.04.2028 – 29.09.2028 | 1 | 1 | 0 | 26 | Tarayıcı tabanlı, kurulum gerektirmeyen, çok kullanıcılı gerçek zamanlı sanal sınıf. |
| **EP-21** Avatar ve mekânsal ses | Faz 2 | 01.05.2028 – 31.10.2028 | 2 | 0 | 0 | 21 | Kişiselleştirilebilir avatarlar, çalışma odaları ve mekânsal ses. |
| **EP-22** Sınıf içi YZ asistanı | Faz 2 | 03.07.2028 – 29.12.2028 | 1 | 0 | 0 | 13 | Faz 1 YZ'sinin sınıf bağlamını anlayan bir asistan olarak sınıfa katılması. |
| **EP-23** Faz 2 pilotu ve Faz 3 başvurusu | Faz 2 | 01.11.2028 – 28.02.2029 | 0 | 0 | 2 | — | Sanal sınıfın pilotu ve proje zincirinin sürdürülmesi. |
| **EP-30** Uyarlanabilir öğrenme | Faz 3 | 02.04.2029 – 27.04.2029 | 0 | 0 | 1 | — | Öğrenci modelleme, kişisel çalışma rotası ve erken uyarı. |

## 4. Kanban görünümü

26.11.2026 itibarıyla:

| Sütun | Öğeler |
|---|---|
| Devam ediyor | G-001, G-002, G-003, G-004, G-006 |
| Önümüzdeki 14 gün | G-005, G-007, G-008 |
| Yapılacak | 101 öğe |

GitHub'da durumlar `durum:` etiketleriyle izlenir: yapılacak → bu sprint → devam ediyor → incelemede → kapalı.

## 5. Hazırlık dönemi (Faz 0)

| Öğe | Başlık | Başlangıç | Bitiş | Sorumlu | Teknolojiler |
|---|---|---|---|---|---|
| G-001 | Yıldız Teknopark ile ön görüşme | 24.11.2026 | 27.11.2026 | Yönetim | Toplantı tutanağı |
| G-002 | Mali müşavir görüşü: şube, kazanç ayrıştırma ve ana sözleşme | 24.11.2026 | 04.12.2026 | Mali Müşavir | Ofis yazılımı |
| G-003 | YTÜ akademik danışmanlarının belirlenmesi ve niyet mektupları | 24.11.2026 | 15.01.2027 | Proje Yöneticisi | Toplantı tutanağı |
| G-004 | Eğitmen ve öğrenci ihtiyaç anketi | 25.11.2026 | 08.12.2026 | Eğitim Koordinatörü | LimeSurvey, pandas |
| G-005 | Kıdemli YZ mühendisinin işe alımı | 30.11.2026 | 29.01.2027 | Yönetim | Ofis yazılımı |
| G-006 | Rakip, literatür, patent ve pazar doğrulaması | 25.11.2026 | 04.12.2026 | Proje Yöneticisi | Web ve kaynak araştırması, TÜRKPATENT, Espacenet, Google Patents |
| G-007 | Kavram kanıtı (küçük ölçekli prototip) | 30.11.2026 | 10.12.2026 | Backend | Python 3.12, Docling, Gömme modeli adayları: bge-m3, turkish-e5-large, pgvector, Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi, Next.js |
| G-008 | Başvuru evrakı, sunum ve proje özetinin tamamlanması | 30.11.2026 | 10.12.2026 | Proje Yöneticisi | Ofis yazılımı, Elektronik imza |
| G-009 | Online aday firma başvurusunun gönderilmesi | 11.12.2026 | 11.12.2026 | Proje Yöneticisi | Web ve kaynak araştırması |
| G-010 | Aday komisyon ve hakem değerlendirme süreçleri | 14.12.2026 | 12.03.2027 | Proje Yöneticisi | Yıldız ARGEPORTAL, Ofis yazılımı |
| G-011 | Kira, şube tescili, faaliyet onayı ve personel işlemleri | 08.03.2027 | 31.03.2027 | Mali Müşavir | Yıldız ARGEPORTAL, Elektronik imza |
| G-014 | Faz 2 proje dosyası ve başvurusu (son tarih 31.01.2028) | 11.11.2027 | 19.01.2028 | Proje Yöneticisi | Ofis yazılımı, Yıldız ARGEPORTAL |
| G-015 | Fikri mülkiyet başvurusu ve YTÜ ile ortak yayın | 25.11.2027 | 01.03.2028 | Proje Yöneticisi | TÜRKPATENT, Espacenet, Google Patents, Ofis yazılımı |
| G-016 | Faz 1 sonuç raporu ve proje bitirme belgesi | 02.03.2028 | 29.03.2028 | Proje Yöneticisi | Ofis yazılımı, Yıldız ARGEPORTAL |

## 6. Faz 1 sprint planı

### Sprint 01 · 01.04–14.04.2027

**Başlayan öğe:** 5 · **Hikâye puanı:** 16 · **Teknolojiler:** Toplantı tutanağı, Web ve kaynak araştırması, GitHub, GitHub Actions, FastAPI, Next.js, PostgreSQL 16, Keycloak, Docker ve Docker Compose, pytest

| Öğe | Tür | Başlık | Epik | Süre | Sorumlu | Öncelik | Puan |
|---|---|---|---|---|---|---|---|
| US-104 | Kullanıcı hikâyesi | Rol tabanlı yetkilendirme | EP-01 | Sprint 01 – Sprint 02 | Backend | Olmazsa olmaz | 8 |
| US-204 | Kullanıcı hikâyesi | Kurumlar arası veri yalıtımı | EP-02 | Sprint 01 – Sprint 02 | Backend | Olmazsa olmaz | 8 |
| G-1201 | Görev | Gereksinim çalıştayı (eğitmen ve öğrencilerle) | EP-12 | Sprint 01 | Proje Yöneticisi | Olmazsa olmaz | — |
| G-1202 | Görev | Güncel literatür raporu | EP-12 | Sprint 01 – Sprint 02 | YZ Mühendisi | Olmazsa olmaz | — |
| G-1501 | Görev | Geliştirme ortamı, kod deposu ve CI/CD | EP-15 | Sprint 01 | DevOps | Olmazsa olmaz | — |

### Sprint 02 · 15.04–28.04.2027

**Başlayan öğe:** 7 · **Hikâye puanı:** 15 · **Teknolojiler:** Label Studio, Python 3.12, Jupyter ve pandas, SciPy ve scikit-learn, FastAPI, Next.js, PostgreSQL 16, Yurt içi S3 uyumlu nesne deposu, Keycloak, Kubernetes, Terraform

| Öğe | Tür | Başlık | Epik | Süre | Sorumlu | Öncelik | Puan |
|---|---|---|---|---|---|---|---|
| US-101 | Kullanıcı hikâyesi | Giriş ekranı: e-posta ve şifreyle giriş | EP-01 | Sprint 02 | Frontend | Olmazsa olmaz | 5 |
| US-102 | Kullanıcı hikâyesi | Davet bağlantısıyla hesap oluşturma | EP-01 | Sprint 02 – Sprint 03 | Backend | Olmazsa olmaz | 5 |
| US-201 | Kullanıcı hikâyesi | Kurum oluşturma ve kurum ayarları | EP-02 | Sprint 02 | Backend | Olmazsa olmaz | 5 |
| G-1203 | Görev | Türkçe soru-cevap test seti | EP-12 | Sprint 02 – Sprint 04 | Eğitim Koordinatörü | Olmazsa olmaz | — |
| G-1204 | Görev | Ödev değerlendirme test seti | EP-12 | Sprint 02 – Sprint 04 | Eğitim Koordinatörü | Olmazsa olmaz | — |
| G-1205 | Görev | Değerlendirme protokolü (akademik danışmanla) | EP-12 | Sprint 02 – Sprint 04 | Akademik Danışman | Olmazsa olmaz | — |
| G-1502 | Görev | Yurt içi barındırma ve Kubernetes ortamları (test ve canlı) | EP-15 | Sprint 02 – Sprint 04 | DevOps | Olmazsa olmaz | — |

### Sprint 03 · 29.04–12.05.2027

**Başlayan öğe:** 3 · **Hikâye puanı:** 13 · **Teknolojiler:** FastAPI, Next.js, PostgreSQL 16, Keycloak

| Öğe | Tür | Başlık | Epik | Süre | Sorumlu | Öncelik | Puan |
|---|---|---|---|---|---|---|---|
| US-103 | Kullanıcı hikâyesi | Şifremi unuttum ve şifre sıfırlama | EP-01 | Sprint 03 | Frontend | Olmazsa olmaz | 3 |
| US-203 | Kullanıcı hikâyesi | Kullanıcı listesi, rol atama ve hesap pasifleştirme | EP-02 | Sprint 03 | Frontend | Olmazsa olmaz | 5 |
| US-301 | Kullanıcı hikâyesi | Ders oluşturma | EP-03 | Sprint 03 | Backend | Olmazsa olmaz | 5 |

### Sprint 04 · 13.05–26.05.2027

**Başlayan öğe:** 4 · **Hikâye puanı:** 16 · **Teknolojiler:** GitHub Actions, FastAPI, Next.js, Redis ve Arq, Yurt içi S3 uyumlu nesne deposu, Langfuse, Değerlendirme düzeneği

| Öğe | Tür | Başlık | Epik | Süre | Sorumlu | Öncelik | Puan |
|---|---|---|---|---|---|---|---|
| US-202 | Kullanıcı hikâyesi | Toplu kullanıcı içe aktarma (CSV) | EP-02 | Sprint 04 | Backend | Olmalı | 5 |
| US-302 | Kullanıcı hikâyesi | Derse davet koduyla katılma | EP-03 | Sprint 04 | Frontend | Olmazsa olmaz | 3 |
| US-401 | Kullanıcı hikâyesi | Ders kaynağı yükleme | EP-04 | Sprint 04 – Sprint 05 | Backend | Olmazsa olmaz | 8 |
| G-1206 | Görev | Otomatik değerlendirme düzeneği ve CI kalite kapısı | EP-12 | Sprint 04 – Sprint 06 | YZ Mühendisi | Olmazsa olmaz | — |

### Sprint 05 · 27.05–09.06.2027

**Başlayan öğe:** 6 · **Hikâye puanı:** 28 · **Teknolojiler:** Python 3.12, FastAPI, Next.js, PostgreSQL 16, Redis ve Arq, Yurt içi S3 uyumlu nesne deposu, Docling, Marker, Tesseract OCR, Langfuse, Prometheus ve Grafana

| Öğe | Tür | Başlık | Epik | Süre | Sorumlu | Öncelik | Puan |
|---|---|---|---|---|---|---|---|
| US-106 | Kullanıcı hikâyesi | Profil ve kişisel veri tercihleri | EP-01 | Sprint 05 | Frontend | Olmazsa olmaz | 5 |
| US-303 | Kullanıcı hikâyesi | Öğrenci panosu | EP-03 | Sprint 05 | Frontend | Olmazsa olmaz | 5 |
| US-402 | Kullanıcı hikâyesi | Kaynak sürümleme ve yayın durumu | EP-04 | Sprint 05 | Backend | Olmazsa olmaz | 5 |
| US-601 | Kullanıcı hikâyesi | Ödev oluşturma | EP-06 | Sprint 05 – Sprint 06 | Backend | Olmazsa olmaz | 5 |
| AR-801 | Ar-Ge araştırması | Belge ayrıştırma ve yapı koruma | EP-08 | Sprint 05 – Sprint 06 | YZ Mühendisi | Olmazsa olmaz | 8 |
| G-1503 | Görev | Gözlemleme ve LLM izleme | EP-15 | Sprint 05 – Sprint 06 | DevOps | Olmazsa olmaz | — |

### Sprint 06 · 10.06–23.06.2027

**Başlayan öğe:** 8 · **Hikâye puanı:** 42 · **Teknolojiler:** SciPy ve scikit-learn, FastAPI, Next.js, PostgreSQL tam metin arama, Zemberek-NLP, Redis ve Arq, Yurt içi S3 uyumlu nesne deposu, python-pptx, Görsel-dil modeli, faster-whisper, vLLM, BigBlueButton, Yurt içi GPU bulutu, pytest

| Öğe | Tür | Başlık | Epik | Süre | Sorumlu | Öncelik | Puan |
|---|---|---|---|---|---|---|---|
| US-304 | Kullanıcı hikâyesi | Ders duyuruları | EP-03 | Sprint 06 | Frontend | Olmalı | 3 |
| US-403 | Kullanıcı hikâyesi | Kaynak görüntüleyici | EP-04 | Sprint 06 | Frontend | Olmazsa olmaz | 5 |
| US-501 | Kullanıcı hikâyesi | Canlı ders planlama ve başlatma | EP-05 | Sprint 06 – Sprint 07 | Backend | Olmazsa olmaz | 8 |
| US-602 | Kullanıcı hikâyesi | Ödev teslimi | EP-06 | Sprint 06 | Frontend | Olmazsa olmaz | 5 |
| AR-802 | Ar-Ge araştırması | Slayt ve görsel içerik işleme | EP-08 | Sprint 06 – Sprint 07 | YZ Mühendisi | Olmalı | 5 |
| AR-803 | Ar-Ge araştırması | Türkçe metin normalizasyonu ve kök bulma | EP-08 | Sprint 06 | YZ Mühendisi | Olmazsa olmaz | 5 |
| AR-804 | Ar-Ge araştırması | Ders kaydı konuşma tanıma | EP-08 | Sprint 06 – Sprint 08 | YZ Mühendisi | Olmazsa olmaz | 8 |
| US-808 | Kullanıcı hikâyesi | Kaynak işleme durumunun izlenmesi | EP-08 | Sprint 06 | Frontend | Olmalı | 3 |

### Sprint 07 · 24.06–07.07.2027

**Başlayan öğe:** 5 · **Hikâye puanı:** 23 · **Teknolojiler:** Python 3.12, Jupyter ve pandas, FastAPI, Next.js, Değerlendirme düzeneği, Keycloak, BigBlueButton

| Öğe | Tür | Başlık | Epik | Süre | Sorumlu | Öncelik | Puan |
|---|---|---|---|---|---|---|---|
| US-502 | Kullanıcı hikâyesi | Canlı derse katılma | EP-05 | Sprint 07 | Frontend | Olmazsa olmaz | 3 |
| US-603 | Kullanıcı hikâyesi | Teslimleri listeleme ve not verme | EP-06 | Sprint 07 | Frontend | Olmazsa olmaz | 5 |
| US-701 | Kullanıcı hikâyesi | Takvim ve dışa aktarma | EP-07 | Sprint 07 | Frontend | Olmalı | 5 |
| AR-805 | Ar-Ge araştırması | Parçalama stratejisi deneyi | EP-08 | Sprint 07 – Sprint 08 | YZ Mühendisi | Olmazsa olmaz | 5 |
| US-1301 | Kullanıcı hikâyesi | Bireysel eğitmen kaydı ve deneme süresi | EP-13 | Sprint 07 | Backend | Olmalı | 5 |

### Sprint 08 · 08.07–21.07.2027

**Başlayan öğe:** 9 · **Hikâye puanı:** 45 · **Teknolojiler:** SciPy ve scikit-learn, FastAPI, Next.js, pgvector, Redis ve Arq, Yurt içi S3 uyumlu nesne deposu, faster-whisper, Gömme modeli adayları: bge-m3, turkish-e5-large, bge-reranker-v2-m3, Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi, vLLM, Langfuse, Değerlendirme düzeneği, BigBlueButton, iyzico, Playwright, axe-core

| Öğe | Tür | Başlık | Epik | Süre | Sorumlu | Öncelik | Puan |
|---|---|---|---|---|---|---|---|
| US-503 | Kullanıcı hikâyesi | Ders kaydının kaynaklara otomatik eklenmesi | EP-05 | Sprint 08 | Backend | Olmazsa olmaz | 5 |
| US-504 | Kullanıcı hikâyesi | Yoklama raporu | EP-05 | Sprint 08 | Backend | Olmalı | 3 |
| US-604 | Kullanıcı hikâyesi | Not ve geri bildirimi görüntüleme | EP-06 | Sprint 08 | Frontend | Olmazsa olmaz | 3 |
| US-702 | Kullanıcı hikâyesi | Bildirimler ve hatırlatmalar | EP-07 | Sprint 08 | Backend | Olmazsa olmaz | 5 |
| AR-806 | Ar-Ge araştırması | Türkçe gömme modeli seçimi | EP-08 | Sprint 08 – Sprint 09 | YZ Mühendisi | Olmazsa olmaz | 5 |
| US-901 | Kullanıcı hikâyesi | Ders asistanına soru sorma ve atıflı yanıt | EP-09 | Sprint 08 – Sprint 09 | YZ Mühendisi | Olmazsa olmaz | 8 |
| AR-903 | Ar-Ge araştırması | Cevaplanabilirlik kapısı ve ceza-duyarlı eşik | EP-09 | Sprint 08 – Sprint 10 | YZ Mühendisi | Olmazsa olmaz | 8 |
| US-1302 | Kullanıcı hikâyesi | Abonelik planı seçimi ve ödeme | EP-13 | Sprint 08 | Backend | Olmalı | 8 |
| G-1509 | Görev | Erişilebilirlik denetimi (WCAG 2.2 AA) | EP-15 | Sprint 08 | Frontend | Olmalı | — |

### Sprint 09 · 22.07–04.08.2027

**Başlayan öğe:** 5 · **Hikâye puanı:** 31 · **Teknolojiler:** SciPy ve scikit-learn, FastAPI, Next.js, pgvector, PostgreSQL tam metin arama, bge-reranker-v2-m3, Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi, Değerlendirme düzeneği, Keycloak, iyzico

| Öğe | Tür | Başlık | Epik | Süre | Sorumlu | Öncelik | Puan |
|---|---|---|---|---|---|---|---|
| US-105 | Kullanıcı hikâyesi | Kurumsal tek oturum açma (SSO) | EP-01 | Sprint 09 | Backend | Olmalı | 8 |
| AR-807 | Ar-Ge araştırması | Hibrit arama ve yeniden sıralama | EP-08 | Sprint 09 – Sprint 11 | YZ Mühendisi | Olmazsa olmaz | 8 |
| US-902 | Kullanıcı hikâyesi | Atıftan kaynağa gitme | EP-09 | Sprint 09 | Frontend | Olmazsa olmaz | 5 |
| AR-1001 | Ar-Ge araştırması | Soru niyeti sınıflandırma | EP-10 | Sprint 09 – Sprint 10 | YZ Mühendisi | Olmazsa olmaz | 5 |
| US-1303 | Kullanıcı hikâyesi | Abonelik ve fatura yönetimi | EP-13 | Sprint 09 | Frontend | Olmalı | 5 |

### Sprint 10 · 05.08–18.08.2027

**Başlayan öğe:** 4 · **Hikâye puanı:** 31 · **Teknolojiler:** FastAPI, Next.js, Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi, Doğal dil çıkarımı modeli / LLM yargıç, Değerlendirme düzeneği, Keycloak

| Öğe | Tür | Başlık | Epik | Süre | Sorumlu | Öncelik | Puan |
|---|---|---|---|---|---|---|---|
| US-107 | Kullanıcı hikâyesi | İki aşamalı doğrulama | EP-01 | Sprint 10 | Backend | Olabilir | 5 |
| AR-904 | Ar-Ge araştırması | İddia düzeyinde yanıt doğrulama | EP-09 | Sprint 10 – Sprint 12 | YZ Mühendisi | Olmazsa olmaz | 13 |
| US-905 | Kullanıcı hikâyesi | Kaynakta olmayan soruya gerekçeli ret | EP-09 | Sprint 10 | Backend | Olmazsa olmaz | 5 |
| US-1101 | Kullanıcı hikâyesi | Rubrik oluşturma | EP-11 | Sprint 10 – Sprint 11 | Frontend | Olmazsa olmaz | 8 |

### Sprint 11 · 19.08–01.09.2027

**Başlayan öğe:** 5 · **Hikâye puanı:** 21 · **Teknolojiler:** Ofis yazılımı, FastAPI, Next.js, Gömme modeli adayları: bge-m3, turkish-e5-large, Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi, vLLM, Langfuse

| Öğe | Tür | Başlık | Epik | Süre | Sorumlu | Öncelik | Puan |
|---|---|---|---|---|---|---|---|
| US-907 | Kullanıcı hikâyesi | Yanıtı değerlendirme | EP-09 | Sprint 11 | Frontend | Olmalı | 2 |
| US-1002 | Kullanıcı hikâyesi | Pedagojik mod seçimi | EP-10 | Sprint 11 | Frontend | Olmazsa olmaz | 3 |
| AR-1003 | Ar-Ge araştırması | Ödev eşleme ve ipucu merdiveni | EP-10 | Sprint 11 – Sprint 12 | YZ Mühendisi | Olmazsa olmaz | 8 |
| AR-1102 | Ar-Ge araştırması | Kriter başına kanıt çıkarımı | EP-11 | Sprint 11 – Sprint 12 | YZ Mühendisi | Olmazsa olmaz | 8 |
| G-1504 | Görev | KVKK uyum paketi | EP-15 | Sprint 11 – Sprint 12 | Proje Yöneticisi | Olmazsa olmaz | — |

### Sprint 12 · 02.09–15.09.2027

**Başlayan öğe:** 5 · **Hikâye puanı:** 39 · **Teknolojiler:** Python 3.12, SciPy ve scikit-learn, FastAPI, Next.js, PostgreSQL 16, Gömme modeli adayları: bge-m3, turkish-e5-large, Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi, vLLM, Hugging Face Transformers ve PEFT/LoRA, Kubernetes, Yurt içi GPU bulutu, pytest

| Öğe | Tür | Başlık | Epik | Süre | Sorumlu | Öncelik | Puan |
|---|---|---|---|---|---|---|---|
| US-906 | Kullanıcı hikâyesi | Cevapsız ve sık sorulan sorular raporu | EP-09 | Sprint 12 | Frontend | Olmalı | 5 |
| AR-1004 | Ar-Ge araştırması | Yanıt sızıntısı tarayıcısı | EP-10 | Sprint 12 – Sprint 13 | YZ Mühendisi | Olmazsa olmaz | 8 |
| AR-1103 | Ar-Ge araştırması | Örneklerle karşılaştırmalı puanlama ve belirsizlik | EP-11 | Sprint 12 – Sprint 14 | YZ Mühendisi | Olmazsa olmaz | 13 |
| G-1505 | Görev | Kişisel veri maskeleme ve anonimleştirme hattı | EP-15 | Sprint 12 – Sprint 13 | Backend | Olmazsa olmaz | — |
| AR-1506 | Ar-Ge araştırması | Yurt içi model servisi ve ince ayar | EP-15 | Sprint 12 – Sprint 16 | YZ Mühendisi | Olmazsa olmaz | 13 |

### Sprint 13 · 16.09–29.09.2027

**Başlayan öğe:** 2 · **Hikâye puanı:** 8 · **Teknolojiler:** Ofis yazılımı, Label Studio, Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi, Değerlendirme düzeneği

| Öğe | Tür | Başlık | Epik | Süre | Sorumlu | Öncelik | Puan |
|---|---|---|---|---|---|---|---|
| AR-1005 | Ar-Ge araştırması | Manipülasyon test seti ve dayanıklılık | EP-10 | Sprint 13 – Sprint 14 | YZ Mühendisi | Olmazsa olmaz | 8 |
| G-1601 | Görev | Pilot planı ve bilgilendirilmiş onam | EP-16 | Sprint 13 | Proje Yöneticisi | Olmazsa olmaz | — |

### Sprint 14 · 30.09–13.10.2027

**Başlayan öğe:** 4 · **Hikâye puanı:** 18 · **Teknolojiler:** Ofis yazılımı, FastAPI, Next.js, PostgreSQL 16, Redis ve Arq, Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi, Langfuse, Prometheus ve Grafana

| Öğe | Tür | Başlık | Epik | Süre | Sorumlu | Öncelik | Puan |
|---|---|---|---|---|---|---|---|
| US-1104 | Kullanıcı hikâyesi | Teslim sonrası YZ ön-değerlendirmesi | EP-11 | Sprint 14 | Backend | Olmazsa olmaz | 5 |
| US-1401 | Kullanıcı hikâyesi | Kurum kullanım panosu | EP-14 | Sprint 14 | Frontend | Olmalı | 5 |
| US-1402 | Kullanıcı hikâyesi | YZ kalite panosu | EP-14 | Sprint 14 – Sprint 15 | Frontend | Olmazsa olmaz | 8 |
| G-1602 | Görev | Eğitmen eğitimi ve kullanım kılavuzu | EP-16 | Sprint 14 – Sprint 15 | Eğitim Koordinatörü | Olmazsa olmaz | — |

### Sprint 15 · 14.10–27.10.2027

**Başlayan öğe:** 3 · **Hikâye puanı:** 26 · **Teknolojiler:** Jupyter ve pandas, SciPy ve scikit-learn, FastAPI, Next.js, PostgreSQL 16

| Öğe | Tür | Başlık | Epik | Süre | Sorumlu | Öncelik | Puan |
|---|---|---|---|---|---|---|---|
| US-1105 | Kullanıcı hikâyesi | Eğitmen onay ekranı | EP-11 | Sprint 15 – Sprint 16 | Frontend | Olmazsa olmaz | 8 |
| AR-1106 | Ar-Ge araştırması | Kalibrasyon, uyum ölçümü ve yanlılık analizi | EP-11 | Sprint 15 – Sprint 17 | YZ Mühendisi | Olmazsa olmaz | 13 |
| US-1403 | Kullanıcı hikâyesi | Eğitmen ders analitiği | EP-14 | Sprint 15 | Frontend | Olmalı | 5 |

### Sprint 16 · 28.10–10.11.2027

**Başlayan öğe:** 4 · **Hikâye puanı:** 11 · **Teknolojiler:** pandas, SciPy ve scikit-learn, Next.js, Redis ve Arq, Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi, Ticari LLM API, vLLM, SGLang, Langfuse, Kubernetes, Prometheus ve Grafana

| Öğe | Tür | Başlık | Epik | Süre | Sorumlu | Öncelik | Puan |
|---|---|---|---|---|---|---|---|
| US-1107 | Kullanıcı hikâyesi | Kanıtlı ve kaynağa atıflı geri bildirim | EP-11 | Sprint 16 | Frontend | Olmazsa olmaz | 3 |
| AR-1507 | Ar-Ge araştırması | Model karşılaştırması, önbellek ve yönlendirme | EP-15 | Sprint 16 – Sprint 18 | DevOps | Olmazsa olmaz | 8 |
| G-1603 | Görev | Pilot 1: kurumumuzda gerçek ortam kullanımı | EP-16 | Sprint 16 – Sprint 19 | Proje Yöneticisi | Olmazsa olmaz | — |
| G-1604 | Görev | Eğitmen süre ölçümü (YZ önerili ve YZ'siz değerlendirme) | EP-16 | Sprint 16 – Sprint 18 | Eğitim Koordinatörü | Olmazsa olmaz | — |

### Sprint 17 · 11.11–24.11.2027

**Başlayan öğe:** 2 · **Hikâye puanı:** 8 · **Teknolojiler:** Ofis yazılımı, Yıldız ARGEPORTAL, SciPy ve scikit-learn, Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi

| Öğe | Tür | Başlık | Epik | Süre | Sorumlu | Öncelik | Puan |
|---|---|---|---|---|---|---|---|
| G-014 | Görev | Faz 2 proje dosyası ve başvurusu (son tarih 31.01.2028) | EP-00 | Sprint 17 – Sprint 21 | Proje Yöneticisi | Olmazsa olmaz | — |
| AR-1108 | Ar-Ge araştırması | YZ ile yazılmış metin tespiti (isteğe bağlı) | EP-11 | Sprint 17 – Sprint 19 | YZ Mühendisi | Olabilir | 8 |

### Sprint 18 · 25.11–08.12.2027

**Başlayan öğe:** 4 · **Hikâye puanı:** 5 · **Teknolojiler:** Ofis yazılımı, TÜRKPATENT, Espacenet, Google Patents, FastAPI, PostgreSQL 16, Keycloak, Kubernetes, Prometheus ve Grafana, k6, OWASP ZAP ve bağımsız sızma testi

| Öğe | Tür | Başlık | Epik | Süre | Sorumlu | Öncelik | Puan |
|---|---|---|---|---|---|---|---|
| G-015 | Görev | Fikri mülkiyet başvurusu ve YTÜ ile ortak yayın | EP-00 | Sprint 18 – Sprint 24 | Proje Yöneticisi | Olmalı | — |
| US-1304 | Kullanıcı hikâyesi | Kurum faturalaması (aktif öğrenci sayısına göre) | EP-13 | Sprint 18 | Backend | Olmalı | 5 |
| G-1508 | Görev | Yük testi ve bağımsız sızma testi | EP-15 | Sprint 18 – Sprint 19 | DevOps | Olmazsa olmaz | — |
| G-1605 | Görev | Dış kurum pilotunun sözleşmesi ve kurulumu | EP-16 | Sprint 18 – Sprint 21 | Yönetim | Olmazsa olmaz | — |

### Sprint 19 · 09.12–22.12.2027

**Başlayan öğe:** 1 · **Hikâye puanı:** 0 · **Teknolojiler:** Ofis yazılımı

| Öğe | Tür | Başlık | Epik | Süre | Sorumlu | Öncelik | Puan |
|---|---|---|---|---|---|---|---|
| G-1607 | Görev | Satış paketi, fiyat listesi ve sözleşme şablonu | EP-16 | Sprint 19 – Sprint 22 | Yönetim | Olmalı | — |

### Sprint 21 · 06.01–19.01.2028

**Başlayan öğe:** 1 · **Hikâye puanı:** 0 · **Teknolojiler:** Jupyter ve pandas, Langfuse, Prometheus ve Grafana

| Öğe | Tür | Başlık | Epik | Süre | Sorumlu | Öncelik | Puan |
|---|---|---|---|---|---|---|---|
| G-1606 | Görev | Pilot 2 izleme ve pilot raporu | EP-16 | Sprint 21 – Sprint 25 | Proje Yöneticisi | Olmazsa olmaz | — |

### Sprint 25 · 02.03–15.03.2028

**Başlayan öğe:** 1 · **Hikâye puanı:** 0 · **Teknolojiler:** Ofis yazılımı, Yıldız ARGEPORTAL

| Öğe | Tür | Başlık | Epik | Süre | Sorumlu | Öncelik | Puan |
|---|---|---|---|---|---|---|---|
| G-016 | Görev | Faz 1 sonuç raporu ve proje bitirme belgesi | EP-00 | Sprint 25 – Sprint 26 | Proje Yöneticisi | Olmazsa olmaz | — |

**Faz 1 boyunca sürekli işler:** G-012 Aylık muafiyet raporları ve teknopark raporlaması; G-013 Çeyreklik ilerleme ve risk gözden geçirmeleri (akademik danışmanlarla).

## 7. Faz 2 ve Faz 3 yol haritası

| Öğe | Tür | Başlık | Epik | Başlangıç | Bitiş | Teknolojiler |
|---|---|---|---|---|---|---|
| US-2001 | Kullanıcı hikâyesi | Kurulumsuz sanal sınıfa katılma | EP-20 | 03.04.2028 | 30.06.2028 | Three.js / React Three Fiber, Colyseus, LiveKit |
| AR-2002 | Ar-Ge araştırması | Gerçek zamanlı durum senkronizasyonu | EP-20 | 01.05.2028 | 29.09.2028 | Colyseus, Yjs, k6 |
| US-2101 | Kullanıcı hikâyesi | Avatar oluşturma | EP-21 | 01.05.2028 | 31.07.2028 | Three.js / React Three Fiber, VRM/GLB açık avatar formatı |
| US-2102 | Kullanıcı hikâyesi | Çalışma odaları ve mekânsal ses | EP-21 | 03.07.2028 | 31.10.2028 | LiveKit, Yjs |
| US-2201 | Kullanıcı hikâyesi | Sınıf içinde YZ asistanına soru sorma | EP-22 | 03.07.2028 | 29.12.2028 | Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi, vLLM, LiveKit, faster-whisper |
| G-2301 | Görev | Sanal sınıf pilotu ve etkileşim analitiği | EP-23 | 01.11.2028 | 28.02.2029 | Prometheus ve Grafana, Langfuse, pandas |
| G-2302 | Görev | Faz 3 başvurusu | EP-23 | 01.11.2028 | 15.01.2029 | Ofis yazılımı, Yıldız ARGEPORTAL |
| G-3001 | Görev | Faz 3 kapsamı: öğrenci modelleme, kişisel çalışma rotası, erken uyarı | EP-30 | 02.04.2029 | 27.04.2029 | Ofis yazılımı |

## 8. Kritik tarihler

| Tarih | Olay | Kural |
|---|---|---|
| 11.12.2026 | Online aday firma başvurusu | Eksik veya hatalı beyan başvurunun yok sayılmasına yol açar |
| ≤ 09.02.2027 | Aday komisyon sonucu | En geç 60 gün; itiraz yolu yok |
| 01.04.2027 | Faz 1 ve Sprint 01 başlangıcı (tahmini) | Faaliyet onay yazısının tarihi esas alınır |
| Her ayın 20'si | Aylık muafiyet raporu | Gecikme aykırı faaliyet sayılır |
| 31.01.2028 | Faz 2 başvurusu son tarihi | Mevcut proje bitmeden en az 60 gün önce |
| 31.03.2028 | Faz 1 bitişi | 90 gün projesiz kalan firma bölgeden çıkarılır |
| 31.12.2028 | 4691 sayılı Kanun teşvik süresi sonu (mevcut mevzuat) | Uzatma kararı izlenmelidir |

## 9. Teknoloji kullanımı

Seçim gerekçeleri: [`04-teknoloji-kararlari.md`](04-teknoloji-kararlari.md).

| Teknoloji | Öğe sayısı | İlk kullanıldığı sprint |
|---|---|---|
| Toplantı tutanağı (Markdown, repoda) | 4 | Sprint 01 |
| Ofis yazılımı (Word / LibreOffice) ve PDF | 14 | Sprint 11 |
| Elektronik imza | 3 | Hazırlık / Faz 2 |
| Yıldız ARGEPORTAL | 6 | Sprint 17 |
| Web ve kaynak araştırması | 3 | Sprint 01 |
| TÜRKPATENT, Espacenet, Google Patents | 2 | Sprint 18 |
| GitHub (issue, milestone, proje panosu) | 3 | Sprint 01 |
| GitHub Actions (sürekli entegrasyon ve dağıtım) | 2 | Sprint 01 |
| LimeSurvey (kendi sunucumuzda anket) | 1 | Hazırlık / Faz 2 |
| Label Studio (kendi sunucumuzda veri etiketleme) | 3 | Sprint 02 |
| Python 3.12 | 6 | Sprint 02 |
| Jupyter ve pandas (analiz ve raporlama) | 4 | Sprint 02 |
| pandas (veri analizi) | 3 | Sprint 16 |
| SciPy ve scikit-learn (istatistik, Kappa, bootstrap, sınıflandırıcı, kalibrasyon) | 9 | Sprint 02 |
| FastAPI (Python arka uç ve REST API) | 34 | Sprint 01 |
| Next.js (React, TypeScript) ön yüz | 38 | Sprint 01 |
| PostgreSQL 16 (satır düzeyi güvenlik ile kurum ayrımı) | 9 | Sprint 01 |
| pgvector (HNSW vektör indeksi) | 3 | Sprint 08 |
| PostgreSQL tam metin arama ('turkish' sözlüğü) | 2 | Sprint 06 |
| Zemberek-NLP (Türkçe biçimbirim çözümleme) | 1 | Sprint 06 |
| Redis ve Arq (iş kuyruğu, önbellek) | 9 | Sprint 04 |
| Yurt içi S3 uyumlu nesne deposu (kurum içi pakette SeaweedFS, Apache-2.0) | 5 | Sprint 02 |
| Docling (PDF/DOCX ayrıştırma, MIT lisansı) | 2 | Sprint 05 |
| Marker (karşılaştırma kolu, GPL-3.0) | 1 | Sprint 05 |
| Tesseract OCR (Türkçe dil paketi) | 1 | Sprint 05 |
| python-pptx (slayt ayrıştırma) | 1 | Sprint 06 |
| Görsel-dil modeli (Qwen2.5-VL / Gemma 3 adayları, deneyle seçilir) | 1 | Sprint 06 |
| faster-whisper (Whisper large-v3; turbo sürüm hız kolu) | 3 | Sprint 06 |
| Gömme modeli adayları: bge-m3, turkish-e5-large (YTÜ COSMOS), multilingual-e5-large, embeddinggemma-300m | 4 | Sprint 08 |
| bge-reranker-v2-m3 (yeniden sıralama) | 2 | Sprint 08 |
| Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi | 16 | Sprint 08 |
| Ticari LLM API (yalnızca karşılaştırma ve anonim veri) | 1 | Sprint 16 |
| vLLM (model servis sunucusu) | 6 | Sprint 06 |
| SGLang (karşılaştırma kolu) | 1 | Sprint 16 |
| Hugging Face Transformers ve PEFT/LoRA (ince ayar) | 1 | Sprint 12 |
| Doğal dil çıkarımı modeli / LLM yargıç (iddia doğrulama) | 1 | Sprint 10 |
| Langfuse (kendi sunucumuzda LLM izleme ve değerlendirme kaydı) | 9 | Sprint 04 |
| Değerlendirme düzeneği (kendi kodumuz + RAGAS metrikleri) | 6 | Sprint 04 |
| Keycloak (OIDC/SAML kimlik yönetimi, kurumsal SSO) | 8 | Sprint 01 |
| BigBlueButton (yurt içi canlı ders) | 4 | Sprint 06 |
| iyzico (abonelik ve ödeme) | 2 | Sprint 08 |
| Docker ve Docker Compose | 1 | Sprint 01 |
| Kubernetes (k3s/RKE2) ve Helm | 4 | Sprint 02 |
| Terraform (altyapı kodu) | 1 | Sprint 02 |
| Yurt içi GPU bulutu (L40S/H100 sınıfı; teklifle seçilir) | 2 | Sprint 06 |
| Prometheus ve Grafana (izleme) | 7 | Sprint 05 |
| pytest (birim ve entegrasyon testi) | 4 | Sprint 01 |
| Playwright (uçtan uca test) | 1 | Sprint 08 |
| k6 (yük testi) | 2 | Sprint 18 |
| OWASP ZAP ve bağımsız sızma testi | 1 | Sprint 18 |
| axe-core (erişilebilirlik denetimi, WCAG 2.2 AA) | 1 | Sprint 08 |
| LiveKit (gerçek zamanlı ses/video altyapısı) | 3 | Hazırlık / Faz 2 |
| Colyseus (oda ve durum senkronizasyonu) | 2 | Hazırlık / Faz 2 |
| Yjs (ortak beyaz tahta, CRDT) | 2 | Hazırlık / Faz 2 |
| Three.js / React Three Fiber (3B sahne) | 2 | Hazırlık / Faz 2 |
| VRM/GLB açık avatar formatı (VRoid Studio, Avatar SDK değerlendirmesi) | 1 | Hazırlık / Faz 2 |

