from datetime import datetime, timezone
from uuid import uuid4

tickets_db=[]

def get_all_tickets():
    return tickets_db

def create_ticket_record(
        title:str,
        description:str,
        analysis:dict)->dict:
    ticket = {
        "ticket_id": str(uuid4()),
        "title": title,
        "description": description,
        "category": analysis["category"],
        "priority": analysis["priority"],
        "sentiment": analysis["sentiment"],
        "assigned_department": analysis["assigned_department"],
        "requires_escalation": analysis["requires_escalation"],
        "selected_action": analysis["selected_action"],
        "status": "Created",
        "created_at": datetime.now(timezone.utc).isoformat()
    }

    tickets_db.append(ticket)

    return ticket