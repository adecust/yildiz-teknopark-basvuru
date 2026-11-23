# Proje Planı: Makro Plan, Sprintler ve Kanban

> Bu belge `plan/proje-plani.json` dosyasından `scripts/plan_olustur.py` ile üretilir. Elle düzenlenmez; plan dosyası güncellenip betik yeniden çalıştırılır. Son üretim: 23.11.2026.

**Proje:** KAYNAK-YZ: Türkçe Eğitim İçeriği İçin Kaynağa Dayalı Üretken Yapay Zekâ ile Soru-Cevap ve Rubrik Tabanlı Otomatik Ödev Değerlendirme Platformu

**Kurum notu:** Başvuran kurumun asıl faaliyet alanı eğitimdir. Yapay zekâ, kurumun eğitim hizmetini güçlendirmek amacıyla geliştirilmektedir; ilk kullanıcı kurumun kendisidir.

**Planlama yaklaşımı:** Proje üç düzeyde planlanmıştır. Makro düzeyde fazlar ve epikler (iş paketleri), mikro düzeyde iki haftalık sprintlere yerleştirilmiş görevler. Faz 0 ve Faz 1 sprint düzeyinde ayrıntılandırılmıştır. Faz 2 ve Faz 3 makro düzeyde planlanmış olup sprint planlaması bir önceki fazın son çeyreğinde yapılacaktır.

## 1. Makro plan: fazlar

| Faz | Başlangıç | Bitiş | Epik | Görev | Planlama düzeyi |
|---|---|---|---|---|---|
| Faz 0 · Başvuru Hazırlığı | 23.11.2026 | 11.12.2026 | 6 | 32 | Sprint (mikro) |
| Faz 0 · Değerlendirme ve Yerleşme | 14.12.2026 | 31.03.2027 | 2 | 12 | Sprint (mikro) |
| Faz 1 · Platform ve Kaynağa Dayalı Eğitim YZ'si | 01.04.2027 | 31.03.2028 | 9 | 92 | Sprint (mikro) |
| Faz 2 · Sanal Sınıf ve Sınıf İçi YZ Asistanı | 01.04.2028 | 31.03.2029 | 5 | 11 | Makro |
| Faz 3 · Uyarlanabilir Öğrenme | 01.04.2029 | 31.03.2030 | 1 | 1 | Makro |

## 2. Epikler (iş paketleri)

| Epik | Faz | Tarih aralığı | Sprintler | Görev | Amaç |
|---|---|---|---|---|---|
| E01 · Kurumsal hazırlık ve ön görüşmeler | Faz 0 | 24.11.2026 – 11.12.2026 | S01–S01 | 5 | Yıldız Teknopark ile ön görüşme, mali yapı ve ana sözleşme kararlarının verilmesi. |
| E02 · Akademik iş birliği | Faz 0 | 24.11.2026 – 15.01.2027 | S01–S02 | 4 | YTÜ'den iki akademik danışmanın (Bilgisayar Mühendisliği ve Eğitim Fakültesi) belirlenmesi. |
| E03 · Ekip ve kurum verisi | Faz 0 | 24.11.2026 – 29.01.2027 | S01–S02 | 7 | Ar-Ge ekibinin netleştirilmesi; eğitmen ve öğrenci ihtiyacının kurum verisiyle belgelenmesi. |
| E04 · Pazar ve rekabet çalışması | Faz 0 | 25.11.2026 – 11.12.2026 | S01–S01 | 4 | Rakip, literatür, patent ve pazar varsayımlarının doğrulanması. |
| E05 · Kavram kanıtı (prototip) | Faz 0 | 30.11.2026 – 10.12.2026 | S01–S02 | 6 | Başvuru öncesinde küçük ölçekli çalışan bir prototip ve ilk ölçümler (isteğe bağlı, önerilir). |
| E06 · Başvuru dosyası ve gönderim | Faz 0 | 30.11.2026 – 11.12.2026 | S01–S02 | 6 | Online aday firma başvurusunun eksiksiz gönderilmesi. |
| E07 · Değerlendirme süreci | Faz 0 | 14.12.2026 – 12.03.2027 | S02–S07 | 6 | Aday komisyon ve hakem heyeti süreçlerinin başarıyla tamamlanması. |
| E08 · Yerleşme ve resmi işlemler | Faz 0 | 01.03.2027 – 31.03.2027 | S08–S09 | 6 | Kira, şube tescili, faaliyet onayı ve personel işlemlerinin tamamlanması. |
| E10 · İP-0 · Proje yönetimi ve teknopark raporlaması | Faz 1 | 01.04.2027 – 20.04.2028 | S10–S35 | 10 | Projenin planlı yürütülmesi ve teknopark yükümlülüklerinin zamanında yerine getirilmesi. |
| E11 · İP-1 · Gereksinim, literatür ve Türkçe test setleri | Faz 1 | 01.04.2027 – 31.05.2027 | S10–S14 | 9 | Ölçüm altyapısının geliştirmeden önce kurulması. |
| E12 · İP-2 · Platform çekirdeği (test yatağı) | Faz 1 | 01.04.2027 – 30.07.2027 | S10–S17 | 13 | YZ'nin gerçek kullanıcılarla çalışacağı eğitim platformunun kurulması. |
| E13 · İP-3 · İçerik işleme ve Türkçe bilgi erişimi | Faz 1 | 03.05.2027 – 31.08.2027 | S12–S20 | 9 | AR-2 ve AR-5 hedefleri: Recall@5 ≥ %90, ders kaydı WER ≤ %10. |
| E14 · İP-4 · Kaynağa dayalı soru-cevap ve pedagojik sınırlar | Faz 1 | 01.07.2027 – 29.10.2027 | S16–S24 | 12 | AR-1 ve AR-4 hedefleri: sadakat ≥ %95, ret ≥ %90, sızıntı ≤ %2. |
| E15 · İP-5 · Rubrik tabanlı ödev değerlendirme | Faz 1 | 02.08.2027 – 24.12.2027 | S19–S28 | 10 | AR-3 hedefi: eğitmenle uyum (ağırlıklı Kappa) ≥ 0,75. |
| E16 · İP-6 · Ölçeklenebilirlik, KVKK ve yurt içi model | Faz 1 | 01.09.2027 – 24.12.2027 | S21–S28 | 8 | AR-6 hedefi: kalite farkı ≤ %5, yanıt süresi p50 ≤ 3 sn; KVKK uyumu. |
| E17 · İP-7 · Pilot uygulama | Faz 1 | 04.10.2027 – 10.03.2028 | S23–S33 | 10 | Kendi kurumumuzda ve en az bir dış kurumda gerçek ortam doğrulaması. |
| E18 · İP-8 · Fikri mülkiyet, ticarileşme ve Faz 2 başvurusu | Faz 1 | 15.11.2027 – 31.03.2028 | S26–S35 | 11 | Çıktıların korunması, satışa hazırlık ve proje zincirinin kesintisiz sürmesi. |
| E20 · Sanal sınıf altyapısı | Faz 2 | 03.04.2028 – 29.09.2028 | Makro | 3 | Tarayıcı tabanlı, çok kullanıcılı gerçek zamanlı sanal sınıf. |
| E21 · Avatar ve mekânsal ses | Faz 2 | 01.05.2028 – 31.10.2028 | Makro | 2 | Kişiselleştirilebilir avatarlar, mekânsal ses ve çalışma odaları. |
| E22 · Sınıf içi YZ asistanı | Faz 2 | 03.07.2028 – 29.12.2028 | Makro | 2 | Faz 1 YZ'sinin sınıf bağlamını anlayan bir asistan olarak sınıfa katılması. |
| E23 · Etkileşim analitiği | Faz 2 | 04.09.2028 – 31.01.2029 | Makro | 1 | Kişisel veri işlemeden grup düzeyinde katılım ölçümü. |
| E24 · Faz 2 pilot, ticarileşme ve Faz 3 başvurusu | Faz 2 | 01.11.2028 – 30.03.2029 | Makro | 3 | Sanal sınıfın pilotu ve proje zincirinin sürdürülmesi. |
| E30 · Uyarlanabilir öğrenme ve öğrenci modelleme | Faz 3 | 02.04.2029 – 27.04.2029 | Makro | 1 | Öğrencinin bilmediği kavramın tahmini, kişisel çalışma rotası ve erken uyarı. |

## 3. Kanban görünümü

Görevlerin 23.11.2026 tarihine göre durumu. GitHub'da aynı durumlar `durum:` etiketleriyle izlenir.

| Sütun | Görevler |
|---|---|
| Tamamlandı | Araştırma raporu, faz yapısı ve kabul analizi, proje dosyası, sunum ve özet belgesi |
| Devam ediyor | — |
| Bu sprint (Sprint 01 · 23.11.2026–06.12.2026) | 0101, 0102, 0103, 0104, 0105, 0201, 0202, 0203, 0301, 0302, 0303, 0305, 0306, 0401, 0402, 0403, 0404, 0501, 0502, 0503, 0601, 0602 |
| Sonraki sprint (Sprint 02 · 07.12.2026–20.12.2026) | 0204, 0304, 0307, 0504, 0505, 0506, 0603, 0604, 0605, 0606, 0701, 0702 |
| Yapılacak (sonraki sprintler ve makro fazlar) | 114 görev |

## 4. Sprint planı (mikro düzey)

### Sprint 01 · 23.11.2026–06.12.2026

**Başlayan görev:** 22 · **Kullanılacak teknolojiler:** Toplantı tutanağı (Markdown, repoda); Ofis yazılımı (Word / LibreOffice) ve PDF; Elektronik imza; Web ve kaynak araştırması; TÜRKPATENT, Espacenet, Google Patents; GitHub (issue, milestone, proje panosu); LimeSurvey (kendi sunucumuzda anket); Label Studio (kendi sunucumuzda veri etiketleme); Python 3.12; pandas (veri analizi); PostgreSQL 16 (satır düzeyi güvenlik ile kurum ayrımı); pgvector (HNSW vektör indeksi); PostgreSQL tam metin arama ('turkish' sözlüğü); MinIO / yurt içi S3 uyumlu nesne deposu; Docling (PDF/DOCX ayrıştırma, MIT lisansı); Gömme modeli adayları: bge-m3, turkish-e5-large (YTÜ COSMOS), multilingual-e5-large, embeddinggemma-300m

