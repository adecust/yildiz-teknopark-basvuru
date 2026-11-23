# KAYNAK-YZ: YTÜ Yıldız Teknopark Başvurusu ve Proje Planı

Bu depo, eğitim kurumumuzun YTÜ Yıldız Teknopark'a aday firma başvurusunu ve **KAYNAK-YZ** projesinin tüm planını içerir.

**Proje:** Türkçe Eğitim İçeriği İçin Kaynağa Dayalı Üretken Yapay Zekâ ile Soru-Cevap ve Rubrik Tabanlı Otomatik Ödev Değerlendirme Platformu

**Kurum notu:** Kurumumuzun asıl faaliyet alanı eğitimdir. Yapay zekâ, eğitim hizmetimizi güçlendirmek amacıyla geliştirilmektedir. Sistemin ilk kullanıcısı kurumumuz olacak; gerçek ortamda doğrulandıktan sonra aynı ihtiyacı yaşayan kurumlara sunulacaktır.

---

## Başvuruya gönderilecek dosyalar

`teslim/` klasöründedir:

| Dosya | Kullanım |
|---|---|
| `KAYNAK-YZ_Firma_Proje_Sunumu.pdf` | Başvuru formundaki "Firma / Proje Sunumu" alanına yüklenir (18 slayt) |
| `KAYNAK-YZ_Firma_Proje_Sunumu.pptx` | Sunumun düzenlenebilir hâli |
| `KAYNAK-YZ_Proje_Ozeti.pdf` | Proje özeti (9 sayfa); ön görüşmede ve hakem sürecinde sunulur |
| `KAYNAK-YZ_Proje_Ozeti.docx` | Özetin düzenlenebilir hâli |

Dosyalardaki sarı vurgulu ve köşeli ayraçlı (‹…›) alanlar kurum bilgileriyle doldurulmalıdır.

## Belgeler

| Belge | İçerik |
|---|---|
| [01 · Araştırma raporu](docs/01-yildiz-teknopark-arastirma-raporu.md) | Yıldız Teknopark başvuru süreci, komisyonlar, hakem ölçütleri ve kurallar |
| [02 · Faz yapısı ve kabul analizi](docs/02-faz-yapisi-ve-kabul-analizi.md) | Faz 1 ve Faz 2'nin kabul değerlendirmesi ve puan simülasyonu |
| [03 · Proje planı: sprintler ve kanban](docs/03-proje-plani-sprint-ve-kanban.md) | Makro plan, 33 sprint, 148 görev; her görevde tarih, sorumlu, teknoloji ve kabul kriteri |
| [04 · Teknoloji kararları](docs/04-teknoloji-kararlari.md) | 20 teknoloji kararının alternatiflerle karşılaştırması ve gerekçeleri |
| [Proje dosyası (00–05)](docs/proje-dosyasi/00-ozet-ve-kunye.md) | Ayrıntılı proje dosyası: künye, pazar, Ar-Ge tasarımı, test planı, bütçe, risk ve hakem hazırlığı |
| [Kaynak metinler](docs/kaynaklar/) | Yıldız Bölge İşletme Yönergesi 2025 ve karşılaştırma için İTÜ yönergesi |

## Proje yapısı

| Faz | Dönem | İçerik | Planlama |
|---|---|---|---|
| Faz 0 | Kasım 2026 – Mart 2027 | Başvuru hazırlığı, değerlendirme süreci ve yerleşme | Sprint düzeyinde |
| Faz 1 | Nisan 2027 – Mart 2028 | Eğitim platformu ve kaynağa dayalı eğitim yapay zekâsı | Sprint düzeyinde |
| Faz 2 | Nisan 2028 – Mart 2029 | Avatarlı sanal sınıf ve sınıf içi yapay zekâ asistanı | Makro düzeyde |
| Faz 3 | Nisan 2029 – Mart 2030 | Uyarlanabilir öğrenme ve öğrenci modelleme | Makro düzeyde |

## İş takibi (GitHub)

- **Epikler:** Her iş paketi bir epik issue'dur (`epik` etiketi). Görevler epiklere alt iş olarak bağlıdır.
- **Sprintler:** Her iki haftalık sprint bir milestone'dur. Milestone açıklamasında o sprintte kullanılacak teknolojiler yazılıdır.
- **Görevler:** Her görev issue'sunda faz, epik, sprint, başlangıç ve bitiş tarihi, sorumlu, bağımlılıklar, kullanılacak teknolojiler ve kabul kriteri yer alır.
- **Durumlar:** `durum: yapılacak` → `durum: bu sprint` → `durum: devam ediyor` → `durum: incelemede` → kapalı.
- **Diğer etiketler:** `faz-0` … `faz-3`, `rol: …`, `kritik`, `ar-ge`, `platform`, `kvkk`, `opsiyonel`, `tekrarlayan`.

## Planın güncellenmesi

Planın tek kaynağı [`plan/proje-plani.json`](plan/proje-plani.json) dosyasıdır.

```bash
python scripts/plan_olustur.py                       # docs/03 belgesini yeniden üretir
python scripts/github_yukle.py OWNER/REPO            # yeni görevleri GitHub'a ekler (var olanları atlar)
node scripts/teslim/sunum.js                         # sunumu yeniden üretir
node scripts/teslim/ozet.js                          # proje özetini yeniden üretir
```
