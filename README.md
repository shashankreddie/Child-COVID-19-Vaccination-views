# Child COVID-19 Vaccination Views

This project gathers and processes Twitter data to explore public sentiment around COVID-19 vaccinations for children. The repository includes simple utilities for scraping Twitter replies to the CDC and converting them into a structured CSV format for further analysis.

## Project Goals

- Collect replies to specific CDC tweets that discuss child vaccinations.
- Convert the scraped JSON replies into CSV files for analysis or visualization.
- Provide a lightweight starting point for sentiment analysis or other research around vaccination conversations on social media.

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd Child-COVID-19-Vaccination-views
   ```
2. **Create a virtual environment (optional but recommended)**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install dependencies**
   The tools rely on `tweepy` and the standard library. Install Tweepy with:
   ```bash
   pip install tweepy
   ```
4. **Configure Twitter credentials**
   Update `data_scraping/replies.py` with your own Twitter API keys.

## Usage Examples

1. **Scrape replies**
   ```bash
   python data_scraping/replies.py
   ```
   The script saves each reply as a JSON file in the path specified inside the script.

2. **Convert JSON files to CSV**
   Place your JSON filenames inside a text file (e.g., `filename.txt`) and run:
   ```bash
   python sentiment_analysis/loading_data_from_json_to_csv/LoadingJsontoCSV.py
   ```
   This generates `filename.csv` with selected fields from the tweets.

## Repository Structure

- `data_scraping/` – scripts for collecting Twitter replies.
- `sentiment_analysis/loading_data_from_json_to_csv/` – utility to turn JSON data into CSV for analysis.

Feel free to adapt these scripts for your own research on vaccination discourse.
