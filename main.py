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
for issue in issues:
    print(issue["title"])
    issue["date"] = issue["date"].replace(".", "").replace("Sept", "Sep")
    
    metadata = {
        "date": parse_date(issue["date"]).strftime(out_format),
        "tags": "",
        "category": issue["category"],
        "slug": issue["url"].rstrip("/").split("/")[-1],
        "author": "J S Ng",
        "summary": "",
    }

    folder = issue["category"].lower().replace(" ", "")
    name, _ = os.path.splitext(issue["file"])
    path = os.path.join("contents", folder, name, issue["file"])
    print("path:", path)
    for field, data in metadata.items():
        print("--", f"{field.title()}:", data)