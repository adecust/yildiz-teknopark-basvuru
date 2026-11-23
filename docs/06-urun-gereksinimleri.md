# Ürün Gereksinimleri Belgesi

> Bu belge `plan/backlog.json` dosyasından üretilir. Fonksiyonel gereksinim numaraları kullanıcı hikâyesi numarasından türetilir (ör. US-101 → FR-101.1).

**Ürün:** KAYNAK-YZ: Türkçe Eğitim İçeriği İçin Kaynağa Dayalı Üretken Yapay Zekâ ile Soru-Cevap ve Rubrik Tabanlı Otomatik Ödev Değerlendirme Platformu

**Amaç:** Başvuran kurumun asıl faaliyet alanı eğitimdir. Yapay zekâ, kurumun eğitim hizmetini güçlendirmek amacıyla geliştirilmektedir; ilk kullanıcı kurumun kendisidir.

## 1. Personalar

| Persona | Tanım |
|---|---|
| Öğrenci | Kurumda kayıtlı, derslere katılan, ödev teslim eden ve ders dışında soru soran kullanıcı. |
| Eğitmen | Ders açan, kaynak yükleyen, canlı ders yürüten, ödev veren ve değerlendiren kullanıcı. |
| Kurum yöneticisi | Kurumun kullanıcılarını, derslerini, ayarlarını ve raporlarını yöneten kullanıcı. |
| Bireysel eğitmen | Bir kuruma bağlı olmadan kendi kendine kayıt olan, abonelikle kendi derslerini yürüten kullanıcı. |
| Sistem yöneticisi | Platformu işleten, kurum oluşturan ve altyapıyı yöneten kurum içi teknik personel. |

## 2. Fonksiyonel olmayan gereksinimler

| No | Alan | Gereksinim |
|---|---|---|
| NFR-01 | Güvenlik | Tüm trafik TLS 1.3 ile şifrelenir; durağan veri AES-256 ile şifrelenir; OWASP ASVS Seviye 2 karşılanır. |
| NFR-02 | Kurum ayrımı | Bir kurumun verisi başka bir kurumdan hiçbir koşulda okunamaz (veritabanında satır düzeyi güvenlik). |
| NFR-03 | KVKK | Kişisel veriler yurt içinde işlenir; açık rıza ve aydınlatma kayıt altındadır; 18 yaş altı için veli onayı alınır; silme talebi 30 gün içinde yerine getirilir. |
| NFR-04 | Performans (platform) | Sayfa yanıt süresi p95 ≤ 1 sn; 300 eşzamanlı kullanıcıda hata oranı < %1. |
| NFR-05 | Performans (YZ) | Asistan yanıtı p50 ≤ 3 sn, p95 ≤ 6 sn. |
| NFR-06 | Erişilebilirlik | WCAG 2.2 AA; klavye ile tam kullanım; ekran okuyucu uyumu. |
| NFR-07 | Kullanılabilirlik | Mobil tarayıcıda tüm öğrenci akışları çalışır; Türkçe arayüz, ileride çok dilli yapıya uygun (i18n). |
| NFR-08 | Erişilebilirlik süresi | Aylık hizmet erişilebilirliği ≥ %99,5 (planlı bakım hariç). |
| NFR-09 | İzlenebilirlik | Her YZ kararı (yanıt, ret, puan önerisi) girdi, kanıt ve model sürümüyle kaydedilir (AB YZ Yasası). |
| NFR-10 | İnsan gözetimi | YZ puan önerileri eğitmen onayı olmadan öğrenciye not olarak yansımaz. |
| NFR-11 | Yedekleme | Günlük yedek; kurtarma noktası hedefi ≤ 24 saat, kurtarma süresi hedefi ≤ 4 saat. |
| NFR-12 | Lisans | Kurum içi kurulum paketinde GPL/AGPL lisanslı bileşen dağıtılmaz. |

## 3. Epik bazında fonksiyonel gereksinimler ve kabul kriterleri

### EP-01 · Kimlik doğrulama ve hesap yönetimi

_Kullanıcıların güvenli biçimde giriş yapması, hesap oluşturması ve rollerine göre yetkilendirilmesi._

#### US-101 · Giriş ekranı: e-posta ve şifreyle giriş

Tür: Kullanıcı hikâyesi · Öncelik: Olmazsa olmaz · Puan: 5 · Planlanan: Sprint 02

Bir **öğrenci** olarak, **e-posta adresim ve şifremle platforma giriş yapmak** istiyorum; böylece derslerime ve ödevlerime güvenli biçimde erişebileyim.

**Fonksiyonel gereksinimler**

- FR-101.1: E-posta ve şifre alanları, 'Beni hatırla' seçeneği ve 'Şifremi unuttum' bağlantısı bulunur.
- FR-101.2: Hatalı girişte hangi alanın yanlış olduğu belirtilmeden genel bir hata mesajı gösterilir.
- FR-101.3: Art arda 5 hatalı denemeden sonra hesap 15 dakika kilitlenir.
- FR-101.4: Başarılı girişte kullanıcı rolüne göre ilgili panoya yönlendirilir.
- FR-101.5: Oturum 8 saat hareketsizlikten sonra sona erer.

**Kabul kriterleri**

- **Verilen** kayıtlı ve aktif bir öğrenci, **olduğunda** doğru e-posta ve şifreyle giriş yaptığında, **o zaman** öğrenci panosuna yönlendirilir.
- **Verilen** kayıtlı bir kullanıcı, **olduğunda** yanlış şifre girdiğinde, **o zaman** 'E-posta veya şifre hatalı' mesajı görür ve hangi alanın hatalı olduğu belirtilmez.
- **Verilen** art arda 5 hatalı deneme yapan bir kullanıcı, **olduğunda** 6. kez denediğinde, **o zaman** hesabın 15 dakika kilitlendiği bildirilir.

#### US-102 · Davet bağlantısıyla hesap oluşturma

Tür: Kullanıcı hikâyesi · Öncelik: Olmazsa olmaz · Puan: 5 · Planlanan: Sprint 02 – Sprint 03

Bir **öğrenci** olarak, **kurumumdan gelen davet bağlantısıyla hesabımı oluşturmak** istiyorum; böylece ayrıca bir kayıt işlemiyle uğraşmadan derse başlayabileyim.

**Fonksiyonel gereksinimler**

- FR-102.1: Davet bağlantısı tek kullanımlıktır ve 7 gün geçerlidir.
- FR-102.2: Kullanıcı ad, soyad ve şifre belirler; şifre en az 10 karakterdir.
- FR-102.3: Aydınlatma metni gösterilir ve açık rıza onayı alınır; 18 yaş altı için veli onayı adımı vardır.
- FR-102.4: Hesap oluşturulunca kullanıcı davet edildiği kuruma ve derse otomatik eklenir.

**Kabul kriterleri**

- **Verilen** geçerli bir davet bağlantısı, **olduğunda** öğrenci formu doldurup onayladığında, **o zaman** hesabı oluşturulur ve davet edildiği derse eklenir.
- **Verilen** süresi geçmiş bir davet bağlantısı, **olduğunda** açıldığında, **o zaman** bağlantının geçersiz olduğu ve kurumla iletişime geçilmesi gerektiği bildirilir.

#### US-103 · Şifremi unuttum ve şifre sıfırlama

Tür: Kullanıcı hikâyesi · Öncelik: Olmazsa olmaz · Puan: 3 · Planlanan: Sprint 03

Bir **kullanıcı** olarak, **şifremi unuttuğumda e-postama gelen bağlantıyla yeni şifre belirlemek** istiyorum; böylece destek talebi açmadan hesabıma yeniden erişebileyim.

**Fonksiyonel gereksinimler**

- FR-103.1: Sıfırlama bağlantısı 30 dakika geçerlidir ve tek kullanımlıktır.
- FR-103.2: Kayıtlı olmayan e-posta adresi için de aynı onay mesajı gösterilir (hesap varlığı ifşa edilmez).
- FR-103.3: Şifre değişince açık oturumlar sonlandırılır.

**Kabul kriterleri**

