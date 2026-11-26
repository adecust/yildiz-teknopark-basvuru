"""KAYNAK-YZ kavram kanıtı: çekirdek bileşenler.

Tamamen yerel ve açık modellerle çalışır:
  - Gömme: BAAI/bge-m3, ytu-ce-cosmos/turkish-e5-large
  - Yeniden sıralama ve cevaplanabilirlik kapısı: BAAI/bge-reranker-v2-m3
  - İddia doğrulama: MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7
  - Üretim: ytu-ce-cosmos/Turkish-Gemma-9b-T1 (Ollama, Q4_K_M)

Bu dosya deney betiklerinin ortak kütüphanesidir; doğrudan çalıştırılmaz.
"""
import json
import re
import unicodedata
import urllib.request
from pathlib import Path

KOK = Path(__file__).resolve().parent
VERI = KOK / "veri"
SONUC = KOK / "sonuclar"
AYRINTI = SONUC / "ayrinti"
DERSLER = {"gerontoloji": VERI / "gerontoloji", "matematik": VERI / "matematik"}

URETIM_MODELI = "hf.co/ytu-ce-cosmos/Turkish-Gemma-9b-T1-GGUF:Q4_K_M"
NLI_MODELI = "MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7"
RERANKER = "BAAI/bge-reranker-v2-m3"
GOMMELER = {
    "bge-m3": {"ad": "BAAI/bge-m3", "sorgu": "", "belge": ""},
    "turkish-e5-large": {"ad": "ytu-ce-cosmos/turkish-e5-large", "sorgu": "query: ", "belge": "passage: "},
}
RED = "Bu sorunun cevabı ders kaynaklarında yer almıyor."
PARCA_KARAKTER = 900


# ---------------------------------------------------------------- Türkçe metin işleme
def tr_kucuk(m: str) -> str:
    """Türkçeye özgü küçük harfe çevirme. str.lower() 'I'yı 'i' yapar; Türkçede 'ı' olmalıdır."""
    m = unicodedata.normalize("NFC", m)
    return m.replace("I", "ı").replace("İ", "i").lower()


SADE = str.maketrans("çğıöşüâîû", "cgiosuaiu")


def sadelestir(m: str) -> str:
    """Şapka ve Türkçe karakterleri kaldırır ('kâr' = 'kar', 'ogrenci' = 'öğrenci' eşleşmesi için)."""
    return tr_kucuk(m).translate(SADE)


KELIME = re.compile(r"[a-zçğıöşüâîû0-9]+")
_stemmer = None


def belirtec(m: str, yontem: str) -> list:
    """BM25 için belirteçler. yontem: ham | onek5 | snowball."""
    global _stemmer
    kelimeler = [w for w in KELIME.findall(tr_kucuk(m)) if len(w) > 1]
    if yontem == "ham":
        return [w.translate(SADE) for w in kelimeler]
    if yontem == "onek5":
        return [w.translate(SADE)[:5] for w in kelimeler]
    if yontem == "snowball":
        if _stemmer is None:
            import snowballstemmer
            _stemmer = snowballstemmer.stemmer("turkish")
        return [w.translate(SADE) for w in _stemmer.stemWords(kelimeler)]
    raise ValueError(yontem)


# ---------------------------------------------------------------- Belge ayrıştırma ve parçalama
def _temizle(m):
    m = re.sub(r"[ \t]+", " ", m)
    return re.sub(r"\n\s*\n+", "\n", m).strip()


def gurultu_mu(m: str) -> bool:
    """Vikipedi gezinme kutuları, otorite kontrolü ve bağlantı listeleri gibi içerik dışı parçalar."""
    if "Otorite kontrolü" in m or "action=edit" in m or "web.archive.org" in m:
        return True
    return m.count("·") >= 8


