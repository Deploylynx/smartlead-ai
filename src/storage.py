import pandas as pd
import os

FILE = "data/leads.csv"

def save_leads(leads):
    # ✅ STEP 1: create folder if not exists
    os.makedirs("data", exist_ok=True)

    df = pd.DataFrame(leads)

    # ✅ STEP 2: save safely
    if os.path.exists(FILE):
        df.to_csv(FILE, mode='a', header=False, index=False)
    else:
        df.to_csv(FILE, index=False)

    print("Leads saved successfully!")