| Görev | Epik | Başlangıç | Bitiş | Sorumlu | Teknolojiler | Kabul kriteri |
|---|---|---|---|---|---|---|
| **0101** Yıldız Teknopark ile ön görüşme randevusunun alınması | E01 | 24.11.2026 | 25.11.2026 | Yönetim | Toplantı tutanağı | Kurumsal Kiralama birimiyle görüşme tarihi kesinleşti. |
| **0102** Ön görüşmede teyit sorularının sorulması ve tutanak | E01 | 26.11.2026 | 27.11.2026 | Yönetim | Toplantı tutanağı, GitHub | Başvuru ücreti, m² bedeli, boş alan, hakem sunumu, destekli proje muafiyeti, proje süresi, şube yaklaşımı ve takvim soruları yanıtlandı; tutanak repoya eklendi. |
| **0103** Mali müşavir görüşü: şube, kazanç ayrıştırma ve KDV istisnası | E01 | 24.11.2026 | 02.12.2026 | Mali Müşavir | Toplantı tutanağı | Eğitim hizmeti geliri ile teknoparktaki Ar-Ge kazancının nasıl ayrıştırılacağına dair yazılı görüş alındı. |
| **0104** Ana sözleşme amaç ve konu maddesinin kontrolü | E01 | 24.11.2026 | 27.11.2026 | Mali Müşavir | Ofis yazılımı | Ana sözleşmede yazılım geliştirme ve Ar-Ge faaliyetinin bulunup bulunmadığı tespit edildi. |
| **0105** Ana sözleşme tadil kararı ve genel kurul hazırlığı (gerekirse) | E01 | 30.11.2026 | 11.12.2026 | Mali Müşavir | Ofis yazılımı | Tadil gerekiyorsa karar alındı ve tescil süreci başlatıldı; gerekmiyorsa bu durum kayda geçirildi. |
| **0201** Yıldız TTO'ya akademik danışman eşleştirme talebi | E02 | 24.11.2026 | 27.11.2026 | Proje Yöneticisi | Toplantı tutanağı | Bilgisayar Mühendisliği (Türkçe dil modelleri) ve Eğitim Fakültesi (ölçme-değerlendirme) için yazılı talep iletildi. |
| **0202** YTÜ COSMOS araştırma grubuyla tanışma talebi | E02 | 24.11.2026 | 27.11.2026 | Proje Yöneticisi | Toplantı tutanağı | TTO aracılığıyla Türkçe dil modeli çalışmaları yürüten grupla görüşme talebi iletildi. |
| **0203** Akademisyen görüşmeleri | E02 | 30.11.2026 | 09.12.2026 | Proje Yöneticisi | Toplantı tutanağı | En az bir, hedef olarak iki öğretim üyesiyle proje görüşmesi yapıldı. |
| **0301** Yazılım ekibi envanteri | E03 | 24.11.2026 | 02.12.2026 | Proje Yöneticisi | Ofis yazılımı | Her çalışan için diploma, unvan, deneyim ve olası proje rolü tablosu hazırlandı. |
| **0302** Ar-Ge, destek ve kapsam dışı personel sınıflandırması | E03 | 30.11.2026 | 02.12.2026 | Proje Yöneticisi | Ofis yazılımı | Teknoparkta çalışacak 7 kişinin statüsü belirlendi; oran sınırları kontrol edildi. |
| **0303** Kıdemli YZ mühendisi iş ilanının yayımlanması | E03 | 30.11.2026 | 04.12.2026 | Yönetim | Ofis yazılımı | İlan yayımlandı; değerlendirme ölçütleri belirlendi. |
| **0305** Eğitmen anketi (iş yükü ve ödev okuma süresi) | E03 | 25.11.2026 | 04.12.2026 | Eğitim Koordinatörü | LimeSurvey | Tüm eğitmenlerden yanıt toplandı. |
| **0306** Öğrenci anketi (ders sonrası destek ihtiyacı) | E03 | 25.11.2026 | 04.12.2026 | Eğitim Koordinatörü | LimeSurvey | Son üç ayın öğrencilerinden yanıt toplandı. |
| **0401** Rakip ürün incelemesi ve karşılaştırma tablosunun güncellenmesi | E04 | 25.11.2026 | 02.12.2026 | Proje Yöneticisi | Web ve kaynak araştırması | Karşılaştırma tablosu güncel ürün özellikleriyle doğrulandı. |
| **0402** Literatür ve patent ön taraması | E04 | 25.11.2026 | 04.12.2026 | Proje Yöneticisi | TÜRKPATENT, Espacenet, Google Patents | TÜRKPATENT ve uluslararası patent veri tabanlarında tarama özeti hazırlandı. |
| **0403** Pazar büyüklüğü ve fiyat varsayımlarının doğrulanması | E04 | 30.11.2026 | 04.12.2026 | Yönetim | pandas | Fiyat önerisi en az beş kurumla yapılan kısa görüşmeyle sınandı. |
| **0404** İlk üç hedef dış kurumun belirlenmesi ve ön temas | E04 | 30.11.2026 | 11.12.2026 | Yönetim | Toplantı tutanağı | Üç kurumla ön görüşme yapıldı; mümkünse niyet mektubu alındı. |
| **0501** Örnek ders seçimi ve kaynakların toplanması | E05 | 30.11.2026 | 01.12.2026 | Eğitim Koordinatörü | MinIO / yurt içi S3 uyumlu nesne deposu | Bir dersin iki PDF kaynağı ve bir ders kaydı toplandı. |
| **0502** 60 soruluk mini test setinin hazırlanması | E05 | 30.11.2026 | 02.12.2026 | Eğitim Koordinatörü | Label Studio | 45 cevaplanabilir ve 15 kaynak dışı soru, doğru kaynak bilgisiyle etiketlendi. |
| **0503** Erişim hattının kurulması ve iki gömme modelinin karşılaştırılması | E05 | 02.12.2026 | 04.12.2026 | Backend | Python 3.12, Docling, Gömme modeli adayları: bge-m3, turkish-e5-large, PostgreSQL 16, pgvector, PostgreSQL tam metin arama | Recall@5 değeri iki model için ölçüldü. |
| **0601** Zorunlu evrakların metni seçilebilir PDF olarak hazırlanması | E06 | 30.11.2026 | 09.12.2026 | Mali Müşavir | Ofis yazılımı, Elektronik imza | Vergi levhası, TTSG, son üç yıl gelir tablosu ve bilanço, vergi dairesi ve SGK borç yoktur yazıları hazır. |
| **0602** Başvuru formu metinlerinin son hâli | E06 | 02.12.2026 | 07.12.2026 | Proje Yöneticisi | Ofis yazılımı | Formun tüm alanları dolduruldu; özet en az 1200 karakter. |

### Sprint 02 · 07.12.2026–20.12.2026

**Başlayan görev:** 12 · **Kullanılacak teknolojiler:** Toplantı tutanağı (Markdown, repoda); Ofis yazılımı (Word / LibreOffice) ve PDF; Web ve kaynak araştırması; pandas (veri analizi); SciPy ve scikit-learn (istatistik, Kappa, bootstrap, sınıflandırıcı, kalibrasyon); FastAPI (Python arka uç ve REST API); Next.js (React, TypeScript) ön yüz; Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi; Ticari LLM API (yalnızca karşılaştırma ve anonim veri); vLLM (model servis sunucusu)

| Görev | Epik | Başlangıç | Bitiş | Sorumlu | Teknolojiler | Kabul kriteri |
|---|---|---|---|---|---|---|
| **0204** Akademik danışmanlık niyet mektuplarının alınması | E02 | 07.12.2026 | 15.01.2027 | Proje Yöneticisi | Ofis yazılımı | Niyet mektupları detaylı proje dosyasına eklendi. |
| **0304** Kıdemli YZ mühendisi mülakat ve teklif süreci | E03 | 07.12.2026 | 29.01.2027 | Yönetim | Ofis yazılımı | Aday seçildi ve teklif kabul edildi; özgeçmiş proje dosyasına eklendi. |
| **0307** Anket sonuçlarının analizi ve sunuma aktarılması | E03 | 07.12.2026 | 08.12.2026 | Proje Yöneticisi | pandas | Sorun tanımı slaytındaki değerler kurum verisiyle dolduruldu. |
| **0504** Atıflı cevap üretimi ve basit reddetme eşiği | E05 | 07.12.2026 | 08.12.2026 | Backend | Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi, Ticari LLM API, vLLM | 60 soruda sadakat ve reddetme doğruluğu elle ölçüldü. |
| **0505** 20 ödevlik rubrik puanlama denemesi | E05 | 07.12.2026 | 09.12.2026 | Backend | Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi, Ticari LLM API, SciPy ve scikit-learn | Eğitmen puanıyla ağırlıklı Kappa değeri hesaplandı. |
| **0506** Demo arayüzü, ekran görüntüleri ve demo videosu | E05 | 09.12.2026 | 10.12.2026 | Frontend | Next.js, FastAPI | Sunuma eklenecek ekran görüntüleri ve iki dakikalık video hazır. |
| **0603** Sunumun kurum bilgileri ve anket verileriyle tamamlanması | E06 | 07.12.2026 | 09.12.2026 | Proje Yöneticisi | Ofis yazılımı | Sunumdaki tüm doldurulacak alanlar tamamlandı ve PDF'e çevrildi. |
| **0604** Proje özeti belgesinin son hâli | E06 | 07.12.2026 | 09.12.2026 | Proje Yöneticisi | Ofis yazılımı | Özet belgesindeki tüm doldurulacak alanlar tamamlandı. |
| **0605** İç hakem simülasyonu ve düzeltmeler | E06 | 09.12.2026 | 10.12.2026 | Yönetim | Ofis yazılımı | Dosya hakem ölçütlerine göre puanlandı; zayıf kalan bölümler düzeltildi. |
| **0606** Online aday firma başvurusunun gönderilmesi | E06 | 11.12.2026 | 11.12.2026 | Proje Yöneticisi | Web ve kaynak araştırması | Başvuru gönderildi ve teyit kaydı alındı. |
| **0701** Aday Girişimci Değerlendirme Komisyonu sürecinin takibi | E07 | 14.12.2026 | 15.01.2027 | Proje Yöneticisi | Toplantı tutanağı | Komisyon sonucu alındı (yönergeye göre en geç 60 gün). |
| **0702** Detaylı proje dosyasının hakem formatına getirilmesi | E07 | 14.12.2026 | 15.01.2027 | Proje Yöneticisi | Ofis yazılımı | Araştırma soruları, deney planı, iş paketleri ve ekip bilgisi hakem formatında hazır. |