def parcala(ders: str) -> list:
    """Bir dersin tüm kaynaklarını yapıyı koruyarak parçalara böler.
    pptx: 1 slayt = 1 parça (+ ders konusu ve önceki slayt bağlamı)
    docx: ara başlık altında ≤ 900 karakterlik cümle grupları
    pdf : sayfa içinde 900 karakterlik, 150 karakter örtüşmeli pencereler
    """
    klasor = DERSLER[ders]
    parcalar = []

    def ekle(dosya, yer, on, govde):
        if gurultu_mu(govde):
            return
        parcalar.append({"id": f"{dosya.stem} {yer}", "ders": ders, "kaynak": dosya.stem, "yer": yer,
                         "metin": on + govde, "cekirdek": govde})

    for dosya in sorted(klasor.iterdir()):
        uz = dosya.suffix.lower()
        if uz == ".pptx":
            from pptx import Presentation
            slaytlar = []
            for slayt in Presentation(dosya).slides:
                t = [sh.text_frame.text for sh in slayt.shapes if sh.has_text_frame]
                if slayt.has_notes_slide:
                    t.append(slayt.notes_slide.notes_text_frame.text)
                slaytlar.append(_temizle("\n".join(t)))
            konu = " - ".join(slaytlar[0].splitlines()[:2]) if slaytlar else dosya.stem
            for no, metin in enumerate(slaytlar, 1):
                if len(metin) < 15 or metin.upper().startswith("KAYNAK"):
                    continue
                onceki = slaytlar[no - 2][:300] if no > 1 else ""
                on = f"[Ders konusu: {konu}]\n" + (f"[Önceki slayt: {onceki}]\n" if onceki else "")
                ekle(dosya, f"slayt {no}", on, metin)
        elif uz == ".docx":
            import docx
            paragraflar = [p.text.strip() for p in docx.Document(dosya).paragraphs if p.text.strip()]
            baslik, alt, tampon, no = paragraflar[0], "", "", 0

            def bosalt():
                nonlocal tampon, no
                if tampon.strip():
                    no += 1
                    ekle(dosya, f"bölüm {no}", f"[Belge: {baslik}" + (f" / {alt}" if alt else "") + "]\n", tampon.strip())
                tampon = ""

            for p in paragraflar[1:]:
                if len(p) < 60 and not p.endswith("."):
                    bosalt(); alt = p; continue
                for c in re.split(r"(?<=[.!?])\s+", p):
                    if len(tampon) + len(c) > PARCA_KARAKTER:
                        bosalt()
                    tampon += c + " "
                tampon += "\n"
            bosalt()
        elif uz == ".pdf":
            import pymupdf
            for no, s in enumerate(pymupdf.open(dosya), 1):
                m = _temizle(s.get_text())
                for i in range(0, len(m), PARCA_KARAKTER - 150):
                    if len(m[i:i + PARCA_KARAKTER]) > 80:
                        ekle(dosya, f"s.{no}#{i // (PARCA_KARAKTER - 150) + 1}", f"[Belge: {dosya.stem}]\n", m[i:i + PARCA_KARAKTER])
    return parcalar


