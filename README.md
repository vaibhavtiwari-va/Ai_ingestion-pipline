# AI Intelligence Data Ingestion Pipeline

## Overview
Production-ready data pipeline built for extracting, structuring, and canonicalizing multi-dimensional AI datasets including Startups, Products, Research Papers, Jobs, and News.

## Project Structure
- `src/scraper.py`: Bulk data extractor for Startups, Products, and Arxiv Research Papers (with GitHub stars).
- `src/llm_pipeline.py`: LiteLLM fallback chain setup (Gemini Flash -> Groq Llama 3) and Fuzzy Entity Resolution.
- `src/news_jobs_generator.py`: Fresh 24-hour signal ingestion module for news & jobs.
- `architecture.pdf`: System design, scaling strategies for 500k+ records, and storage choices.

## Setup & Execution
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
