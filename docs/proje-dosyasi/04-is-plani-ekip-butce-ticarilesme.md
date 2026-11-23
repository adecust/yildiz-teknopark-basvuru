# PROJE DOSYASI · 04 · İş Planı, Ekip, Bütçe ve Ticarileşme

Bu bölüm hakem formundaki şu ölçütleri besliyor: **süre uygunluğu (temel soru), ticarileşme (%15), ekip (%6), üniversite-sanayi iş birliği (%10), katma değer (%6)**. Görev düzeyindeki ayrıntılı plan ve tarihler [`docs/03-proje-plani-sprint-ve-kanban.md`](../03-proje-plani-sprint-ve-kanban.md) dosyasında ve GitHub issue'larında.

---

## 1. İş paketleri ve çıktılar

| İP | Ad | Ay | Kişi-ay | Ana çıktılar (Ç) |
|---|---|---|---|---|
| İP-0 | Proje yönetimi ve teknopark raporlaması | 1–12 | 4,0 | Ç0.1 Aylık muafiyet ve izleme raporları · Ç0.2 Çeyreklik ilerleme raporları |
| İP-1 | Gereksinim, literatür ve Türkçe test setleri | 1–2 | 4,5 | Ç1.1 Gereksinim ve mimari dokümanı · Ç1.2 SOTA raporu · Ç1.3 TS-QA · Ç1.4 TS-ODEV · Ç1.5 Değerlendirme protokolü |
| İP-2 | Platform çekirdeği (test yatağı) | 1–4 | 18,5 | Ç2.1 Çok kiracılı platform MVP (rol, ders, kaynak, ödev, takvim, canlı ders, B2C ödeme) |
| İP-3 | İçerik işleme ve Türkçe bilgi erişimi (AR-2, AR-5) | 2–5 | 7,5 | Ç3.1 İçerik alım hattı · Ç3.2 Konuşma tanıma hattı · Ç3.3 Erişim deney raporu (E-2, E-5) |
| İP-4 | Kaynağa dayalı soru-cevap ve pedagojik sınırlar (AR-1, AR-4) | 4–7 | 9,0 | Ç4.1 Soru-cevap motoru · Ç4.2 Pedagojik politika motoru · Ç4.3 TS-SIZINTI · Ç4.4 Deney raporu (E-1, E-4) |
| İP-5 | Rubrik tabanlı otomatik ödev değerlendirme (AR-3) | 5–9 | 11,5 | Ç5.1 Rubrik arayüzü · Ç5.2 Değerlendirme motoru · Ç5.3 Kalibrasyon modülü · Ç5.4 Deney raporu (E-3) |
| İP-6 | Ölçeklenebilirlik, KVKK ve yurt içi model (AR-6) | 6–9 | 8,5 | Ç6.1 Yurt içi model servisi · Ç6.2 Model karşılaştırma raporu (E-6) · Ç6.3 KVKK uyum paketi · Ç6.4 Yük testi raporu |
| İP-7 | Pilot uygulama | 7–12 | 10,5 | Ç7.1 Ölçüm altyapısı · Ç7.2 Pilot 1 raporu · Ç7.3 Pilot 2 (dış kurum) raporu |
| İP-8 | Fikri mülkiyet, ticarileşme ve Faz 2 başvurusu | 8–12 | 4,0 | Ç8.1 Tescil/patent başvurusu · Ç8.2 Satış paketi · Ç8.3 Faz 2 proje dosyası · Ç8.4 Proje sonuç raporu |
| | **Toplam** | | **78,0** | Platform (İP-2) payı: 18,5 / 78 = **%23,7** |

## 2. Kilometre taşları ve devam/dur kararları

| KT | Tarih | Kilometre taşı | Devam kriteri | Kriter sağlanmazsa |
|---|---|---|---|---|
| KT-1 | 31.05.2027 | Test setleri ve protokol hazır | TS-QA ≥ 500, TS-ODEV ≥ 300, etiketleyici uyumu raporlandı | Set toplama 3 hafta uzatılır; İP-4/5 başlangıcı kaydırılır |
| KT-2 | 30.07.2027 | Platform MVP | Kritik akışlar çalışıyor; iç testler geçti | Kapsam azaltılır (B2C ödeme sonraya) |
| KT-3 | 31.08.2027 | Erişim hedefi | Recall@5 ≥ %85 (ara eşik) | Alan uyarlamalı ince ayar kolu (E2-f) açılır |
| KT-4 | 29.10.2027 | Soru-cevap ve pedagoji hedefleri | Sadakat ≥ %93, sızıntı ≤ %3 (ara eşik) | Pilot 1 "kapalı mod" ile başlar |
| KT-5 | 24.12.2027 | Değerlendirme ve ölçek hedefleri | QWK ≥ 0,70 (ara eşik), p95 ≤ 6 sn | Asistan modu (B planı) ile pilota devam |
| KT-6 | 14.01.2028 | **Faz 2 başvurusu teslim** | Dosya hazır | **Kritik:** 90 gün kuralı. Bu kilometre taşı kaydırılamaz |
| KT-7 | 31.03.2028 | Faz 1 kapanış | §10 (belge 03) kabul kriterleri | Proje bitirme belgesi + sonuç raporu |