# ---------------------------------------------------------------- Dizin ve arama
class Dizin:
    """Bir dersin parçaları üzerinde seyrek (BM25), yoğun (gömme) ve yeniden sıralamalı arama."""

    def __init__(self, ders, gommeler=("bge-m3",), belirtecler=("ham", "onek5", "snowball"), cihaz="cuda"):
        import torch
        from rank_bm25 import BM25Okapi
        from sentence_transformers import SentenceTransformer
        self.np = __import__("numpy")
        self.parcalar = parcala(ders)
        self.idx = {p["id"]: i for i, p in enumerate(self.parcalar)}
        self.bm25 = {y: BM25Okapi([belirtec(p["metin"], y) for p in self.parcalar]) for y in belirtecler}
        self.gom, self.V, self.qv = {}, {}, {}
        self.cihaz = cihaz
        for g in gommeler:
            c = GOMMELER[g]
            self.gom[g] = SentenceTransformer(c["ad"], device=cihaz, model_kwargs={"torch_dtype": torch.float16})
            self.V[g] = self.gom[g].encode([c["belge"] + p["metin"] for p in self.parcalar], normalize_embeddings=True, batch_size=8)
        self.rr = None

    def onbellekle(self, gomme, sorular):
        """4 GB GPU için: soruları önceden kodlayıp gömme modelini bellekten atar (yogun() önbellekten okur)."""
        c = GOMMELER[gomme]
        v = self.gom[gomme].encode([c["sorgu"] + s for s in sorular], normalize_embeddings=True, batch_size=16)
        self.qv.setdefault(gomme, {}).update(dict(zip(sorular, v)))
        del self.gom[gomme]
        import gc, torch
        gc.collect(); torch.cuda.empty_cache()

    def seyrek(self, soru, yontem, k=20):
        p = self.bm25[yontem].get_scores(belirtec(soru, yontem))
        return [int(i) for i in self.np.argsort(-p)[:k]]

    def yogun(self, soru, gomme, k=20):
        if soru in self.qv.get(gomme, {}):
            q = self.qv[gomme][soru]
        else:
            q = self.gom[gomme].encode([GOMMELER[gomme]["sorgu"] + soru], normalize_embeddings=True)[0]
        return [int(i) for i in self.np.argsort(-(self.V[gomme] @ q))[:k]]

    @staticmethod
    def rrf(*listeler, k=60, n=20):
        p = {}
        for liste in listeler:
            for sira, i in enumerate(liste):
                p[i] = p.get(i, 0) + 1 / (k + sira + 1)
        return sorted(p, key=p.get, reverse=True)[:n]

    def yeniden_sirala(self, soru, adaylar):
        """(sıralı parça indeksleri, puanlar). Puan 0–1 arası (sigmoid)."""
        if self.rr is None:
            import torch
            from sentence_transformers import CrossEncoder
            self.rr = CrossEncoder(RERANKER, device=self.cihaz, model_kwargs={"torch_dtype": torch.float16})
        if not adaylar:
            return [], []
        p = self.rr.predict([(soru, self.parcalar[i]["metin"]) for i in adaylar])
        sira = self.np.argsort(-p)
        return [adaylar[j] for j in sira], [float(p[j]) for j in sira]

    def ara(self, soru, gomme="bge-m3", yontem="snowball", k=5):
        """Tam hat: hibrit (yoğun + seyrek) → RRF → yeniden sıralama. (parça indeksleri, puanlar, kapı puanı)"""
        adaylar = self.rrf(self.yogun(soru, gomme), self.seyrek(soru, yontem))
        sirali, puan = self.yeniden_sirala(soru, adaylar)
        return sirali[:k], puan[:k], (puan[0] if puan else 0.0)


# ---------------------------------------------------------------- Üretim (Ollama)
def ollama(prompt, model=URETIM_MODELI, en_fazla=500, sicaklik=0.1, ham=False, dusun=None, bicim=None, baglam=6144):
    govde = {"model": model, "prompt": prompt, "stream": False, "raw": ham,
             "options": {"num_ctx": baglam, "temperature": sicaklik, "num_predict": en_fazla}}
    if dusun is not None:
        govde["think"] = dusun
    if bicim:
        govde["format"] = bicim
    istek = urllib.request.Request("http://localhost:11434/api/generate", json.dumps(govde).encode(), {"Content-Type": "application/json"})
    with urllib.request.urlopen(istek, timeout=1200) as r:
        return json.loads(r.read())


DUSUNME_ATLA = "<think>\nKaynaklara bakarak doğrudan cevaplıyorum.\n</think>\n\n"


