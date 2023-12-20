
import csv
import os
import re


class Article:
    __slots__ = ("metadata", "content")

    def __init__(self, content: str = "") -> None:
        self.metadata: dict[str, str] = {
            "title": "",
            "date": "",
            "tags": "",
            "category": "",
            "slug": "",
            "author": "",
            "summary": "",
            "modified": ""
        }
        self.content: str = content
        self.prev: str
        self.next: str

    @classmethod
    def from_file(cls, path: str) -> "Article":
        article = Article()
        with open(path, 'r') as f:
            while (line := f.readline()) != "\n":
                assert ": " in line
                field, value = line.split(": ", 1)
                assert field.lower() in article.metadata
                article.metadata[field.lower()] = value.strip()
            article.content = f.read()
        return article

    def get_summary(self) -> str | None:
        label = "**Issue summary:** "
        summ_pos = self.content.find(label)
        if summ_pos == -1:
            print(f"Could not find summary in {self.metadata['title']}")
            return
        try:
            summ_end = self.content.find("\n", summ_pos)
        except:
            breakpoint()
        return self.content[summ_pos:summ_end].lstrip(label)

    def to_file(self, path: str) -> None:
        with open(path, 'w') as f:
            for field, value in self.metadata.items():
                f.write(f"{field.title()}: {value}\n")
            f.write("\n")
            f.write(self.content)

def mkfig(match) -> str:
    alt_text, img_url, caption = match.group(1), match.group(2), match.group(3)
    return f"""<figure>
    ![{alt_text}]({img_url})
    <figcaption>{caption}</figcaption>    
</figure>"""



re_fig = re.compile(r"\!\[(.*?)\]\((.+?)\)\n*(?:<br />)*\n*<small>(.*?)</small>", re.MULTILINE)


with open("metadata.csv") as f:
    issues = list(csv.DictReader(f))

for issue in issues:
    print(issue["file"])
    _, num = issue["category"].split(" ")
    season = f"season{int(num):02}"
    name, _ = os.path.splitext(issue["file"])
    path = os.path.join("content", season, name, issue["file"])

    article = Article.from_file(path)
    article.metadata["summary"] = article.get_summary() or ""
    # article.content = re.sub("\)\n\*", ")  \n*", article.content)
    article.to_file(path)