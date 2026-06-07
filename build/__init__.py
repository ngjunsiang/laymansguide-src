"""
Build pipeline for Layman's Guide newsletter processing.

This module handles the complete content pipeline from scraping to processing.
"""

from .scrape import scrape_issues, ButtondownScraper
from .process import ContentProcessor

__all__ = ['scrape_issues', 'ContentProcessor', 'ButtondownScraper', 'build_pipeline']


def build_pipeline(scrape: bool = False, process: bool = True):
    """
    Run the complete content pipeline.

    Args:
        scrape: If True, scrape fresh content from Buttondown
        process: If True, process content for Pelican
    """
    print("🚀 Starting build pipeline...")

    if scrape:
        print("Step 1: Scraping content from Buttondown...")
        scrape_issues()
        print()

    if process:
        print("Step 2: Processing content for Pelican...")
        processor = ContentProcessor()
        processor.process_all()
        print()

    print("✅ Build pipeline complete!")
