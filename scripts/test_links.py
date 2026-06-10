#!/usr/bin/env python3
"""
Test script to verify all internal links work correctly using Playwright.
Tests both article links and category page links.
"""

import asyncio
from pathlib import Path
from urllib.parse import urljoin
from playwright.async_api import async_playwright, Page, Browser
import re

BASE_URL = "file:///home/kureshii/ngjunsiang/laymansguide-src/output/"
OUTPUT_DIR = Path("/home/kureshii/ngjunsiang/laymansguide-src/output")

class LinkTester:
    def __init__(self):
        self.broken_links = []
        self.tested_links = 0
        self.successful_links = 0

    async def test_page_links(self, page: Page, page_path: str) -> dict:
        """Test all links on a specific page."""
        page_url = urljoin(BASE_URL, page_path)

        try:
            await page.goto(page_url, wait_until="domcontentloaded")
            print(f"✓ Successfully loaded: {page_path}")

            # Get all links on the page
            links = await page.query_selector_all("a")
            page_results = {
                'page': page_path,
                'total_links': len(links),
                'broken_links': [],
                'external_links': []
            }

            for link in links:
                try:
                    href = await link.get_attribute("href")
                    text = await link.inner_text()

                    if not href or href.startswith("#") or href.startswith("mailto:"):
                        continue

                    # Check if it's an internal link
                    if href.startswith("/") or href.startswith("http"):
                        # Convert file:// URLs to proper format
                        if href.startswith("/"):
                            test_url = urljoin(BASE_URL, href)
                        else:
                            test_url = href

                        # Only test internal links
                        if "laymansguide" in test_url or test_url.startswith("file://"):
                            self.tested_links += 1

                            # Try to navigate to the link
                            try:
                                response = await page.goto(test_url, wait_until="domcontentloaded")
                                if response and response.status == 200:
                                    self.successful_links += 1
                                    print(f"  ✓ Link works: {text[:30]}... -> {href}")
                                else:
                                    status = response.status if response else "No response"
                                    page_results['broken_links'].append({
                                        'text': text[:50],
                                        'href': href,
                                        'status': status
                                    })
                                    print(f"  ✗ BROKEN: {text[:30]}... -> {href} ({status})")
                            except Exception as e:
                                page_results['broken_links'].append({
                                    'text': text[:50],
                                    'href': href,
                                    'error': str(e)
                                })
                                print(f"  ✗ ERROR: {text[:30]}... -> {href} - {e}")

                        else:
                            page_results['external_links'].append(href)

                except Exception as e:
                    print(f"  ! Error processing link: {e}")

            return page_results

        except Exception as e:
            print(f"✗ Failed to load page {page_path}: {e}")
            return {'page': page_path, 'error': str(e)}

async def test_season14_links():
    """Test all Season 14 issue links and category navigation."""
    tester = LinkTester()

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        print("=" * 60)
        print("Testing Season 14 Internal Links")
        print("=" * 60)

        # Test Season 14 pages
        season14_pages = [
            "issue170.html",
            "issue171.html",
            "issue172.html",
            "issue173.html",
            "issue174.html",
            "issue175.html",
            "issue176.html",
            "issue177.html",
            "issue178.html",
            "issue179.html",
            "issue180.html",
            "issue181.html",
            "issue182.html"
        ]

        results = []
        for page_file in season14_pages:
            result = await tester.test_page_links(page, page_file)
            results.append(result)

        # Test category pages
        print("\n" + "=" * 60)
        print("Testing Category Pages")
        print("=" * 60)

        category_pages = ["categories.html", "category.html"]
        for cat_page in category_pages:
            if (OUTPUT_DIR / cat_page).exists():
                result = await tester.test_page_links(page, cat_page)
                results.append(result)

        # Test main index page
        print("\n" + "=" * 60)
        print("Testing Main Index")
        print("=" * 60)
        result = await tester.test_page_links(page, "index.html")
        results.append(result)

        await browser.close()

        # Print summary
        print("\n" + "=" * 60)
        print("TEST SUMMARY")
        print("=" * 60)
        print(f"Total links tested: {tester.tested_links}")
        print(f"Successful links: {tester.successful_links}")
        print(f"Failed links: {len(tester.broken_links)}")

        # Collect all broken links
        all_broken = []
        for result in results:
            if 'broken_links' in result:
                all_broken.extend(result['broken_links'])

        if all_broken:
            print("\n" + "=" * 60)
            print("BROKEN LINKS DETAILS")
            print("=" * 60)
            for broken in all_broken:
                print(f"\nPage: {broken.get('page', 'unknown')}")
                print(f"  Text: {broken['text']}")
                print(f"  Link: {broken['href']}")
                if 'status' in broken:
                    print(f"  Status: {broken['status']}")
                if 'error' in broken:
                    print(f"  Error: {broken['error']}")
        else:
            print("\n✓ All internal links are working correctly!")

        return len(all_broken) == 0

if __name__ == "__main__":
    success = asyncio.run(test_season14_links())
    exit(0 if success else 1)