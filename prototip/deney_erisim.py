"""E-2 (erişim yapılandırması, AR-2) ve E-1a (cevaplanabilirlik kapısı, AR-1) deneyleri.

Soru setleri:
  - Set A: veri/sorular_gerontoloji.json içindeki C01–C24 (önceki prototip seti; altın konum etiketli)
  - Set B: veri/sentetik_sorular_onayli.json (bu çalışmada proje ekibince yazıldı; altın parça kanıt ifadesinden otomatik)
  - Kaynak dışı: kaynak_disi_sorular.json (derlemde geçmediği otomatik doğrulandı)
Çıktı: sonuclar/erisim.json, sonuclar/kapi.json ve ekrana özet tablo.
Kullanım: python deney_erisim.py
"""
import json
import sys

import numpy as np

from kaynak_yz import SONUC, VERI, KOK, Dizin, bootstrap, tr_kucuk, wilson

sys.stdout.reconfigure(encoding="utf-8")
CEZA = 4  # yanlış cevabın maliyeti (doğru +1, yanlış −4, ret 0); arXiv:2608.26385 ile aynı şema


def insan_sorulari(dizin):
    """C-sorularının altın parçaları: slayt verilmişse o slayt; yalnız dosya verilmişse o dosyada anahtar geçen parçalar."""
    sonuc = []
    for s in json.loads((VERI / "sorular_gerontoloji.json").read_text(encoding="utf-8")):
        if s["tur"] != "cevapli":
            continue
        k = s["kaynak"].replace("ders izlencesi", "00-ders-izlencesi")
        dosya = k.split()[0]
        if "slayt" in k:
            altin = [k] if k in dizin.idx else []
        else:
            anahtar = [tr_kucuk(a) for a in s["anahtar"]]
            altin = [p["id"] for p in dizin.parcalar if p["kaynak"] == dosya and any(a in tr_kucuk(p["cekirdek"]) for a in anahtar)]
        if not altin:
            print("UYARI: altın parça bulunamadı", s["id"], k)
            continue
        sonuc.append({"id": s["id"], "ders": "gerontoloji", "kaynakli": "A", "soru": s["soru"], "altin": altin})
    return sonuc


def kollar(d):
    """Her kol: soru -> sıralı parça indeksleri (ilk 10)."""
    return {
        "BM25 (ham sözcük)": lambda q: d.seyrek(q, "ham", 10),
        "BM25 (5 harf önek)": lambda q: d.seyrek(q, "onek5", 10),
        "BM25 (Snowball Türkçe kök)": lambda q: d.seyrek(q, "snowball", 10),
        "Yoğun: bge-m3": lambda q: d.yogun(q, "bge-m3", 10),
        "Yoğun: turkish-e5-large (YTÜ)": lambda q: d.yogun(q, "turkish-e5-large", 10),
        "Hibrit: bge-m3 + Snowball (RRF)": lambda q: d.rrf(d.yogun(q, "bge-m3"), d.seyrek(q, "snowball"), n=10),
        "Hibrit: e5 + Snowball (RRF)": lambda q: d.rrf(d.yogun(q, "turkish-e5-large"), d.seyrek(q, "snowball"), n=10),
        "Hibrit (bge-m3) + yeniden sıralama": lambda q: d.yeniden_sirala(q, d.rrf(d.yogun(q, "bge-m3"), d.seyrek(q, "snowball")))[0][:10],
        "Hibrit (üçlü) + yeniden sıralama": lambda q: d.yeniden_sirala(q, d.rrf(d.yogun(q, "bge-m3"), d.yogun(q, "turkish-e5-large"), d.seyrek(q, "snowball")))[0][:10],
    }


def sira_olcutleri(sirali, altin_idx):
    r = next((n for n, i in enumerate(sirali, 1) if i in altin_idx), None)
    return {"r1": float(r == 1), "r5": float(r is not None and r <= 5), "mrr": 1 / r if r else 0.0}


def kapi_analizi(cevapli, disarida):
    """Cevaplanabilir (y=1) ve kaynak dışı (y=0) soruların kapı puanlarından eşik seçimi ve başarım.
    Eşik, ceza-duyarlı faydayı en büyükleyen değer olarak 5 katlı çapraz doğrulamayla seçilir."""
    from sklearn.metrics import roc_auc_score
    from sklearn.model_selection import StratifiedKFold
    X = np.array([s["kapi"] for s in cevapli] + [s["kapi"] for s in disarida])
    y = np.array([1] * len(cevapli) + [0] * len(disarida))
    bulundu = np.array([s["bulundu"] for s in cevapli] + [0] * len(disarida))  # altın parça ilk 5'te mi

    def fayda(esik, idx):
        kabul = X[idx] >= esik
        dogru = kabul & (y[idx] == 1) & (bulundu[idx] == 1)
        yanlis = kabul & ~((y[idx] == 1) & (bulundu[idx] == 1))
        return dogru.sum() - CEZA * yanlis.sum()

    adaylar = np.unique(np.concatenate([X, [0.0, 1.0]]))
    tahmin = np.zeros(len(X), dtype=bool)
    esikler = []
    for egitim, test in StratifiedKFold(5, shuffle=True, random_state=7).split(X, y):
        e = max(adaylar, key=lambda t: fayda(t, egitim))
        esikler.append(float(e))
        tahmin[test] = X[test] >= e
    ret_dogru = int((~tahmin[y == 0]).sum()); n0 = int((y == 0).sum())
    gereksiz = int((~tahmin[y == 1]).sum()); n1 = int((y == 1).sum())
    tum_esik = float(max(adaylar, key=lambda t: fayda(t, np.arange(len(X)))))
    return {
        "auc": float(roc_auc_score(y, X)),
        "cv_esikler": esikler, "tum_veri_esigi": tum_esik,
        "red_dogrulugu": ret_dogru / n0, "red_ga": wilson(ret_dogru, n0), "n_kaynak_disi": n0,
        "gereksiz_red": gereksiz / n1, "gereksiz_ga": wilson(gereksiz, n1), "n_cevapli": n1,
    }


