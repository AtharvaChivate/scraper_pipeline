# Hackathon Scraper Pipeline

A robust data pipeline that automatically scrapes and aggregates hackathon information from Major League Hacking (MLH) and Devpost platforms. The pipeline runs every three days, collecting hackathon details and storing them in AWS S3.

## 🎯 Features

- Automated scraping of hackathon data from multiple sources:
  - MLH (Major League Hacking) events
  - Devpost hackathons
- AWS S3 integration for data storage
- Automated data cleaning and combination
- GitHub Actions workflow for scheduled execution
- Comprehensive error handling and logging

## 🏗️ Architecture

The pipeline consists of three main components:

1. **MLH Scraper** (`scrape_mlh.py`):
   - Scrapes hackathon data from MLH's event page
   - Uses BeautifulSoup for HTML parsing
   - Extracts title, location, dates, and event URLs

2. **Devpost Scraper** (`scrape_devpost.py`):
   - Fetches hackathon data from Devpost's API
   - Supports pagination (currently set to 5 pages)
   - Collects similar event information

3. **Data Processor** (`combine_and_clean.py`):
   - Combines data from both sources
   - Removes duplicates
   - Stores final dataset in S3

## 🚀 Setup

### Prerequisites

- Python 3.10.11 or higher
- AWS Account with S3 access
- GitHub Account (for automated pipeline)

### Environment Variables

Set up the following AWS credentials as environment variables or GitHub Secrets:
```
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/scraper_pipeline.git
cd scraper_pipeline
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Configure AWS S3:
   - Create an S3 bucket named `my-hackathon-data-bucket` (or update the bucket name in the scripts)
   - Ensure your AWS credentials have appropriate permissions

### GitHub Actions Setup

1. Go to your repository's Settings > Secrets
2. Add the following secrets:
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`

## 🔄 Pipeline Execution

### Automated Execution

The pipeline automatically runs every three days at midnight UTC through GitHub Actions. The workflow:

1. Scrapes MLH data
2. Scrapes Devpost data
3. Combines and cleans the data
4. Stores results in S3

### Manual Execution

To run the pipeline locally:

```bash
python scrape_mlh.py
python scrape_devpost.py
python combine_and_clean.py
```

## 📊 Data Structure

The pipeline generates CSV files with the following structure:

```
Title    | Location | Dates           | URL
---------|----------|-----------------|----------------
Event 1  | Online   | Mar 15-17, 2024 | https://...
Event 2  | New York | Apr 1-3, 2024   | https://...
```

Files generated:
- `mlh.csv`: Raw MLH data
- `devpost.csv`: Raw Devpost data
- `combined.csv`: Clean, combined dataset

## 📝 Dependencies

Key dependencies include:
- beautifulsoup4: Web scraping
- boto3: AWS S3 integration
- pandas: Data processing
- requests: HTTP requests
- lxml: HTML parsing

Full dependencies are listed in `requirements.txt`.

## ⚡ Performance Considerations

- MLH scraper uses browser headers to avoid blocking
- Devpost API pagination is limited to 5 pages to prevent rate limiting
- Data deduplication is performed before storage

## 🔒 Security Notes

- AWS credentials should never be committed to the repository
- Use GitHub Secrets for credential management
- The pipeline uses minimal required AWS permissions