- **Verilen** kayıtlı bir kullanıcı, **olduğunda** sıfırlama bağlantısıyla yeni şifre belirlediğinde, **o zaman** yeni şifreyle giriş yapabilir ve diğer oturumları kapanır.
- **Verilen** kayıtlı olmayan bir e-posta, **olduğunda** sıfırlama istendiğinde, **o zaman** kayıtlı kullanıcıdakiyle aynı onay mesajı gösterilir.

#### US-104 · Rol tabanlı yetkilendirme

Tür: Kullanıcı hikâyesi · Öncelik: Olmazsa olmaz · Puan: 8 · Planlanan: Sprint 01 – Sprint 02

Bir **kurum yöneticisi** olarak, **kullanıcıların yalnızca rollerine uygun ekranları ve işlemleri görmesini** istiyorum; böylece verilerin yetkisiz kişilerce değiştirilmesini önleyebileyim.

**Fonksiyonel gereksinimler**

- FR-104.1: Roller: öğrenci, eğitmen, asistan eğitmen, kurum yöneticisi, bireysel eğitmen, sistem yöneticisi.
- FR-104.2: Yetki kontrolü hem arayüzde hem API katmanında yapılır.
- FR-104.3: Yetkisiz istekler 403 yanıtı alır ve denetim kaydına yazılır.

**Kabul kriterleri**

- **Verilen** öğrenci rolündeki bir kullanıcı, **olduğunda** eğitmen ekranına doğrudan bağlantıyla gitmek istediğinde, **o zaman** erişim engellenir ve deneme kayıt altına alınır.

#### US-105 · Kurumsal tek oturum açma (SSO)

Tür: Kullanıcı hikâyesi · Öncelik: Olmalı · Puan: 8 · Planlanan: Sprint 09

Bir **kurum yöneticisi** olarak, **çalışanlarımızın kurum hesabıyla (OIDC/SAML) giriş yapmasını** istiyorum; böylece ayrı şifre yönetimi gerekmesin.

**Fonksiyonel gereksinimler**

- FR-105.1: Kurum bazında OIDC veya SAML kimlik sağlayıcısı tanımlanabilir.
- FR-105.2: İlk girişte kullanıcı otomatik oluşturulur ve varsayılan role atanır.

**Kabul kriterleri**

- **Verilen** SSO tanımlı bir kurum, **olduğunda** çalışan kurum hesabıyla giriş yaptığında, **o zaman** platformda oturum açılır ve kullanıcı kurumuna bağlanır.

#### US-106 · Profil ve kişisel veri tercihleri

Tür: Kullanıcı hikâyesi · Öncelik: Olmazsa olmaz · Puan: 5 · Planlanan: Sprint 05

Bir **öğrenci** olarak, **profil bilgilerimi, rızalarımı ve kişisel verilerimi yönetmek** istiyorum; böylece KVKK kapsamındaki haklarımı kullanabileyim.

**Fonksiyonel gereksinimler**

- FR-106.1: Kullanıcı ad, iletişim ve bildirim tercihlerini güncelleyebilir.
- FR-106.2: Verdiği rızaları ve tarihlerini görebilir, isteğe bağlı rızaları geri çekebilir.
- FR-106.3: Kişisel verilerinin dökümünü indirebilir ve silme talebi oluşturabilir.

**Kabul kriterleri**

- **Verilen** oturum açmış bir öğrenci, **olduğunda** veri dökümü istediğinde, **o zaman** verileri makine tarafından okunabilir biçimde indirilebilir.

#### US-107 · İki aşamalı doğrulama

Tür: Kullanıcı hikâyesi · Öncelik: Olabilir · Puan: 5 · Planlanan: Sprint 10

Bir **eğitmen** olarak, **hesabımı ikinci bir doğrulama adımıyla korumak** istiyorum; böylece öğrenci notlarına yetkisiz erişim engellensin.

**Fonksiyonel gereksinimler**

- FR-107.1: Kimlik doğrulayıcı uygulamayla zamana dayalı tek kullanımlık kod (TOTP) desteklenir.
- FR-107.2: Kurum yöneticisi eğitmen ve yöneticiler için zorunlu kılabilir.

**Kabul kriterleri**

- **Verilen** iki aşamalı doğrulaması açık bir eğitmen, **olduğunda** şifresini doğru girdiğinde, **o zaman** doğrulama kodu istenir ve kod olmadan giriş yapılamaz.

### EP-02 · Kurum ve kullanıcı yönetimi

_Kurumların ayrı alanlarda yönetilmesi ve kullanıcıların toplu olarak eklenip yönetilmesi._

#### US-201 · Kurum oluşturma ve kurum ayarları

Tür: Kullanıcı hikâyesi · Öncelik: Olmazsa olmaz · Puan: 5 · Planlanan: Sprint 02

Bir **sistem yöneticisi** olarak, **yeni bir kurum oluşturup temel ayarlarını yapmak** istiyorum; böylece kurum kendi alanında hemen çalışmaya başlayabilsin.

**Fonksiyonel gereksinimler**

- FR-201.1: Kurum adı, logo, iletişim, veri saklama süresi ve varsayılan pedagojik mod ayarlanabilir.
- FR-201.2: İlk kurum yöneticisine davet gönderilir.

**Kabul kriterleri**

- **Verilen** sistem yöneticisi, **olduğunda** kurum bilgilerini girip kaydettiğinde, **o zaman** kurum oluşturulur ve kurum yöneticisine davet e-postası gider.

#### US-202 · Toplu kullanıcı içe aktarma (CSV)

Tür: Kullanıcı hikâyesi · Öncelik: Olmalı · Puan: 5 · Planlanan: Sprint 04

Bir **kurum yöneticisi** olarak, **öğrenci ve eğitmen listesini dosyayla toplu olarak eklemek** istiyorum; böylece yüzlerce kullanıcıyı tek tek tanımlamak zorunda kalmayayım.

**Fonksiyonel gereksinimler**

- FR-202.1: Şablon CSV dosyası indirilebilir.
- FR-202.2: Yükleme öncesi önizleme ve satır bazında hata raporu gösterilir.
- FR-202.3: Geçerli satırlar için davet e-postaları gönderilir.

**Kabul kriterleri**

- **Verilen** hatalı satırlar içeren bir CSV dosyası, **olduğunda** yüklendiğinde, **o zaman** geçerli satırlar aktarılır, hatalı satırlar nedeniyle birlikte listelenir.

#### US-203 · Kullanıcı listesi, rol atama ve hesap pasifleştirme

Tür: Kullanıcı hikâyesi · Öncelik: Olmazsa olmaz · Puan: 5 · Planlanan: Sprint 03

Bir **kurum yöneticisi** olarak, **kullanıcıları listeleyip rollerini değiştirmek ve ayrılanları pasifleştirmek** istiyorum; böylece kurumumun kullanıcı yapısı güncel kalsın.

**Fonksiyonel gereksinimler**

- FR-203.1: Ad, rol ve duruma göre arama ve filtreleme yapılır.
- FR-203.2: Pasifleştirilen kullanıcı giriş yapamaz; verileri saklama süresince korunur.

**Kabul kriterleri**

- **Verilen** pasifleştirilmiş bir kullanıcı, **olduğunda** giriş yapmaya çalıştığında, **o zaman** hesabın pasif olduğu bildirilir.

#### US-204 · Kurumlar arası veri yalıtımı

Tür: Kullanıcı hikâyesi · Öncelik: Olmazsa olmaz · Puan: 8 · Planlanan: Sprint 01 – Sprint 02

Bir **kurum yöneticisi** olarak, **kurumumun verilerinin başka hiçbir kurum tarafından görülemeyeceğinden emin olmak** istiyorum; böylece KVKK ve sözleşme yükümlülüklerimizi karşılayalım.

**Fonksiyonel gereksinimler**

- FR-204.1: Tüm tablolarda kurum kimliği bulunur ve satır düzeyi güvenlik etkindir.
- FR-204.2: Kurumlar arası erişim denemeleri otomatik testlerle her sürümde doğrulanır.

**Kabul kriterleri**

- **Verilen** A kurumunun bir kullanıcısı, **olduğunda** B kurumuna ait bir dersin kimliğiyle istek gönderdiğinde, **o zaman** veri dönmez, 403 yanıtı alınır ve deneme denetim kaydına yazılır.