---

## 3. Ekip ve organizasyon

### 3.1 Roller

| Rol | Kişi | Tam zamanlı eşdeğer | Statü (teknopark) | Profil | Sorumluluk |
|---|---|---|---|---|---|
| **Proje yöneticisi / ürün sahibi** | 1 | 1,0 | Ar-Ge personeli | Mühendislik veya ilgili lisans; yazılım ürün yönetimi deneyimi | Planlama, teknopark raporlaması, pilot, paydaş yönetimi |
| **Kıdemli YZ / dil işleme mühendisi (teknik lider)** | 1 | 1,0 | Ar-Ge personeli (araştırmacı) | Yüksek lisans/doktora tercihen; RAG, değerlendirme, LLM servis deneyimi | AR-1, AR-2, AR-6 teknik liderliği; deney tasarımı |
| **YZ mühendisi** | 1 | 1,0 | Ar-Ge personeli (araştırmacı) | Lisans + ML/NLP deneyimi | AR-3, AR-4, AR-5; değerlendirme düzeneği |
| **Backend geliştirici** | 2 | 2,0 | Ar-Ge personeli (yazılımcı) | Python/FastAPI, PostgreSQL | Platform, YZ servis entegrasyonu, güvenlik |
| **Frontend geliştirici** | 1 | 1,0 | Ar-Ge personeli (yazılımcı) | React/Next.js, erişilebilirlik | Öğrenci, eğitmen ve kurum arayüzleri |
| **DevOps / güvenlik** | 1 | 0,5 | Ar-Ge personeli (yazılımcı) | Kubernetes, GPU servis, gözlemleme | Altyapı, yük testi, KVKK teknik önlemleri |
| **Eğitim tasarımcısı / alan uzmanı** | 1 | 1,0 | **Ana şirkette** (teknopark dışı) **[TEYİT: mali müşavir]** | Eğitmen kökenli | Rubrik tasarımı, test seti etiketleme koordinasyonu |
| **YTÜ akademik danışman: Türkçe NLP / LLM** | 1 | ≈ 0,1 | Akademik danışman (TTO üzerinden) | Hedef: YTÜ Bilgisayar Müh., Türkçe dil modeli çalışmaları (COSMOS grubu) **[TEYİT]** | Yöntem danışmanlığı, deney tasarımı denetimi, ortak yayın |
| **YTÜ akademik danışman: ölçme-değerlendirme** | 1 | ≈ 0,1 | Akademik danışman (TTO üzerinden) | Hedef: YTÜ Eğitim Fakültesi **[TEYİT]** | Rubrik geçerliliği, QWK analizi, pilot tasarımı ve etik |
| **YTÜ stajyer / tez öğrencisi** | 2 | 2 × 0,5 | Stajyer | Bilgisayar Müh. / BÖTE öğrencileri | Etiketleme, deney koşturma, test |

**Personel kuralı kontrolü:** Teknoparkta 7 kişi Ar-Ge personeli. Destek personeli 0 (eğitim tasarımcısı ana şirkette). Kapsam dışı personel 0. Yıldız sınırları (destek ≈ %10, kapsam dışı ≤ %15) içinde.

