"""E-1 uçtan uca: kaynağa dayalı cevap üretimi ve reddetme (AR-1), Cosmos T1 ile.

Her soru için üretim BİR kez yapılır; dört kol aynı çıktıdan türetilir (kol farkı modelin rastgeleliğinden değil yöntemden gelir):
  A: yalnızca talimat ("kaynakta yoksa reddet")
  B: A + iddia (cümle) düzeyinde NLI doğrulaması
  C: cevaplanabilirlik kapısı + A
  D: cevaplanabilirlik kapısı + B   (önerilen hat)
Kapı eşiği sonuclar/kapi.json'daki ceza-duyarlı eşiktir (deney_erisim.py). Sorular eşik seçiminde de kullanıldığı için
 her soruya, o sorunun eğitimde kullanılmadığı çapraz doğrulama katının eşiği uygulanır (katlar dışı karar).

Kullanım:
  python deney_uctan_uca.py calistir   # üretim (uzun sürer; kaldığı yerden devam eder)
  python deney_uctan_uca.py ozet       # kolların karşılaştırması (değerlendirme dosyasıyla)
"""
import json
import statistics
import sys
import time

from kaynak_yz import (AYRINTI, KOK, RED, SONUC, VERI, Dizin, Dogrulayici, cevap_istemi, cosmos, dogrula,
                       kaynak_metni, tr_kucuk, wilson)

sys.stdout.reconfigure(encoding="utf-8")
CIKTI = AYRINTI / "uctan_uca.json"
DEGER = AYRINTI / "uctan_uca_degerlendirme.json"  # matematik cevaplarının elle değerlendirmesi
CEZA = 4


def soru_seti():
    sorular = []
    for s in json.loads((VERI / "sorular_gerontoloji.json").read_text(encoding="utf-8")):
        if s["tur"] == "cevapli":
            sorular.append({**s, "ders": "gerontoloji", "kaynakli": "insan"})
    for s in json.loads((VERI / "sentetik_sorular_onayli.json").read_text(encoding="utf-8")):
        if s["ders"] == "matematik" and s.get("uctan_uca"):
            sorular.append(s)
    for s in json.loads((KOK / "kaynak_disi_sorular.json").read_text(encoding="utf-8")):
        sorular.append({**s, "tur": "kaynak_disi"})
    return sorular


def calistir():
    AYRINTI.mkdir(parents=True, exist_ok=True)
    sonuc = json.loads(CIKTI.read_text(encoding="utf-8")) if CIKTI.exists() else []
    biten = {s["id"] for s in sonuc}
    sorular = [s for s in soru_seti() if s["id"] not in biten]
    # 1. aşama: arama (gömme + yeniden sıralama); 4 GB GPU nedeniyle modeller sonra bellekten atılır
    arama, dizinler = {}, {}
    for ders in ("gerontoloji", "matematik"):
        grup = [s for s in sorular if s["ders"] == ders]
        if not grup:
            continue
        d = Dizin(ders, gommeler=("bge-m3",), belirtecler=("snowball",))
        d.onbellekle("bge-m3", [s["soru"] for s in grup])
        for s in grup:
            t0 = time.time()
            secilen, _, kapi = d.ara(s["soru"], k=4)
            arama[s["id"]] = (secilen, kapi, time.time() - t0)
        d.rr = None
        dizinler[ders] = d
    import gc, torch
    gc.collect(); torch.cuda.empty_cache()
    # 2. aşama: üretim (Cosmos, Ollama) ve NLI doğrulaması
    dog = Dogrulayici()
    for ders, d in dizinler.items():
        for s in [x for x in sorular if x["ders"] == ders]:
            secilen, kapi, t_erisim = arama[s["id"]]
            t1 = time.time()
            t0 = t1 - t_erisim
            ham, r = cosmos(cevap_istemi(s["soru"], kaynak_metni(d, secilen)))
            t2 = time.time()
            ham = ham or RED
            if RED.rstrip(".") in ham:
                dogrulanmis, silinen, nli = RED, [], []
            else:
                dogrulanmis, silinen, nli = dogrula(dog, ham, [d.parcalar[i]["cekirdek"] for i in secilen])
            t3 = time.time()
            sonuc.append({**s, "kapi": round(kapi, 4), "getirilen": [d.parcalar[i]["id"] for i in secilen],
                          "ham": ham, "dogrulanmis": dogrulanmis, "silinen": silinen, "nli": nli,
                          "sure": {"erisim": round(t1 - t0, 2), "uretim": round(t2 - t1, 2), "dogrulama": round(t3 - t2, 2)},
                          "token": r.get("eval_count")})
            CIKTI.write_text(json.dumps(sonuc, ensure_ascii=False, indent=1), encoding="utf-8")
            print(f"[{len(sonuc)}] {s['id']} kapı={kapi:.3f} ({t3 - t0:.0f} sn) -> {dogrulanmis[:110]}", flush=True)


def v2():
    """Deney sonrası analiz: saklanan ham cevaplara düzeltilmiş doğrulamayı (dogrula_v2) uygular; üretim tekrarlanmaz."""
    from kaynak_yz import dogrula_v2, parcala
    sonuc = json.loads(CIKTI.read_text(encoding="utf-8"))
    parca = {d: {p["id"]: p["cekirdek"] for p in parcala(d)} for d in ("gerontoloji", "matematik")}
    dog = Dogrulayici()
    for s in sonuc:
        kaynaklar = [parca[s["ders"]][g] for g in s["getirilen"]]
        s["dogrulanmis_v2"], s["silinen_v2"], s["nli_v2"] = dogrula_v2(dog, s["ham"], kaynaklar)
    CIKTI.write_text(json.dumps(sonuc, ensure_ascii=False, indent=1), encoding="utf-8")
    print("v2 uygulandı:", len(sonuc))