def cosmos(kullanici, en_fazla=450):
    """Cosmos T1 (Gemma sohbet şablonu); düşünme adımı atlanır (gecikme için)."""
    prompt = f"<start_of_turn>user\n{kullanici}<end_of_turn>\n<start_of_turn>model\n{DUSUNME_ATLA}"
    r = ollama(prompt, ham=True, en_fazla=en_fazla)
    return re.sub(r"<think>.*?(</think>|$)", "", r["response"], flags=re.S).strip(), r


def cevap_istemi(soru, kaynak_metni):
    return ("Sen bir ders asistanısın. Yalnızca aşağıdaki KAYNAKLAR'daki bilgiyi kullan, kendi bilgini ekleme.\n"
            "Kaynakta yalnızca adı geçen bir kavramı açıklama; açıklaması kaynakta yoksa cevap yok say.\n"
            "Her cümlenin sonuna dayandığın kaynağı [K1] biçiminde yaz.\n"
            f"Cevap kaynaklarda yoksa yalnızca şunu yaz: \"{RED}\"\n"
            "Kısa ve açık Türkçe kullan (en fazla 4 cümle). Kaynaklar hakkında yorum cümlesi yazma.\n\n"
            f"KAYNAKLAR:\n{kaynak_metni}\n\nSORU: {soru}")


def kaynak_metni(dizin, secilen):
    return "\n\n".join(f"[K{n}] ({dizin.parcalar[i]['kaynak']}, {dizin.parcalar[i]['yer']})\n{dizin.parcalar[i]['metin']}"
                       for n, i in enumerate(secilen, 1))


# ---------------------------------------------------------------- İddia doğrulama (NLI)
KISALTMA = r"(?<!Öğr\.)(?<!Gör\.)(?<!Dr\.)(?<!Prof\.)(?<!Doç\.)(?<!vb\.)(?<!ör\.)(?<!bkz\.)(?<![0-9]\.)"


def cumlelere_bol(m):
    m = re.sub(r"\*\*|^#+\s*|^\s*[-*]\s+", "", m, flags=re.M)
    parcalar = [c.strip() for c in re.split(KISALTMA + r"(?<=[.!?])\s+|\n+", m) if c.strip()]
    sonuc = []
    for c in parcalar:
        if re.fullmatch(r"(\[K[\d,\sK-]*\]\s*)+\.?", c) and sonuc:
            sonuc[-1] += " " + c
        else:
            sonuc.append(c)
    return sonuc


def atifsiz(c):
    return re.sub(r"\s*\[K[\d,\sK-]*\]", "", c).strip()


class Dogrulayici:
    """Her cümlenin getirilen kaynak parçalarınca desteklenip desteklenmediğini ölçer (çok dilli NLI)."""

    def __init__(self, cihaz="cuda"):
        import torch
        from transformers import AutoModelForSequenceClassification, AutoTokenizer
        self.torch, self.cihaz = torch, cihaz
        self.tok = AutoTokenizer.from_pretrained(NLI_MODELI)
        self.m = AutoModelForSequenceClassification.from_pretrained(NLI_MODELI).to(cihaz).eval()
        self.ent = [i for i, l in self.m.config.id2label.items() if l.lower().startswith("entail")][0]

    def puan(self, cumle, kaynaklar):
        if not kaynaklar:
            return 0.0
        x = self.tok(kaynaklar, [cumle] * len(kaynaklar), truncation="only_first", max_length=512,
                     padding=True, return_tensors="pt").to(self.cihaz)
        with self.torch.no_grad():
            p = self.m(**x).logits.softmax(-1)[:, self.ent]
        return float(p.max())


def sozcuk_destegi(cumle, kaynaklar):
    """Cümledeki sayıların hepsi kaynakta geçiyorsa, içerik kelimelerinin kaynakta bulunma oranı; geçmiyorsa 0."""
    kaynak = " ".join(kaynaklar)
    if any(s not in kaynak for s in re.findall(r"\d+(?:[.,]\d+)?", cumle)):
        return 0.0
    kk = set(belirtec(kaynak, "onek5"))
    ck = [w for w in belirtec(cumle, "onek5") if len(w) > 2]
    return sum(w in kk for w in ck) / len(ck) if ck else 0.0


