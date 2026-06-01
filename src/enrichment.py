import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

EMAIL_REGEX = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

def enrich_lead(lead):

    lead["email"] = ""
    lead["contact_page"] = ""

    website = lead.get("website", "")

    if not website:
        return lead

    try:
        response = requests.get(
            website,
            timeout=10,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        html = response.text

        emails = re.findall(EMAIL_REGEX, html)

        if emails:
            lead["email"] = emails[0]

        soup = BeautifulSoup(html, "html.parser")

        for a in soup.find_all("a", href=True):

            href = a["href"]

            if "contact" in href.lower():
                lead["contact_page"] = urljoin(
                    website,
                    href
                )
                break

    except Exception:
        pass

    score = 0

    if lead["email"]:
        score += 50

    if lead["contact_page"]:
        score += 30

    if lead.get("website"):
        score += 20

    lead["score"] = score

    return lead