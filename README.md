# KAYNAK-YZ: YTÜ Yıldız Teknopark Başvurusu ve Proje Planı

Bu depo, eğitim kurumumuzun YTÜ Yıldız Teknopark'a aday firma başvurusunu ve **KAYNAK-YZ** projesinin tüm planını içerir.

**Proje:** Türkçe Eğitim İçeriği İçin Kaynağa Dayalı Üretken Yapay Zekâ ile Soru-Cevap ve Rubrik Tabanlı Otomatik Ödev Değerlendirme Platformu

**Kurum notu:** Kurumumuzun asıl faaliyet alanı eğitimdir. Yapay zekâ, eğitim hizmetimizi güçlendirmek amacıyla geliştirilmektedir. Sistemin ilk kullanıcısı kurumumuz olacak; gerçek ortamda doğrulandıktan sonra aynı ihtiyacı yaşayan kurumlara sunulacaktır.

---

## Başvuruya gönderilecek dosyalar

`teslim/` klasöründedir:

| Dosya | Kullanım |
|---|---|
| `KAYNAK-YZ_Firma_Proje_Sunumu.pdf` | Başvuru formundaki "Firma / Proje Sunumu" alanına yüklenir (19 slayt) |
| `KAYNAK-YZ_Firma_Proje_Sunumu.pptx` | Sunumun düzenlenebilir hâli |
| `KAYNAK-YZ_Proje_Ozeti.pdf` | Proje özeti (9 sayfa); ön görüşmede ve hakem sürecinde sunulur |
| `KAYNAK-YZ_Proje_Ozeti.docx` | Özetin düzenlenebilir hâli |

Dosyalardaki sarı vurgulu ve köşeli ayraçlı (‹…›) alanlar kurum bilgileriyle doldurulmalıdır.

## Belgeler

| Belge | İçerik |
|---|---|
| [01 · Araştırma raporu](docs/01-yildiz-teknopark-arastirma-raporu.md) | Yıldız Teknopark başvuru süreci, komisyonlar, hakem ölçütleri ve kurallar |
| [02 · Faz yapısı ve kabul analizi](docs/02-faz-yapisi-ve-kabul-analizi.md) | Faz 1 ve Faz 2'nin kabul değerlendirmesi ve puan simülasyonu |
| [03 · Proje planı: sprintler ve kanban](docs/03-proje-plani-sprint-ve-kanban.md) | Fazlar, epikler, hazırlık dönemi, Faz 1'in 26 sprinti ve Faz 2–3 yol haritası |
| [04 · Teknoloji kararları](docs/04-teknoloji-kararlari.md) | 20 teknoloji kararının alternatiflerle karşılaştırması ve gerekçeleri |
| [06 · Ürün gereksinimleri](docs/06-urun-gereksinimleri.md) | Personalar, fonksiyonel olmayan gereksinimler (NFR) ve her kullanıcı hikâyesinin fonksiyonel gereksinimleri (FR) ile kabul kriterleri |
| [05 · Bağımsız değerlendirme raporu](docs/05-degerlendirme-raporu.md) | Dosyanın hakem ölçütlerine göre değerlendirilmesi, yapılan düzeltmeler ve gönderim öncesi zorunlu işlemler |
| [Proje dosyası (00–05)](docs/proje-dosyasi/00-ozet-ve-kunye.md) | Ayrıntılı proje dosyası: künye, pazar, Ar-Ge tasarımı, test planı, bütçe, risk ve hakem hazırlığı |
| [Kaynak metinler](docs/kaynaklar/) | Yıldız Bölge İşletme Yönergesi 2025 ve karşılaştırma için İTÜ yönergesi |

## Proje yapısı

| Faz | Dönem | İçerik | Planlama |
|---|---|---|---|
| Faz 0 | Kasım 2026 – Mart 2027 | Başvuru hazırlığı, değerlendirme süreci ve yerleşme | Sprint düzeyinde |
| Faz 1 | Nisan 2027 – Mart 2028 | Eğitim platformu ve kaynağa dayalı eğitim yapay zekâsı | Sprint düzeyinde |
| Faz 2 | Nisan 2028 – Mart 2029 | Avatarlı sanal sınıf ve sınıf içi yapay zekâ asistanı | Makro düzeyde |
| Faz 3 | Nisan 2029 – Mart 2030 | Uyarlanabilir öğrenme ve öğrenci modelleme | Makro düzeyde |

## Ürün backlog'u (GitHub Issues)

Backlog dört tür öğeden oluşur:

| Tür | Kimlik | İçerik |
|---|---|---|
| Epik | `EP-01` … | Ürünün işlev alanı (ör. Kimlik doğrulama ve hesap yönetimi, Ödev ve teslim, YZ ders asistanı). Kapsamdaki öğeler alt iş olarak bağlıdır. |
| Kullanıcı hikâyesi | `US-101` … | "Bir öğrenci olarak … istiyorum; böylece …" kalıbı, numaralı fonksiyonel gereksinimler (FR), "Verilen / olduğunda / o zaman" kabul kriterleri, tamamlanma tanımı |
| Ar-Ge araştırması | `AR-801` … | Araştırma sorusu, hipotez, ölçüt ve hedef değer |
| Görev | `G-001` … | Teknopark süreçleri, test setleri, altyapı ve pilot işleri |

- **Sprintler:** Faz 1, iki haftalık 26 sprinte bölünmüştür; her sprint bir milestone'dur ve açıklamasında odak epikler ile teknolojiler yazılıdır. Hazırlık dönemi ve Faz 2–3 için ayrı milestone'lar vardır.
- **Her öğede:** epik, sprint, başlangıç ve bitiş tarihi, sorumlu, öncelik, hikâye puanı, bağımlılıklar ve kullanılacak teknolojiler.
- **Etiketler:** `tür: …`, `öncelik: olmazsa olmaz / olmalı / olabilir`, `puan: …`, `faz-0` … `faz-3`, `rol: …`, `durum: yapılacak → bu sprint → devam ediyor → incelemede`.
- **Yeni iş açarken:** "New issue" ekranındaki kullanıcı hikâyesi, Ar-Ge araştırması ve hata bildirimi şablonları kullanılır.

## Planın güncellenmesi

Planın tek kaynağı [`plan/backlog.json`](plan/backlog.json), teknoloji kataloğu [`plan/teknolojiler.json`](plan/teknolojiler.json) dosyasıdır.

```bash
python scripts/plan_olustur.py                       # docs/03 ve docs/06 belgelerini yeniden üretir
python scripts/github_yukle.py OWNER/REPO            # yeni öğeleri GitHub'a ekler (var olanları atlar)
node scripts/teslim/sunum.js                         # sunumu yeniden üretir
node scripts/teslim/ozet.js                          # proje özetini yeniden üretir
```