def reddetti(m):
    """Genişletilmiş ret tespiti: model reddi kendi cümleleriyle de yapabilir ('kaynaklarda belirtilmemiştir')."""
    from kaynak_yz import ret_mi
    return ret_mi(m)


def ret_iceriyor(m):
    from kaynak_yz import cumlelere_bol, ret_cumlesi_mi, atifsiz
    return any(ret_cumlesi_mi(atifsiz(c)) for c in cumlelere_bol(m))


def ozet():
    sonuc = json.loads(CIKTI.read_text(encoding="utf-8"))
    deger = json.loads(DEGER.read_text(encoding="utf-8"))  # cevaplanabilir soruların ELLE değerlendirmesi
    # Kapı eşiği: her soru için, o sorunun EĞİTİMDE KULLANILMADIĞI çapraz doğrulama katının eşiği (katlar dışı karar).
    # deney_erisim.py'deki StratifiedKFold(5, shuffle=True, random_state=7) bölmesi aynı sırayla yeniden üretilir.
    import numpy as np
    from sklearn.model_selection import StratifiedKFold
    kapi = json.loads((SONUC / "kapi.json").read_text(encoding="utf-8"))
    sira = [s["id"] for s in kapi["puanlar"]["cevapli"]] + [s["id"] for s in kapi["puanlar"]["disarida"]]
    y = np.array([1] * len(kapi["puanlar"]["cevapli"]) + [0] * len(kapi["puanlar"]["disarida"]))
    oof = {}
    for kat, (_, test) in enumerate(StratifiedKFold(5, shuffle=True, random_state=7).split(np.zeros(len(y)), y)):
        for i in test:
            oof[sira[i]] = kapi["ozet"]["tümü"]["cv_esikler"][kat]
    esik = kapi["ozet"]["tümü"]["tum_veri_esigi"]
    kollar = {"A · yalnız talimat": (False, "ham"), "B · + NLI doğrulama (v1)": (False, "dogrulanmis"),
              "C · kapı + talimat": (True, "ham"), "D · kapı + NLI (v1, önceden belirlenen)": (True, "dogrulanmis"),
              "B2 · + NLI doğrulama (v2, deney sonrası)": (False, "dogrulanmis_v2"),
              "D2 · kapı + NLI (v2, deney sonrası)": (True, "dogrulanmis_v2")}
    rapor = {"esik": esik, "kollar": {}, "not": "Kaynak dışı: cevapta açık ret ifadesi varsa doğru ret. Cevaplanabilir: elle değerlendirme."}
    print(f"Kapı eşiği (tüm veri): {esik:.3f}; kat eşikleri {sorted(set(oof.values()))} · n = {len(sonuc)}")
    for ad, (kapili, alan) in kollar.items():
        if alan not in sonuc[0]:
            continue
        say = {"dogru": 0, "yanlis": 0, "yanlis_red": 0, "dogru_red": 0, "uydurma": 0}
        for s in sonuc:
            kapida = kapili and s["kapi"] < oof[s["id"]]
            cevap = RED if kapida else s[alan]
            if s["tur"] == "kaynak_disi":
                say["dogru_red" if (reddetti(cevap) or ret_iceriyor(cevap)) else "uydurma"] += 1
            elif kapida or reddetti(cevap):
                say["yanlis_red"] += 1
            else:
                ok = deger[s["id"]][alan] == "dogru"
                say["dogru" if ok else "yanlis"] += 1
        n1 = say["dogru"] + say["yanlis"] + say["yanlis_red"]
        n0 = say["dogru_red"] + say["uydurma"]
        fayda = (say["dogru"] - CEZA * (say["yanlis"] + say["uydurma"])) / (n0 + n1)
        rapor["kollar"][ad] = {**say, "n_cevapli": n1, "n_kaynak_disi": n0, "ceza_duyarli_puan": fayda,
                               "red_dogrulugu": say["dogru_red"] / n0, "red_ga": wilson(say["dogru_red"], n0),
                               "dogruluk": say["dogru"] / n1, "dogruluk_ga": wilson(say["dogru"], n1),
                               "gereksiz_red": say["yanlis_red"] / n1}
        print(f"{ad:28} doğru {say['dogru']}/{n1}  yanlış {say['yanlis']}  gereksiz ret {say['yanlis_red']}  |  "
              f"doğru ret {say['dogru_red']}/{n0}  uydurma {say['uydurma']}  |  ceza-duyarlı puan {fayda:+.3f}")
    sure = [sum(s["sure"].values()) for s in sonuc]
    uretim = [s["sure"]["uretim"] for s in sonuc]
    rapor["sure"] = {"toplam_p50": statistics.median(sure), "toplam_p95": sorted(sure)[int(0.95 * len(sure)) - 1],
                     "uretim_p50": statistics.median(uretim),
                     "erisim_p50": statistics.median([s["sure"]["erisim"] for s in sonuc]),
                     "dogrulama_p50": statistics.median([s["sure"]["dogrulama"] for s in sonuc])}
    print("Süre (sn):", {k: round(v, 2) for k, v in rapor["sure"].items()})
    (SONUC / "uctan_uca.json").write_text(json.dumps(rapor, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    {"calistir": calistir, "v2": v2, "ozet": ozet}[sys.argv[1]]()
