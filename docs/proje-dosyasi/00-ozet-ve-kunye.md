# PROJE DOSYASI · 00 · Yönetici Özeti ve Künye

> **Belge seti:** Bu dosya, YTÜ Yıldız Teknopark başvurusunda kullanılacak proje dosyasının giriş bölümüdür. Bölümler:
>
> | # | Belge | İçerik |
> |---|---|---|
> | 00 | **Yönetici özeti ve künye** (bu belge) | Proje kimliği, özet, forma yapıştırılacak hazır metinler |
> | 01 | [Problem, pazar ve rekabet](01-problem-pazar-rekabet.md) | İhtiyaç, pazar büyüklüğü, rakip analizi, farklılaşma |
> | 02 | [Ar-Ge içeriği ve teknik tasarım](02-ar-ge-ve-teknik-tasarim.md) | Araştırma soruları, hipotezler, mimari, algoritmalar, veri modeli |
> | 03 | [Test, doğrulama ve senaryolar](03-test-dogrulama-senaryolar.md) | Ölçüm protokolü, deney tasarımı, senaryo testleri, hata türleri analizi |
> | 04 | [İş planı, ekip, bütçe ve ticarileşme](04-is-plani-ekip-butce-ticarilesme.md) | İş paketleri, kilometre taşları, ekip, bütçe, iş modeli, gelir projeksiyonu |
> | 05 | [Risk, etki, fikri mülkiyet ve hakem hazırlığı](05-risk-etki-fmh-hakem-sunum.md) | Risk yönetimi, etkiler, FMH stratejisi, hakem soru-cevap, sunum metni |
>
> **Etiketler:** **[VARSAYIM]** = firma tarafından güncellenmesi gereken tahmin. **[TEYİT]** = dış kurumdan doğrulanması gereken bilgi. **[LİTERATÜR]** = yayımlanmış çalışmadan alınan değer.
>
> **Dürüstlük notu:** Proje henüz uygulanmamıştır. Bu belgedeki tüm başarım değerleri **hedeftir**; "beklenen" değerler literatüre dayanan öngörülerdir. Hiçbir sonuç deney yapılmış gibi sunulmamıştır.

---

## 1. Proje künyesi

| Alan | Değer |
|---|---|
| **Proje adı** | Türkçe Eğitim İçeriği İçin Kaynağa Dayalı Üretken Yapay Zekâ ile Soru-Cevap ve Rubrik Tabanlı Otomatik Ödev Değerlendirme Platformu |
| **Kısa ad (çalışma adı)** | **KAYNAK-YZ** *(ürün markası ayrıca belirlenecek)* |
| **Proje türü** | Ar-Ge + Yazılım (birlikte) |
| **Başvuran** | ‹Kurum Unvanı› · eğitim hizmetleri; teknoparkta **şube** ile faaliyet |
| **Hedef bölge** | YTÜ Yıldız Teknopark (yerleşke tercihi [TEYİT]: Davutpaşa / İkitelli / Maslak / Arnavutköy) |
| **Süre** | 12 ay (tahmini başlangıç 01.04.2027) |
| **Teknoloji hazırlık seviyesi (TRL)** | Başlangıç TRL 2–3 → hedef TRL 6–7 (gerçek kullanıcılarla pilot) |
| **NACE (öneri)** | 62.01 Bilgisayar programlama faaliyetleri · 72.19 Doğa bilimleri ve mühendislikle ilgili diğer araştırma ve deneysel geliştirme faaliyetleri [TEYİT: mali müşavir] |
| **Anahtar kelimeler (hakem eşleşmesi için)** | Kaynağa dayalı üretim (RAG) · Türkçe doğal dil işleme · büyük dil modelleri · otomatik ödev değerlendirme · halüsinasyon tespiti · öğrenme yönetim sistemi · eğitim teknolojileri · bilgi erişimi |
| **Ar-Ge kategorileri** | (b) yenilik unsuru içeren yazılım geliştirme · (d) kavram geliştirme · (f) teknik yapılabilirlik etüdü · (h) prototip geliştirme · (e) patent çalışmaları |
| **Tahmini proje bütçesi** | ≈ 17,6 milyon TL teşvik sonrası (teşvik öncesi ≈ 21,2 milyon TL); 12 ay; bkz. belge 04 **[VARSAYIM]** |
| **Finansman** | Öz kaynak (firma yıllık geliri ≈ 240 milyon TL) + TÜBİTAK 1507/1501 başvurusu planlanıyor |
| **Planlanan Ar-Ge personeli (teknopark)** | 7 kişi (6,5 tam zamanlı eşdeğer) + 2 YTÜ akademik danışman + 2 YTÜ stajyer |
| **Faz zinciri** | Faz 1 (bu proje) → Faz 2: avatarlı sanal sınıf + sınıf içi YZ asistanı → Faz 3 (aday): uyarlanabilir öğrenme ve öğrenci modelleme |