### EP-03 · Ders yönetimi

_Eğitmenlerin ders açması ve öğrencilerin derslere katılıp derslerini tek yerden izlemesi._

#### US-301 · Ders oluşturma

Tür: Kullanıcı hikâyesi · Öncelik: Olmazsa olmaz · Puan: 5 · Planlanan: Sprint 03

Bir **eğitmen** olarak, **ders adı, dönemi ve haftalık yapısıyla yeni bir ders açmak** istiyorum; böylece ders materyallerimi ve öğrencilerimi tek yerde yönetebileyim.

**Fonksiyonel gereksinimler**

- FR-301.1: Ders adı, açıklama, dönem, başlangıç-bitiş tarihi ve hafta sayısı girilir.
- FR-301.2: Ders için davet kodu ve bağlantısı otomatik üretilir.

**Kabul kriterleri**

- **Verilen** eğitmen rolündeki bir kullanıcı, **olduğunda** ders bilgilerini girip kaydettiğinde, **o zaman** ders oluşturulur ve davet kodu gösterilir.

#### US-302 · Derse davet koduyla katılma

Tür: Kullanıcı hikâyesi · Öncelik: Olmazsa olmaz · Puan: 3 · Planlanan: Sprint 04

Bir **öğrenci** olarak, **eğitmenimin paylaştığı kodla derse katılmak** istiyorum; böylece ders içeriğine hemen erişebileyim.

**Fonksiyonel gereksinimler**

- FR-302.1: Kod büyük-küçük harf duyarsızdır.
- FR-302.2: Eğitmen isterse katılımı onaya bağlayabilir.

**Kabul kriterleri**

- **Verilen** geçerli bir ders kodu, **olduğunda** öğrenci kodu girdiğinde, **o zaman** derse eklenir ve ders panosunda görünür.

#### US-303 · Öğrenci panosu

Tür: Kullanıcı hikâyesi · Öncelik: Olmazsa olmaz · Puan: 5 · Planlanan: Sprint 05

Bir **öğrenci** olarak, **kayıtlı derslerimi, yaklaşan canlı dersleri ve ödev tarihlerini tek ekranda görmek** istiyorum; böylece hiçbir şeyi kaçırmayayım.

**Fonksiyonel gereksinimler**

- FR-303.1: Ders kartları, yaklaşan 7 günün etkinlikleri ve teslim edilmemiş ödevler gösterilir.
- FR-303.2: Mobil tarayıcıda tam çalışır.

**Kabul kriterleri**

- **Verilen** iki derse kayıtlı bir öğrenci, **olduğunda** panosunu açtığında, **o zaman** iki ders ve yaklaşan etkinlikleri tarih sırasıyla görür.

#### US-304 · Ders duyuruları

Tür: Kullanıcı hikâyesi · Öncelik: Olmalı · Puan: 3 · Planlanan: Sprint 06

Bir **eğitmen** olarak, **dersteki tüm öğrencilere duyuru yayımlamak** istiyorum; böylece önemli bilgileri tek seferde iletebileyim.

**Fonksiyonel gereksinimler**

- FR-304.1: Duyuru metni ve isteğe bağlı ek dosya desteklenir.
- FR-304.2: Öğrencilere uygulama içi ve e-posta bildirimi gider.

**Kabul kriterleri**

- **Verilen** bir dersin eğitmeni, **olduğunda** duyuru yayımladığında, **o zaman** dersteki tüm öğrenciler bildirim alır.

### EP-04 · Ders kaynakları

_Ders notu, sunum ve kayıtların yüklenmesi, sürümlenmesi ve öğrenciye sunulması._

#### US-401 · Ders kaynağı yükleme

Tür: Kullanıcı hikâyesi · Öncelik: Olmazsa olmaz · Puan: 8 · Planlanan: Sprint 04 – Sprint 05

Bir **eğitmen** olarak, **ders notu, sunum, görsel ve video kaynaklarımı yüklemek** istiyorum; böylece öğrencilerim ve YZ asistanı bu kaynakları kullanabilsin.

**Fonksiyonel gereksinimler**

- FR-401.1: PDF, DOCX, PPTX, PNG/JPG ve MP4 biçimleri desteklenir; dosya başına üst sınır 500 MB'dir.
- FR-401.2: Kaynak bir haftaya veya konuya atanabilir.
- FR-401.3: Yüklenen kaynak otomatik olarak içerik işleme hattına gönderilir.

**Kabul kriterleri**

- **Verilen** bir dersin eğitmeni, **olduğunda** PDF dosyası yüklediğinde, **o zaman** kaynak listeye eklenir ve işleme durumu 'işleniyor' olarak görünür.

#### US-402 · Kaynak sürümleme ve yayın durumu

Tür: Kullanıcı hikâyesi · Öncelik: Olmazsa olmaz · Puan: 5 · Planlanan: Sprint 05

Bir **eğitmen** olarak, **kaynağımı güncellediğimde eski sürümün arşivlenmesini ve taslakları gizlemeyi** istiyorum; böylece öğrenciler ve YZ yalnızca güncel ve yayımlanmış içeriği görsün.

**Fonksiyonel gereksinimler**

- FR-402.1: Kaynaklar taslak veya yayında durumundadır.
- FR-402.2: Yeni sürüm yüklenince eski sürüm arşivlenir ve YZ önbelleği geçersiz kılınır.

**Kabul kriterleri**

- **Verilen** yayında bir kaynak, **olduğunda** eğitmen yeni sürüm yüklediğinde, **o zaman** YZ yanıtları yalnızca yeni sürüme dayanır.

#### US-403 · Kaynak görüntüleyici

Tür: Kullanıcı hikâyesi · Öncelik: Olmazsa olmaz · Puan: 5 · Planlanan: Sprint 06

Bir **öğrenci** olarak, **ders kaynaklarını platform içinde açıp belirli bir sayfaya veya video dakikasına gitmek** istiyorum; böylece YZ'nin verdiği atıfları doğrudan kontrol edebileyim.

**Fonksiyonel gereksinimler**

- FR-403.1: PDF görüntüleyici sayfa bağlantısını, video oynatıcı zaman damgasını destekler.
- FR-403.2: Bağlantı paylaşıldığında aynı konum açılır.

**Kabul kriterleri**

- **Verilen** 's. 12' atıflı bir bağlantı, **olduğunda** öğrenci tıkladığında, **o zaman** PDF 12. sayfada açılır.

### EP-05 · Canlı ders

_Yurt içinde barındırılan canlı ders altyapısının platforma entegrasyonu._

#### US-501 · Canlı ders planlama ve başlatma

Tür: Kullanıcı hikâyesi · Öncelik: Olmazsa olmaz · Puan: 8 · Planlanan: Sprint 06 – Sprint 07

Bir **eğitmen** olarak, **platform içinden canlı ders planlayıp başlatmak** istiyorum; böylece ayrı bir video konferans aracına ihtiyaç kalmasın.

**Fonksiyonel gereksinimler**

- FR-501.1: Canlı ders yurt içinde barındırılan BigBlueButton üzerinden açılır.
- FR-501.2: Planlanan ders takvime ve öğrenci panosuna eklenir.
- FR-501.3: Kayıt varsayılan olarak açıktır; eğitmen kapatabilir.

**Kabul kriterleri**

- **Verilen** planlanmış bir canlı ders, **olduğunda** eğitmen 'Başlat'a bastığında, **o zaman** oturum açılır ve öğrencilere bildirim gider.

#### US-502 · Canlı derse katılma

Tür: Kullanıcı hikâyesi · Öncelik: Olmazsa olmaz · Puan: 3 · Planlanan: Sprint 07

Bir **öğrenci** olarak, **takvimden tek tıkla canlı derse katılmak** istiyorum; böylece bağlantı aramak zorunda kalmayayım.

**Fonksiyonel gereksinimler**

- FR-502.1: Katılım bağlantısı ders başlamadan 10 dakika önce etkinleşir.
- FR-502.2: Mobil tarayıcıdan katılım desteklenir.

**Kabul kriterleri**

- **Verilen** başlamış bir canlı ders, **olduğunda** kayıtlı öğrenci 'Katıl'a bastığında, **o zaman** oturuma doğrudan bağlanır.

