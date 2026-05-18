import requests

def find_leads(keyword):
    print(f"Searching leads for: {keyword}")
    
    # Dummy leads (safe version)
    leads = [
        {"name": "John Smith", "company": "TechCorp", "need": keyword},
        {"name": "Ahmed Ali", "company": "CloudX", "need": keyword},
        {"name": "Sarah Lee", "company": "StartupHub", "need": keyword}
    ]
    
    return leads