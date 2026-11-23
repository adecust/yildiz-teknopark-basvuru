"""plan/faz1-plan.json içeriğini GitHub reposuna etiket, milestone ve issue olarak aktarır.

Kullanım:  python scripts/github_yukle.py OWNER/REPO [--bugun YYYY-MM-DD]
Tekrar çalıştırılabilir: var olan etiket / milestone / issue (başlıktaki [ID] ile) atlanır.
"""
import argparse
import json
import subprocess
import time
from datetime import date, timedelta
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
PLAN = KOK / "plan" / "faz1-plan.json"

ETIKET_RENK = {
    "kritik": "B60205", "yildiz": "5319E7", "mali": "FBCA04", "evrak": "C2E0C6", "akademik": "0E8A16",
    "ekip": "1D76DB", "ar-ge": "D93F0B", "ticari": "F9D0C4", "dosya": "BFDADC", "platform": "0052CC",
    "veri": "C5DEF5", "kvkk": "E99695", "test": "EDEDED", "rapor": "D4C5F9", "pilot": "006B75",
    "faz-2": "5319E7", "fmh": "0E8A16", "opsiyonel": "FFFFFF", "tekrarlayan": "BFD4F2",
    "durum:backlog": "EDEDED", "durum:bu-hafta": "FBCA04", "durum:devam": "1D76DB",
    "durum:inceleme": "D4C5F9",
}


def gh(method, path, body=None):
    cmd = ["gh", "api", "-X", method, path, "-H", "Accept: application/vnd.github+json"]
    if body is not None:
        cmd += ["--input", "-"]
    r = subprocess.run(cmd, input=json.dumps(body) if body is not None else None,
                       capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        raise RuntimeError(f"{method} {path} başarısız: {r.stderr.strip() or r.stdout.strip()}")
    return json.loads(r.stdout) if r.stdout.strip() else None


def tumunu_al(path):
    sonuc, sayfa = [], 1
    while True:
        parca = gh("GET", f"{path}{'&' if '?' in path else '?'}per_page=100&page={sayfa}")
        sonuc += parca
        if len(parca) < 100:
            return sonuc
        sayfa += 1


def tr(s):
    return date.fromisoformat(s).strftime("%d.%m.%Y")


def durum(g, bugun):
    s, e = date.fromisoformat(g["s"]), date.fromisoformat(g["e"])
    if s <= bugun <= e:
        return "durum:devam"
    if s <= bugun + timedelta(days=6):
        return "durum:bu-hafta"
    return "durum:backlog"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("repo")
    ap.add_argument("--bugun", default=date.today().isoformat())
    a = ap.parse_args()
    repo, bugun = a.repo, date.fromisoformat(a.bugun)
    veri = json.loads(PLAN.read_text(encoding="utf-8"))

    mevcut_etiket = {x["name"] for x in tumunu_al(f"repos/{repo}/labels")}
    for ad, renk in ETIKET_RENK.items():
        if ad not in mevcut_etiket:
            gh("POST", f"repos/{repo}/labels", {"name": ad, "color": renk})
    print("etiketler tamam")

    mevcut_ms = {m["title"]: m["number"] for m in tumunu_al(f"repos/{repo}/milestones?state=all")}
    ms_no = {}
    for m in veri["milestones"]:
        if m["title"] in mevcut_ms:
            ms_no[m["key"]] = mevcut_ms[m["title"]]
        else:
            yeni = gh("POST", f"repos/{repo}/milestones", {
                "title": m["title"], "description": m["desc"], "due_on": f"{m['due']}T20:59:59Z"})
            ms_no[m["key"]] = yeni["number"]
    print("milestone'lar tamam")

    mevcut_issue = {}
    for i in tumunu_al(f"repos/{repo}/issues?state=all"):
        if "pull_request" not in i and i["title"].startswith("["):
            mevcut_issue[i["title"].split("]")[0][1:]] = i["number"]

    id_no = dict(mevcut_issue)
    olusan = 0
    for g in veri["gorevler"]:
        if g["id"] in id_no:
            continue
        bag = ", ".join(f"#{id_no[d]} ({d})" if d in id_no else d for d in g["dep"]) or "—"
        govde = "\n".join([
            "| | |", "|---|---|",
            f"| 📅 **Başlangıç** | {tr(g['s'])} |",
            f"| 🏁 **Bitiş (son tarih)** | **{tr(g['e'])}** |",
            f"| 👤 **Sorumlu rol** | {g['r']} |",
            f"| 🔗 **Bağımlılıklar** | {bag} |",
            "", "### Kabul kriteri", f"- [ ] {g['k']}", "",
            "### Notlar", "- Kriter sayısal ise ölçüm sonucunu bu issue'ya yorum olarak ekleyin (hakem / denetim kanıtı).",
            "", f"_Kaynak: `plan/faz1-plan.json` · görev `{g['id']}` · ayrıntı: `docs/03-faz1-kanban-ve-zaman-plani.md`_",
        ])
        yeni = gh("POST", f"repos/{repo}/issues", {
            "title": f"[{g['id']}] {g['t']} · son: {tr(g['e'])}",
            "body": govde,
            "milestone": ms_no[g["m"]],
            "labels": g["l"] + [durum(g, bugun)],
        })
        id_no[g["id"]] = yeni["number"]
        olusan += 1
        print(f"#{yeni['number']} {g['id']}")
        time.sleep(1.2)  # GitHub ikincil hız sınırı için
    print(f"{olusan} yeni issue oluşturuldu; toplam {len(id_no)}")


if __name__ == "__main__":
    main()