---

## 2. Yönetici özeti (1 sayfa)

**Başvuran kurum.** Kurumumuzun asıl faaliyet alanı eğitimdir. Yapay zekâ, eğitmenin yerini almak için değil; eğitim hizmetimizi güçlendirmek, eğitmenin öğrenciye ayırdığı zamanı artırmak ve öğrenciye ders dışında güvenilir destek sağlamak için geliştirilmektedir. Sistemin ilk kullanıcısı kurumumuz olacak; gerçek ortamda doğrulandıktan sonra aynı ihtiyacı yaşayan kurumlara sunulacaktır. Teknopark şubesinde yalnızca Ar-Ge ve yazılım faaliyeti yürütülecek, eğitim hizmeti kurum merkezinde sürdürülecektir.

**Problem.** Türkiye'de kurs, dershane-etüt merkezi, özel okul, üniversite sürekli eğitim merkezi ve kurumsal akademi gibi binlerce eğitim kurumu dijital derslerini dağınık araçlarla (video konferans + dosya paylaşımı + mesajlaşma) yürütüyor. Öğrenciler dersten sonra sorularına anında, **o dersin kendi içeriğine uygun** cevap bulamıyor. Eğitmenler ise zamanlarının önemli kısmını tekrar eden soruları yanıtlamaya ve ödev okumaya harcıyor. Genel amaçlı yapay zekâ sohbet araçları bu boşluğu dolduramıyor: **dersin kaynağına bağlı kalmıyor, uydurabiliyor (halüsinasyon), ödevin cevabını doğrudan verip öğrenmeyi baltalayabiliyor** ve verileri yurt dışında işliyor.

**Çözüm.** Eğitmenin yüklediği ders kaynaklarına (ders notu, PDF, slayt, ders videosu transkripti) **kilitlenen**, Türkçe için optimize edilmiş bir eğitim YZ'si. Bu YZ üç şey yapıyor:
1. Öğrencinin sorusunu **yalnızca o dersin kaynaklarından**, sayfa veya dakika atfıyla yanıtlıyor; kaynakta yoksa uydurmak yerine "bu ders kaynaklarında yok" diyor.
2. Ödev sorularında cevabı vermek yerine **ipucu merdiveniyle** öğrenciyi yönlendiriyor.
3. Eğitmenin **rubriğine göre** ödevleri ön-değerlendiriyor, kanıtlı ve gerekçeli geri bildirim üretiyor. Son karar her zaman eğitmende.

Bu YZ, kayıt, ders alanı, canlı ders, ödev teslimi ve takvim işlevlerini içeren bir eğitim platformunun içinde çalışıyor. Platform aynı zamanda YZ'nin gerçek kullanıcılarla test edileceği zemin.

**Ar-Ge içeriği.** Projenin teknik belirsizlikleri:
- **AR-1:** Türkçe içerikte kaynağa sadakat ve doğru reddetme
- **AR-2:** Sondan eklemeli Türkçe için hibrit bilgi erişimi
- **AR-3:** Rubrik tabanlı puanlamada eğitmenle uyum. Literatürde YZ-insan uyumu ağırlıklı Kappa ile **0,4–0,7** bandında; hedef **≥ 0,75**
- **AR-4:** Pedagojik cevap sızıntısının önlenmesi
- **AR-5:** Çok kipli içerik (PDF, slayt, görsel, ders videosu) işleme
- **AR-6:** Yurt içinde barındırılan açık ağırlıklı Türkçe modellerle düşük maliyetli ve veri egemenliği korunarak çalışma

Her biri ölçülebilir hedef ve deney protokolüyle tanımlandı (belge 02 ve 03).

**Neden biz?**
- Aylık 200–300 aktif öğrencisi olan, yıllık ≈ 240 milyon TL gelirli bir eğitim kurumuyuz. **Gerçek kullanıcı, gerçek içerik ve gerçek eğitmen puanı** verisine ilk günden sahibiz.
- Şirket içinde yazılım ekibimiz var; YZ/dil işleme uzmanlığı işe alım ve YTÜ akademik iş birliğiyle güçlendiriliyor.
- Hedef akademik ortaklık: YTÜ Bilgisayar Mühendisliği'nde Prof. Dr. Mehmet Fatih Amasyalı liderliğindeki COSMOS YZ Araştırma Grubu (Cosmos T1 ve turkish-e5-large modellerini geliştiren ekip; prototipimizde bu modeller kullanılıyor) ve YTÜ Eğitim Fakültesi'nde ölçme-değerlendirme veya öğretim teknolojileri alanında bir öğretim üyesi **[TEYİT: Yıldız TTO üzerinden görüşme yapılacak; henüz temas kurulmadı]**.

