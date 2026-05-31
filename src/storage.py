import pandas as pd
import os

FILE = "data/leads.csv"

COLUMNS = [
    "name",
    "company",
    "website",
    "email",
    "contact_page",
    "keyword",
    "need",
    "message"
]

def save_leads(leads):

    os.makedirs("data", exist_ok=True)

    df = pd.DataFrame(leads)

    for col in COLUMNS:
        if col not in df.columns:
            df[col] = ""

    df = df[COLUMNS]

    if os.path.exists(FILE):
        df.to_csv(FILE, mode="a", header=False, index=False)
    else:
        df.to_csv(FILE, index=False)

    print("Leads saved successfully!")