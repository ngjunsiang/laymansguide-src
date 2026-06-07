#!/usr/bin/env python3
"""
Build pipeline orchestrator for Layman's Guide newsletter site.

This script coordinates the complete content pipeline:
1. Scraping newsletter content from Buttondown (optional)
2. Processing content for Pelican
3. Building the static site
"""

import argparse
import subprocess
import sys
from pathlib import Path


def step_scrape(args):
    """Step 1: Scrape content from Buttondown."""
    print("🔍 Step 1: Scraping newsletter content...")
    print("   This requires: pip install beautifulsoup4 requests")

    if args.force:
        from build.scrape import scrape_issues
        scrape_issues(
            max_pages=args.pages,
            json_output=args.json_output,
            csv_output=args.csv_output
        )
    else:
        print("   ⏭️  Skipping scraping (use --force to enable)")


def step_process(args):
    """Step 2: Process content for Pelican."""
    print("🔧 Step 2: Processing content for Pelican...")

    from build.process import ContentProcessor

    metadata_path = args.csv_output if args.csv_output else "build/metadata/metadata.csv"
    processor = ContentProcessor(metadata_path)

    if args.metadata:
        print("   Adding Pelican metadata headers...")
        processor.process_metadata_headers()
    else:
        print("   ⏭️  Skipping metadata headers (use --metadata to enable)")

    if args.figures:
        print("   Processing figures and summaries...")
        processor.process_figures_and_summaries()
    else:
        print("   ⏭️  Skipping figure processing (use --figures to enable)")


def step_build(args):
    """Step 3: Build the static site."""
    print("🏗️  Step 3: Building static site...")

    if args.production:
        print("   Building production version...")
        subprocess.run(["make", "publish"], check=True)
    else:
        print("   Building development version...")
        subprocess.run(["make", "html"], check=True)


def main():
    """Main pipeline orchestrator."""
    parser = argparse.ArgumentParser(
        description="Build pipeline for Layman's Guide newsletter site"
    )

    # Pipeline steps
    parser.add_argument("--scrape", action="store_true",
                       help="Run scraping step")
    parser.add_argument("--process", action="store_true",
                       help="Run processing step")
    parser.add_argument("--build", action="store_true",
                       help="Run build step")

    # Scraping options
    parser.add_argument("--force", action="store_true",
                       help="Force scraping from Buttondown")
    parser.add_argument("--pages", type=int, default=4,
                       help="Number of archive pages to scrape")
    parser.add_argument("--json-output", default="build/metadata/issues_v4.json",
                       help="Path for JSON output")
    parser.add_argument("--csv-output", default="build/metadata/metadata.csv",
                       help="Path for CSV output")

    # Processing options
    parser.add_argument("--metadata", action="store_true",
                       help="Add Pelican metadata headers")
    parser.add_argument("--figures", action="store_true",
                       help="Process figures and summaries")

    # Build options
    parser.add_argument("--production", action="store_true",
                       help="Build production version")

    # Convenience options
    parser.add_argument("--all", action="store_true",
                       help="Run all pipeline steps with default settings")
    parser.add_argument("--full", action="store_true",
                       help="Run complete pipeline with all processing enabled")

    args = parser.parse_args()

    # Handle convenience options
    if args.full:
        args.scrape = True
        args.process = True
        args.build = True
        args.force = True
        args.metadata = True
        args.figures = True
        args.production = True
    elif args.all:
        args.scrape = True
        args.process = True
        args.build = True

    # Validate data files exist before processing
    if args.process and not Path(args.csv_output).exists():
        print(f"❌ Error: Metadata file not found: {args.csv_output}")
        print("   Run with --scrape --force to generate it, or place it manually.")
        sys.exit(1)

    print("🚀 Starting Layman's Guide build pipeline...")
    print()

    try:
        if args.scrape:
            step_scrape(args)
            print()

        if args.process:
            step_process(args)
            print()

        if args.build:
            step_build(args)
            print()

        print("✅ Build pipeline completed successfully!")

    except subprocess.CalledProcessError as e:
        print(f"❌ Error: Command failed with exit code {e.returncode}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