#### US-503 · Ders kaydının kaynaklara otomatik eklenmesi

Tür: Kullanıcı hikâyesi · Öncelik: Olmazsa olmaz · Puan: 5 · Planlanan: Sprint 08

Bir **eğitmen** olarak, **canlı ders bittiğinde kaydın otomatik olarak ders kaynaklarına eklenmesini** istiyorum; böylece öğrenciler kaydı izleyebilsin ve YZ asistanı ders anlatımından da yanıt verebilsin.

**Fonksiyonel gereksinimler**

- FR-503.1: Kayıt hazır olduğunda kaynak listesine eklenir ve transkript üretimi başlar.
- FR-503.2: Eğitmen kaydı yayımlamadan önce inceleyebilir.

**Kabul kriterleri**

- **Verilen** sona ermiş ve kaydı açık bir canlı ders, **olduğunda** kayıt hazır olduğunda, **o zaman** ders kaynaklarında taslak olarak görünür ve transkripti üretilir.

#### US-504 · Yoklama raporu

Tür: Kullanıcı hikâyesi · Öncelik: Olmalı · Puan: 3 · Planlanan: Sprint 08

Bir **eğitmen** olarak, **canlı derse kimin ne kadar süre katıldığını görmek** istiyorum; böylece devam takibini elle yapmak zorunda kalmayayım.

**Fonksiyonel gereksinimler**

- FR-504.1: Katılım süresi öğrenci bazında listelenir ve CSV olarak indirilebilir.

**Kabul kriterleri**

- **Verilen** tamamlanmış bir canlı ders, **olduğunda** eğitmen yoklama raporunu açtığında, **o zaman** her öğrencinin katılım süresini görür.

### EP-06 · Ödev ve teslim

_Ödev verilmesi, teslim alınması ve değerlendirilmesi._

#### US-601 · Ödev oluşturma

Tür: Kullanıcı hikâyesi · Öncelik: Olmazsa olmaz · Puan: 5 · Planlanan: Sprint 05 – Sprint 06

Bir **eğitmen** olarak, **açıklaması, son tarihi ve değerlendirme rubriği olan bir ödev vermek** istiyorum; böylece öğrencilerim neyin beklendiğini açıkça bilsin.

**Fonksiyonel gereksinimler**

- FR-601.1: Başlık, açıklama, ek dosya, son tarih ve geç teslim kuralı tanımlanır.
- FR-601.2: Rubrik bağlanabilir; cevap anahtarı yalnızca eğitmene görünür biçimde eklenebilir.
- FR-601.3: Ödev soruları 'korumalı' olarak işaretlenebilir (YZ asistanı yanıt vermez, yönlendirir).

**Kabul kriterleri**

- **Verilen** bir dersin eğitmeni, **olduğunda** ödevi yayımladığında, **o zaman** öğrencilerin panosunda son tarihiyle görünür.

#### US-602 · Ödev teslimi

Tür: Kullanıcı hikâyesi · Öncelik: Olmazsa olmaz · Puan: 5 · Planlanan: Sprint 06

Bir **öğrenci** olarak, **ödevimi bir veya birden fazla dosyayla teslim etmek** istiyorum; böylece eğitmenim değerlendirebilsin.

**Fonksiyonel gereksinimler**

- FR-602.1: Son tarihe kadar teslim güncellenebilir.
- FR-602.2: Geç teslim kuralına göre teslim engellenir veya 'geç' olarak işaretlenir.
- FR-602.3: Teslim onayı e-postayla bildirilir.

**Kabul kriterleri**

- **Verilen** süresi dolmamış bir ödev, **olduğunda** öğrenci dosyasını yükleyip teslim ettiğinde, **o zaman** teslim kaydedilir ve onay bildirimi alır.
- **Verilen** süresi dolmuş ve geç teslime kapalı bir ödev, **olduğunda** öğrenci teslim etmeye çalıştığında, **o zaman** teslim engellenir ve nedeni gösterilir.

#### US-603 · Teslimleri listeleme ve not verme

Tür: Kullanıcı hikâyesi · Öncelik: Olmazsa olmaz · Puan: 5 · Planlanan: Sprint 07

Bir **eğitmen** olarak, **teslimleri tek ekranda görüp not ve geri bildirim vermek** istiyorum; böylece değerlendirmeyi hızlı yapabileyim.

**Fonksiyonel gereksinimler**

- FR-603.1: Teslim edilen, edilmeyen ve geç teslimler filtrelenebilir.
- FR-603.2: Not ve geri bildirim taslak olarak kaydedilip toplu yayımlanabilir.

**Kabul kriterleri**

- **Verilen** 10 teslimi olan bir ödev, **olduğunda** eğitmen notları girip yayımladığında, **o zaman** öğrenciler notlarını görür.

#### US-604 · Not ve geri bildirimi görüntüleme

Tür: Kullanıcı hikâyesi · Öncelik: Olmazsa olmaz · Puan: 3 · Planlanan: Sprint 08

Bir **öğrenci** olarak, **notumu ve eğitmenimin geri bildirimini görmek** istiyorum; böylece eksiklerimi anlayıp gelişebileyim.

**Fonksiyonel gereksinimler**

- FR-604.1: Not yayımlandığında bildirim gider.
- FR-604.2: Rubrik kullanılmışsa kriter bazında puan gösterilir.

**Kabul kriterleri**

- **Verilen** notu yayımlanmış bir ödev, **olduğunda** öğrenci ödev sayfasını açtığında, **o zaman** notunu, kriter puanlarını ve geri bildirimi görür.

### EP-07 · Takvim ve bildirimler

_Ders, canlı ders ve ödev tarihlerinin takibi ve hatırlatılması._

#### US-701 · Takvim ve dışa aktarma

Tür: Kullanıcı hikâyesi · Öncelik: Olmalı · Puan: 5 · Planlanan: Sprint 07

Bir **öğrenci** olarak, **ders, canlı ders ve ödev tarihlerini takvimde görmek ve kendi takvimime aktarmak** istiyorum; böylece planımı tek yerden yapabileyim.

**Fonksiyonel gereksinimler**

- FR-701.1: Haftalık ve aylık görünüm bulunur.
- FR-701.2: Kişisel iCal bağlantısı ile dış takvimlere abone olunabilir.

**Kabul kriterleri**

- **Verilen** iCal bağlantısını telefon takvimine eklemiş bir öğrenci, **olduğunda** yeni bir ödev yayımlandığında, **o zaman** ödev son tarihi telefon takviminde görünür.

#### US-702 · Bildirimler ve hatırlatmalar

Tür: Kullanıcı hikâyesi · Öncelik: Olmazsa olmaz · Puan: 5 · Planlanan: Sprint 08

Bir **öğrenci** olarak, **ödev son tarihleri ve canlı dersler için zamanında hatırlatma almak** istiyorum; böylece teslimleri kaçırmayayım.

**Fonksiyonel gereksinimler**

- FR-702.1: Ödev son tarihinden 24 saat önce ve canlı dersten 15 dakika önce hatırlatma gider.
- FR-702.2: Kullanıcı bildirim kanallarını (e-posta, uygulama içi) seçebilir.

**Kabul kriterleri**

- **Verilen** teslim etmemiş bir öğrenci, **olduğunda** son tarihe 24 saat kala, **o zaman** hatırlatma bildirimi alır.

### EP-08 · İçerik işleme ve Türkçe bilgi erişimi (Ar-Ge)

_AR-2 ve AR-5: ders kaynaklarının aranabilir bilgi tabanına dönüştürülmesi; Recall@5 ≥ %90, ders kaydı WER ≤ %10._

#### AR-801 · Belge ayrıştırma ve yapı koruma

Tür: Ar-Ge araştırması · Öncelik: Olmazsa olmaz · Puan: 8 · Planlanan: Sprint 05 – Sprint 06

**Hipotez ve ölçüt:** PDF ve DOCX kaynaklarında başlık, paragraf, tablo ve sayfa bilgisinin korunması; Docling (seçim) ile Marker (karşılaştırma) tablo doğruluğunda karşılaştırılır.

**Kabul kriterleri**