**Ticarileşme.** Ürün, kurumlara öğrenci başı aylık abonelikle (SaaS), bireysel eğitmenlere aylık planla satılacak. Kurumlara isterlerse kendi sunucularında çalışan lisans seçeneği sunulacak.
- **Pazar:** Türkiye eğitim teknolojileri pazarı 2024'te ≈ 2,2 milyar $ olarak tahmin ediliyor ve 2033'e kadar 6 milyar $'ı aşması bekleniyor **[LİTERATÜR: IMARC, Ekonomist]**.
- **İthal ikame ve ihracat:** Yurt dışı LMS, video konferans ve YZ aboneliklerinin (Canvas, Zoom, ChatGPT Edu, Google Workspace eklentileri) yerini alması hedefleniyor. İhracat önce Türk dilli ülkelere (Azerbaycan, Kazakistan, Özbekistan) yapılacak; AB pazarına AB YZ Yasası'na uyumlu tasarımla girilecek.

**Yıldız Teknopark'a katkı (36 ay):** 15+ Ar-Ge personeli, 2+ fikri mülkiyet başvurusu, 2+ destekli proje, YTÜ ile ortak yayın, stajyer istihdamı ve ihracat geliri. Bu metriklerin hepsi Bakanlık TGB performans endeksinde sayılıyor.

---

## 3. Forma yapıştırılacak hazır metinler

### 3.1 "Proje Adı"
```
Türkçe Eğitim İçeriği İçin Kaynağa Dayalı Üretken Yapay Zekâ ile Soru-Cevap ve Rubrik Tabanlı Otomatik Ödev Değerlendirme Platformu
```

### 3.2 "Faaliyet Alanınız" (çoklu seçim)
☑ Yapay Zeka · ☑ Yazılım Geliştirme · ☑ SaaS / Bulut Tabanlı Çözümler · ☑ EdTech · ☑ Veri / Analitik

### 3.3 "Geliştirdiğiniz ürünü/projeyi özetleyiniz" (≥1200 karakter; aşağıdaki metin 2.092 karakter)
```
Kurumumuz bir eğitim kurumudur ve bu proje, eğitim hizmetimizi güçlendirmek amacıyla geliştirilmektedir. Projemiz, eğitmenin yüklediği ders kaynaklarına (ders notu, PDF, slayt, ders videosu transkripti) kilitlenen, Türkçe için optimize edilmiş bir eğitim yapay zekâsı ve bu yapay zekânın çalıştığı bir eğitim platformu geliştirmeyi amaçlamaktadır. Genel amaçlı sohbet botları ders kaynağına bağlı kalmadığı için bilgi uydurabilmekte (halüsinasyon), ödevin cevabını doğrudan vererek öğrenmeyi zayıflatabilmekte ve öğrenci verisini yurt dışında işlemektedir. Geliştireceğimiz sistem öğrencinin sorusunu yalnızca ilgili dersin kaynaklarından, sayfa/dakika atfı vererek yanıtlayacak; kaynakta bulunmayan sorularda uydurmak yerine bunu açıkça belirtecek; ödev sorularında cevabı vermek yerine kademeli ipuçlarıyla öğrenciyi yönlendirecek ve eğitmenin rubriğine göre ödevleri ön-değerlendirerek kanıtlı, gerekçeli geri bildirim üretecektir; nihai not kararı eğitmende kalacaktır.

Projenin Ar-Ge çekirdeği altı teknik belirsizliğe dayanır: (1) Türkçe içerikte kaynağa sadakat ve doğru reddetme (hedef sadakat ≥%95, red doğruluğu ≥%90), (2) sondan eklemeli Türkçe için hibrit bilgi erişimi (Recall@5 ≥%90), (3) rubrik tabanlı puanlamada eğitmenle uyum (literatürde 0,4–0,7 olan ağırlıklı Kappa değerinin ≥0,75'e çıkarılması), (4) ödev cevabı sızıntısının ≤%2'ye indirilmesi, (5) PDF, slayt, görsel ve ders videosundan çok kipli bilgi tabanı oluşturma, (6) yurt içinde barındırılan açık ağırlıklı Türkçe dil modelleriyle düşük maliyetli ve KVKK uyumlu çalışma.

Sistem, kendi kurumumuzdaki aylık 200–300 öğrenci ve eğitmenlerle gerçek ortamda pilot edilecek, ardından en az bir dış kurumda doğrulanacaktır. Ürün kurumlara öğrenci başı abonelik (SaaS), bireysel eğitmenlere aylık plan ve kurum içi kurulum lisansı olarak ticarileştirilecek; yurt dışı LMS ve yapay zekâ aboneliklerine yerli bir alternatif sunarken Türk dilli ülkelere ihracat hedeflenmektedir. Projede YTÜ Bilgisayar Mühendisliği (Türkçe dil modelleri) ve Eğitim Fakültesi (ölçme-değerlendirme) ile akademik iş birliği planlanmaktadır.
```