### Sprint 05 · 18.01.2027–31.01.2027

**Başlayan görev:** 1 · **Kullanılacak teknolojiler:** Elektronik imza; Yıldız ARGEPORTAL

| Görev | Epik | Başlangıç | Bitiş | Sorumlu | Teknolojiler | Kabul kriteri |
|---|---|---|---|---|---|---|
| **0703** ARGEPORTAL kaydı, dosya yüklemesi ve başvuru ücreti | E07 | 18.01.2027 | 29.01.2027 | Proje Yöneticisi | Yıldız ARGEPORTAL, Elektronik imza | Proje dosyası sisteme yüklendi; ücret dekontu iletildi. |

### Sprint 06 · 01.02.2027–14.02.2027

**Başlayan görev:** 2 · **Kullanılacak teknolojiler:** Ofis yazılımı (Word / LibreOffice) ve PDF

| Görev | Epik | Başlangıç | Bitiş | Sorumlu | Teknolojiler | Kabul kriteri |
|---|---|---|---|---|---|---|
| **0704** Hakem sunumu ve soru-cevap provası | E07 | 01.02.2027 | 12.02.2027 | Yönetim | Ofis yazılımı | Olası hakem soruları üzerinden en az iki prova yapıldı. |
| **0706** TÜBİTAK 1507 / 1501 uygunluk değerlendirmesi | E07 | 01.02.2027 | 26.02.2027 | Mali Müşavir | Ofis yazılımı | Kurumun uygunluğu ve başvuru takvimi netleşti. |

### Sprint 07 · 15.02.2027–28.02.2027

**Başlayan görev:** 1 · **Kullanılacak teknolojiler:** Yıldız ARGEPORTAL

| Görev | Epik | Başlangıç | Bitiş | Sorumlu | Teknolojiler | Kabul kriteri |
|---|---|---|---|---|---|---|
| **0705** Hakem süreci takibi ve ek bilgi taleplerinin yanıtlanması | E07 | 15.02.2027 | 12.03.2027 | Proje Yöneticisi | Yıldız ARGEPORTAL | Hakem heyeti kararı alındı. |

### Sprint 08 · 01.03.2027–14.03.2027

**Başlayan görev:** 2 · **Kullanılacak teknolojiler:** Elektronik imza; Yıldız ARGEPORTAL

| Görev | Epik | Başlangıç | Bitiş | Sorumlu | Teknolojiler | Kabul kriteri |
|---|---|---|---|---|---|---|
| **0801** Kira müzakeresi, sözleşme ve güvence bedeli | E08 | 08.03.2027 | 19.03.2027 | Yönetim | Elektronik imza | Kira sözleşmesi imzalandı; alan teslim alındı. |
| **0806** Akademisyen görevlendirme yazılarının onayı | E08 | 01.03.2027 | 31.03.2027 | Proje Yöneticisi | Yıldız ARGEPORTAL | Üniversite görevlendirme yazıları alındı ve yönetici şirket tarafından onaylandı. |

### Sprint 09 · 15.03.2027–28.03.2027

**Başlayan görev:** 4 · **Kullanılacak teknolojiler:** Elektronik imza; Yıldız ARGEPORTAL; GitHub (issue, milestone, proje panosu); Docker ve Docker Compose

| Görev | Epik | Başlangıç | Bitiş | Sorumlu | Teknolojiler | Kabul kriteri |
|---|---|---|---|---|---|---|
| **0802** Teknopark şubesinin tescili ve vergi dairesi kaydı | E08 | 15.03.2027 | 26.03.2027 | Mali Müşavir | Elektronik imza | Şube tescil edildi. |
| **0803** Faaliyet onay yazısı ve vergi dairesi / SGK bildirimleri | E08 | 22.03.2027 | 31.03.2027 | Mali Müşavir | Yıldız ARGEPORTAL, Elektronik imza | Faaliyet onay yazısı alındı ve ilgili kurumlara ibraz edildi. |
| **0804** Personel onayları ve giriş kartları | E08 | 22.03.2027 | 31.03.2027 | Proje Yöneticisi | Yıldız ARGEPORTAL | Tüm Ar-Ge personeli sistemde onaylı; giriş kartları aktif. |
| **0805** Ofis kurulumu ve geliştirme ortamı | E08 | 22.03.2027 | 31.03.2027 | DevOps | Docker ve Docker Compose, GitHub | Ofis ve geliştirme ortamı kullanıma hazır. |

### Sprint 10 · 29.03.2027–11.04.2027

**Başlayan görev:** 7 · **Kullanılacak teknolojiler:** Toplantı tutanağı (Markdown, repoda); Web ve kaynak araştırması; GitHub (issue, milestone, proje panosu); GitHub Actions (sürekli entegrasyon ve dağıtım); Mermaid (mimari ve akış diyagramları); FastAPI (Python arka uç ve REST API); Next.js (React, TypeScript) ön yüz; PostgreSQL 16 (satır düzeyi güvenlik ile kurum ayrımı); Docker ve Docker Compose; pytest (birim ve entegrasyon testi)

| Görev | Epik | Başlangıç | Bitiş | Sorumlu | Teknolojiler | Kabul kriteri |
|---|---|---|---|---|---|---|
| **1001** Proje başlangıç toplantısı ve rol dağılımı | E10 | 01.04.2027 | 02.04.2027 | Proje Yöneticisi | GitHub, Toplantı tutanağı | Roller, iletişim düzeni ve karar mekanizması yazılı olarak belirlendi. |
| **1002** Sprint düzeninin ve iş takibinin kurulması | E10 | 01.04.2027 | 09.04.2027 | Proje Yöneticisi | GitHub, GitHub Actions | İki haftalık sprint takvimi, toplantı düzeni ve iş takibi kuralları yürürlükte. |
| **1101** Gereksinim çalıştayı (eğitmenler ve öğrencilerle) | E11 | 01.04.2027 | 09.04.2027 | Proje Yöneticisi | Toplantı tutanağı | Eğitmen ve öğrenci ihtiyaçları önceliklendirilmiş liste hâlinde yazıldı. |
| **1102** Gereksinim ve sistem mimarisi dokümanı | E11 | 05.04.2027 | 16.04.2027 | YZ Mühendisi | Mermaid, GitHub | Onaylı gereksinim listesi ve mimari diyagram. |
| **1103** Güncel literatür (SOTA) raporu | E11 | 01.04.2027 | 23.04.2027 | YZ Mühendisi | Web ve kaynak araştırması | Seçilecek yöntemlerin gerekçeleri yazıldı. |
| **1201** Teknoloji yığını kurulumu, kod deposu ve sürekli entegrasyon | E12 | 01.04.2027 | 09.04.2027 | Backend | FastAPI, Next.js, PostgreSQL 16, Docker ve Docker Compose, GitHub Actions | Geliştirme, test ve canlı ortam iskeleti çalışıyor. |
| **1202** Veri modeli ve kurumlar arası veri ayrımı | E12 | 05.04.2027 | 23.04.2027 | Backend | PostgreSQL 16, FastAPI, pytest | Bir kurumun verisinin başka kurumdan görülemediği testlerle doğrulandı. |

### Sprint 11 · 12.04.2027–25.04.2027

**Başlayan görev:** 5 · **Kullanılacak teknolojiler:** Label Studio (kendi sunucumuzda veri etiketleme); Python 3.12; Jupyter ve pandas (analiz ve raporlama); SciPy ve scikit-learn (istatistik, Kappa, bootstrap, sınıflandırıcı, kalibrasyon); FastAPI (Python arka uç ve REST API); Next.js (React, TypeScript) ön yüz; PostgreSQL 16 (satır düzeyi güvenlik ile kurum ayrımı); Keycloak (OIDC/SAML kimlik yönetimi, kurumsal SSO)

| Görev | Epik | Başlangıç | Bitiş | Sorumlu | Teknolojiler | Kabul kriteri |
|---|---|---|---|---|---|---|
| **1104** Soru-cevap test seti: ders seçimi ve soru toplama | E11 | 12.04.2027 | 30.04.2027 | Eğitim Koordinatörü | Label Studio | En az beş dersten en az 500 soru toplandı; en az 150'si kaynak dışı. |
| **1106** Ödev veri seti: açık rıza ve anonimleştirme | E11 | 12.04.2027 | 30.04.2027 | Eğitim Koordinatörü | Python 3.12, Label Studio | En az 300 ödev için rıza alındı ve kişisel bilgiler çıkarıldı. |
| **1108** Değerlendirme protokolü (akademik danışmanla) | E11 | 19.04.2027 | 07.05.2027 | Akademik Danışman | SciPy ve scikit-learn, Jupyter ve pandas | Tüm metriklerin ölçüm yöntemi ve istatistiksel analiz planı yazıldı. |
| **1203** Kimlik doğrulama ve rol yönetimi | E12 | 12.04.2027 | 30.04.2027 | Backend | Keycloak, FastAPI, Next.js | Öğrenci, eğitmen, kurum yöneticisi ve bireysel eğitmen rolleri çalışıyor. |
| **1204** Ders alanı, kayıt ve davet akışı | E12 | 19.04.2027 | 14.05.2027 | Backend | FastAPI, Next.js, PostgreSQL 16 | Eğitmen ders açabiliyor; öğrenci davet bağlantısı veya kodla katılabiliyor. |