- En az 50 sayfalık örnek sette tablo ve başlık doğruluğu ölçüldü ve raporlandı.
- Seçilen ayrıştırıcı içerik işleme hattına entegre edildi.

#### AR-802 · Slayt ve görsel içerik işleme

Tür: Ar-Ge araştırması · Öncelik: Olmalı · Puan: 5 · Planlanan: Sprint 06 – Sprint 07

**Hipotez ve ölçüt:** Slayt metni, konuşmacı notu ve görsel açıklamasının tek parçada birleştirilmesi; görsel ve tablo kaynaklı sorularda doğru yanıt ≥ %85.

**Kabul kriterleri**

- Görsel-dil modeli adayları karşılaştırıldı.
- Görsel kaynaklı soru alt kümesinde doğruluk ölçüldü.

#### AR-803 · Türkçe metin normalizasyonu ve kök bulma

Tür: Ar-Ge araştırması · Öncelik: Olmazsa olmaz · Puan: 5 · Planlanan: Sprint 06

**Hipotez ve ölçüt:** Türkçe büyük-küçük harf (İ/ı), şapkalı harf ve ek farklılıklarına dayanıklı arama; Snowball ile Zemberek karşılaştırılır.

**Kabul kriterleri**

- Normalizasyon birim testleri yazıldı (İ/ı dönüşümü dahil).
- İki kök bulma yönteminin erişime etkisi ölçüldü.

#### AR-804 · Ders kaydı konuşma tanıma

Tür: Ar-Ge araştırması · Öncelik: Olmazsa olmaz · Puan: 8 · Planlanan: Sprint 06 – Sprint 08

**Hipotez ve ölçüt:** Gerçek ders kayıtlarında kelime hata oranı ≤ %10; zaman damgalı transkript ve konu segmentleri.

**Kabul kriterleri**

- En az 5 saatlik elle düzeltilmiş kayıtta WER ölçüldü.
- Ders terim sözlüğünün etkisi raporlandı.

#### AR-805 · Parçalama stratejisi deneyi

Tür: Ar-Ge araştırması · Öncelik: Olmazsa olmaz · Puan: 5 · Planlanan: Sprint 07 – Sprint 08

**Hipotez ve ölçüt:** Yapı-farkındalıklı parçalamanın sabit uzunluklu parçalamadan daha iyi erişim sağladığı hipotezinin sınanması.

**Kabul kriterleri**

- En az üç parçalama yöntemi test setinde karşılaştırıldı.

#### AR-806 · Türkçe gömme modeli seçimi

Tür: Ar-Ge araştırması · Öncelik: Olmazsa olmaz · Puan: 5 · Planlanan: Sprint 08 – Sprint 09

**Hipotez ve ölçüt:** bge-m3, turkish-e5-large, multilingual-e5-large ve embeddinggemma modellerinin kurumun Türkçe test setinde karşılaştırılması.

**Kabul kriterleri**

- Dört model karşılaştırıldı; seçim gerekçesiyle teknoloji kararları belgesine işlendi.

#### AR-807 · Hibrit arama ve yeniden sıralama

Tür: Ar-Ge araştırması · Öncelik: Olmazsa olmaz · Puan: 8 · Planlanan: Sprint 09 – Sprint 11

**Hipotez ve ölçüt:** Yoğun ve seyrek aramanın birleştirilmesi ve yeniden sıralama ile Recall@5 ≥ %90 (ara eşik ≥ %85, KT-3).

**Kabul kriterleri**

- Recall@5 ve MRR@10 %95 güven aralığıyla raporlandı.
- Kilometre taşı 3 kararı kayda geçirildi.

#### US-808 · Kaynak işleme durumunun izlenmesi

Tür: Kullanıcı hikâyesi · Öncelik: Olmalı · Puan: 3 · Planlanan: Sprint 06

Bir **eğitmen** olarak, **yüklediğim kaynağın YZ asistanına hazır olup olmadığını görmek** istiyorum; böylece öğrencilerime ne zaman duyurabileceğimi bileyim.

**Fonksiyonel gereksinimler**

- FR-808.1: Durumlar: sırada, işleniyor, hazır, hata.
- FR-808.2: Hata durumunda neden ve önerilen çözüm gösterilir.

**Kabul kriterleri**

- **Verilen** taranmış ve okunamayan bir PDF, **olduğunda** işleme tamamlandığında, **o zaman** eğitmen 'metin çıkarılamadı' uyarısı ve öneri görür.

### EP-09 · YZ ders asistanı (Ar-Ge)

_AR-1: öğrencinin sorusunu yalnızca ders kaynağından, atıflı yanıtlaması; sadakat ≥ %95, ret ≥ %90._

#### US-901 · Ders asistanına soru sorma ve atıflı yanıt

Tür: Kullanıcı hikâyesi · Öncelik: Olmazsa olmaz · Puan: 8 · Planlanan: Sprint 08 – Sprint 09

Bir **öğrenci** olarak, **ders sayfasındaki asistana soru sorup yalnızca ders kaynaklarına dayanan yanıt almak** istiyorum; böylece ders saatleri dışında da doğru bilgiyle çalışabileyim.

**Fonksiyonel gereksinimler**

- FR-901.1: Yanıt yalnızca dersin yayımlanmış kaynaklarına dayanır.
- FR-901.2: Her cümle bir kaynağa atıf verir (sayfa, slayt veya video dakikası).
- FR-901.3: Önceki konuşma bağlamı dikkate alınır.

**Kabul kriterleri**

- **Verilen** kaynaklarda yanıtı bulunan bir soru, **olduğunda** öğrenci sorduğunda, **o zaman** en geç 3 saniyede atıflı yanıt alır.
- **Verilen** aynı oturumda önceki soruya atıf yapan bir takip sorusu, **olduğunda** sorulduğunda, **o zaman** yanıt önceki bağlamı dikkate alır.

#### US-902 · Atıftan kaynağa gitme

Tür: Kullanıcı hikâyesi · Öncelik: Olmazsa olmaz · Puan: 5 · Planlanan: Sprint 09

Bir **öğrenci** olarak, **yanıttaki atfa tıklayınca kaynağın ilgili yerini açmak** istiyorum; böylece yanıtı kendim doğrulayabileyim.

**Fonksiyonel gereksinimler**

- FR-902.1: Atıf önizlemesi üzerine gelince gösterilir.
- FR-902.2: Tıklamada görüntüleyici ilgili sayfada veya dakikada açılır.

**Kabul kriterleri**

- **Verilen** video atfı içeren bir yanıt, **olduğunda** öğrenci atfa tıkladığında, **o zaman** ders kaydı ilgili dakikadan oynatılır.

#### AR-903 · Cevaplanabilirlik kapısı ve ceza-duyarlı eşik

Tür: Ar-Ge araştırması · Öncelik: Olmazsa olmaz · Puan: 8 · Planlanan: Sprint 08 – Sprint 10

**Hipotez ve ölçüt:** Kaynakta yanıtı olmayan soruların reddedilmesi: ret doğruluğu ≥ %90, gereksiz ret ≤ %8 (H1.2).

**Kabul kriterleri**

- Eşik doğrulama setinde ceza-duyarlı skorla ayarlandı.
- Kaynak dışı test alt kümesinde ret doğruluğu raporlandı.

#### AR-904 · İddia düzeyinde yanıt doğrulama

Tür: Ar-Ge araştırması · Öncelik: Olmazsa olmaz · Puan: 13 · Planlanan: Sprint 10 – Sprint 12

**Hipotez ve ölçüt:** Yanıtın atomik iddialara ayrılıp her birinin kaynakla doğrulanması; sadakat ≥ %95, atıf doğruluğu ≥ %95 (H1.1).

**Kabul kriterleri**

- Doğrulamalı ve doğrulamasız kollar karşılaştırıldı.
- Sadakat ve atıf doğruluğu %95 güven aralığıyla raporlandı.

#### US-905 · Kaynakta olmayan soruya gerekçeli ret

Tür: Kullanıcı hikâyesi · Öncelik: Olmazsa olmaz · Puan: 5 · Planlanan: Sprint 10

