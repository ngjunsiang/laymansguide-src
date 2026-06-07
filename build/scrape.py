"""
Web scraping module for harvesting newsletter content from Buttondown.

This module handles downloading newsletter content from the Buttondown email service
and extracting metadata for processing.
"""

import json
import csv
import re
from datetime import datetime
from typing import List, Dict

try:
    from bs4 import BeautifulSoup
    import requests
    BS4_AVAILABLE = True
except ImportError:
    BS4_AVAILABLE = False
    print("Warning: BeautifulSoup and requests not available. Install with: pip install beautifulsoup4 requests")


class ButtondownScraper:
    """Scraper for Buttondown email newsletter archive."""

    def __init__(self, newsletter_name: str = "laymansguide"):
        """Initialize scraper for specific newsletter."""
        self.newsletter_name = newsletter_name
        self.base_url = f"https://buttondown.email/{newsletter_name}"
        self.issues: List[Dict] = []

    def fetch_archive_page(self, page_num: int = 1) -> str:
        """Fetch a single archive page."""
        if not BS4_AVAILABLE:
            raise ImportError("BeautifulSoup and requests required for scraping")

        url = f"{self.base_url}/archive/?page={page_num}"
        response = requests.get(url)
        response.raise_for_status()
        return response.text

    def parse_archive_page(self, html: str) -> List[Dict]:
        """Parse archive page and extract issue metadata."""
        if not BS4_AVAILABLE:
            raise ImportError("BeautifulSoup required for parsing")

        soup = BeautifulSoup(html, "html.parser")
        issues = []

        for email in soup.find_all('div', class_="email"):
            issues.append({
                "title": email.a.h2.text.strip(),
                "url": email.a["href"]
            })

        return issues

    def fetch_issue_details(self, issue: Dict) -> Dict:
        """Fetch detailed information for a single issue."""
        if not BS4_AVAILABLE:
            raise ImportError("requests required for fetching issue details")

        response = requests.get(issue["url"])
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract publication date
        date_element = soup.find('h3', class_="byline")
        if date_element:
            issue["date"] = date_element.text.strip()

        # Extract season from title
        match = re.search(r"\[(.*?)\]", issue["title"])
        if match:
            issue["season"] = match.group(1).replace("LMG S", "Season ")

        # Determine category (season)
        season_match = re.search(r"s(\d+)", issue.get("url", ""))
        if season_match:
            season_num = int(season_match.group(1))
            issue["category"] = f"Season {season_num}"

        return issue

    def scrape_all_issues(self, max_pages: int = 4) -> List[Dict]:
        """Scrape all issues from archive pages."""
        print(f"Scraping {max_pages} pages from {self.base_url}/archive/")

        all_issues = []

        for page in range(1, max_pages + 1):
            print(f"Fetching page {page}...")
            html = self.fetch_archive_page(page)
            issues = self.parse_archive_page(html)

            # Fetch details for each issue
            for issue in issues:
                print(f"  Fetching details for: {issue['title'][:50]}...")
                try:
                    detailed_issue = self.fetch_issue_details(issue)
                    all_issues.append(detailed_issue)
                except Exception as e:
                    print(f"    Error fetching details: {e}")
                    continue

        self.issues = all_issues
        return all_issues

    def assign_filenames(self, issues: List[Dict]) -> List[Dict]:
        """Assign markdown filenames to issues based on issue number."""
        for issue in issues:
            # Extract issue number from URL
            match = re.search(r"issue-?(\d+)", issue["url"])
            if match:
                issue_num = int(match.group(1))
                issue["file"] = f"issue{issue_num:03}.md"
            else:
                print(f"Warning: Could not extract issue number from {issue['url']}")
                issue["file"] = "unknown.md"

        return issues


def export_to_json(issues: List[Dict], output_path: str = "build/metadata/issues_v4.json"):
    """Export issues to JSON format."""
    # Ensure directory exists
    import os
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w") as f:
        json.dump(issues, f, indent=2)

    print(f"✅ Exported {len(issues)} issues to {output_path}")


def export_to_csv(issues: List[Dict], output_path: str = "build/metadata/metadata.csv"):
    """Export issues to CSV format."""
    # Ensure directory exists
    import os
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    if not issues:
        print("Warning: No issues to export")
        return

    fieldnames = ["file", "title", "date", "category", "url"]

    with open(output_path, "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for issue in issues:
            writer.writerow({
                "file": issue.get("file", ""),
                "title": issue.get("title", ""),
                "date": issue.get("date", ""),
                "category": issue.get("category", ""),
                "url": issue.get("url", "")
            })

    print(f"✅ Exported {len(issues)} issues to {output_path}")


def scrape_issues(
    newsletter_name: str = "laymansguide",
    max_pages: int = 4,
    json_output: str = "build/metadata/issues_v4.json",
    csv_output: str = "build/metadata/metadata.csv"
):
    """
    Main function to scrape issues and export to both JSON and CSV formats.

    Args:
        newsletter_name: Name of the Buttondown newsletter
        max_pages: Maximum number of archive pages to scrape
        json_output: Path for JSON output file
        csv_output: Path for CSV output file
    """
    print(f"🔍 Starting scrape for {newsletter_name} newsletter...")

    scraper = ButtondownScraper(newsletter_name)
    issues = scraper.scrape_all_issues(max_pages)
    issues = scraper.assign_filenames(issues)

    print(f"\n📊 Scraped {len(issues)} issues")

    # Export to both formats
    export_to_json(issues, json_output)
    export_to_csv(issues, csv_output)

    print("✅ Scraping complete!")
    return issues


if __name__ == "__main__":
    # Example usage
    scrape_issues(max_pages=4)