### Sprint 12 · 26.04.2027–09.05.2027

**Başlayan görev:** 5 · **Kullanılacak teknolojiler:** Elektronik imza; Yıldız ARGEPORTAL; Label Studio (kendi sunucumuzda veri etiketleme); Python 3.12; SciPy ve scikit-learn (istatistik, Kappa, bootstrap, sınıflandırıcı, kalibrasyon); FastAPI (Python arka uç ve REST API); Redis ve Arq (iş kuyruğu, önbellek); MinIO / yurt içi S3 uyumlu nesne deposu; Docling (PDF/DOCX ayrıştırma, MIT lisansı); Marker (karşılaştırma kolu, GPL-3.0); Tesseract OCR (Türkçe dil paketi)

| Görev | Epik | Başlangıç | Bitiş | Sorumlu | Teknolojiler | Kabul kriteri |
|---|---|---|---|---|---|---|
| **1003** Aylık muafiyet raporları: Nisan, Mayıs, Haziran 2027 | E10 | 01.05.2027 | 20.07.2027 | Proje Yöneticisi | Yıldız ARGEPORTAL, Elektronik imza | Üç rapor her ayın 20'sine kadar e-imzayla sunuldu. |
| **1105** Soru-cevap test seti: etiketleme ve etiketleyici uyumu | E11 | 03.05.2027 | 21.05.2027 | Eğitim Koordinatörü | Label Studio, SciPy ve scikit-learn | Her soru iki kişi tarafından etiketlendi; uyum oranı raporlandı. |
| **1107** Ödev veri seti: rubrik hazırlığı ve eğitmen puanlaması | E11 | 03.05.2027 | 28.05.2027 | Eğitim Koordinatörü | Label Studio | Ödevler rubriğe göre puanlandı; en az %20'si iki eğitmen tarafından. |
| **1205** Ders kaynağı yükleme ve depolama | E12 | 03.05.2027 | 28.05.2027 | Backend | FastAPI, MinIO / yurt içi S3 uyumlu nesne deposu, Redis ve Arq | PDF, slayt, görsel ve video yüklenip sürümlenebiliyor. |
| **1301** Belge ayrıştırma (PDF ve DOCX) | E13 | 03.05.2027 | 21.05.2027 | YZ Mühendisi | Docling, Marker, Tesseract OCR, Python 3.12 | Başlık, paragraf, tablo ve sayfa bilgisi korunarak metin çıkarılıyor. |

### Sprint 13 · 10.05.2027–23.05.2027

**Başlayan görev:** 4 · **Kullanılacak teknolojiler:** SciPy ve scikit-learn (istatistik, Kappa, bootstrap, sınıflandırıcı, kalibrasyon); FastAPI (Python arka uç ve REST API); Next.js (React, TypeScript) ön yüz; PostgreSQL tam metin arama ('turkish' sözlüğü); Zemberek-NLP (Türkçe biçimbirim çözümleme); MinIO / yurt içi S3 uyumlu nesne deposu; python-pptx (slayt ayrıştırma); Görsel-dil modeli (Qwen2.5-VL / Gemma 3 adayları, deneyle seçilir); faster-whisper (Whisper large-v3; turbo sürüm hız kolu); vLLM (model servis sunucusu); Yurt içi GPU bulutu (L40S/H100 sınıfı; teklifle seçilir); pytest (birim ve entegrasyon testi)

| Görev | Epik | Başlangıç | Bitiş | Sorumlu | Teknolojiler | Kabul kriteri |
|---|---|---|---|---|---|---|
| **1206** Ödev oluşturma ve teslim modülü | E12 | 17.05.2027 | 11.06.2027 | Backend | FastAPI, Next.js, MinIO / yurt içi S3 uyumlu nesne deposu | Teslim tarihi, geç teslim ve dosya yükleme çalışıyor. |
| **1302** Slayt ve görsel içerik işleme | E13 | 17.05.2027 | 04.06.2027 | YZ Mühendisi | python-pptx, Görsel-dil modeli, vLLM | Slayt metni, konuşmacı notu ve görsel açıklaması tek parçada birleşiyor. |
| **1303** Türkçe metin normalizasyonu ve kök bulma | E13 | 17.05.2027 | 28.05.2027 | YZ Mühendisi | Zemberek-NLP, PostgreSQL tam metin arama, pytest | Türkçe büyük-küçük harf ve şapkalı harf dönüşümleri testlerle doğrulandı. |
| **1304** Ders kaydı konuşma tanıma hattı ve hata oranı ölçümü | E13 | 17.05.2027 | 18.06.2027 | YZ Mühendisi | faster-whisper, Yurt içi GPU bulutu, SciPy ve scikit-learn | Kelime hata oranı en az beş saatlik kayıtta ölçüldü (hedef ≤ %10). |

### Sprint 14 · 24.05.2027–06.06.2027

**Başlayan görev:** 3 · **Kullanılacak teknolojiler:** GitHub (issue, milestone, proje panosu); Python 3.12; Jupyter ve pandas (analiz ve raporlama); FastAPI (Python arka uç ve REST API); Next.js (React, TypeScript) ön yüz; Redis ve Arq (iş kuyruğu, önbellek); Değerlendirme düzeneği (kendi kodumuz + RAGAS metrikleri)

| Görev | Epik | Başlangıç | Bitiş | Sorumlu | Teknolojiler | Kabul kriteri |
|---|---|---|---|---|---|---|
| **1109** Kilometre taşı 1 kontrolü: test setleri hazır | E11 | 31.05.2027 | 31.05.2027 | Proje Yöneticisi | GitHub | Test setleri kilitlendi; devam kararı kayda geçirildi. |
| **1207** Takvim, duyuru ve bildirimler | E12 | 31.05.2027 | 25.06.2027 | Frontend | Next.js, FastAPI, Redis ve Arq | Ders ve ödev takvimi görüntüleniyor; e-posta ve uygulama içi bildirim gidiyor. |
| **1305** Parçalama stratejileri deneyi | E13 | 31.05.2027 | 18.06.2027 | YZ Mühendisi | Python 3.12, Değerlendirme düzeneği, Jupyter ve pandas | En az üç parçalama yöntemi test setinde karşılaştırıldı. |

### Sprint 15 · 07.06.2027–20.06.2027

**Başlayan görev:** 2 · **Kullanılacak teknolojiler:** FastAPI (Python arka uç ve REST API); pgvector (HNSW vektör indeksi); Gömme modeli adayları: bge-m3, turkish-e5-large (YTÜ COSMOS), multilingual-e5-large, embeddinggemma-300m; Değerlendirme düzeneği (kendi kodumuz + RAGAS metrikleri); BigBlueButton (yurt içi canlı ders)

| Görev | Epik | Başlangıç | Bitiş | Sorumlu | Teknolojiler | Kabul kriteri |
|---|---|---|---|---|---|---|
| **1208** Canlı ders entegrasyonu (yurt içi BigBlueButton) | E12 | 07.06.2027 | 25.06.2027 | Backend | BigBlueButton, FastAPI | Platform içinden canlı ders başlatılıp katılınabiliyor. |
| **1306** Türkçe gömme modeli karşılaştırması | E13 | 07.06.2027 | 02.07.2027 | YZ Mühendisi | Gömme modeli adayları: bge-m3, turkish-e5-large, pgvector, Değerlendirme düzeneği | En az dört model karşılaştırıldı; seçim gerekçesiyle kaydedildi. |

### Sprint 16 · 21.06.2027–04.07.2027

**Başlayan görev:** 5 · **Kullanılacak teknolojiler:** Toplantı tutanağı (Markdown, repoda); GitHub (issue, milestone, proje panosu); FastAPI (Python arka uç ve REST API); Next.js (React, TypeScript) ön yüz; pgvector (HNSW vektör indeksi); PostgreSQL tam metin arama ('turkish' sözlüğü); Zemberek-NLP (Türkçe biçimbirim çözümleme); Redis ve Arq (iş kuyruğu, önbellek); MinIO / yurt içi S3 uyumlu nesne deposu; Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi; vLLM (model servis sunucusu); Langfuse (kendi sunucumuzda LLM izleme ve değerlendirme kaydı); Keycloak (OIDC/SAML kimlik yönetimi, kurumsal SSO); BigBlueButton (yurt içi canlı ders)

| Görev | Epik | Başlangıç | Bitiş | Sorumlu | Teknolojiler | Kabul kriteri |
|---|---|---|---|---|---|---|
| **1007** Birinci çeyrek gözden geçirmesi (akademik danışmanlarla) | E10 | 28.06.2027 | 02.07.2027 | Proje Yöneticisi | Toplantı tutanağı, GitHub | Toplantı notu ve güncel risk tablosu repoya eklendi. |
| **1209** Ders kayıtlarının otomatik olarak ders kaynağına eklenmesi | E12 | 21.06.2027 | 09.07.2027 | Backend | BigBlueButton, MinIO / yurt içi S3 uyumlu nesne deposu, Redis ve Arq | Biten dersin kaydı otomatik olarak kaynak kütüphanesine düşüyor. |
| **1210** Bireysel eğitmen kaydı ve abonelik planları | E12 | 21.06.2027 | 09.07.2027 | Backend | FastAPI, Next.js, Keycloak | Bireysel eğitmen kendi kendine kayıt olup ders açabiliyor. |
| **1307** Hibrit arama (yoğun + seyrek) ve sıralama birleştirme | E13 | 21.06.2027 | 16.07.2027 | YZ Mühendisi | pgvector, PostgreSQL tam metin arama, Zemberek-NLP | Hibrit aramanın tek yöntemlere göre etkisi ölçüldü. |
| **1401** Atıflı cevap üretimi: istem ve çıktı biçimi tasarımı | E14 | 01.07.2027 | 16.07.2027 | YZ Mühendisi | Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi, vLLM, Langfuse | Her cümlede kaynak atfı bulunan cevap biçimi çalışıyor. |

