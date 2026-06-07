# Scripts

This directory contains utility scripts for building and deploying the Layman's Guide newsletter site.

## Available Scripts

### `pipeline.py`
Main orchestrator for the content processing pipeline.

#### Usage Examples

```bash
# Run complete pipeline with all features
python scripts/pipeline.py --full

# Process existing content
python scripts/pipeline.py --process --metadata --figures

# Scrape new content and process it
python scripts/pipeline.py --scrape --force --process

# Build development site
python scripts/pipeline.py --build

# Build production site
python scripts/pipeline.py --build --production
```

#### Options

- `--scrape`: Run scraping step
- `--process`: Run processing step  
- `--build`: Run build step
- `--force`: Force scraping from Buttondown
- `--pages N`: Number of archive pages to scrape (default: 4)
- `--metadata`: Add Pelican metadata headers
- `--figures`: Process figures and summaries
- `--production`: Build production version
- `--all`: Run all steps with default settings
- `--full`: Run complete pipeline with all features enabled

## Integration with Make

The pipeline is integrated with the Makefile for convenience:

```bash
make pipeline          # Process content
make scrape            # Scrape newsletter content
make process-content   # Process with metadata and figures
make full-pipeline     # Run complete pipeline
```

## Error Handling

The pipeline includes error checking:
- Validates metadata files exist before processing
- Provides clear error messages for missing dependencies
- Exits with appropriate status codes

## Future Enhancements

Potential additions to this directory:
- `deploy.py`: Enhanced deployment script with multiple environments
- `validate.py`: Content validation and link checking
- `test.py`: Automated testing for build pipeline