Bir **öğrenci** olarak, **sorumun yanıtı ders kaynaklarında yoksa bunu açıkça öğrenmek** istiyorum; böylece yanlış ya da dersle çelişen bilgiyle çalışmayayım.

**Fonksiyonel gereksinimler**

- FR-905.1: Ret mesajı, varsa ilgili olabilecek bölümleri önerir.
- FR-905.2: Soru eğitmenin 'cevapsız sorular' listesine eklenir.

**Kabul kriterleri**

- **Verilen** ders kaynaklarında karşılığı olmayan bir soru, **olduğunda** öğrenci sorduğunda, **o zaman** uydurma yanıt yerine gerekçeli ret alır ve soru eğitmene iletilir.

#### US-906 · Cevapsız ve sık sorulan sorular raporu

Tür: Kullanıcı hikâyesi · Öncelik: Olmalı · Puan: 5 · Planlanan: Sprint 12

Bir **eğitmen** olarak, **öğrencilerin asistana en çok sorduğu ve yanıt alamadığı soruları görmek** istiyorum; böylece ders içeriğimi eksiklere göre geliştirebileyim.

**Fonksiyonel gereksinimler**

- FR-906.1: Haftalık özet ve konu bazında gruplama yapılır.
- FR-906.2: Öğrenci kimliği gösterilmez.

**Kabul kriterleri**

- **Verilen** bir hafta boyunca kullanılmış bir ders, **olduğunda** eğitmen raporu açtığında, **o zaman** en sık ve cevapsız soruları konu bazında görür.

#### US-907 · Yanıtı değerlendirme

Tür: Kullanıcı hikâyesi · Öncelik: Olmalı · Puan: 2 · Planlanan: Sprint 11

Bir **öğrenci** olarak, **yanıtın işime yarayıp yaramadığını işaretlemek** istiyorum; böylece asistanın kalitesi gelişsin.

**Fonksiyonel gereksinimler**

- FR-907.1: Yararlı / yararsız işareti ve isteğe bağlı açıklama alınır.
- FR-907.2: Geri bildirimler kalite panosuna yansır.

**Kabul kriterleri**

- **Verilen** bir yanıt, **olduğunda** öğrenci 'yararsız' olarak işaretlediğinde, **o zaman** geri bildirim kaydedilir ve kalite panosunda görünür.

### EP-10 · Pedagojik mod (Ar-Ge)

_AR-4: ödev sorularında yanıt yerine yönlendirme; sızıntı ≤ %2._

#### AR-1001 · Soru niyeti sınıflandırma

Tür: Ar-Ge araştırması · Öncelik: Olmazsa olmaz · Puan: 5 · Planlanan: Sprint 09 – Sprint 10

**Hipotez ve ölçüt:** Kavram sorusu, ödev çözüm talebi, kapsam dışı ve platform yardımı ayrımının test setinde ≥ %90 doğrulukla yapılması.

**Kabul kriterleri**

- Sınıflandırıcı test setinde ölçüldü; karışıklık matrisi raporlandı.

#### US-1002 · Pedagojik mod seçimi

Tür: Kullanıcı hikâyesi · Öncelik: Olmazsa olmaz · Puan: 3 · Planlanan: Sprint 11

Bir **eğitmen** olarak, **ders veya ödev bazında asistanın serbest, Sokratik ya da kapalı modda çalışmasını seçmek** istiyorum; böylece ödev süresince öğrencilerin yanıtı hazır almasını önleyebileyim.

**Fonksiyonel gereksinimler**

- FR-1002.1: Varsayılan mod kurum ayarından gelir; eğitmen ders ve ödev bazında değiştirebilir.
- FR-1002.2: Öğrenciye aktif mod açıkça gösterilir.

**Kabul kriterleri**

- **Verilen** Sokratik moddaki bir ödev, **olduğunda** öğrenci ödev sorusunun yanıtını istediğinde, **o zaman** yanıt yerine yönlendirici ipucu alır.

#### AR-1003 · Ödev eşleme ve ipucu merdiveni

Tür: Ar-Ge araştırması · Öncelik: Olmazsa olmaz · Puan: 8 · Planlanan: Sprint 11 – Sprint 12

**Hipotez ve ölçüt:** Öğrenci sorusunun aktif ödevle eşleştirilmesi ve dört seviyeli ipucu (kavram, yönlendirici soru, ilk adım, benzer örnek) ile öğrencinin kendi adımlarının değerlendirilmesi.

**Kabul kriterleri**

- Ödev eşleme doğruluğu ölçüldü.
- İpucu merdiveni eğitmen değerlendirmesiyle sınandı.

#### AR-1004 · Yanıt sızıntısı tarayıcısı

Tür: Ar-Ge araştırması · Öncelik: Olmazsa olmaz · Puan: 8 · Planlanan: Sprint 12 – Sprint 13

**Hipotez ve ölçüt:** Ödev yanıtını içeren çıktıların deterministik olarak engellenmesi; sızıntı ≤ %2, meşru sorularda aşırı kısıtlama ≤ %5 (H4.1).

**Kabul kriterleri**

- Sızıntı ve aşırı kısıtlama oranları Wilson güven aralığıyla raporlandı.

#### AR-1005 · Manipülasyon test seti ve dayanıklılık

Tür: Ar-Ge araştırması · Öncelik: Olmazsa olmaz · Puan: 8 · Planlanan: Sprint 13 – Sprint 14

**Hipotez ve ölçüt:** En az 500 saldırı istemi (rol yapma, sahte yetki, parçalı sorma, dil değiştirme, biçim hilesi, dosyaya gizlenmiş talimat) karşısında direnç ≥ %95.

**Kabul kriterleri**

- Test seti hazırlandı ve CI kalite kapısına eklendi.
- Kilometre taşı 4 kararı kayda geçirildi.

### EP-11 · Rubrik ve YZ destekli ödev değerlendirme (Ar-Ge)

_AR-3: rubriğe göre kanıtlı ön-değerlendirme; eğitmenle uyum (Kappa) ≥ 0,75._

#### US-1101 · Rubrik oluşturma

Tür: Kullanıcı hikâyesi · Öncelik: Olmazsa olmaz · Puan: 8 · Planlanan: Sprint 10 – Sprint 11

Bir **eğitmen** olarak, **ödev için kriter, ağırlık ve seviye tanımlarından oluşan bir rubrik hazırlamak** istiyorum; böylece değerlendirmem tutarlı olsun ve YZ önerileri bu ölçütlere dayansın.

**Fonksiyonel gereksinimler**

- FR-1101.1: Kriter adı, ağırlık (toplam %100) ve seviye betimleyicileri tanımlanır.
- FR-1101.2: Hazır şablonlardan başlanabilir; rubrik başka ödevlere kopyalanabilir.
- FR-1101.3: Eğitmen puanladığı örnek ödevleri 'çapa' olarak işaretleyebilir.

**Kabul kriterleri**

- **Verilen** ağırlıkları toplamı %100 olmayan bir rubrik, **olduğunda** kaydedilmek istendiğinde, **o zaman** kayıt engellenir ve uyarı gösterilir.

#### AR-1102 · Kriter başına kanıt çıkarımı

Tür: Ar-Ge araştırması · Öncelik: Olmazsa olmaz · Puan: 8 · Planlanan: Sprint 11 – Sprint 12

**Hipotez ve ölçüt:** Her rubrik kriteri için ödevden ilgili alıntının ve konumunun çıkarılması; eğitmen değerlendirmesinde kanıtların ≥ %85 oranında isabetli bulunması.

**Kabul kriterleri**

- Kanıt isabeti eğitmen örneklemiyle ölçüldü.

#### AR-1103 · Örneklerle karşılaştırmalı puanlama ve belirsizlik

Tür: Ar-Ge araştırması · Öncelik: Olmazsa olmaz · Puan: 13 · Planlanan: Sprint 12 – Sprint 14

**Hipotez ve ölçüt:** Çapa örneklerle karşılaştırmalı puanlamanın doğrudan puanlamaya göre Kappa'yı ≥ 0,15 artırması (H3.1); belirsiz kriterlerin eğitmene yönlendirilmesi.

**Kabul kriterleri**

- E-3 deney kolları karşılaştırıldı.
- Belirsizlik eşiğinin etkisi raporlandı.

