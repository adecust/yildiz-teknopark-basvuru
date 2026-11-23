# YTÜ Yıldız Teknopark Başvurusu ve Faz 1 Planı

Kaynağa dayalı Türkçe eğitim YZ'si + eğitim platformu projesinin teknopark başvurusu ve Faz 1 yürütme planı.

## Belgeler
| # | Belge | İçerik |
|---|---|---|
| 01 | [Araştırma raporu](docs/01-yildiz-teknopark-arastirma-raporu.md) | Yıldız Teknopark başvuru süreci, komisyonlar, hakem ölçütleri, kurallar |
| 02 | [Faz yapısı ve kabul analizi](docs/02-faz-yapisi-ve-kabul-analizi.md) | Faz 1 (platform + YZ), Faz 2 (sanal sınıf), puan simülasyonu, 7 zorunlu şart |
| 03 | [Faz 1 kanban ve zaman planı](docs/03-faz1-kanban-ve-zaman-plani.md) | 73 görev, milestone'lar, kritik tarihler, aylık çizelge |
| — | [Kaynak metinler](docs/kaynaklar/) | Yıldız İşletme Yönergesi 2025, İTÜ yönergesi (hakem formu) |

## Proje dosyası (başvuruda kullanılacak)
| # | Belge | İçerik |
|---|---|---|
| 00 | [Yönetici özeti ve künye](docs/proje-dosyasi/00-ozet-ve-kunye.md) | Künye, 1 sayfalık özet, **forma yapıştırılacak hazır metinler** |
| 01 | [Problem, pazar ve rekabet](docs/proje-dosyasi/01-problem-pazar-rekabet.md) | İhtiyaç, pazar, rakip matrisi, ithal ikame ve ihracat |
| 02 | [Ar-Ge ve teknik tasarım](docs/proje-dosyasi/02-ar-ge-ve-teknik-tasarim.md) | AR-1…AR-7 hipotezleri, mimari, algoritmalar, veri modeli, KVKK/AB YZ Yasası |
| 03 | [Test, doğrulama ve senaryolar](docs/proje-dosyasi/03-test-dogrulama-senaryolar.md) | Test setleri, metrikler, deneyler, 8 senaryo, hata türleri analizi, 2 haftalık PoC planı, pilot |
| 04 | [İş planı, ekip, bütçe, ticarileşme](docs/proje-dosyasi/04-is-plani-ekip-butce-ticarilesme.md) | İP'ler, kilometre taşları, kişi-ay, bütçe, fiyatlama, gelir projeksiyonu |
| 05 | [Risk, etki, FMH, hakem hazırlığı](docs/proje-dosyasi/05-risk-etki-fmh-hakem-sunum.md) | Risk tablosu, etkiler, patent stratejisi, 15 hakem sorusu, 13 slayt metni |

## Plan nasıl güncellenir?
Tek doğru kaynak: [`plan/faz1-plan.json`](plan/faz1-plan.json).

```bash
python scripts/plan_olustur.py                 # docs/03 belgesini yeniden üretir
python scripts/github_yukle.py OWNER/REPO      # yeni görevleri issue olarak ekler (var olanları atlar)
```

## Kanban
Her görev bir issue. Kolon durumu `durum:backlog` → `durum:bu-hafta` → `durum:devam` → `durum:inceleme` → kapalı etiketleriyle izlenir. Milestone'lar iş paketlerine karşılık gelir ve son tarihleri taşır.
