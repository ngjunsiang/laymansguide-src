from bs4 import BeautifulSoup
from datetime import datetime
import csv
import json
import re
import requests

# Download index pages
# for i in range(1, 5):
#     doc = requests.get(f"https://buttondown.email/laymansguide/archive/?page={i}").text
#     with open(f"index{i}.html", "w") as f:
#         f.write(doc)

# Store issue titles and urls
# issues = []
# for i in range(1, 5):
#     with open(f"indexes/index{i}.html", "r") as f:
#         doc = f.read()

#     soup = BeautifulSoup(doc, "html.parser")

#     for email in soup.find_all('div', class_="email"):
#         issues.append({
#             "title": email.a.h2.text,
#             "url": email.a["href"]
#         })

# Scrape issues for published date
# for issue in issues:
#     doc = requests.get(issue["url"]).text
#     soup = BeautifulSoup(doc, "html.parser")
#     print(issue["title"])
#     match = re.search(r"\[(.*?)\]", issue["title"])
#     if match:
#         issue["season"] = match.group(1).replace("LMG S", "Season ")
#     date_string = soup.find('h3', class_="byline").text.strip()
#     issue["date"] = date_string

# Export to CSV
# with open("issues_v4.json", "r") as f:
#     issues = json.load(f)

# with open("metadata.csv", "w") as f:
#     writer = csv.DictWriter(f, fieldnames=["file", "title", "date", "category", "url"])
#     writer.writeheader()
#     for issue in issues:
#         writer.writerow(issue)