### 3.4 "Ürün/proje hangi aşamadadır?"
- **"Prototip"**. Kavram kanıtı Kasım 2026'da tamamlandı ve gerçek ders içeriğiyle ölçüldü (docs/07; kod `prototip/`). Platformun kendisi henüz geliştirilmediği için "Beta" veya üstü seçilmemelidir; gerçeğe aykırı beyan başvurunun yok sayılmasına yol açar (Yönerge md. 10.1).

### 3.5 Akademik iş birliği soruları
| Soru | Cevap |
|---|---|
| Somut akademik iş birliği var mı? | Niyet mektubu alındıysa **Evet**, alınmadıysa **Hayır** |
| Evet ise detay | "YTÜ Bilgisayar Mühendisliği [Öğretim üyesi adı] – Türkçe büyük dil modelleri ve bilgi erişimi danışmanlığı; YTÜ Eğitim Fakültesi [Öğretim üyesi adı] – rubrik geçerliliği ve ölçme-değerlendirme" |
| Akademisyen danışmanlığı planlanıyor mu? | **Evet** |
| Hangi alanlarda? | "Türkçe doğal dil işleme ve büyük dil modelleri; bilgi erişimi ve değerlendirme metrikleri; ölçme-değerlendirme ve rubrik geçerliliği; deney tasarımı ve istatistiksel analiz" |

### 3.6 Diğer alanlar
| Soru | Cevap |
|---|---|
| Ulusal / uluslararası proje desteği aldınız mı? | Hayır *(TÜBİTAK 1507/1501 başvurusu planlanıyor; varsa yazın)* |
| Yatırım aldınız mı? | Hayır *(öz kaynakla finanse edilecek)* |
| İş ve gelir modeli | ☑ Abonelik (SaaS) · ☑ Lisans satışı · ☑ Veri/analitik/API kullanımı · ☑ Bakım ve destek hizmeti |
| Fatura kesilen müşteri sayısı (geçen yıl) | **[Gerçek değer: muhasebeden]**. Eğitim hizmeti verilen bireysel müşteri sayısı yüksek olacağı için güçlü bir ticari kanıt. |
| Yurt dışı ofis var mı? | Hayır |
| Yurt dışı ofis planı | **Evet**: Azerbaycan (Bakü) ve Kazakistan (Almatı) öncelikli; AB pazarı için Almanya (2029+) |
| Firmanın toplam çalışan sayısı | [Gerçek değer] |
| Teknoparkta çalışacak personel | 7 (Faz 1) |
| Tercih edilen yerleşke | **[TEYİT: ön görüşmede boş alana göre]** |
| Ofis türü / m² | Kapalı ofis, ≈ 60–80 m² **[VARSAYIM: Yıldız'ın kişi başı m² oranına göre]** |

### 3.7 Zorunlu evrak kontrol listesi
- [ ] Vergi levhası (PDF, metni seçilebilir)
- [ ] Ticaret Sicil Gazetesi (kuruluş + son değişiklikler)
- [ ] Son 3 yıl gelir tablosu ve bilanço (kurumlar vergisi beyannamesi)
- [ ] Borç yoktur yazısı: vergi dairesi (güncel)
- [ ] Borç yoktur yazısı: SGK (güncel)
- [ ] Firma / proje sunumu (`teslim/KAYNAK-YZ_Firma_Proje_Sunumu.pdf`, 20 slayt)
- [ ] Sertifika ve lisanslar (varsa: ISO, MEB kurum izinleri, ödüller)
- [ ] **Tüm PDF'ler OCR'lı.** Taranmış görüntü PDF kabul edilmiyor.

---

## 4. Faz yol haritası (bütün resim)

```
2026-Ara        2027-Nis                         2028-Mar   2028-Nis                        2029-Mar
   │ Başvuru       │◄──────── FAZ 1 (12 ay) ────────►│◄──────── FAZ 2 (12 ay) ──────────►│
   │               │ Platform + Kaynağa Dayalı YZ     │ Sanal sınıf + sınıf içi YZ ajanı  │
   │               │ AR-1…AR-6                        │ 3B/2,5B web, mekânsal ses,        │
   │               │ Pilot: kendi kurum + 1 dış kurum │ bağlam farkındalıklı YZ asistanı  │
   │               │                   ▲ Ay 10: Faz 2 başvurusu (≤31.01.2028)             │
   │                                                                  ▲ Faz 3 başvurusu  │
   │                                                                    (uyarlanabilir öğrenme)
```

Her faz, Yıldız Teknopark kurallarına uygun olarak ayrı bir TGB projesi: en fazla 12 ay, sonraki başvuru bitişten en az 60 gün önce, projesiz kalınan süre 90 günü geçmeyecek.
