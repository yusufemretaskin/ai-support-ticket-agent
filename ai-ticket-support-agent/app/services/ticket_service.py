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

def get_ticket_by_id(ticket_id:str)->dict | None:
    for ticket in tickets_db:
        if(ticket["ticket_id"]==ticket_id):
            return ticket
        
    return None



def add_customer_message(ticket_id: str, message: str) -> dict | None:
    ticket = get_ticket_by_id(ticket_id)

    if ticket is None:
        return None

    if "messages" not in ticket:
        ticket["messages"] = []

    ticket["messages"].append({
        "role": "customer",
        "content": message
    })

    return ticket

def build_ticket_context(ticket : dict) -> str:
    context_parts = [
        f"Title: {ticket['title']}",
        f"Original description: {ticket['description']}"
    ]
    
    messages = ticket.get("messages", [])

    if messages:
        context_parts.append("Follow-up messages:")

        for message in messages:
            context_parts.append(
                f"{message['role']}: {message['content']}"
            )
    
    return "\n".join(context_parts)