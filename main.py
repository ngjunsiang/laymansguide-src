# Add metadata to each issue
# date
# tags
# category
# slug
# authors
# summary

import csv
from datetime import datetime
import os
import re


def parse_date(dt: str) -> datetime:
    abbrev_mths = ["Jan", "Feb", "Mar", "Apr", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    mth_day, yr, time = dt.split(", ")
    mth, day = mth_day.split(" ")
    m_fmt = "%b" if mth in abbrev_mths else "%B"
    hm, ap = time.split(" ")
    # Python can handle no leading zeros for %d, %I
    d_fmt = "%d"
    y_fmt = "%Y"
    h_fmt = "%I:%M" if ":" in hm else "%I"
    p_fmt = "%p"
    return datetime.strptime(dt, f"{m_fmt} {d_fmt}, {y_fmt}, {h_fmt} {p_fmt}")



with open("metadata.csv") as f:
    issues = list(csv.DictReader(f))

out_format = "%Y-%m-%d %H:%M"
host = "https://buttondown.email"
md_link = re.compile(r"[^!]\[([^\]]+)\]\(([^\)]+)\)")
md_img = re.compile(r"!\[(.+)\]\((.+)\)")

lmg_slug = re.compile(r"https://buttondown.email/laymansguide/archive/lmg-s([0-9]+)-issue-([0-9]+).*")
def lmg_slug_sub(match) -> str:
    s_num, i_num = int(match.group(1)), int(match.group(2))
    return f"{{filename}}/season{s_num}/issue{i_num:03}/issue{i_num:03}.md"

lmg_slug2 = re.compile(r"https://buttondown.email/laymansguide/archive/lmg-issue-([0-9]+)-.*")
def lmg_slug2_sub(match) -> str:
    s_num, i_num = 1, int(match.group(1))
    return f"{{filename}}/season{s_num}/issue{i_num:03}/issue{i_num:03}.md"

lmg_img = re.compile(r"https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/([^/]+)/([^/]+)/([^/?\)]+)")
lmg_img2 = re.compile(r"https://github.com/ngjunsiang/laymansguide/blob/release/([^/]+)/([^/]+)/([^/?\)]+)")
def lmg_img_sub(match) -> str:
    season, folder, filename = match.group(1), match.group(2), match.group(3)
    assert filename
    return f"{{attach}}{filename}"



for issue in issues:
    issue["date"] = issue["date"].replace(".", "").replace("Sept", "Sep")

    metadata = {
        "Title": issue["title"],
        "Date": parse_date(issue["date"]).strftime(out_format),
        "Tags": "",
        "Category": issue["category"],
        "Slug": issue["url"].rstrip("/").split("/")[-1],
        "Author": "J S Ng",
        "Summary": "",
    }

    folder = issue["category"].lower().replace(" ", "")
    name, _ = os.path.splitext(issue["file"])
    path = os.path.join("content", folder, name, issue["file"])
    print()

    print("Path:", path)
    # for field, data in metadata.items():
    #     print("--", f"{field.title()}:", data)

    with open(path) as f:
        doc = f.read()

    urls = list(md_link.findall(doc))
    imgs = list(md_img.findall(doc))
    if urls:
        # print("--", "Issue URLs to replace:")
        # for i, (label, url) in enumerate(urls, start=1):
            # if match := lmg_slug.search(url):
            #     print(lmg_slug_sub(match))
        doc = lmg_slug.sub(lmg_slug_sub, doc)
            # elif match := lmg_slug2.search(url):
            #     print(lmg_slug2_sub(match))
        doc = lmg_slug2.sub(lmg_slug2_sub, doc)
            # else:
            #     print(url)

    if imgs:
        # print("--", "Image URLs:")
        # for i, (label, img) in enumerate(imgs, start=1):
            # match = lmg_img.search(img) or lmg_img2.search(img)
            # if match:
            #     print(lmg_img_sub(match))
        doc = lmg_img.sub(lmg_img_sub, doc)
        doc = lmg_img2.sub(lmg_img_sub, doc)
            # else:
            #     print(img)

    with open(path, "w") as f:
        f.write(doc)