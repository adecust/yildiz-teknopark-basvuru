# KAYNAK-YZ Kavram Kanıtı (Prototip)

Ar-Ge çekirdeğinin (kaynağa dayalı Türkçe soru-cevap, cevaplanabilirlik kapısı, iddia doğrulama ve pedagojik sızıntı kontrolü) **tamamen yerel ve açık modellerle** çalışan kavram kanıtıdır. Sonuçlar ve yorum: [`docs/07-arastirma-ve-kavram-kaniti.md`](../docs/07-arastirma-ve-kavram-kaniti.md).

## Dosyalar

| Dosya | İçerik |
|---|---|
| `kaynak_yz.py` | Ortak kütüphane: belge ayrıştırma ve parçalama, Türkçe normalleştirme, BM25 / gömme / RRF / yeniden sıralama, cevaplanabilirlik kapısı, Cosmos T1 çağrısı, NLI doğrulama, istatistik |
| `deney_erisim.py` | E-2 (erişim kolları) ve E-1a (cevaplanabilirlik kapısı, ceza-duyarlı eşik, 5 katlı çapraz doğrulama) |
| `deney_uctan_uca.py` | E-1 uçtan uca: aynı üretimden türetilen 4 kol (talimat, NLI, kapı, kapı + NLI) ve deney sonrası v2 analizi |
| `deney_sizinti.py` | E-4: Sokratik mod, 8 saldırı türü × 5 ödev, 15 meşru soru; deterministik sızıntı tarayıcısı |
| `soru_uret.py` | Otomatik soru üretme denemesi (qwen3:4b); çıktıların çoğu elendiği için Set B elle yazıldı |
| `kaynak_disi_sorular.json` | 47 kaynak dışı soru (anahtar terimlerin derlemde geçmediği otomatik doğrulandı) |
| `sonuclar/*.json` | Toplu sonuçlar (ders içeriği içermez) |
| `veri/`, `sonuclar/ayrinti/` | Ders kaynakları, soru setleri ve soru başına çıktılar. **Repoda değildir** (ders malzemelerinin lisansı) |

## Gereksinimler

- Python 3.12; `torch`, `transformers`, `sentence-transformers`, `rank-bm25`, `snowballstemmer`, `scikit-learn`, `pymupdf`, `python-pptx`, `python-docx`
- [Ollama](https://ollama.com) ve `hf.co/ytu-ce-cosmos/Turkish-Gemma-9b-T1-GGUF:Q4_K_M`
- Hugging Face modelleri: `BAAI/bge-m3`, `ytu-ce-cosmos/turkish-e5-large`, `BAAI/bge-reranker-v2-m3`, `MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7`
- Ölçümler 4 GB GPU'lu (RTX 3050) dizüstü bilgisayarda alındı; betikler bu nedenle modelleri sırayla yükleyip bellekten atar.

## Çalıştırma

```bash
python veri/soru_seti_olustur.py        # Set B (veri/ klasörü gerekir)
python deney_erisim.py
python deney_uctan_uca.py calistir && python deney_uctan_uca.py v2 && python deney_uctan_uca.py ozet
python deney_sizinti.py baglam && python deney_sizinti.py calistir && python deney_sizinti.py ozet
```

`ozet` adımları, cevaplanabilir soruların ve sızıntı çıktılarının **elle değerlendirildiği** dosyaları (`sonuclar/ayrinti/*_degerlendirme.json`) kullanır.
