import sys
import os
from flask import Flask, render_template, request, send_file

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.lead_finder import find_leads
from src.ai_writer import generate_message
from src.storage import save_leads
from src.enrichment import enrich_lead

app = Flask(__name__)

latest_leads = []

@app.route("/", methods=["GET", "POST"])
def home():
    global latest_leads

    leads = []

    if request.method == "POST":
        keyword = request.form.get("keyword", "").strip()

        if keyword:
            leads = find_leads(keyword)

            for lead in leads:
                lead = enrich_lead(lead)
                lead["message"] = generate_message(lead)

                lead["website"] = lead.get("website") or "Not found"
                lead["company"] = lead.get("company") or "Unknown Company"
                lead["keyword"] = keyword
            save_leads(leads)    

            latest_leads = leads
        else:
            latest_leads = []

    return render_template("index.html", leads=latest_leads)


@app.route("/export")
def export():
    return send_file("../data/leads.csv", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)