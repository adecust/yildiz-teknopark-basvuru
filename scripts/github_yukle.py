"""plan/proje-plani.json içeriğini GitHub reposuna aktarır.

Oluşturulanlar: etiketler, sprint milestone'ları, epik issue'ları ve görev issue'ları
(görevler epiklerin alt işi olarak bağlanır). Emoji kullanılmaz.

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
from plan_olustur import yukle, sprintler, sprint_bul, sprint_ad, t, tr  # noqa: E402

RENK = {
    "faz-0": "5B6770", "faz-1": "14786E", "faz-2": "2E5E8C", "faz-3": "8FC1B5",
    "epik": "0B3D3A", "kritik": "B60205", "opsiyonel": "C5DEF5", "ar-ge": "D93F0B",
    "platform": "0052CC", "kvkk": "E99695", "tekrarlayan": "BFD4F2", "akademik": "0E8A16",
    "durum: yapılacak": "EDEDED", "durum: bu sprint": "FBCA04", "durum: devam ediyor": "1D76DB", "durum: incelemede": "D4C5F9",
}
ROL_RENK = "F2A541"


def gh(method, path, body=None, izin_hata=False):
    cmd = ["gh", "api", "-X", method, path, "-H", "Accept: application/vnd.github+json"]
    if body is not None:
        cmd += ["--input", "-"]
    r = subprocess.run(cmd, input=json.dumps(body) if body is not None else None,
                       capture_output=True, text=True, encoding="utf-8")
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
        if "pull_request" in i:
            continue
        subprocess.run(["gh", "issue", "delete", str(i["number"]), "--repo", repo, "--yes"], capture_output=True)
        print("silindi issue", i["number"])
    for m in hepsi(f"repos/{repo}/milestones?state=all"):
        gh("DELETE", f"repos/{repo}/milestones/{m['number']}")
    for l in hepsi(f"repos/{repo}/labels"):
        gh("DELETE", f"repos/{repo}/labels/{urllib.parse.quote(l['name'], safe='')}")
    print("sıfırlama tamam")


def rol_etiket(r):
    return "rol: " + r.lower().replace("ı", "ı")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("repo")
    ap.add_argument("--bugun", default=date.today().isoformat())
    ap.add_argument("--sifirla", action="store_true")
    a = ap.parse_args()
    repo, bugun = a.repo, t(a.bugun)
    v = yukle()
    sp = sprintler(v)
    fazlar = {f["key"]: f for f in v["fazlar"]}
    epikler = {e["id"]: e for e in v["epikler"]}
    tek, gt = v["teknolojiler"], v["gorev_teknoloji"]
    gorevler = v["gorevler"]
    for g in gorevler:
        g["_faz"] = epikler[g["epik"]]["faz"]
        g["_sp"] = None if fazlar[g["_faz"]].get("makro") else sprint_bul(sp, t(g["s"]))

    if a.sifirla:
        sifirla(repo)

    # Etiketler
    mevcut = {l["name"] for l in hepsi(f"repos/{repo}/labels")}
    roller = sorted({g["r"] for g in gorevler})
    for ad, renk in list(RENK.items()) + [(rol_etiket(r), ROL_RENK) for r in roller]:
        if ad not in mevcut:
            gh("POST", f"repos/{repo}/labels", {"name": ad, "color": renk})
    print("etiketler hazır")

    # Milestone'lar: görev içeren her sprint + makro fazlar
    ms = {m["title"]: m["number"] for m in hepsi(f"repos/{repo}/milestones?state=all")}

    def milestone(baslik, aciklama, bitis):
        if baslik not in ms:
            ms[baslik] = gh("POST", f"repos/{repo}/milestones", {"title": baslik, "description": aciklama, "due_on": f"{bitis.isoformat()}T20:59:59Z"})["number"]
        return ms[baslik]

    for s in sp:
        gs = [g for g in gorevler if g["_sp"] and g["_sp"]["no"] == s["no"]]
        if gs:
            kodlar = sorted({k for g in gs for k in gt[g["id"]]}, key=lambda k: list(tek).index(k))
            aciklama = f"{len(gs)} görev. Teknolojiler: " + "; ".join(tek[k].split(" (")[0] for k in kodlar)
            milestone(sprint_ad(s), aciklama[:250], s["bit"])
    for k, f in fazlar.items():
        if f.get("makro"):
            milestone(f"{f['ad']} (makro plan)", "Sprint planlaması bir önceki fazın son çeyreğinde yapılacaktır.", t(f["bit"]))
    print("milestone'lar hazır")

    # Var olan issue'lar (yeniden çalıştırmada atlamak için)
    var = {}
    for i in hepsi(f"repos/{repo}/issues?state=all"):
        if "pull_request" not in i:
            var[i["title"].split(" · ")[0]] = i
    time.sleep(1)

    def durum(g):
        if t(g["s"]) <= bugun <= t(g["e"]):
            return "durum: devam ediyor"
        akt = sprint_bul(sp, bugun)
        if akt and g["_sp"] and g["_sp"]["no"] == akt["no"]:
            return "durum: bu sprint"
        return "durum: yapılacak"

    # Epikler
    epik_no, epik_id = {}, {}
    for e in epikler.values():
        gs = [g for g in gorevler if g["epik"] == e["id"]]
        b, s = min(t(g["s"]) for g in gs), max(t(g["e"]) for g in gs)
        baslik = f"{e['id']} · {e['ad']}"
        if e["id"] in var:
            epik_no[e["id"]], epik_id[e["id"]] = var[e["id"]]["number"], var[e["id"]]["id"]
            continue
        yeni = gh("POST", f"repos/{repo}/issues", {
            "title": baslik, "body": f"**Amaç:** {e['amac']}\n\n**Faz:** {fazlar[e['faz']]['ad']}\n\n**Tarih aralığı:** {tr(b)} – {tr(s)}\n\nGörev listesi oluşturuluyor.",
            "labels": ["epik", fazlar[e["faz"]]["etiket"]]})
        epik_no[e["id"]], epik_id[e["id"]] = yeni["number"], yeni["id"]
        print("epik", baslik, "#", yeni["number"])
        time.sleep(1)

    # Görevler
    gno = {}
    for g in gorevler:
        if g["id"] in var:
            gno[g["id"]] = var[g["id"]]["number"]
            continue
        f = fazlar[g["_faz"]]
        mil = ms[sprint_ad(g["_sp"])] if g["_sp"] else ms[f"{f['ad']} (makro plan)"]
        bag = ", ".join(f"#{gno[d]} ({d})" if d in gno else d for d in g["dep"]) or "Yok"
        govde = "\n".join([
            f"**Faz:** {f['ad']}",
            f"**Epik:** #{epik_no[g['epik']]} {g['epik']} · {epikler[g['epik']]['ad']}",
            f"**Sprint:** {sprint_ad(g['_sp']) if g['_sp'] else 'Makro plan (sprint planlaması sonra yapılacak)'}",
            f"**Başlangıç:** {tr(t(g['s']))}",
            f"**Bitiş:** {tr(t(g['e']))}",
            f"**Sorumlu:** {g['r']}",
            f"**Bağımlı olduğu görevler:** {bag}",
            "",
            "### Kullanılacak teknolojiler",
            *[f"- {tek[k]}" for k in gt[g["id"]]],
            "",
            "### Kabul kriteri",
            f"- [ ] {g['k']}",
            "",
            "Kabul kriteri sayısal ise ölçüm sonucu bu issue'ya yorum olarak eklenir.",
            "",
            f"Kaynak: `plan/proje-plani.json`, görev {g['id']}",
        ])
        yeni = gh("POST", f"repos/{repo}/issues", {
            "title": f"{g['id']} · {g['t']} · bitiş {tr(t(g['e']))}", "body": govde, "milestone": mil,
            "labels": [f["etiket"], rol_etiket(g["r"]), durum(g)] + g["l"]})
        gno[g["id"]] = yeni["number"]
        gh("POST", f"repos/{repo}/issues/{epik_no[g['epik']]}/sub_issues", {"sub_issue_id": yeni["id"]}, izin_hata=True)
        print("görev", g["id"], "#", yeni["number"])
        time.sleep(1)

    # Epik gövdelerini görev listesiyle güncelle
    for e in epikler.values():
        gs = [g for g in gorevler if g["epik"] == e["id"]]
        b, s = min(t(g["s"]) for g in gs), max(t(g["e"]) for g in gs)
        sps = sorted({g["_sp"]["no"] for g in gs if g["_sp"]})
        kodlar = sorted({k for g in gs for k in gt[g["id"]]}, key=lambda k: list(tek).index(k))
        govde = "\n".join([
            f"**Amaç:** {e['amac']}",
            f"**Faz:** {fazlar[e['faz']]['ad']}",
            f"**Tarih aralığı:** {tr(b)} – {tr(s)}",
            f"**Sprintler:** {'Sprint %02d – Sprint %02d' % (sps[0], sps[-1]) if sps else 'Makro plan'}",
            "",
            "### Kullanılacak teknolojiler",
            *[f"- {tek[k]}" for k in kodlar],
            "",
            "### Görevler",
            *[f"- [ ] #{gno[g['id']]} {g['id']} · {g['t']} (bitiş {tr(t(g['e']))})" for g in gs],
        ])
        gh("PATCH", f"repos/{repo}/issues/{epik_no[e['id']]}", {"body": govde})
        time.sleep(0.5)
    print(f"tamam: {len(epikler)} epik, {len(gno)} görev")


if __name__ == "__main__":
    main()
