"""Erişim test seti için parça başına sentetik soru üretir (TS-RET genişletmesi).

Soru üreten model (qwen3:4b) cevap üreten modelden (Cosmos T1) bilinçli olarak farklıdır.
Modelden metindeki ifadeleri kopyalamadan, öğrenci ağzıyla soru yazması istenir; altın parça,
sorunun üretildiği parçadır. Çıktı: veri/sentetik_sorular.json (ders içeriği içerdiği için repoya girmez).
Kullanım: python soru_uret.py
"""
import json
import sys

from kaynak_yz import VERI, ollama, parcala

sys.stdout.reconfigure(encoding="utf-8")
MODEL = "qwen3:4b"
CIKTI = VERI / "sentetik_sorular.json"

ISTEM = """Aşağıda bir dersin kaynağından bir bölüm var. Bu bölümü okumuş bir öğrencinin sorabileceği TEK bir soru yaz.
Kurallar:
- Soru yalnızca bu bölümdeki bilgiyle cevaplanabilmeli.
- Bölümdeki cümleleri ve kelime dizilerini aynen kopyalama; öğrencinin kendi kelimeleriyle soracağı gibi yaz.
- Soru tek başına anlaşılır olsun ("bu bölümde", "metinde" gibi ifadeler kullanma).
- Kısa cevabı da yaz.
Yalnızca şu JSON biçiminde cevap ver: {{"soru": "...", "cevap": "..."}}

BÖLÜM:
{metin}"""


def main():
    sonuc = json.loads(CIKTI.read_text(encoding="utf-8")) if CIKTI.exists() else []
    biten = {s["altin"][0] for s in sonuc}
    for ders in ("gerontoloji", "matematik"):
        for p in parcala(ders):
            if p["id"] in biten or len(p["cekirdek"]) < 120:
                continue
            try:
                r = ollama(ISTEM.format(metin=p["cekirdek"]), model=MODEL, dusun=False, bicim="json",
                           en_fazla=300, sicaklik=0.3, baglam=4096)
                j = json.loads(r["response"])
                soru, cevap = j["soru"].strip(), j["cevap"].strip()
            except Exception as e:  # noqa: BLE001
                print("atlandı", p["id"], e)
                continue
            sonuc.append({"id": f"S{len(sonuc) + 1:03d}", "ders": ders, "tur": "cevapli", "kaynakli": "sentetik",
                          "soru": soru, "beklenen": cevap, "altin": [p["id"]]})
            CIKTI.write_text(json.dumps(sonuc, ensure_ascii=False, indent=1), encoding="utf-8")
            print(len(sonuc), p["id"], "|", soru, flush=True)


if __name__ == "__main__":
    main()
