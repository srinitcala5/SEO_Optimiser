# Optimisr: SEO Keyword Analyzer using Google Ads API

Optimisr is an internal tool built to help content creators and SEO specialists optimize their existing content by identifying better keywords and analyzing keyword opportunities using Google's Keyword Plan Idea Service.

## 🚀 Features
- Analyze content or URLs to extract existing keywords
- Use Google Ads API to get keyword suggestions
- Retrieve keyword metrics (search volume, competition)
- Display top keyword recommendations

## 🧰 Tech Stack
- Python 3.10+
- Google Ads API (via `google-ads` library)
- OAuth2 Authentication
- UiPath (for workflow automation - optional)

## 📦 Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourname/optimisr-seo.git
cd optimisr-seo
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup Credentials
- Place your `google-ads.yaml` or `client_secret.json` in the project root
- Follow Google’s OAuth2 guide to generate your `refresh_token`

### 4. Environment Variables (optional)
Create a `.env` file:
```
DEVELOPER_TOKEN=your_token_here
CLIENT_ID=your_client_id_here
CLIENT_SECRET=your_secret_here
REFRESH_TOKEN=your_refresh_token_here
CUSTOMER_ID=your_customer_id
```

## 🧪 Run the Tool (Example)
```bash
python run_keyword_analysis.py --text "Affordable solar batteries for off-grid homes"
```

Or
```bash
python run_keyword_analysis.py --url "https://example.com/solar"
```

## 📊 Output
- Ranked list of keyword suggestions with:
  - Search volume
  - Competition
  - CPC estimates (if available)

## ⚠️ Disclaimer
This tool is in development. It does not access or manage Google Ads accounts or campaigns. It is used exclusively for SEO research and internal automation.

## 📄 License
MIT License

---

Feel free to fork, test, or contribute.

---

_This repo was created as part of a Google Ads API access request to demonstrate intent, design, and use case._
