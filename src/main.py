from lead_finder import find_leads
from ai_writer import generate_message
from storage import save_leads

def run():
    keyword = input("Enter client requirement: ")
    
    leads = find_leads(keyword)
    
    for lead in leads:
        message = generate_message(lead)
        lead['message'] = message
        print("\n--- Generated Message ---")
        print(message)
    
    save_leads(leads)

if __name__ == "__main__":
    run()