def main():
    sentetik = json.loads((VERI / "sentetik_sorular_onayli.json").read_text(encoding="utf-8"))
    disarida_tum = json.loads((KOK / "kaynak_disi_sorular.json").read_text(encoding="utf-8"))
    satirlar, kayit, kapi_kayit = {}, {}, {"cevapli": [], "disarida": []}
    for ders in ("gerontoloji", "matematik"):
        d = Dizin(ders, gommeler=("bge-m3", "turkish-e5-large"))
        sorular = (insan_sorulari(d) if ders == "gerontoloji" else []) + [{**s, "kaynakli": "B"} for s in sentetik if s["ders"] == ders]
        tum = [s["soru"] for s in sorular] + [x["soru"] for x in disarida_tum if x["ders"] == ders]
        for g in ("bge-m3", "turkish-e5-large"):  # 4 GB GPU: önce kodla, sonra modeli bellekten at
            d.onbellekle(g, tum)
        print(f"{ders}: {len(d.parcalar)} parça, {len(sorular)} cevaplanabilir soru", flush=True)
        for ad, f in kollar(d).items():
            for s in sorular:
                altin = {d.idx[a] for a in s["altin"] if a in d.idx}
                o = sira_olcutleri(f(s["soru"]), altin)
                satirlar.setdefault(ad, []).append({**o, "kaynakli": s["kaynakli"], "ders": ders})
        # Kapı: tam hattın (hibrit bge-m3 + yeniden sıralama) en yüksek puanı
        for s in sorular:
            sirali, puan, kapi = d.ara(s["soru"])
            altin = {d.idx[a] for a in s["altin"] if a in d.idx}
            kapi_kayit["cevapli"].append({"id": s["id"], "ders": ders, "kaynakli": s["kaynakli"], "kapi": kapi,
                                          "bulundu": int(any(i in altin for i in sirali[:5]))})
        for s in [x for x in disarida_tum if x["ders"] == ders]:
            kapi_kayit["disarida"].append({"id": s["id"], "ders": ders, "kapi": d.ara(s["soru"])[2]})
        del d

    print("\n=== E-2 · Erişim (Recall@k, MRR@10; köşeli parantez: %95 bootstrap GA) ===")
    for grup in ("tümü", "A", "B"):
        print(f"\n--- {grup} ---")
        for ad, r in satirlar.items():
            r = [x for x in r if grup == "tümü" or x["kaynakli"] == grup]
            if not r:
                continue
            o = {m: float(np.mean([x[m] for x in r])) for m in ("r1", "r5", "mrr")}
            ga = bootstrap([x["r5"] for x in r])
            kayit.setdefault(grup, {})[ad] = {**o, "r5_ga": ga, "n": len(r)}
            print(f"{ad:38} n={len(r):3}  R@1 {o['r1']:.3f}  R@5 {o['r5']:.3f} [{ga[0]:.2f}–{ga[1]:.2f}]  MRR {o['mrr']:.3f}")

    # Eşleştirilmiş fark: tam hat - en iyi tekil yöntem
    tam = "Hibrit (bge-m3) + yeniden sıralama"
    tekil = ["BM25 (Snowball Türkçe kök)", "Yoğun: bge-m3", "Yoğun: turkish-e5-large (YTÜ)", "BM25 (ham sözcük)", "BM25 (5 harf önek)"]
    en_iyi = max(tekil, key=lambda a: np.mean([x["r5"] for x in satirlar[a]]))
    fark = [a["r5"] - b["r5"] for a, b in zip(satirlar[tam], satirlar[en_iyi])]
    kayit["fark"] = {"kol": tam, "karsi": en_iyi, "ort": float(np.mean(fark)), "ga": bootstrap(fark)}
    print(f"\nEşleştirilmiş fark (R@5): '{tam}' − '{en_iyi}' = {np.mean(fark):+.3f}  GA {bootstrap(fark)}")

    print("\n=== E-1a · Cevaplanabilirlik kapısı (ceza: doğru +1, yanlış −4, ret 0; 5 katlı ÇD) ===")
    kapi = {}
    for grup in ("tümü", "A"):
        cev = [s for s in kapi_kayit["cevapli"] if grup == "tümü" or s["kaynakli"] == "A"]
        dis = [s for s in kapi_kayit["disarida"] if grup == "tümü" or s["ders"] == "gerontoloji"]
        k = kapi_analizi(cev, dis)
        kapi[grup] = k
        print(f"[{grup}] AUC {k['auc']:.3f} | doğru ret {k['red_dogrulugu']:.3f} [{k['red_ga'][0]:.2f}–{k['red_ga'][1]:.2f}] (n={k['n_kaynak_disi']}) | "
              f"gereksiz ret {k['gereksiz_red']:.3f} [{k['gereksiz_ga'][0]:.2f}–{k['gereksiz_ga'][1]:.2f}] (n={k['n_cevapli']}) | eşik {k['tum_veri_esigi']:.3f}")
    SONUC.mkdir(exist_ok=True)
    (SONUC / "erisim.json").write_text(json.dumps(kayit, ensure_ascii=False, indent=1), encoding="utf-8")
    (SONUC / "kapi.json").write_text(json.dumps({"ozet": kapi, "puanlar": kapi_kayit}, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