def dogrula(dogrulayici, cevap, kaynaklar, esik=0.5):
    """Desteklenmeyen cümleleri çıkarır. İlk (ana) cümle desteklenmiyorsa cevabın tamamı reddedilir."""
    kalan, silinen, puanlar = [], [], []
    for n, c in enumerate(cumlelere_bol(cevap)):
        p, w = dogrulayici.puan(atifsiz(c), kaynaklar), sozcuk_destegi(atifsiz(c), kaynaklar)
        puanlar.append([round(p, 3), round(w, 2)])
        if p >= esik or w >= 0.75:
            kalan.append(c)
        elif n == 0 or c.rstrip().endswith(":"):
            return RED, cumlelere_bol(cevap), puanlar
        else:
            silinen.append(c)
    return (" ".join(kalan) if kalan else RED), silinen, puanlar


RET_KALIBI = re.compile(
    r"(kaynak(lar)?(ın)?da (yer )?(almıyor|almamaktadır|bulunmuyor|bulunmamaktadır|belirtilmemiş|belirtilmiyor|tanımlanmamış|geçmiyor|yok)"
    r"|bilgi (bulunmamaktadır|bulunmuyor|yer almıyor|yok)|veri bulunmamaktadır|ders kaynaklarında yer almıyor)", re.I)


def ret_cumlesi_mi(c):
    return bool(RET_KALIBI.search(tr_kucuk(c)))


def ret_mi(cevap):
    """Cevap (tamamı) bir ret mi? İçerik cümlesi kalmamışsa ret sayılır."""
    cumleler = [atifsiz(c) for c in cumlelere_bol(cevap)]
    cumleler = [c for c in cumleler if c and not re.fullmatch(r"[\W\d]*", c)]
    return not cumleler or all(ret_cumlesi_mi(c) for c in cumleler)


def dogrula_v2(dogrulayici, cevap, kaynaklar, esik=0.5):
    """Deney sonrası düzeltilmiş doğrulama (v2):
    - Ret cümleleri doğrulamadan muaf tutulur ve korunur (kısmi ret mümkün olur);
    - içerik cümlesi yalnızca NLI ile kabul edilir (sözcük örtüşmesi yedeği kaldırıldı; matematikte gevşek bulundu);
    - içerik cümlelerinin hiçbiri desteklenmiyorsa cevap reddedilir."""
    kalan, silinen, puanlar, icerik_kaldi = [], [], [], False
    for c in cumlelere_bol(cevap):
        a = atifsiz(c)
        if not a or re.fullmatch(r"[\W\d]*", a):
            continue
        if ret_cumlesi_mi(a):
            kalan.append(c); continue
        p = dogrulayici.puan(a, kaynaklar)
        puanlar.append(round(p, 3))
        if p >= esik:
            kalan.append(c); icerik_kaldi = True
        else:
            silinen.append(c)
    if not icerik_kaldi:
        return RED, silinen, puanlar
    return " ".join(kalan), silinen, puanlar


# ---------------------------------------------------------------- İstatistik
def wilson(k, n, z=1.96):
    """Oran için Wilson %95 güven aralığı."""
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    d = 1 + z * z / n
    m = (p + z * z / (2 * n)) / d
    h = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5) / d
    return (max(0.0, m - h), min(1.0, m + h))


def bootstrap(degerler, b=2000, tohum=7):
    """Ortalama için yüzdelik bootstrap %95 güven aralığı."""
    import numpy as np
    r = np.random.default_rng(tohum)
    d = np.asarray(degerler, dtype=float)
    o = [d[r.integers(0, len(d), len(d))].mean() for _ in range(b)]
    return float(np.percentile(o, 2.5)), float(np.percentile(o, 97.5))


def yuzde(x):
    return f"%{100 * x:.1f}".replace(".", ",")
