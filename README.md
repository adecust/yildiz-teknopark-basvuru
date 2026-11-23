# YTÜ Yıldız Teknopark Başvurusu ve Faz 1 Planı

Kaynağa dayalı Türkçe eğitim YZ'si + eğitim platformu projesinin teknopark başvurusu ve Faz 1 yürütme planı.

## Belgeler
| # | Belge | İçerik |
|---|---|---|
| 01 | [Araştırma raporu](docs/01-yildiz-teknopark-arastirma-raporu.md) | Yıldız Teknopark başvuru süreci, komisyonlar, hakem ölçütleri, kurallar |
| 02 | [Faz yapısı ve kabul analizi](docs/02-faz-yapisi-ve-kabul-analizi.md) | Faz 1 (platform + YZ), Faz 2 (sanal sınıf), puan simülasyonu, 7 zorunlu şart |
| 03 | [Faz 1 kanban ve zaman planı](docs/03-faz1-kanban-ve-zaman-plani.md) | 73 görev, milestone'lar, kritik tarihler, aylık çizelge |
| — | [Kaynak metinler](docs/kaynaklar/) | Yıldız İşletme Yönergesi 2025, İTÜ yönergesi (hakem formu) |

## Plan nasıl güncellenir?
Tek doğru kaynak: [`plan/faz1-plan.json`](plan/faz1-plan.json).

```bash
python scripts/plan_olustur.py                 # docs/03 belgesini yeniden üretir
python scripts/github_yukle.py OWNER/REPO      # yeni görevleri issue olarak ekler (var olanları atlar)
```

## Kanban
Her görev bir issue. Kolon durumu `durum:backlog` → `durum:bu-hafta` → `durum:devam` → `durum:inceleme` → kapalı etiketleriyle izlenir. Milestone'lar iş paketlerine karşılık gelir ve son tarihleri taşır.
