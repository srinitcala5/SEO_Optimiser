import argparse
from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException


def get_keyword_ideas(client, customer_id, keywords):
    keyword_plan_idea_service = client.get_service("KeywordPlanIdeaService")
    location_ids = [1023191]  # Australia
    language_id = "1000"  # English

    geo_target_constants = [f"geoTargetConstants/{loc_id}" for loc_id in location_ids]

    keyword_seed = client.get_type("KeywordSeed")
    keyword_seed.keywords.extend(keywords)

    request = client.get_type("GenerateKeywordIdeasRequest")
    request.customer_id = customer_id
    request.language = f"languages/{language_id}"
    request.geo_target_constants.extend(geo_target_constants)
    request.keyword_seed = keyword_seed
    request.keyword_plan_network = client.enums.KeywordPlanNetworkEnum.GOOGLE_SEARCH

    try:
        response = keyword_plan_idea_service.generate_keyword_ideas(request=request)
        print("Keyword Ideas:\n")
        for idea in response:
            metrics = idea.keyword_idea_metrics
            print(
                f"{idea.text:30} | Volume: {metrics.avg_monthly_searches:6} | Competition: {metrics.competition.name}"
            )
    except GoogleAdsException as ex:
        print(f"Request failed with status {ex.error.code().name}")
        for error in ex.failure.errors:
            print(f"\t{error.message}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", help="Text to extract keywords from", required=False)
    parser.add_argument("--url", help="URL to analyze", required=False)
    args = parser.parse_args()

    if not args.text:
        print("Provide input text for keyword suggestion")
        return

    keywords = [word.strip() for word in args.text.split() if len(word) > 3]

    client = GoogleAdsClient.load_from_storage("google-ads.yaml")
    customer_id = client.login_customer_id or "INSERT_YOUR_CUSTOMER_ID"

    get_keyword_ideas(client, customer_id, keywords)


if __name__ == "__main__":
    main()