### Sprint 17 · 05.07.2027–18.07.2027

**Başlayan görev:** 4 · **Kullanılacak teknolojiler:** SciPy ve scikit-learn (istatistik, Kappa, bootstrap, sınıflandırıcı, kalibrasyon); FastAPI (Python arka uç ve REST API); Next.js (React, TypeScript) ön yüz; bge-reranker-v2-m3 (yeniden sıralama); Değerlendirme düzeneği (kendi kodumuz + RAGAS metrikleri); iyzico (abonelik ve ödeme); pytest (birim ve entegrasyon testi); Playwright (uçtan uca test); axe-core (erişilebilirlik denetimi, WCAG 2.2 AA)

| Görev | Epik | Başlangıç | Bitiş | Sorumlu | Teknolojiler | Kabul kriteri |
|---|---|---|---|---|---|---|
| **1211** Ödeme entegrasyonu (yerli ödeme kuruluşu) | E12 | 05.07.2027 | 23.07.2027 | Backend | iyzico, FastAPI | Abonelik ödemesi test ortamında uçtan uca çalışıyor. |
| **1212** Mobil uyum ve erişilebilirlik | E12 | 05.07.2027 | 23.07.2027 | Frontend | Next.js, axe-core | Telefon tarayıcısında tüm temel akışlar çalışıyor; temel erişilebilirlik denetimi geçti. |
| **1213** Platform iç testi ve kilometre taşı 2 | E12 | 12.07.2027 | 30.07.2027 | Frontend | Playwright, pytest, axe-core | Kritik akışlar test edildi; açık hata kalmadı; devam kararı kayda geçirildi. |
| **1308** Yeniden sıralama ve Recall@5 ölçümü | E13 | 12.07.2027 | 13.08.2027 | YZ Mühendisi | bge-reranker-v2-m3, Değerlendirme düzeneği, SciPy ve scikit-learn | Recall@5 ölçüldü (hedef ≥ %90; ara eşik ≥ %85). |

### Sprint 18 · 19.07.2027–01.08.2027

**Başlayan görev:** 4 · **Kullanılacak teknolojiler:** Elektronik imza; Yıldız ARGEPORTAL; SciPy ve scikit-learn (istatistik, Kappa, bootstrap, sınıflandırıcı, kalibrasyon); FastAPI (Python arka uç ve REST API); Next.js (React, TypeScript) ön yüz; bge-reranker-v2-m3 (yeniden sıralama); Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi

| Görev | Epik | Başlangıç | Bitiş | Sorumlu | Teknolojiler | Kabul kriteri |
|---|---|---|---|---|---|---|
| **1004** Aylık muafiyet raporları: Temmuz, Ağustos, Eylül 2027 | E10 | 01.08.2027 | 20.10.2027 | Proje Yöneticisi | Yıldız ARGEPORTAL, Elektronik imza | Üç rapor zamanında sunuldu. |
| **1402** Atıfların sayfa, slayt ve video dakikasına bağlanması | E14 | 19.07.2027 | 30.07.2027 | Backend | FastAPI, Next.js | Atfa tıklandığında ilgili sayfa veya video dakikası açılıyor. |
| **1403** Soru niyeti sınıflandırma | E14 | 19.07.2027 | 06.08.2027 | YZ Mühendisi | Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi, SciPy ve scikit-learn | Kavram sorusu, ödev talebi ve kapsam dışı soru ayrımı test setinde ölçüldü. |
| **1404** Cevaplanabilirlik kapısı | E14 | 19.07.2027 | 13.08.2027 | YZ Mühendisi | bge-reranker-v2-m3, SciPy ve scikit-learn, Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi | Kaynakta cevabı olmayan sorular tespit edilip reddediliyor. |

### Sprint 19 · 02.08.2027–15.08.2027

**Başlayan görev:** 3 · **Kullanılacak teknolojiler:** Jupyter ve pandas (analiz ve raporlama); SciPy ve scikit-learn (istatistik, Kappa, bootstrap, sınıflandırıcı, kalibrasyon); FastAPI (Python arka uç ve REST API); Next.js (React, TypeScript) ön yüz; Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi; Doğal dil çıkarımı modeli / LLM yargıç (iddia doğrulama); Değerlendirme düzeneği (kendi kodumuz + RAGAS metrikleri)

| Görev | Epik | Başlangıç | Bitiş | Sorumlu | Teknolojiler | Kabul kriteri |
|---|---|---|---|---|---|---|
| **1405** Ceza-duyarlı reddetme eşiğinin ayarlanması | E14 | 09.08.2027 | 27.08.2027 | YZ Mühendisi | SciPy ve scikit-learn, Jupyter ve pandas | Eşik doğrulama setinde ayarlandı; reddetme doğruluğu ölçüldü. |
| **1406** İddia düzeyinde cevap doğrulama | E14 | 09.08.2027 | 17.09.2027 | YZ Mühendisi | Doğal dil çıkarımı modeli / LLM yargıç, Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi, Değerlendirme düzeneği | Sadakat ölçüldü (hedef ≥ %95). |
| **1501** Rubrik tanımlama arayüzü | E15 | 02.08.2027 | 27.08.2027 | Frontend | Next.js, FastAPI | Eğitmen kriter, ağırlık ve seviye tanımlayabiliyor; hazır şablonlar var. |

### Sprint 20 · 16.08.2027–29.08.2027

**Başlayan görev:** 3 · **Kullanılacak teknolojiler:** GitHub (issue, milestone, proje panosu); Jupyter ve pandas (analiz ve raporlama); Gömme modeli adayları: bge-m3, turkish-e5-large (YTÜ COSMOS), multilingual-e5-large, embeddinggemma-300m; Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi; vLLM (model servis sunucusu)

| Görev | Epik | Başlangıç | Bitiş | Sorumlu | Teknolojiler | Kabul kriteri |
|---|---|---|---|---|---|---|
| **1309** İP-3 ara raporu ve kilometre taşı 3 | E13 | 16.08.2027 | 31.08.2027 | YZ Mühendisi | Jupyter ve pandas, GitHub | Deney sonuçları raporlandı; devam kararı kayda geçirildi. |
| **1407** Ödev eşleme ve ipucu merdiveni | E14 | 23.08.2027 | 17.09.2027 | YZ Mühendisi | Gömme modeli adayları: bge-m3, turkish-e5-large, Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi | Ödev sorularında cevap yerine kademeli ipucu veriliyor. |
| **1502** Kriter başına kanıt çıkarımı | E15 | 16.08.2027 | 10.09.2027 | YZ Mühendisi | Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi, vLLM | Her kriter için ödevden ilgili alıntı ve konumu çıkarılıyor. |

### Sprint 21 · 30.08.2027–12.09.2027

**Başlayan görev:** 4 · **Kullanılacak teknolojiler:** Ofis yazılımı (Word / LibreOffice) ve PDF; Python 3.12; FastAPI (Python arka uç ve REST API); Next.js (React, TypeScript) ön yüz; Gömme modeli adayları: bge-m3, turkish-e5-large (YTÜ COSMOS), multilingual-e5-large, embeddinggemma-300m; Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi

| Görev | Epik | Başlangıç | Bitiş | Sorumlu | Teknolojiler | Kabul kriteri |
|---|---|---|---|---|---|---|
| **1408** Cevap sızıntısı tarayıcısı | E14 | 30.08.2027 | 30.09.2027 | YZ Mühendisi | Python 3.12, Gömme modeli adayları: bge-m3, turkish-e5-large | Ödev cevabını içeren yanıtlar engelleniyor. |
| **1411** Sohbet asistanının platforma entegrasyonu | E14 | 30.08.2027 | 08.10.2027 | Frontend | Next.js, FastAPI | Her ders sayfasında asistan çalışıyor; eğitmen pedagojik modu seçebiliyor. |
| **1503** Çapa örneklerle seviye tahmini | E15 | 30.08.2027 | 24.09.2027 | YZ Mühendisi | Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi | Eğitmen puanlı örneklerle karşılaştırmalı puanlama çalışıyor. |
| **1601** KVKK veri envanteri, aydınlatma ve rıza metinleri | E16 | 01.09.2027 | 24.09.2027 | DevOps | Ofis yazılımı | Aydınlatma ve rıza metinleri hukuk onayıyla yayımlandı. |

### Sprint 22 · 13.09.2027–26.09.2027

**Başlayan görev:** 5 · **Kullanılacak teknolojiler:** Label Studio (kendi sunucumuzda veri etiketleme); Python 3.12; SciPy ve scikit-learn (istatistik, Kappa, bootstrap, sınıflandırıcı, kalibrasyon); FastAPI (Python arka uç ve REST API); pgvector (HNSW vektör indeksi); Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi; vLLM (model servis sunucusu); Kubernetes (k3s/RKE2) ve Helm; Terraform (altyapı kodu); Yurt içi GPU bulutu (L40S/H100 sınıfı; teklifle seçilir)

