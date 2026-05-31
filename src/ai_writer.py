def generate_message(lead):
    company = lead.get("company", "your company")
    need = lead.get("need", "business")

    return f"""
Hi {company},

I noticed that {company} may be interested in improving their {need} processes.

We help companies automate deployments, cloud infrastructure, DevOps workflows and platform engineering.

Would you be open to a quick discussion?

Best regards,
DeployLynx
"""