#### US-1104 · Teslim sonrası YZ ön-değerlendirmesi

Tür: Kullanıcı hikâyesi · Öncelik: Olmazsa olmaz · Puan: 5 · Planlanan: Sprint 14

Bir **eğitmen** olarak, **teslim edilen her ödev için rubriğe göre YZ ön-değerlendirmesinin hazırlanmasını** istiyorum; böylece değerlendirmeye kanıtlarla başlayabileyim.

**Fonksiyonel gereksinimler**

- FR-1104.1: Ön-değerlendirme yalnızca eğitmene görünür.
- FR-1104.2: Her kriter için önerilen seviye, kanıt alıntısı ve güven düzeyi gösterilir.
- FR-1104.3: Ödev dosyasındaki gizli talimatlar taranır ve eğitmene uyarı verilir.

**Kabul kriterleri**

- **Verilen** rubrik bağlı bir ödev, **olduğunda** öğrenci teslim ettiğinde, **o zaman** eğitmen ekranında birkaç dakika içinde ön-değerlendirme görünür.

#### US-1105 · Eğitmen onay ekranı

Tür: Kullanıcı hikâyesi · Öncelik: Olmazsa olmaz · Puan: 8 · Planlanan: Sprint 15 – Sprint 16

Bir **eğitmen** olarak, **YZ önerisini tek tıkla onaylamak ya da düzeltmek** istiyorum; böylece değerlendirme süremi kısaltırken son kararı ben vereyim.

**Fonksiyonel gereksinimler**

- FR-1105.1: Kriter bazında onayla, düzelt ve yorum ekle işlemleri yapılır.
- FR-1105.2: Belirsiz kriterler vurgulanır.
- FR-1105.3: Eğitmen düzeltmeleri kalibrasyon verisi olarak kaydedilir.
- FR-1105.4: Onaylanmadan hiçbir puan öğrenciye yansımaz (NFR-10).

**Kabul kriterleri**

- **Verilen** YZ önerisi bulunan bir teslim, **olduğunda** eğitmen bir kriteri düzeltip yayımladığında, **o zaman** öğrenci yalnızca eğitmenin onayladığı puanı görür ve düzeltme kaydedilir.

#### AR-1106 · Kalibrasyon, uyum ölçümü ve yanlılık analizi

Tür: Ar-Ge araştırması · Öncelik: Olmazsa olmaz · Puan: 13 · Planlanan: Sprint 15 – Sprint 17

**Hipotez ve ölçüt:** Ders bazında kalibrasyonla eğitmen-YZ uyumu ağırlıklı Kappa ≥ 0,75; uzunluk ve yazım hatası yanlılığının ölçülmesi.

**Kabul kriterleri**

- Kappa %95 güven aralığıyla ve insan-insan uyumuyla birlikte raporlandı.
- Kilometre taşı 5 kararı kayda geçirildi.

#### US-1107 · Kanıtlı ve kaynağa atıflı geri bildirim

Tür: Kullanıcı hikâyesi · Öncelik: Olmazsa olmaz · Puan: 3 · Planlanan: Sprint 16

Bir **öğrenci** olarak, **notumla birlikte hangi kriterde neden puan kaybettiğimi ve hangi kaynağa bakmam gerektiğini görmek** istiyorum; böylece eksiğimi doğrudan kapatabileyim.

**Fonksiyonel gereksinimler**

- FR-1107.1: Kriter bazında güçlü yön ve geliştirme önerisi gösterilir.
- FR-1107.2: Öneri ders kaynağına atıf verir.

**Kabul kriterleri**

- **Verilen** eğitmenin onayladığı geri bildirim, **olduğunda** öğrenci ödev sayfasını açtığında, **o zaman** kriter bazında açıklama ve kaynak bağlantısı görür.

#### AR-1108 · YZ ile yazılmış metin tespiti (isteğe bağlı)

Tür: Ar-Ge araştırması · Öncelik: Olabilir · Puan: 8 · Planlanan: Sprint 17 – Sprint 19

**Hipotez ve ölçüt:** Türkçe ödevlerde tespit doğruluğu ≥ %85, yanlış suçlama ≤ %5; sonuç yalnızca eğitmene inceleme önerisi olarak gösterilir.

**Kabul kriterleri**

- Doğruluk ölçüldü ya da kapsamdan çıkarma kararı gerekçesiyle kaydedildi.

### EP-13 · Bireysel abonelik ve faturalama

_Bireysel eğitmenlerin kendi kendine kayıt olması, abonelik ve kurum faturalaması._

#### US-1301 · Bireysel eğitmen kaydı ve deneme süresi

Tür: Kullanıcı hikâyesi · Öncelik: Olmalı · Puan: 5 · Planlanan: Sprint 07

Bir **bireysel eğitmen** olarak, **kurum olmadan kendi hesabımı açıp 14 günlük deneme başlatmak** istiyorum; böylece ödeme yapmadan önce platformu deneyebileyim.

**Fonksiyonel gereksinimler**

- FR-1301.1: E-posta doğrulamasıyla kayıt yapılır.
- FR-1301.2: Deneme süresince Eğitmen Pro özellikleri açıktır; bitişten 3 gün önce hatırlatma gider.

**Kabul kriterleri**

- **Verilen** yeni kayıt olmuş bir bireysel eğitmen, **olduğunda** e-postasını doğruladığında, **o zaman** 14 günlük deneme başlar ve ilk dersini açabilir.

#### US-1302 · Abonelik planı seçimi ve ödeme

Tür: Kullanıcı hikâyesi · Öncelik: Olmalı · Puan: 8 · Planlanan: Sprint 08

Bir **bireysel eğitmen** olarak, **uygun planı seçip kartla güvenli ödeme yapmak** istiyorum; böylece aboneliğim kesintisiz devam etsin.

**Fonksiyonel gereksinimler**

- FR-1302.1: Planlar: Eğitmen Başlangıç ve Eğitmen Pro (aylık).
- FR-1302.2: Ödeme yerli ödeme kuruluşu üzerinden alınır; kart bilgisi platformda saklanmaz.
- FR-1302.3: Başarısız ödemede 7 günlük ek süre tanınır.

**Kabul kriterleri**

- **Verilen** deneme süresi biten bir eğitmen, **olduğunda** plan seçip ödemeyi tamamladığında, **o zaman** abonelik başlar ve fatura e-postayla gönderilir.

#### US-1303 · Abonelik ve fatura yönetimi

Tür: Kullanıcı hikâyesi · Öncelik: Olmalı · Puan: 5 · Planlanan: Sprint 09

Bir **bireysel eğitmen** olarak, **planımı değiştirmek, iptal etmek ve faturalarımı indirmek** istiyorum; böylece aboneliğimi kendim yönetebileyim.

**Fonksiyonel gereksinimler**

- FR-1303.1: Plan değişikliği bir sonraki dönemde geçerli olur.
- FR-1303.2: İptal sonrası dönem sonuna kadar erişim sürer; veriler 90 gün saklanır.

**Kabul kriterleri**

- **Verilen** aktif aboneliği olan bir eğitmen, **olduğunda** iptal ettiğinde, **o zaman** dönem sonuna kadar erişimi sürer ve onay bildirimi alır.

#### US-1304 · Kurum faturalaması (aktif öğrenci sayısına göre)

Tür: Kullanıcı hikâyesi · Öncelik: Olmalı · Puan: 5 · Planlanan: Sprint 18

Bir **kurum yöneticisi** olarak, **aylık aktif öğrenci sayısına göre oluşan faturayı ve dökümünü görmek** istiyorum; böylece maliyetimi öngörebileyim.

**Fonksiyonel gereksinimler**

- FR-1304.1: Aktif öğrenci tanımı: ay içinde en az bir kez giriş yapan öğrenci.
- FR-1304.2: Aylık döküm CSV olarak indirilebilir.

**Kabul kriterleri**

- **Verilen** ay içinde 180 aktif öğrencisi olan bir kurum, **olduğunda** ay kapandığında, **o zaman** 180 öğrenci üzerinden fatura ve döküm oluşur.

### EP-14 · Raporlama ve kalite panosu

_Kullanım ve YZ kalite metriklerinin kurum ve eğitmene gösterilmesi._

