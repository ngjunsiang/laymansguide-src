
import csv
import os


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

    def to_file(self, path: str) -> None:
        with open(path, 'w') as f:
            for field, value in self.metadata.items():
                f.write(f"{field.title()}: {value}\n")
            f.write("\n")
            f.write(self.content)


with open("metadata.csv") as f:
    issues = list(csv.DictReader(f))

for issue in issues:
    _, num = issue["category"].split(" ")
    season = f"season{int(num):02}"
    name, _ = os.path.splitext(issue["file"])
    path = os.path.join("content", season, name, issue["file"])
    
    article = Article.from_file(path)
    article.metadata["slug"] = name
    article.to_file(path)