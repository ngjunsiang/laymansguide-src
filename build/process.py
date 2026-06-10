"""
Content processing module for converting newsletter content to Pelican format.

Handles URL conversion, metadata addition, and figure formatting.
"""

import csv
import os
import re
from datetime import datetime
from typing import Optional


class Article:
    """Represents a newsletter article with metadata and content."""

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
        """Load an article from a markdown file."""
        article = Article()
        with open(path, 'r') as f:
            while (line := f.readline()) != "\n":
                assert ": " in line, f"Invalid metadata line: {line}"
                field, value = line.split(": ", 1)
                assert field.lower() in article.metadata, f"Unknown field: {field}"
                article.metadata[field.lower()] = value.strip()
            article.content = f.read()
        return article

    def get_summary(self) -> Optional[str]:
        """Extract the issue summary from content."""
        label = "**Issue summary:** "
        summ_pos = self.content.find(label)
        if summ_pos == -1:
            print(f"Could not find summary in {self.metadata['title']}")
            return None
        try:
            summ_end = self.content.find("\n", summ_pos)
            return self.content[summ_pos:summ_end].lstrip(label)
        except Exception as e:
            print(f"Error extracting summary from {self.metadata['title']}: {e}")
            return None

    def to_file(self, path: str) -> None:
        """Save article to a markdown file with Pelican metadata."""
        with open(path, 'w') as f:
            for field, value in self.metadata.items():
                f.write(f"{field.title()}: {value}\n")
            f.write("\n")
            f.write(self.content)