#### US-1401 · Kurum kullanım panosu

Tür: Kullanıcı hikâyesi · Öncelik: Olmalı · Puan: 5 · Planlanan: Sprint 14

Bir **kurum yöneticisi** olarak, **aktif öğrenci, soru, teslim ve canlı ders sayılarını görmek** istiyorum; böylece platformun kurumda nasıl kullanıldığını izleyebileyim.

**Fonksiyonel gereksinimler**

- FR-1401.1: Günlük, haftalık ve aylık görünüm; ders bazında kırılım.
- FR-1401.2: Kişisel veri içermeyen toplu göstergeler kullanılır.

**Kabul kriterleri**

- **Verilen** bir ay kullanılmış bir kurum, **olduğunda** yönetici panoyu açtığında, **o zaman** seçilen döneme ait göstergeleri ders bazında görür.

#### US-1402 · YZ kalite panosu

Tür: Kullanıcı hikâyesi · Öncelik: Olmazsa olmaz · Puan: 8 · Planlanan: Sprint 14 – Sprint 15

Bir **kurum yöneticisi** olarak, **asistanın sadakat, ret ve eğitmen düzeltme oranlarını görmek** istiyorum; böylece YZ'nin güvenilirliğini şeffaf biçimde izleyebileyim.

**Fonksiyonel gereksinimler**

- FR-1402.1: Sadakat (örneklem), ret oranı, yanıt süresi, öğrenci geri bildirimi ve eğitmen düzeltme oranı gösterilir.
- FR-1402.2: Eşik altına düşen metriklerde uyarı verilir.

**Kabul kriterleri**

- **Verilen** eşiğin altına düşmüş bir metrik, **olduğunda** pano açıldığında, **o zaman** uyarı ve ilgili dönem vurgulanır.

#### US-1403 · Eğitmen ders analitiği

Tür: Kullanıcı hikâyesi · Öncelik: Olmalı · Puan: 5 · Planlanan: Sprint 15

Bir **eğitmen** olarak, **öğrencilerin katılımını ve ödev durumunu bir bakışta görmek** istiyorum; böylece desteğe ihtiyaç duyan öğrencilere zamanında ulaşabileyim.

**Fonksiyonel gereksinimler**

- FR-1403.1: Ödev teslim oranı, canlı ders katılımı ve asistan kullanımı öğrenci bazında listelenir.

**Kabul kriterleri**

- **Verilen** iki ödevi teslim etmemiş bir öğrenci, **olduğunda** eğitmen analitiği açtığında, **o zaman** öğrenci listede işaretli görünür.

### EP-15 · Altyapı, güvenlik, KVKK ve yurt içi model (Ar-Ge)

_AR-6: yurt içi barındırma, güvenlik, KVKK uyumu; yurt içi modelle kalite farkı ≤ %5, p50 ≤ 3 sn._

#### AR-1506 · Yurt içi model servisi ve ince ayar

Tür: Ar-Ge araştırması · Öncelik: Olmazsa olmaz · Puan: 13 · Planlanan: Sprint 12 – Sprint 16

**Hipotez ve ölçüt:** Açık ağırlıklı Türkçe modelin yurt içi GPU'da vLLM ile servisi; en az iki ince ayar deneyi.

**Kabul kriterleri**

- Model servisi canlı ortamda çalışıyor.
- İnce ayar deneyleri raporlandı.

#### AR-1507 · Model karşılaştırması, önbellek ve yönlendirme

Tür: Ar-Ge araştırması · Öncelik: Olmazsa olmaz · Puan: 8 · Planlanan: Sprint 16 – Sprint 18

**Hipotez ve ölçüt:** Yurt içi model ile ticari model arasında kalite farkı ≤ %5; yanıt süresi p50 ≤ 3 sn; öğrenci başı maliyetin hesaplanması (H6.1).

**Kabul kriterleri**

- Kalite, gecikme ve maliyet karşılaştırması raporlandı.
- SGLang ile vLLM karşılaştırıldı.

### EP-20 · Sanal sınıf altyapısı

_Tarayıcı tabanlı, kurulum gerektirmeyen, çok kullanıcılı gerçek zamanlı sanal sınıf._

#### US-2001 · Kurulumsuz sanal sınıfa katılma

Tür: Kullanıcı hikâyesi · Öncelik: Olmazsa olmaz · Puan: 13 · Planlanan: 03.04.2028 – 30.06.2028

Bir **öğrenci** olarak, **tarayıcıdan herhangi bir kurulum yapmadan sanal sınıfa girmek** istiyorum; böylece her cihazdan derse katılabileyim.

**Fonksiyonel gereksinimler**

- FR-2001.1: Orta seviye telefonda ve 2 Mbps bağlantıda çalışır.
- FR-2001.2: Sınıf başına en az 50 eşzamanlı kullanıcı desteklenir.

**Kabul kriterleri**

- **Verilen** 2 Mbps bağlantıdaki bir öğrenci, **olduğunda** sanal sınıfa girdiğinde, **o zaman** sahne en az 30 kare/sn ile çalışır.

#### AR-2002 · Gerçek zamanlı durum senkronizasyonu

Tür: Ar-Ge araştırması · Öncelik: Olmazsa olmaz · Puan: 13 · Planlanan: 01.05.2028 – 29.09.2028

**Hipotez ve ölçüt:** Sınıf başına ≥ 50 kullanıcıda durum senkron gecikmesi ≤ 150 ms.

**Kabul kriterleri**

- Ölçek testleri raporlandı.

### EP-21 · Avatar ve mekânsal ses

_Kişiselleştirilebilir avatarlar, çalışma odaları ve mekânsal ses._

#### US-2101 · Avatar oluşturma

Tür: Kullanıcı hikâyesi · Öncelik: Olmalı · Puan: 8 · Planlanan: 01.05.2028 – 31.07.2028

Bir **öğrenci** olarak, **kendime ait bir avatar oluşturmak** istiyorum; böylece sanal sınıfta kendimi temsil edebileyim.

**Fonksiyonel gereksinimler**

- FR-2101.1: Açık VRM/GLB formatı kullanılır; kapalı platforma bağımlılık yoktur.

**Kabul kriterleri**

- **Verilen** ilk kez giren bir öğrenci, **olduğunda** avatar düzenleyicisini tamamladığında, **o zaman** avatarı sınıfta görünür.

#### US-2102 · Çalışma odaları ve mekânsal ses

Tür: Kullanıcı hikâyesi · Öncelik: Olmazsa olmaz · Puan: 13 · Planlanan: 03.07.2028 – 31.10.2028

Bir **öğrenci** olarak, **arkadaşlarımla çalışma odasında yakındakileri duyarak birlikte çalışmak** istiyorum; böylece grup çalışması doğal bir ortamda yapılabilsin.

**Fonksiyonel gereksinimler**

- FR-2102.1: Ses gecikmesi ≤ 200 ms; en az 10 paralel çalışma odası.

**Kabul kriterleri**

- **Verilen** aynı odadaki iki öğrenci, **olduğunda** birbirine yaklaştığında, **o zaman** birbirlerini daha net duyar.

### EP-22 · Sınıf içi YZ asistanı

_Faz 1 YZ'sinin sınıf bağlamını anlayan bir asistan olarak sınıfa katılması._

#### US-2201 · Sınıf içinde YZ asistanına soru sorma

Tür: Kullanıcı hikâyesi · Öncelik: Olmazsa olmaz · Puan: 13 · Planlanan: 03.07.2028 – 29.12.2028

Bir **öğrenci** olarak, **sanal sınıfta asistana soru sorup ders kaynağına dayalı yanıt almak** istiyorum; böylece dersi bölmeden anlamadığım noktayı netleştirebileyim.

**Fonksiyonel gereksinimler**

- FR-2201.1: Faz 1 sadakat ve pedagojik mod hedefleri korunur.
- FR-2201.2: Asistan soruyu soran kişiyi ve konuşma bağlamını doğru ayırt eder (≥ %90).

**Kabul kriterleri**

- **Verilen** sınıfta devam eden bir ders, **olduğunda** öğrenci asistana soru sorduğunda, **o zaman** ders kaynağına atıflı yanıt alır.

