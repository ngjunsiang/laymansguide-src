# Build Pipeline

This directory contains the content processing pipeline for the Layman's Guide newsletter site.

## Structure

```
build/
├── __init__.py          # Package initialization and main pipeline functions
├── process.py           # Content processing (URL conversion, metadata, figures)
├── scrape.py            # Web scraping from Buttondown email service
└── metadata/            # Generated data files
    ├── issues_v4.json   # JSON database of all newsletter issues
    └── metadata.csv     # CSV version for processing scripts
```

## Usage

### As a Python module

```python
from build import ContentProcessor, build_pipeline

# Process existing content
processor = ContentProcessor()
processor.process_all()

# Or run the complete pipeline
build_pipeline(scrape=False, process=True)
```

### Via command line

```bash
# Process content only (default)
make pipeline

# Scrape fresh content from Buttondown
make scrape

# Process content with metadata and figures
make process-content

# Run complete pipeline (scrape + process + build)
make full-pipeline
```

### Via the pipeline script

```bash
# Show all options
python scripts/pipeline.py --help

# Process content only
python scripts/pipeline.py --process --metadata --figures

# Run complete pipeline
python scripts/pipeline.py --full
```

## Components

### `scrape.py`
Handles downloading newsletter content from Buttondown:
- Fetches archive pages
- Extracts issue metadata (titles, dates, URLs)
- Exports to JSON and CSV formats

### `process.py`
Processes newsletter content for Pelican:
- Converts external URLs to local references
- Adds Pelican metadata headers
- Processes figure formatting
- Extracts issue summaries

### `metadata/`
Contains generated data files:
- `issues_v4.json`: Complete JSON database of issues
- `metadata.csv`: CSV format for content processing

## Dependencies

For scraping functionality:
```bash
pip install beautifulsoup4 requests
```

For basic processing:
```bash
pip install csv
```

## Pipeline Flow

1. **Scrape** (optional): Download content from Buttondown → `metadata/`
2. **Process**: Convert content for Pelican → `content/`
3. **Build**: Generate static site → `output/`

## Notes

- The pipeline uses existing metadata files by default
- Set `--force` flag to re-scrape from Buttondown
- Content files are organized by season in `content/seasonXX/issueXXX/`
