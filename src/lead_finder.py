from tavily import TavilyClient

API_KEY = "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"

client = TavilyClient(api_key=API_KEY)

BAD_WORDS = [
    "top",
    "best",
    "guide",
    "review",
    "reviews",
    "companies",
    "startups",
    "watch",
    "article",
    "blog",
    "list"
]


def clean_company_name(title):
    if "|" in title:
        return title.split("|")[-1].strip()

    if ":" in title:
        return title.split(":")[0].strip()

    if "-" in title:
        return title.split("-")[0].strip()

    return title.strip()


def find_leads(keyword):
    print(f"Searching REAL companies for: {keyword}")

    try:
        response = client.search(
            query=f"{keyword} software company official website",
            search_depth="basic",
            max_results=20
        )

        results = []

        for item in response.get("results", []):

            title = item.get("title", "").strip()
            url = item.get("url", "").strip()

            if not title or not url:
                continue

            title_lower = title.lower()

            # Skip article/list pages
            if any(word in title_lower for word in BAD_WORDS):
                continue

            company = clean_company_name(title)

            results.append({
                "name": "Decision Maker",
                "company": company,
                "website": url,
                "keyword": keyword,
                "need": keyword
            })

            if len(results) >= 10:
                break

        print(f"Found {len(results)} filtered leads")
        return results

    except Exception as e:
        print("API error:", e)
        return []