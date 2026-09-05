import pandas as pd
from datetime import datetime, timezone

# 1. Fresh News Data Sample
news_data = [
    {
        "schemaVersion": "1.0", "recordType": "NEWS",
        "source_name": "TechCrunch AI", 
        "source_url": "https://techcrunch.com/category/artificial-intelligence/",
        "title": "OpenAI Announces Next-Gen Model Architecture",
        "published_date": datetime.now(timezone.utc).isoformat(),
        "summary": "Breakthroughs in reasoning capabilities announced today."
    },
    {
        "schemaVersion": "1.0", "recordType": "NEWS",
        "source_name": "VentureBeat AI", 
        "source_url": "https://venturebeat.com/category/ai/",
        "title": "Anthropic Expands Enterprise Solutions",
        "published_date": datetime.now(timezone.utc).isoformat(),
        "summary": "New features tailored for large enterprise deployment."
    }
]

# 2. Fresh Jobs Data Sample
jobs_data = [
    {
        "schemaVersion": "1.0", "recordType": "JOB",
        "source_name": "AI Jobs Board",
        "source_url": "https://ai-jobs.net/job/101",
        "company": "Anthropic",
        "date": datetime.now(timezone.utc).isoformat(),
        "is_remote": True,
        "role_family": "Engineering"
    },
    {
        "schemaVersion": "1.0", "recordType": "JOB",
        "source_name": "YCombinator Jobs",
        "source_url": "https://www.ycombinator.com/jobs/201",
        "company": "OpenAI",
        "date": datetime.now(timezone.utc).isoformat(),
        "is_remote": False,
        "role_family": "Research"
    }
]

pd.DataFrame(news_data).to_csv("news.csv", index=False)
pd.DataFrame(jobs_data).to_csv("jobs.csv", index=False)
print("✅ news.csv and jobs.csv generated successfully!")