**Mevcut ekip ve işe alım:** Backend, frontend ve DevOps rolleri **mevcut yazılım ekibinden** karşılanır **[VARSAYIM: H-06 envanteriyle doğrulanacak]**. **Kıdemli YZ mühendisi işe alınacak** (H-07, 29.01.2027'ye kadar). İkinci YZ mühendisi mevcut ekipten yetiştirilebilir ya da işe alınır.

### 3.2 Kişi-ay dağılımı (personel × iş paketi)

| Rol | İP-0 | İP-1 | İP-2 | İP-3 | İP-4 | İP-5 | İP-6 | İP-7 | İP-8 | Toplam |
|---|---|---|---|---|---|---|---|---|---|---|
| Proje yöneticisi | 4,0 | 2,0 | | | | | | 3,0 | 3,0 | 12,0 |
| Kıdemli YZ mühendisi | | 1,5 | | 3,0 | 3,5 | 2,5 | 1,5 | | | 12,0 |
| YZ mühendisi | | 1,0 | | 2,5 | 2,5 | 3,5 | 2,5 | | | 12,0 |
| Backend 1 | | | 6,0 | | 1,0 | 1,5 | 1,5 | 2,0 | | 12,0 |
| Backend 2 | | | 5,0 | 2,0 | | 2,0 | | 2,0 | 1,0 | 12,0 |
| Frontend | | | 6,0 | | 2,0 | 2,0 | | 2,0 | | 12,0 |
| DevOps (0,5) | | | 1,5 | | | | 3,0 | 1,5 | | 6,0 |
| **Toplam** | **4,0** | **4,5** | **18,5** | **7,5** | **9,0** | **11,5** | **8,5** | **10,5** | **4,0** | **78,0** |

### 3.3 Proje yönetimi
- **Yöntem:** 2 haftalık sprintler; GitHub issue ve milestone'ları ([repo](https://github.com/adecust/yildiz-teknopark-basvuru)); her issue'da kabul kriteri.
- **Yönlendirme komitesi (aylık):** Firma yönetimi + proje yöneticisi + teknik lider. Bütçe, risk ve kilometre taşı kararları.
- **Akademik değerlendirme (çeyreklik):** İki danışmanla deney sonuçlarının gözden geçirilmesi; kayıtlar teknopark raporlarına eklenir.
- **Kalite panosu (sürekli):** YZ metrikleri canlı izlenir; eşik altına düşünce uyarı verir.
- **Teknopark yükümlülükleri:** Aylık muafiyet raporu her ayın 20'sine kadar; personel giriş-çıkışları; yıllık faaliyet raporu mayıs sonuna kadar.

---

## 4. Bütçe (12 ay)

> **Tüm tutarlar [VARSAYIM]:** 2027 fiyatlarıyla, KDV hariç, TL. İK ve mali müşavirle güncellenmeli. Personel maliyetleri **işverene toplam maliyet**.

### 4.1 Personel

| Rol | Aylık işveren maliyeti (teşvik öncesi) | Tam zamanlı eşdeğer | 12 ay |
|---|---|---|---|
| Proje yöneticisi | 190.000 | 1,0 | 2.280.000 |
| Kıdemli YZ mühendisi | 230.000 | 1,0 | 2.760.000 |
| YZ mühendisi | 160.000 | 1,0 | 1.920.000 |
| Backend × 2 | 150.000 | 2,0 | 3.600.000 |
| Frontend | 140.000 | 1,0 | 1.680.000 |
| DevOps | 170.000 | 0,5 | 1.020.000 |
| **Ar-Ge personeli toplamı (teşvik öncesi)** | | | **13.260.000** |
| Stajyerler (2 × yarı zamanlı) | 20.000 | 2 × 0,5 | 480.000 |
| **Personel toplamı** | | | **13.740.000** |

**Teknopark teşvik etkisi (tahmini):** Ar-Ge personeli ücretlerinde gelir vergisi stopaj istisnası, SGK işveren hissesinin yarısının karşılanması ve damga vergisi istisnası. Bunlarla Ar-Ge personeli maliyetinde **≈ %20–28 azalma** beklenir → ≈ 2,7–3,7 milyon TL tasarruf **[TEYİT: mali müşavir hesabı; bölge dışı çalışma oranlarına bağlı]**.

### 4.2 Diğer kalemler

| Kalem | Açıklama | 12 ay |
|---|---|---|
| **GPU altyapısı** | Yurt içi bulutta 1 × 48 GB GPU (sürekli servis) ≈ 80.000/ay + deney için kısa süreli kiralık yüksek GPU | 1.360.000 |
| Uygulama bulutu | Uygulama sunucuları, veritabanı, nesne deposu, yedekleme (yurt içi) | 420.000 |
| Ticari YZ API (deney karşılaştırmaları) | E-6 için karşılaştırma ve LLM-yargıç kalibrasyonu | 480.000 |
| Kira + işletme gideri | ≈ 70 m² × ≈ 1.000 TL/m²/ay **[TEYİT: Yıldız tarifesi]** | 840.000 |
| Akademik danışmanlık (YTÜ TTO) | 2 danışman × ≈ 40.000/ay **[TEYİT: TTO tarifesi]** | 960.000 |
| Yazılım ve araç lisansları | Geliştirme araçları, tasarım, izleme | 300.000 |
| Etiketleme desteği | Eğitmenlerin test seti etiketleme ek mesaisi | 400.000 |
| Güvenlik | Bağımsız sızma testi | 250.000 |
| Hukuk ve KVKK danışmanlığı | Aydınlatma, rıza, standart sözleşme, sözleşme şablonları | 200.000 |
| Fikri mülkiyet | Patent vekili, başvuru ve tescil ücretleri | 250.000 |
| Pilot ve kullanıcı araştırması | Dış kurum pilotu, anketler, eğitim materyali | 300.000 |
| Seyahat, fuar, ihracat ön çalışması | Azerbaycan/Kazakistan temasları, EdTech etkinlikleri | 300.000 |
| **Ara toplam (diğer)** | | **6.060.000** |

### 4.3 Toplam

| | Teşvik öncesi | Teşvik sonrası (tahmini) |
|---|---|---|
| Personel | 13.740.000 | ≈ 10.400.000 |
| Diğer | 6.060.000 | 6.060.000 |
| Beklenmeyen giderler (%7) | 1.386.600 | ≈ 1.150.000 |
| **TOPLAM** | **≈ 21,2 milyon TL** | **≈ 17,6 milyon TL** |

- Firma yıllık gelirinin (≈ 240 milyon TL) **≈ %7–9'u**. **Proje öz kaynakla finanse edilebilir.** Bu, hakem ve aday komisyon için güçlü bir "gerçekleştirilebilirlik" kanıtı.
- **Kira güvence bedeli** (3 aylık, ≈ 210.000 TL) gider değildir; çıkışta iade edilir.
- **Alternatif:** GPU sunucusu satın alımı (≈ 1,5–2,5 milyon TL). 4691 kapsamında **yeni makine-teçhizat KDV istisnası** uygulanabilir (Yönerge md. 11.3); 3 yıl Ar-Ge dışında kullanılmama şartı var. 24+ aylık ufukta kiralamadan ucuz olabilir; İP-6'da karar verilir.

### 4.4 Ek finansman seçenekleri
| Program | Özet | Uygunluk |
|---|---|---|
| TÜBİTAK 1507 KOBİ Ar-Ge Başlangıç | 2026 çağrılarında proje bütçe üst sınırı 3,5 milyon TL (ikincil kaynak), destek oranı %75, süre ≤ 18 ay | **[TEYİT]** Firmanın KOBİ tanımına uyup uymadığı (çalışan sayısı ve net satış hasılatı eşikleri) ve daha önce 1501/1507 desteği alıp almadığı |
| TÜBİTAK 1501 Sanayi Ar-Ge | Daha büyük bütçeler; KOBİ'ler için daha yüksek destek oranı | KOBİ değilse veya bütçe 1507 sınırını aşıyorsa |
| KOSGEB Ar-Ge, Ür-Ge ve İnovasyon | Hibe + geri ödemeli destek | KOBİ ise **[TEYİT]** |

Bir kamu programından destek alınırsa, Yıldız yönergesine göre proje başvuru ücreti alınmayabilir ve mevzuata göre hakem değerlendirmesinden muaf tutulabilir **[TEYİT: Yıldız]**. **Faz 2 için 1501/1507 başvurusunu Faz 1 sırasında yapmak** zinciri güçlendirir.

---

## 5. Ticarileşme ve iş modeli

### 5.1 Gelir modelleri ve fiyat önerisi

> **[VARSAYIM]:** 2027 sabit fiyatları, KDV hariç. Pilot sonrası fiyat testiyle güncellenecek.

| Paket | Hedef | Fiyat | İçerik |
|---|---|---|---|
| **Eğitmen Başlangıç** (B2C) | Bireysel eğitmen / özel ders | 499 TL/ay | 1 eğitmen, ≤ 50 öğrenci, ≤ 1.000 YZ sorusu/ay, kaynağa dayalı asistan |
| **Eğitmen Pro** (B2C) | Profesyonel eğitmen | 999 TL/ay | ≤ 150 öğrenci, ödev ön-değerlendirme, canlı ders |
| **Kurum Asistan** (B2B SaaS) | Kurs, etüt, SEM | 60 TL / aktif öğrenci / ay (en az 100 öğrenci) | Platform + YZ asistanı + raporlar |
| **Kurum Tam** (B2B SaaS) | Kurs, okul, SEM | 85 TL / aktif öğrenci / ay | + rubrik tabanlı ödev değerlendirme + kalite panosu |
| **Kurum İçi Kurulum** (lisans) | Kurumsal akademi, kamu, üniversite | Yıllık 1,5–3 milyon TL + %20 bakım | Kendi sunucusunda kurulum, yerli model, SLA |
| **API** | Başka LMS'ler ve yayıncılar | 1.000 sorgu başına ücret | Kaynağa dayalı soru-cevap ve değerlendirme API'si |

**Birim ekonomisi hedefi:** Öğrenci başı YZ ve altyapı maliyeti fiyatın ≤ %20'si (AR-6 hedefi) → **brüt kâr marjı ≥ %70**.

### 5.2 Pazara giriş stratejisi
1. **Vitrin müşteri: kendi kurumumuz.** Pilot sonuçları vaka çalışması olur ("eğitmen süresinde %X kazanç").
2. **Sektör ağı:** Özel öğretim kurumu dernekleri ve sektör etkinlikleri; kurs zincirlerine doğrudan satış.
3. **Yıldız ekosistemi:** 750+ teknopark firmasının kurumsal eğitim birimleri; YTÜ SEM; YILDIZ TECH buluşmaları (eğitim teknolojileri).
4. **B2C büyüme:** Ücretsiz deneme (14 gün), içerik pazarlaması, eğitmen topluluğu, yönlendirme programı.
5. **Kanal ortakları:** Eğitim yayınevleri ve LMS entegratörleri (API paketi).
6. **İhracat:** Azerbaycan ve KKTC (2028) → Kazakistan ve Özbekistan (2028–29) → AB (2029+) (belge 01, §6.2).

### 5.3 Gelir projeksiyonu (3 yıl, temkinli senaryo)

| Yıl | Kurum (B2B) | Ort. aktif öğrenci / kurum | Ort. fiyat (TL/öğrenci/ay) | B2B gelir | B2C eğitmen | Ort. fiyat (TL/ay) | B2C gelir | Lisans + ihracat | **Toplam** |
|---|---|---|---|---|---|---|---|---|---|
| 2028 | 10 | 150 | 60 | 1,08 M | 300 | 600 | 2,16 M | — | **≈ 3,2 M TL** |
| 2029 | 40 | 200 | 65 | 6,24 M | 1.200 | 650 | 9,36 M | 1,5 M | **≈ 17,1 M TL** |
| 2030 | 120 | 250 | 70 | 25,2 M | 3.000 | 700 | 25,2 M | 4,0 M | **≈ 54,4 M TL** |

*Kurum ve eğitmen sayıları yıl ortalaması; yıl içi büyüme doğrusal varsayıldı. **[VARSAYIM]** — pilot sonrası güncellenecek.*

**Geri dönüş:** Faz 1 yatırımı (≈ 17,6 M TL) ve ardından gelen fazlar, ≥ %70 brüt marjla 2030 içinde kümülatif olarak karşılanır **[VARSAYIM]**.

### 5.4 Yıldız Teknopark'a katkı göstergeleri

| Gösterge | Şimdi | 12 ay (Faz 1 sonu) | 36 ay |
|---|---|---|---|
| Teknoparktaki Ar-Ge personeli | 0 | 7 | 15+ |
| YTÜ akademik danışman | 0 | 2 | 3+ |
| YTÜ stajyer / tez öğrencisi | 0 | 2 | 6+ |
| Destekli proje (TÜBİTAK/KOSGEB) | 0 | 1 başvuru | 2+ |
| Patent / faydalı model / tescil başvurusu | 0 | 1 | 3+ |
| Ortak akademik yayın | 0 | 1 gönderim | 3+ |
| Teknopark kaynaklı ciro | 0 | Pilot geliri | ≈ 54 M TL/yıl **[VARSAYIM]** |
| İhracat | 0 | Ön temas | 2+ ülke |
| Ödül / yarışma | — | 1 başvuru (EdTech yarışmaları) | — |

---

## 6. Kurumsal ve mali yapı

- **Şube modeli:** Mevcut şirket Yıldız Teknopark'ta şube açıyor. Teknoparkta **yalnızca yazılım ve Ar-Ge** yürütülür. Eğitim hizmeti ana merkezde kalır.
- **Kazanç ayrıştırma:** Teknopark kazanç istisnası yalnızca bölgede yürütülen yazılım ve Ar-Ge faaliyetinden doğan kazanca uygulanır. Eğitim hizmeti geliri istisna dışıdır (özelge örneği). Ayrıştırma yöntemi (şube hesapları, ana şirketin platformu kullanımına emsal bedel) **mali müşavirce kurulmalı (H-02)**.
- **Ana sözleşme:** Amaç ve konu maddesinde yazılım geliştirme ve Ar-Ge faaliyeti yer almalı (H-03, D-05).
- **Faaliyet konusu değişmez:** Yıldız yönergesine göre sözleşme süresince faaliyet konusu değiştirilemez. NACE kodları baştan doğru seçilmeli.
