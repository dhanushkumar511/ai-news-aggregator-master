# 🤖 AI News Aggregator

An automated AI news aggregation and email delivery system that collects the latest AI-related content from multiple sources, stores it in a PostgreSQL database, processes articles, and delivers curated news updates via email.

---

# 📌 Project Overview

The AI industry moves extremely fast, with updates being published daily across blogs, research labs, and YouTube channels.

This project automates the entire workflow:

1. Collect AI news from multiple sources.
2. Store articles and videos in a PostgreSQL database.
3. Process and organize content.
4. Generate AI-powered digests (when API credits are available).
5. Deliver curated news through email.

The goal is to create a personalized AI newsletter system that eliminates the need to manually track multiple AI news sources.

---

# 🏗️ System Architecture

```text
YouTube Channels
        │
        ▼
  YouTube Scraper
        │
        ▼
    PostgreSQL
        ▲
        │
 OpenAI Scraper
        │
        ▼
 Anthropic Scraper
        │
        ▼
  Content Processing
        │
        ▼
 Digest Generation
        │
        ▼
   Email Delivery
```

---

# ✨ Features

### News Collection

* Scrapes AI-related YouTube channels
* Collects OpenAI articles
* Collects Anthropic articles
* Supports RSS-based content ingestion

### Database Storage

* PostgreSQL database
* Structured article storage
* Duplicate prevention
* Historical content tracking

### Content Processing

* Transcript extraction from YouTube videos
* Article processing pipeline
* Content normalization

### AI Digest Generation

* OpenAI API integration
* Automated article summarization
* Digest generation
* Article ranking

### Email Distribution

* Automated email delivery
* HTML email formatting
* Personalized digest generation

---

# 🛠️ Tech Stack

## Backend

* Python 3.14
* SQLAlchemy
* PostgreSQL
* Docker

## Data Collection

* Feedparser
* Requests
* BeautifulSoup4
* YouTube Transcript API

## AI

* OpenAI API
* Pydantic

## Infrastructure

* Docker Desktop
* Docker Compose

## Email

* SMTP
* Gmail App Password Authentication

---

# 📂 Project Structure

```text
ai-news-aggregator/
│
├── app/
│   ├── agent/
│   │   ├── curator_agent.py
│   │   ├── digest_agent.py
│   │   └── email_agent.py
│   │
│   ├── database/
│   │   ├── connection.py
│   │   ├── create_tables.py
│   │   ├── models.py
│   │   └── repository.py
│   │
│   ├── scrapers/
│   │   ├── youtube.py
│   │   ├── openai.py
│   │   └── anthropic.py
│   │
│   ├── services/
│   ├── profiles/
│   ├── runner.py
│   └── daily_runner.py
│
├── docker/
│   └── docker-compose.yml
│
├── main.py
├── pyproject.toml
└── README.md
```

---

# ⚙️ Setup

## Clone Repository

```bash
git clone https://github.com/your-username/ai-news-aggregator.git
cd ai-news-aggregator
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -e .
```

---

## Configure Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key

MY_EMAIL=your_email@gmail.com
APP_PASSWORD=your_gmail_app_password

POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=ai_news_aggregator
POSTGRES_HOST=localhost
POSTGRES_PORT=5433
```

---

## Start PostgreSQL

```bash
cd docker
docker compose up -d
```

---

## Create Database Tables

```bash
python app/database/create_tables.py
```

---

# 🚀 Running the Project

## Run Scrapers

```bash
python -m app.runner
```

---

## Run Full Pipeline

```bash
python main.py
```

---

## Send Email Updates

```bash
python send_simple_email.py
```

---

# 📊 Example Output

```text
YouTube videos: 8
OpenAI articles: 51
Anthropic articles: 23
```

---

# 🔥 Challenges Solved

During development:

* Configured Docker and PostgreSQL locally
* Resolved database connection conflicts
* Managed environment variables securely
* Integrated email delivery using Gmail SMTP
* Implemented scraping and storage pipelines
* Automated content aggregation workflows

---

# 📈 Future Improvements

* Web dashboard
* User authentication
* Scheduled background jobs
* Multi-user newsletters
* Advanced article ranking
* Vector search and semantic retrieval
* Streamlit/React frontend
* Deployment on AWS/GCP/Azure

---

# 🎯 Learning Outcomes

This project strengthened my understanding of:

* Python backend development
* PostgreSQL database design
* Docker containerization
* API integration
* Web scraping
* Email automation
* AI-powered content processing
* End-to-end data pipelines

---

# 👨‍💻 Author

**Dhanush Kumar**

Passionate about AI, automation, backend engineering, and building practical AI-powered products.

Feel free to connect and collaborate.
