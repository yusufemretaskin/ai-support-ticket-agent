from datetime import datetime, timezone
from uuid import uuid4

tickets_db=[]

def create_ticket_obj(
        title:str,
        description:str,
        analysis:dict):
    tickets_db.append({
        "icket_id":str(uuid4()),
        "title":title,
        "description":description,
        "category":analysis["category"],
        "priority":analysis["priority"],
        "sentiment":analysis["sentiment"],
        "assigned_department": analysis["assigned_department"],
        "requires_escalation": analysis["requires_escalation"],
        "selected_action": analysis["selected_action"],
        "status": "Created",
        "created_at": datetime.now(timezone.utc).isoformat()

    })
    