| Görev | Epik | Başlangıç | Bitiş | Sorumlu | Teknolojiler | Kabul kriteri |
|---|---|---|---|---|---|---|
| **1409** Manipülasyon (saldırı) test setinin hazırlanması | E14 | 13.09.2027 | 01.10.2027 | YZ Mühendisi | Label Studio, Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi | En az 500 saldırı ve 200 meşru soru içeren test seti hazır. |
| **1504** Çoklu örnekleme ve belirsizlik ölçümü | E15 | 13.09.2027 | 01.10.2027 | YZ Mühendisi | Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi, SciPy ve scikit-learn | Belirsiz kriterler eğitmen incelemesine işaretleniyor. |
| **1505** Gerekçeli ve kaynağa atıflı geri bildirim üretimi | E15 | 13.09.2027 | 22.10.2027 | YZ Mühendisi | Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi, pgvector | Geri bildirimlerin eğitmenlerce kullanılabilir bulunma oranı ölçüldü (hedef ≥ %80). |
| **1602** Kişisel veri maskeleme ve anonimleştirme hattı | E16 | 13.09.2027 | 01.10.2027 | Backend | Python 3.12, FastAPI | Ad, e-posta, telefon ve kimlik numarası otomatik maskeleniyor. |
| **1603** Yurt içi GPU ortamı ve model servisi | E16 | 13.09.2027 | 08.10.2027 | DevOps | Yurt içi GPU bulutu, vLLM, Kubernetes, Terraform | Açık ağırlıklı model yurt içi sunucuda hizmet veriyor. |

### Sprint 23 · 27.09.2027–10.10.2027

**Başlayan görev:** 5 · **Kullanılacak teknolojiler:** Toplantı tutanağı (Markdown, repoda); Ofis yazılımı (Word / LibreOffice) ve PDF; GitHub (issue, milestone, proje panosu); Next.js (React, TypeScript) ön yüz; PostgreSQL 16 (satır düzeyi güvenlik ile kurum ayrımı); Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi; Hugging Face Transformers ve PEFT/LoRA (ince ayar); Langfuse (kendi sunucumuzda LLM izleme ve değerlendirme kaydı); Değerlendirme düzeneği (kendi kodumuz + RAGAS metrikleri); Yurt içi GPU bulutu (L40S/H100 sınıfı; teklifle seçilir); Prometheus ve Grafana (izleme)

| Görev | Epik | Başlangıç | Bitiş | Sorumlu | Teknolojiler | Kabul kriteri |
|---|---|---|---|---|---|---|
| **1008** İkinci çeyrek gözden geçirmesi | E10 | 27.09.2027 | 01.10.2027 | Proje Yöneticisi | Toplantı tutanağı, GitHub | Toplantı notu ve güncel risk tablosu repoya eklendi. |
| **1410** Dayanıklılık testleri ve iyileştirme | E14 | 27.09.2027 | 15.10.2027 | YZ Mühendisi | Değerlendirme düzeneği, Langfuse | Sızıntı oranı ölçüldü (hedef ≤ %2); aşırı kısıtlama ≤ %5. |
| **1604** Yurt içi model ince ayar denemeleri | E16 | 04.10.2027 | 12.11.2027 | YZ Mühendisi | Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi, Hugging Face Transformers ve PEFT/LoRA, Yurt içi GPU bulutu | En az iki ince ayar deneyi raporlandı. |
| **1701** Pilot planı ve bilgilendirilmiş onam | E17 | 04.10.2027 | 15.10.2027 | Proje Yöneticisi | Ofis yazılımı | Pilot planı ve onam metinleri akademik danışmanla onaylandı. |
| **1702** Kullanım ölçüm altyapısı ve kalite panosu | E17 | 04.10.2027 | 29.10.2027 | Frontend | Next.js, Prometheus ve Grafana, Langfuse, PostgreSQL 16 | Aktif kullanıcı, soru sayısı, memnuniyet ve YZ kalite metrikleri izleniyor. |

### Sprint 24 · 11.10.2027–24.10.2027

**Başlayan görev:** 2 · **Kullanılacak teknolojiler:** Jupyter ve pandas (analiz ve raporlama); SciPy ve scikit-learn (istatistik, Kappa, bootstrap, sınıflandırıcı, kalibrasyon)

| Görev | Epik | Başlangıç | Bitiş | Sorumlu | Teknolojiler | Kabul kriteri |
|---|---|---|---|---|---|---|
| **1412** İP-4 deney raporu ve kilometre taşı 4 | E14 | 11.10.2027 | 29.10.2027 | YZ Mühendisi | Jupyter ve pandas, SciPy ve scikit-learn | AR-1 ve AR-4 sonuçları raporlandı; devam kararı kayda geçirildi. |
| **1506** Ders bazında kalibrasyon modeli | E15 | 11.10.2027 | 05.11.2027 | YZ Mühendisi | SciPy ve scikit-learn | Kalibrasyonun uyuma etkisi ölçüldü. |

### Sprint 25 · 25.10.2027–07.11.2027

**Başlayan görev:** 6 · **Kullanılacak teknolojiler:** Ofis yazılımı (Word / LibreOffice) ve PDF; Elektronik imza; Yıldız ARGEPORTAL; Jupyter ve pandas (analiz ve raporlama); SciPy ve scikit-learn (istatistik, Kappa, bootstrap, sınıflandırıcı, kalibrasyon); FastAPI (Python arka uç ve REST API); Next.js (React, TypeScript) ön yüz; Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi; Ticari LLM API (yalnızca karşılaştırma ve anonim veri); Langfuse (kendi sunucumuzda LLM izleme ve değerlendirme kaydı); Değerlendirme düzeneği (kendi kodumuz + RAGAS metrikleri); Kubernetes (k3s/RKE2) ve Helm; Prometheus ve Grafana (izleme)

| Görev | Epik | Başlangıç | Bitiş | Sorumlu | Teknolojiler | Kabul kriteri |
|---|---|---|---|---|---|---|
| **1005** Aylık muafiyet raporları: Ekim, Kasım, Aralık 2027 | E10 | 01.11.2027 | 20.01.2028 | Proje Yöneticisi | Yıldız ARGEPORTAL, Elektronik imza | Üç rapor zamanında sunuldu. |
| **1507** Eğitmenle uyum (Kappa) ölçümü ve yanlılık analizi | E15 | 25.10.2027 | 19.11.2027 | YZ Mühendisi | SciPy ve scikit-learn, Jupyter ve pandas | Ağırlıklı Kappa ölçüldü (hedef ≥ 0,75); uzunluk ve yazım yanlılığı raporlandı. |
| **1508** Eğitmen onay ekranı | E15 | 01.11.2027 | 26.11.2027 | Frontend | Next.js, FastAPI | Eğitmen YZ önerisini onaylayıp düzeltebiliyor; düzeltmeler kaydediliyor. |
| **1605** Yurt içi ve ticari model kalite karşılaştırması | E16 | 01.11.2027 | 03.12.2027 | YZ Mühendisi | Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi, Ticari LLM API, Değerlendirme düzeneği, Langfuse | Kalite farkı ölçüldü (hedef ≤ %5). |
| **1703** Eğitmenlerin platform ve YZ kullanım eğitimi | E17 | 25.10.2027 | 05.11.2027 | Eğitim Koordinatörü | Ofis yazılımı | Tüm pilot eğitmenleri eğitimi tamamladı. |
| **1704** Pilot 1'in başlatılması (kendi öğrencilerimiz) | E17 | 01.11.2027 | 12.11.2027 | Proje Yöneticisi | Kubernetes, Prometheus ve Grafana | En az üç derste pilot başladı. |

### Sprint 26 · 08.11.2027–21.11.2027

**Başlayan görev:** 5 · **Kullanılacak teknolojiler:** Ofis yazılımı (Word / LibreOffice) ve PDF; GitHub (issue, milestone, proje panosu); pandas (veri analizi); SciPy ve scikit-learn (istatistik, Kappa, bootstrap, sınıflandırıcı, kalibrasyon); Redis ve Arq (iş kuyruğu, önbellek); Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi; vLLM (model servis sunucusu); SGLang (karşılaştırma kolu); Langfuse (kendi sunucumuzda LLM izleme ve değerlendirme kaydı); Prometheus ve Grafana (izleme)

