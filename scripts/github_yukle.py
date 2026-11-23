"""plan/backlog.json içeriğini GitHub reposuna ürün backlog'u olarak aktarır.

Oluşturulanlar:
  - Etiketler: tür, öncelik, hikâye puanı, faz, rol, durum
  - Milestone'lar: hazırlık dönemi, Faz 1'in 26 sprinti, sürekli işler, Faz 2 ve Faz 3 yol haritası
  - Epik issue'ları ve bunlara alt iş olarak bağlı kullanıcı hikâyeleri, Ar-Ge araştırmaları ve görevler

Kullanım:
  python scripts/github_yukle.py OWNER/REPO [--bugun YYYY-MM-DD] [--sifirla]
  --sifirla : önce repodaki tüm issue, milestone ve etiketleri siler (geri alınamaz).
"""
import argparse
import json
import subprocess
import sys
import time
import urllib.parse
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from plan_olustur import (yukle, hazirla, sprint_ad, hikaye_cumlesi, kk_satirlari, t, tr,  # noqa: E402
                          TIP_AD, ONCELIK, M_BASVURU, M_DEGER, M_SUREKLI, M_F2, M_F3)

TUR_ETIKET = {"epik": "tür: epik", "hikaye": "tür: kullanıcı hikâyesi", "arastirma": "tür: Ar-Ge araştırması", "gorev": "tür: görev"}
ONC_ETIKET = {"P1": "öncelik: olmazsa olmaz", "P2": "öncelik: olmalı", "P3": "öncelik: olabilir"}
RENK = {
    "tür: epik": "0B3D3A", "tür: kullanıcı hikâyesi": "1D76DB", "tür: Ar-Ge araştırması": "D93F0B", "tür: görev": "5B6770",
    "öncelik: olmazsa olmaz": "B60205", "öncelik: olmalı": "FBCA04", "öncelik: olabilir": "C5DEF5",
    "faz-0": "BFD4F2", "faz-1": "14786E", "faz-2": "2E5E8C", "faz-3": "8FC1B5",
    "durum: yapılacak": "EDEDED", "durum: bu sprint": "F2A541", "durum: devam ediyor": "0E8A16", "durum: incelemede": "D4C5F9",
}
DOD = {
    "hikaye": ["Kod incelemesinden geçti", "Birim ve entegrasyon testleri yazıldı ve geçiyor", "Kabul kriterleri test ortamında doğrulandı",
               "Güvenlik, KVKK ve erişilebilirlik kontrolleri yapıldı", "Kullanıcı ve teknik dokümantasyon güncellendi"],
    "arastirma": ["Deney tasarımı ve kullanılan veri seti kayıt altına alındı", "Sonuçlar %95 güven aralığıyla raporlandı ve repoya eklendi",
                  "Kararlar teknoloji kararları belgesine işlendi", "Gerekliyse değerlendirme düzeneğine regresyon testi eklendi"],
    "gorev": ["Kabul kriterleri karşılandı", "Çıktılar ve belgeler repoya eklendi"],
}