class ContentProcessor:
    """Processes newsletter content for Pelican static site generator."""

    def __init__(self, metadata_path: str = "build/metadata/metadata.csv"):
        """Initialize processor with metadata file path."""
        self.metadata_path = metadata_path
        self.issues = self._load_metadata()
        self._setup_regex_patterns()

    def _load_metadata(self) -> list[dict]:
        """Load issue metadata from CSV file."""
        if not os.path.exists(self.metadata_path):
            print(f"Warning: Metadata file not found at {self.metadata_path}")
            return []

        with open(self.metadata_path) as f:
            return list(csv.DictReader(f))

    def _setup_regex_patterns(self):
        """Set up regex patterns for URL and content conversion."""
        # Markdown link and image patterns
        self.md_link = re.compile(r"[^!]\[([^\]]+)\]\(([^\)]+)\)")
        self.md_img = re.compile(r"!\[(.+)\]\((.+)\)")

        # URL conversion patterns for internal links
        self.lmg_slug = re.compile(
            r"\(https://buttondown.email/laymansguide/archive/lmg-s([0-9]+)-issue-([0-9]+)[^\)]*"
        )
        self.lmg_slug2 = re.compile(
            r"\(https://buttondown.email/laymansguide/archive/lmg-issue-([0-9]+)-[^\)]*"
        )

        # Image URL conversion patterns
        self.lmg_img = re.compile(
            r"\(https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/([^/]+)/([^/]+)/([^/?\)]+)\)"
        )
        self.lmg_img2 = re.compile(
            r"\(https://github.com/ngjunsiang/laymansguide/blob/release/([^/]+)/([^/]+)/([^/?\)]+)\)"
        )

        # Figure pattern
        self.re_fig = re.compile(
            r"\!\[(.*?)\]\((.+?)\)\n*(?:<br />)*\n*<small>(.*?)</small>",
            re.MULTILINE
        )

    def _lmg_slug_sub(self, match) -> str:
        """Convert LMG URL to local markdown reference."""
        s_num, i_num = int(match.group(1)), int(match.group(2))
        return f"({{filename}}/season{s_num}/issue{i_num:03}/issue{i_num:03}.md)"

    def _lmg_slug2_sub(self, match) -> str:
        """Convert LMG URL (season 1 format) to local markdown reference."""
        i_num = int(match.group(1))
        return f"({{filename}}/season01/issue{i_num:03}/issue{i_num:03}.md)"

    def _lmg_img_sub(self, match) -> str:
        """Convert GitHub image URL to local static file reference."""
        season, folder, filename = match.group(1), match.group(2), match.group(3)
        assert "season" in season, season
        assert "issue" in folder, folder
        return f"({{attach}}/{season}/{folder}/{filename})"

    def _mkfig(self, match) -> str:
        """Convert image with caption to HTML figure."""
        alt_text, img_url, caption = match.group(1), match.group(2), match.group(3)
        return f"""<figure>
    ![{alt_text}]({img_url})
    <figcaption>{caption}</figcaption>
</figure>"""

    def _parse_date(self, dt: str) -> datetime:
        """Parse date string to datetime object."""
        abbrev_mths = ["Jan", "Feb", "Mar", "Apr", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        mth_day, yr, time = dt.split(", ")
        mth, day = mth_day.split(" ")
        m_fmt = "%b" if mth in abbrev_mths else "%B"
        hm, ap = time.split(" ")
        d_fmt = "%d"
        y_fmt = "%Y"
        h_fmt = "%I:%M" if ":" in hm else "%I"
        p_fmt = "%p"
        return datetime.strptime(dt, f"{m_fmt} {d_fmt}, {y_fmt}, {h_fmt} {p_fmt}")

    def _convert_urls(self, doc: str) -> str:
        """Convert external URLs to local references."""
        # Convert markdown links
        doc = self.lmg_slug.sub(self._lmg_slug_sub, doc)
        doc = self.lmg_slug2.sub(self._lmg_slug2_sub, doc)

        # Convert image URLs
        doc = self.lmg_img.sub(self._lmg_img_sub, doc)
        doc = self.lmg_img2.sub(self._lmg_img_sub, doc)

        return doc

    def _add_pelican_metadata(self, issue: dict) -> dict:
        """Generate Pelican metadata for an issue."""
        date_string = issue["date"].replace(".", "").replace("Sept", "Sep")
        out_format = "%Y-%m-%d %H:%M"

        return {
            "Title": issue["title"],
            "Date": self._parse_date(date_string).strftime(out_format),
            "Tags": "",
            "Category": issue["category"],
            "Slug": issue["url"].rstrip("/").split("/")[-1],
            "Author": "J S Ng",
            "Summary": "",
        }

    def _get_content_path(self, issue: dict) -> str:
        """Get the file path for an issue's content."""
        _, num = issue["category"].split(" ")
        season = f"season{int(num):02}"
        name, _ = os.path.splitext(issue["file"])
        return os.path.join("content", season, name, issue["file"])

    def process_metadata_headers(self):
        """Add Pelican metadata headers to all issues."""
        print("Adding Pelican metadata headers...")

        for issue in self.issues:
            metadata = self._add_pelican_metadata(issue)
            path = self._get_content_path(issue)

            if not os.path.exists(path):
                print(f"Warning: File not found: {path}")
                continue

            print(f"Processing: {path}")

            with open(path) as f:
                doc = f.read()

            # Convert URLs to local references
            doc = self._convert_urls(doc)

            # Write back with metadata header
            with open(path, "w") as f:
                for field, value in metadata.items():
                    f.write(f"{field}: {value}\n")
                f.write("\n")
                f.write(doc)

    def process_figures_and_summaries(self):
        """Process figure formatting and extract summaries."""
        print("Processing figures and summaries...")

        for issue in self.issues:
            path = self._get_content_path(issue)

            if not os.path.exists(path):
                print(f"Warning: File not found: {path}")
                continue

            print(f"Processing: {path}")

            article = Article.from_file(path)
            article.metadata["summary"] = article.get_summary() or ""

            # Convert markdown figures to HTML
            article.content = self.re_fig.sub(self._mkfig, article.content)

            article.to_file(path)

    def process_all(self):
        """Run all content processing steps."""
        print("Processing all newsletter content...")
        self.process_metadata_headers()
        self.process_figures_and_summaries()
        print("✅ Content processing complete!")


if __name__ == "__main__":
    processor = ContentProcessor()
    processor.process_all()