| Görev | Epik | Başlangıç | Bitiş | Sorumlu | Teknolojiler | Kabul kriteri |
|---|---|---|---|---|---|---|
| **1509** Yapay zekâ ile yazılmış metin tespiti | E15 | 08.11.2027 | 17.12.2027 | YZ Mühendisi | Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi, SciPy ve scikit-learn | Tespit doğruluğu ölçüldü ya da kapsamdan çıkarma kararı alındı. |
| **1606** Önbellek ve görev bazlı model yönlendirme | E16 | 15.11.2027 | 10.12.2027 | DevOps | Redis ve Arq, vLLM, SGLang | Yanıt süresi ölçüldü (hedef p50 ≤ 3 sn); öğrenci başı maliyet hesaplandı. |
| **1705** Pilot 1 izleme ve haftalık iyileştirmeler | E17 | 15.11.2027 | 24.12.2027 | Proje Yöneticisi | Langfuse, Prometheus ve Grafana, GitHub | Haftalık izleme notları repoya eklendi; öğrencilerin en az %50'si platformu kullandı. |
| **1706** Eğitmen süre ölçümü (YZ önerili ve YZ'siz değerlendirme) | E17 | 15.11.2027 | 17.12.2027 | Eğitim Koordinatörü | pandas, SciPy ve scikit-learn | Ödev başı değerlendirme süresindeki değişim ölçüldü (hedef ≥ %40 azalma). |
| **1801** Faz 2 proje dosyası taslağı | E18 | 15.11.2027 | 10.12.2027 | Proje Yöneticisi | Ofis yazılımı | Sanal sınıf projesinin araştırma soruları ve iş planı taslağı hazır. |

### Sprint 27 · 22.11.2027–05.12.2027

**Başlayan görev:** 2 · **Kullanılacak teknolojiler:** Ofis yazılımı (Word / LibreOffice) ve PDF; TÜRKPATENT, Espacenet, Google Patents

| Görev | Epik | Başlangıç | Bitiş | Sorumlu | Teknolojiler | Kabul kriteri |
|---|---|---|---|---|---|---|
| **1707** Dış kurum pilot sözleşmesi | E17 | 01.12.2027 | 31.12.2027 | Yönetim | Ofis yazılımı | En az bir dış kurumla pilot sözleşmesi imzalandı. |
| **1804** Patentlenebilirlik görüşü (Yıldız TTO) | E18 | 01.12.2027 | 24.12.2027 | Proje Yöneticisi | TÜRKPATENT, Espacenet, Google Patents | Üç aday yöntem için yazılı görüş alındı. |

### Sprint 28 · 06.12.2027–19.12.2027

**Başlayan görev:** 5 · **Kullanılacak teknolojiler:** Ofis yazılımı (Word / LibreOffice) ve PDF; Jupyter ve pandas (analiz ve raporlama); pandas (veri analizi); Prometheus ve Grafana (izleme); k6 (yük testi); OWASP ZAP ve bağımsız sızma testi

| Görev | Epik | Başlangıç | Bitiş | Sorumlu | Teknolojiler | Kabul kriteri |
|---|---|---|---|---|---|---|
| **1510** İP-5 deney raporu ve kilometre taşı 5 | E15 | 13.12.2027 | 24.12.2027 | YZ Mühendisi | Jupyter ve pandas | AR-3 sonuçları raporlandı; devam kararı kayda geçirildi. |
| **1607** Yük testi | E16 | 06.12.2027 | 24.12.2027 | DevOps | k6, Prometheus ve Grafana | Hedef kullanıcı yükünde performans raporlandı. |
| **1608** Bağımsız sızma testi | E16 | 06.12.2027 | 24.12.2027 | DevOps | OWASP ZAP ve bağımsız sızma testi | Rapor alındı; kritik bulgular kapatıldı. |
| **1802** Faz 2 dosyasının pilot verileriyle tamamlanması | E18 | 13.12.2027 | 31.12.2027 | Proje Yöneticisi | Ofis yazılımı, pandas | Faz 1 pilot verileri dosyaya eklendi. |
| **1807** Fiyat listesi ve satış paketi | E18 | 13.12.2027 | 14.01.2028 | Yönetim | Ofis yazılımı | Kurumsal ve bireysel paketler, fiyatlar ve tanıtım materyali hazır. |

### Sprint 29 · 20.12.2027–02.01.2028

**Başlayan görev:** 1 · **Kullanılacak teknolojiler:** Toplantı tutanağı (Markdown, repoda); GitHub (issue, milestone, proje panosu)

| Görev | Epik | Başlangıç | Bitiş | Sorumlu | Teknolojiler | Kabul kriteri |
|---|---|---|---|---|---|---|
| **1009** Üçüncü çeyrek gözden geçirmesi | E10 | 20.12.2027 | 24.12.2027 | Proje Yöneticisi | Toplantı tutanağı, GitHub | Toplantı notu ve güncel risk tablosu repoya eklendi. |

### Sprint 30 · 03.01.2028–16.01.2028

**Başlayan görev:** 5 · **Kullanılacak teknolojiler:** Ofis yazılımı (Word / LibreOffice) ve PDF; Yıldız ARGEPORTAL; TÜRKPATENT, Espacenet, Google Patents; Keycloak (OIDC/SAML kimlik yönetimi, kurumsal SSO); Kubernetes (k3s/RKE2) ve Helm

| Görev | Epik | Başlangıç | Bitiş | Sorumlu | Teknolojiler | Kabul kriteri |
|---|---|---|---|---|---|---|
| **1708** Pilot 2 kurulumu ve kurum eğitimi | E17 | 03.01.2028 | 14.01.2028 | Proje Yöneticisi | Kubernetes, Keycloak | Dış kurumda platform kuruldu; eğitmenler eğitildi. |
| **1803** Faz 2 başvurusunun teslimi (son tarih 31.01.2028) | E18 | 03.01.2028 | 14.01.2028 | Proje Yöneticisi | Yıldız ARGEPORTAL | Başvuru teslim edildi; projesiz kalma riski kapandı. |
| **1805** Tescil veya patent başvurusu | E18 | 03.01.2028 | 28.01.2028 | Proje Yöneticisi | TÜRKPATENT, Espacenet, Google Patents | En az bir başvuru yapıldı. |
| **1806** YTÜ ile ortak akademik makale taslağı | E18 | 03.01.2028 | 25.02.2028 | Akademik Danışman | Ofis yazılımı | Makale taslağı tamamlandı; gönderim yapılacak dergi veya konferans belirlendi. |
| **1808** Kurumsal sözleşme şablonu ve KVKK eki | E18 | 10.01.2028 | 11.02.2028 | Yönetim | Ofis yazılımı | Hukuk onaylı şablon hazır. |

### Sprint 31 · 17.01.2028–30.01.2028

**Başlayan görev:** 2 · **Kullanılacak teknolojiler:** Ofis yazılımı (Word / LibreOffice) ve PDF; Langfuse (kendi sunucumuzda LLM izleme ve değerlendirme kaydı); Prometheus ve Grafana (izleme)

| Görev | Epik | Başlangıç | Bitiş | Sorumlu | Teknolojiler | Kabul kriteri |
|---|---|---|---|---|---|---|
| **1709** Pilot 2 izleme | E17 | 17.01.2028 | 25.02.2028 | Proje Yöneticisi | Langfuse, Prometheus ve Grafana | Kullanım ve kalite metrikleri toplandı; kurum geri bildirimi alındı. |
| **1809** Faz 2 için TÜBİTAK başvurusu | E18 | 17.01.2028 | 25.02.2028 | Proje Yöneticisi | Ofis yazılımı | Başvuru yapıldı. |

### Sprint 32 · 31.01.2028–13.02.2028

**Başlayan görev:** 1 · **Kullanılacak teknolojiler:** Elektronik imza; Yıldız ARGEPORTAL

| Görev | Epik | Başlangıç | Bitiş | Sorumlu | Teknolojiler | Kabul kriteri |
|---|---|---|---|---|---|---|
| **1006** Aylık muafiyet raporları: Ocak, Şubat, Mart 2028 | E10 | 01.02.2028 | 20.04.2028 | Proje Yöneticisi | Yıldız ARGEPORTAL, Elektronik imza | Üç rapor zamanında sunuldu. |

### Sprint 33 · 14.02.2028–27.02.2028

**Başlayan görev:** 1 · **Kullanılacak teknolojiler:** Ofis yazılımı (Word / LibreOffice) ve PDF; Jupyter ve pandas (analiz ve raporlama)

| Görev | Epik | Başlangıç | Bitiş | Sorumlu | Teknolojiler | Kabul kriteri |
|---|---|---|---|---|---|---|
| **1710** Pilot raporu | E17 | 21.02.2028 | 10.03.2028 | Proje Yöneticisi | Jupyter ve pandas, Ofis yazılımı | İki pilotun sonuçları tek raporda toplandı. |

### Sprint 34 · 28.02.2028–12.03.2028

**Başlayan görev:** 1 · **Kullanılacak teknolojiler:** Ofis yazılımı (Word / LibreOffice) ve PDF; Jupyter ve pandas (analiz ve raporlama)

| Görev | Epik | Başlangıç | Bitiş | Sorumlu | Teknolojiler | Kabul kriteri |
|---|---|---|---|---|---|---|
| **1810** Faz 1 sonuç raporu | E18 | 01.03.2028 | 17.03.2028 | Proje Yöneticisi | Ofis yazılımı, Jupyter ve pandas | Tüm hedeflere karşı sonuçlar raporlandı. |

### Sprint 35 · 13.03.2028–26.03.2028

**Başlayan görev:** 2 · **Kullanılacak teknolojiler:** Toplantı tutanağı (Markdown, repoda); Elektronik imza; Yıldız ARGEPORTAL; GitHub (issue, milestone, proje panosu)

| Görev | Epik | Başlangıç | Bitiş | Sorumlu | Teknolojiler | Kabul kriteri |
|---|---|---|---|---|---|---|
| **1010** Dördüncü çeyrek gözden geçirmesi | E10 | 20.03.2028 | 24.03.2028 | Proje Yöneticisi | Toplantı tutanağı, GitHub | Toplantı notu ve kapanış değerlendirmesi repoya eklendi. |
| **1811** Proje bitirme belgesi başvurusu | E18 | 13.03.2028 | 31.03.2028 | Proje Yöneticisi | Yıldız ARGEPORTAL, Elektronik imza | Başvuru yapıldı. |

## 5. Faz 2 ve Faz 3 makro görevleri

| Görev | Epik | Başlangıç | Bitiş | Sorumlu | Teknolojiler | Kabul kriteri |
|---|---|---|---|---|---|---|
| **2001** Sanal sınıf teknik tasarımı ve teknoloji seçimi | E20 | 03.04.2028 | 28.04.2028 | YZ Mühendisi | LiveKit, Colyseus, Three.js / React Three Fiber, Yjs | Mimari ve teknoloji seçimi gerekçeleriyle yazıldı. |
| **2002** Gerçek zamanlı senkronizasyon prototipi | E20 | 01.05.2028 | 30.06.2028 | Backend | Colyseus, LiveKit, Yjs | Sınıf başına en az 50 kullanıcı ile senkronizasyon çalışıyor. |
| **2003** Düşük bant genişliği ve ölçek testleri | E20 | 03.07.2028 | 29.09.2028 | DevOps | k6, LiveKit | Hedef bağlantı ve cihaz koşullarında performans raporlandı. |
| **2101** Avatar oluşturma | E21 | 01.05.2028 | 31.07.2028 | Frontend | Three.js / React Three Fiber, VRM/GLB açık avatar formatı | Kullanıcılar kişisel avatar oluşturabiliyor. |
| **2102** Mekânsal ses ve çalışma odaları | E21 | 03.07.2028 | 31.10.2028 | Backend | LiveKit | Grup çalışması için çalışma odaları ve mekânsal ses çalışıyor. |
| **2201** Çok konuşmacılı sınıf bağlamı modeli | E22 | 03.07.2028 | 29.09.2028 | YZ Mühendisi | Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi, faster-whisper | Asistan, sorunun kimden ve hangi bağlamda geldiğini doğru ayırt ediyor. |
| **2202** Faz 1 YZ'sinin sınıf asistanı olarak entegrasyonu | E22 | 04.09.2028 | 29.12.2028 | YZ Mühendisi | Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi, vLLM, LiveKit | Asistan sınıf içinde ders kaynağına dayalı yanıt veriyor. |
| **2301** Gizliliği koruyan katılım metrikleri | E23 | 04.09.2028 | 31.01.2029 | YZ Mühendisi | pandas, SciPy ve scikit-learn | Kişisel veri işlemeden grup düzeyinde metrikler üretiliyor. |
| **2401** Sanal sınıf pilotu | E24 | 01.11.2028 | 28.02.2029 | Proje Yöneticisi | Prometheus ve Grafana, Langfuse | Kendi kurumumuzda pilot tamamlandı. |
| **2402** Faz 3 başvurusunun teslimi | E24 | 01.11.2028 | 15.01.2029 | Proje Yöneticisi | Ofis yazılımı | Faz 3 başvurusu en geç Faz 2 bitişinden 60 gün önce teslim edildi. |
| **2403** Satış paketinin sanal sınıfla güncellenmesi | E24 | 01.01.2029 | 30.03.2029 | Yönetim | Ofis yazılımı | Güncel paket ve fiyatlar yayımlandı. |
| **3001** Faz 3 kapsamının belirlenmesi: öğrenci modelleme, kişisel çalışma rotası, erken uyarı | E30 | 02.04.2029 | 27.04.2029 | Proje Yöneticisi | Ofis yazılımı | Faz 3 araştırma soruları ve iş planı onaylandı. Ayrıntılı sprint planı bu aşamada yapılacaktır. |

## 6. Kritik tarihler

| Tarih | Olay | Kural |
|---|---|---|
| 11.12.2026 | Online aday firma başvurusu | Eksik veya hatalı beyan başvurunun yok sayılmasına yol açar |
| ≤ 09.02.2027 | Aday komisyon sonucu | En geç 60 gün; itiraz yolu yok |
| ~12.03.2027 | Hakem heyeti sonucu (tahmini) | 21 + 21 gün; salt çoğunluk |
| 01.04.2027 | Faz 1 başlangıcı (tahmini) | Faaliyet onay yazısının tarihi esas alınır |
| Her ayın 20'si | Aylık muafiyet raporu | Gecikme aykırı faaliyet sayılır |
| 31.01.2028 | Faz 2 başvurusu son tarihi | Mevcut proje bitmeden en az 60 gün önce |
| 29.02.2028 | Revizyon başvurusu için son gün | Bitişe 30 günden az kala revizyon yapılamaz |
| 31.03.2028 | Faz 1 bitişi | 90 gün projesiz kalan firma bölgeden çıkarılır |
| 31.05.2028 | 2027 yıllık faaliyet raporu | Mali müşavir onaylı |
| 31.12.2028 | 4691 sayılı Kanun teşvik süresi sonu (mevcut mevzuat) | Uzatma kararı izlenmelidir |

## 7. Teknoloji kataloğu ve kullanım yoğunluğu

Teknoloji seçimlerinin alternatiflerle karşılaştırması ve gerekçeleri: [`docs/04-teknoloji-kararlari.md`](04-teknoloji-kararlari.md).

| Kod | Teknoloji | Görev sayısı | Kullanıldığı ilk sprint |
|---|---|---|---|
| TT | Toplantı tutanağı (Markdown, repoda) | 14 | S01 |
| OFIS | Ofis yazılımı (Word / LibreOffice) ve PDF | 30 | S01 |
| EIMZA | Elektronik imza | 10 | S01 |
| ARGE | Yıldız ARGEPORTAL | 11 | S05 |
| WEB | Web ve kaynak araştırması | 3 | S01 |
| TP | TÜRKPATENT, Espacenet, Google Patents | 3 | S01 |
| GH | GitHub (issue, milestone, proje panosu) | 12 | S01 |
| GHA | GitHub Actions (sürekli entegrasyon ve dağıtım) | 2 | S10 |
| MER | Mermaid (mimari ve akış diyagramları) | 1 | S10 |
| LS | LimeSurvey (kendi sunucumuzda anket) | 2 | S01 |
| ETK | Label Studio (kendi sunucumuzda veri etiketleme) | 6 | S01 |
| PY | Python 3.12 | 6 | S01 |
| NB | Jupyter ve pandas (analiz ve raporlama) | 9 | S11 |
| PD | pandas (veri analizi) | 5 | S01 |
| SCIPY | SciPy ve scikit-learn (istatistik, Kappa, bootstrap, sınıflandırıcı, kalibrasyon) | 15 | S02 |
| FA | FastAPI (Python arka uç ve REST API) | 16 | S02 |
| NX | Next.js (React, TypeScript) ön yüz | 13 | S02 |
| PG | PostgreSQL 16 (satır düzeyi güvenlik ile kurum ayrımı) | 5 | S01 |
| PGV | pgvector (HNSW vektör indeksi) | 4 | S01 |
| FTS | PostgreSQL tam metin arama ('turkish' sözlüğü) | 3 | S01 |
| ZEM | Zemberek-NLP (Türkçe biçimbirim çözümleme) | 2 | S13 |
| RD | Redis ve Arq (iş kuyruğu, önbellek) | 4 | S12 |
| S3 | MinIO / yurt içi S3 uyumlu nesne deposu | 4 | S01 |
| DOC | Docling (PDF/DOCX ayrıştırma, MIT lisansı) | 2 | S01 |
| MRK | Marker (karşılaştırma kolu, GPL-3.0) | 1 | S12 |
| TES | Tesseract OCR (Türkçe dil paketi) | 1 | S12 |
| PPT | python-pptx (slayt ayrıştırma) | 1 | S13 |
| VLM | Görsel-dil modeli (Qwen2.5-VL / Gemma 3 adayları, deneyle seçilir) | 1 | S13 |
| WH | faster-whisper (Whisper large-v3; turbo sürüm hız kolu) | 2 | S13 |
| EMB | Gömme modeli adayları: bge-m3, turkish-e5-large (YTÜ COSMOS), multilingual-e5-large, embeddinggemma-300m | 4 | S01 |
| RR | bge-reranker-v2-m3 (yeniden sıralama) | 2 | S17 |
| LLM | Açık ağırlıklı üretim modeli adayları: Cosmos T1 / Turkish-Gemma-9b-T1, Turkish-Llama-8b, Qwen ailesi | 17 | S02 |
| API | Ticari LLM API (yalnızca karşılaştırma ve anonim veri) | 3 | S02 |
| VLLM | vLLM (model servis sunucusu) | 7 | S02 |
| SGL | SGLang (karşılaştırma kolu) | 1 | S26 |
| PEFT | Hugging Face Transformers ve PEFT/LoRA (ince ayar) | 1 | S23 |
| NLI | Doğal dil çıkarımı modeli / LLM yargıç (iddia doğrulama) | 1 | S19 |
| LF | Langfuse (kendi sunucumuzda LLM izleme ve değerlendirme kaydı) | 7 | S16 |
| RG | Değerlendirme düzeneği (kendi kodumuz + RAGAS metrikleri) | 6 | S14 |
| KC | Keycloak (OIDC/SAML kimlik yönetimi, kurumsal SSO) | 3 | S11 |
| BBB | BigBlueButton (yurt içi canlı ders) | 2 | S15 |
| IYZ | iyzico (abonelik ve ödeme) | 1 | S17 |
| DK | Docker ve Docker Compose | 2 | S09 |
| K8S | Kubernetes (k3s/RKE2) ve Helm | 3 | S22 |
| TF | Terraform (altyapı kodu) | 1 | S22 |
| GPU | Yurt içi GPU bulutu (L40S/H100 sınıfı; teklifle seçilir) | 3 | S13 |
| PROM | Prometheus ve Grafana (izleme) | 6 | S23 |
| PYT | pytest (birim ve entegrasyon testi) | 3 | S10 |
| PW | Playwright (uçtan uca test) | 1 | S17 |
| K6 | k6 (yük testi) | 2 | S28 |
| ZAP | OWASP ZAP ve bağımsız sızma testi | 1 | S28 |
| AXE | axe-core (erişilebilirlik denetimi, WCAG 2.2 AA) | 2 | S17 |
| LK | LiveKit (gerçek zamanlı ses/video altyapısı) | 5 | Faz 2 |
| COL | Colyseus (oda ve durum senkronizasyonu) | 2 | Faz 2 |
| YJS | Yjs (ortak beyaz tahta, CRDT) | 2 | Faz 2 |
| THREE | Three.js / React Three Fiber (3B sahne) | 2 | Faz 2 |
| AV | VRM/GLB açık avatar formatı (VRoid Studio, Avatar SDK değerlendirmesi) | 1 | Faz 2 |

## 8. Çalışma kuralları

- Her görev GitHub'da bir issue'dur; her issue bir epiğe (alt iş olarak) ve bir sprint milestone'una bağlıdır.
- Durum etiketleri: `durum: yapılacak` → `durum: bu sprint` → `durum: devam ediyor` → `durum: incelemede` → kapalı.
- Bir görev ancak kabul kriteri sağlandığında kapatılır. Sayısal kriterlerde ölçüm sonucu issue'ya yorum olarak eklenir; bu kayıtlar hakem ve denetim için kanıttır.
- Sprint başında sprint planlama, sprint sonunda gözden geçirme yapılır; kayan görev bir sonraki sprinte taşınır ve plan dosyası güncellenir.
- Kritik yol: ön görüşme ve TTO talebi → başvuru → aday komisyon → hakem → kira → faaliyet onayı → Faz 1 → Faz 2 başvurusu.

