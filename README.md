## Project Title
Google Ads Keyword Analyzer

## Description
This script utilizes the Google Ads API to fetch keyword ideas, along with their average monthly search volume and competition level. It can take keyword input directly from the command line.

## Features
- Fetches keyword ideas from the Google Ads API.
- Provides average monthly searches for keywords.
- Shows competition level (e.g., LOW, MEDIUM, HIGH) for keywords.
- Accepts direct text input for keyword generation.
- Supports analyzing keywords from a given URL (planned feature).

## Requirements
- Python 3 (typically required by the `google-ads` library)
- Dependencies:
    - google-ads
    - python-dotenv
- To install dependencies, run:
  ```bash
  pip install -r requirements.txt
  ```

## Configuration
1.  **Google Ads API Access:**
    You need to have a Google Ads account and set up API access. Follow the official Google Ads API documentation to configure your `google-ads.yaml` file. This file contains your API credentials.
    A common place to store this file is in your home directory. Ensure it's correctly configured before running the script. The `google-ads.yaml` file is typically loaded from your home directory by default by the client library, but you can also place it in the project directory or specify its path via environment variables. Refer to the Google Ads API client library documentation for more details on configuration loading.

2.  **Customer ID:**
    The script requires your Google Ads Customer ID. The recommended way is to set it as `login_customer_id` in your `google-ads.yaml` file. Alternatively, you can modify the script directly by replacing `"INSERT_YOUR_CUSTOMER_ID"` with your actual customer ID in `run_keyword_analysis.py` (though this is less ideal as your ID might be accidentally committed).

## Usage
The script is run from the command line.

**To get keyword ideas from a text string:**
```bash
python run_keyword_analysis.py --text "your keyword phrases here"
```

**To get keyword ideas from a URL (planned feature):**
```bash
python run_keyword_analysis.py --url <URL_TO_ANALYZE>
```
*(Note: The URL functionality is not fully implemented in the current version of the script.)*

## Example
**Command:**
```bash
python run_keyword_analysis.py --text "digital marketing strategy"
```

**Example Output Format:**
```
Keyword Ideas:

digital marketing strategy     | Volume:   1000 | Competition: HIGH
online advertising plan        | Volume:    500 | Competition: MEDIUM
seo content marketing          | Volume:    750 | Competition: LOW
```
*(Output format and values are illustrative)*

## Contributing
Contributions are welcome. Please open an issue or submit a pull request.

## License
This project is unlicensed.
---
*Disclaimer: This script interacts with the Google Ads API and may incur costs depending on your API usage and account settings.*