def gh(method, path, body=None, izin_hata=False):
    cmd = ["gh", "api", "-X", method, path, "-H", "Accept: application/vnd.github+json"]
    if body is not None:
        cmd += ["--input", "-"]
    r = subprocess.run(cmd, input=json.dumps(body) if body is not None else None, capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        if izin_hata:
            return None
        raise RuntimeError(f"{method} {path}: {r.stderr.strip() or r.stdout.strip()}")
    return json.loads(r.stdout) if r.stdout.strip() else None


def hepsi(path):
    sonuc, s = [], 1
    while True:
        parca = gh("GET", f"{path}{'&' if '?' in path else '?'}per_page=100&page={s}")
        sonuc += parca
        if len(parca) < 100:
            return sonuc
        s += 1


def sifirla(repo):
    for i in hepsi(f"repos/{repo}/issues?state=all"):
        if "pull_request" not in i:
            subprocess.run(["gh", "issue", "delete", str(i["number"]), "--repo", repo, "--yes"], capture_output=True)
    for m in hepsi(f"repos/{repo}/milestones?state=all"):
        gh("DELETE", f"repos/{repo}/milestones/{m['number']}")
    for l in hepsi(f"repos/{repo}/labels"):
        gh("DELETE", f"repos/{repo}/labels/{urllib.parse.quote(l['name'], safe='')}")
    print("sıfırlama tamam")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("repo")
    ap.add_argument("--bugun", default=date.today().isoformat())
    ap.add_argument("--sifirla", action="store_true")
    a = ap.parse_args()
    repo, bugun = a.repo, t(a.bugun)
    v = yukle()
    sp = hazirla(v)
    tek = v["teknolojiler"]
    ep = {e["id"]: e for e in v["epikler"]}
    og = v["ogeler"]
    if a.sifirla:
        sifirla(repo)

    # Etiketler
    mevcut = {l["name"] for l in hepsi(f"repos/{repo}/labels")}
    etiketler = dict(RENK)
    for r in sorted({o["r"] for o in og}):
        etiketler["rol: " + r.lower()] = "F2A541"
    for p in sorted({o.get("sp") for o in og if o.get("sp")}):
        etiketler[f"puan: {p}"] = "EEF4F2"
    for ad, renk in etiketler.items():
        if ad not in mevcut:
            gh("POST", f"repos/{repo}/labels", {"name": ad, "color": renk})
    print("etiketler hazır:", len(etiketler))

    # Milestone'lar
    ms = {m["title"]: m["number"] for m in hepsi(f"repos/{repo}/milestones?state=all")}

    def milestone(baslik, aciklama, bitis):
        if baslik not in ms:
            ms[baslik] = gh("POST", f"repos/{repo}/milestones", {"title": baslik, "description": aciklama, "due_on": f"{bitis.isoformat()}T20:59:59Z"})["number"]

    milestone(M_BASVURU, "Teknopark başvurusunun hazırlanması ve gönderilmesi.", date(2026, 12, 11))
    milestone(M_DEGER, "Aday komisyon ve hakem süreçleri; kira, şube tescili ve faaliyet onayı.", date(2027, 3, 31))
    for s in sp:
        aktif = [o for o in og if o.get("spr") and o["spr"][0] <= s["no"] <= o["spr"][1]]
        epk = sorted({o["epik"] for o in aktif})
        kod = sorted({k for o in aktif for k in o["tek"]}, key=lambda k: list(tek).index(k))
        acik = (f"Odak epikler: {', '.join(epk) or '—'}. Teknolojiler: " + ", ".join(tek[k].split(' (')[0] for k in kod))[:900]
        milestone(sprint_ad(s), acik, s["bit"])
    milestone(M_SUREKLI, "Faz 1 boyunca süren teknopark raporlaması ve çeyreklik gözden geçirmeler.", date(2028, 4, 20))
    milestone(M_F2, "Faz 2 epikleri; sprint planlaması Faz 1'in son çeyreğinde yapılacaktır.", date(2029, 3, 31))
    milestone(M_F3, "Faz 3 kapsamı; ayrıntılı backlog Faz 2 sonunda oluşturulacaktır.", date(2030, 3, 31))
    print("milestone'lar hazır:", len(ms))

    var = {i["title"].split(" · ")[0]: i for i in hepsi(f"repos/{repo}/issues?state=all") if "pull_request" not in i}

    def durum(o):
        if o["_bas"] <= bugun <= o["_bit"]:
            return "durum: devam ediyor"
        if o["_bas"] <= bugun + timedelta(days=13):
            return "durum: bu sprint"
        return "durum: yapılacak"

    # Epikler
    eno, eid = {}, {}
    for e in v["epikler"]:
        if e["id"] in var:
            eno[e["id"]], eid[e["id"]] = var[e["id"]]["number"], var[e["id"]]["id"]
            continue
        y = gh("POST", f"repos/{repo}/issues", {"title": f"{e['id']} · {e['ad']}", "body": f"**Amaç:** {e['amac']}\n\nKapsam listesi oluşturuluyor.",
                                                "labels": [TUR_ETIKET["epik"], v["fazlar"][e["faz"]]["etiket"]]})
        eno[e["id"]], eid[e["id"]] = y["number"], y["id"]
        print("epik", e["id"], "#", y["number"])
        time.sleep(1)

    # Hikâye, araştırma ve görevler
    no = {}
    for o in og:
        if o["id"] in var:
            no[o["id"]] = var[o["id"]]["number"]
            continue
        g = []
        if o["tip"] == "hikaye":
            g += ["## Kullanıcı hikâyesi", "", hikaye_cumlesi(o), "", "## Fonksiyonel gereksinimler", ""]
            num = o["id"].split("-")[1]
            g += [f"- **FR-{num}.{i}:** {x}" for i, x in enumerate(o["gr"], 1)] + [""]
        elif o["tip"] == "arastirma":
            g += ["## Araştırma sorusu ve hedef", "", o["hedef"], ""]
        g += ["## Kabul kriterleri", ""] + [f"- [ ] {k}" for k in kk_satirlari(o)] + [""]
        g += ["## Planlama", "", "| | |", "|---|---|",
              f"| Epik | #{eno[o['epik']]} {o['epik']} · {ep[o['epik']]['ad']} |",
              f"| Faz | {v['fazlar'][o['_faz']]['ad']} |",
              f"| Sprint | {o['_sprint'] or o['_ms']} |",
              f"| Başlangıç | {tr(o['_bas'])} |",
              f"| Bitiş | {tr(o['_bit'])} |",
              f"| Sorumlu | {o['r']} |",
              f"| Öncelik | {ONCELIK[o['on']]} ({o['on']}) |",
              f"| Hikâye puanı | {o.get('sp', '—')} |",
              f"| Bağımlılıklar | {', '.join(f'#{no[d]} {d}' if d in no else d for d in o.get('dep', [])) or 'Yok'} |", ""]
        g += ["## Kullanılacak teknolojiler", ""] + [f"- {tek[k]}" for k in o["tek"]] + [""]
        g += ["## Tamamlanma tanımı", ""] + [f"- [ ] {d}" for d in DOD[o["tip"]]] + ["", f"Kaynak: `plan/backlog.json` · {o['id']}"]
        etk = [TUR_ETIKET[o["tip"]], ONC_ETIKET[o["on"]], v["fazlar"][o["_faz"]]["etiket"], "rol: " + o["r"].lower(), durum(o)]
        if o.get("sp"):
            etk.append(f"puan: {o['sp']}")
        y = gh("POST", f"repos/{repo}/issues", {"title": f"{o['id']} · {o['t']}", "body": "\n".join(g), "milestone": ms[o["_ms"]], "labels": etk})
        no[o["id"]] = y["number"]
        gh("POST", f"repos/{repo}/issues/{eno[o['epik']]}/sub_issues", {"sub_issue_id": y["id"]}, izin_hata=True)
        print(o["id"], "#", y["number"])
        time.sleep(1)

    # Epik gövdeleri
    for e in v["epikler"]:
        gs = [o for o in og if o["epik"] == e["id"]]
        b, s = min(o["_bas"] for o in gs), max(o["_bit"] for o in gs)
        kod = sorted({k for o in gs for k in o["tek"]}, key=lambda k: list(tek).index(k))
        sprs = sorted({n for o in gs if o.get("spr") for n in o["spr"]})
        govde = [f"**Amaç:** {e['amac']}", "", "| | |", "|---|---|",
                 f"| Faz | {v['fazlar'][e['faz']]['ad']} |",
                 f"| Tarih aralığı | {tr(b)} – {tr(s)} |",
                 f"| Sprintler | {'Sprint %02d – Sprint %02d' % (sprs[0], sprs[-1]) if sprs else 'Hazırlık dönemi / yol haritası'} |",
                 f"| Kapsam | {sum(1 for o in gs if o['tip'] == 'hikaye')} kullanıcı hikâyesi, {sum(1 for o in gs if o['tip'] == 'arastirma')} Ar-Ge araştırması, {sum(1 for o in gs if o['tip'] == 'gorev')} görev |",
                 f"| Toplam hikâye puanı | {sum(o.get('sp', 0) for o in gs) or '—'} |", "",
                 "## Kapsamdaki işler", ""]
        govde += [f"- [ ] #{no[o['id']]} {o['id']} · {o['t']} ({TIP_AD[o['tip']].lower()}, {o['_sprint'] or tr(o['_bit'])})" for o in gs]
        govde += ["", "## Kullanılacak teknolojiler", ""] + [f"- {tek[k]}" for k in kod]
        gh("PATCH", f"repos/{repo}/issues/{eno[e['id']]}", {"body": "\n".join(govde)})
        time.sleep(0.5)
    print(f"tamam: {len(eno)} epik, {len(no)} öğe")


if __name__ == "__main__":
    main()
