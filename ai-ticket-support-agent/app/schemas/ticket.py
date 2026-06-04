from typing import Any
from pydantic import BaseModel

class TicketRequest(BaseModel):
    title:str
    description:str

class TicketAnalysis(BaseModel):
    category: str
    priority: str
    sentiment: str
    assigned_department: str
    requires_escalation: bool
    selected_action: str
    summary: str
    response_draft: str
    reason: str

class TicketResponse(BaseModel):
    ticket_id: str
    title:str
    description:str
    analysis: TicketAnalysis
    action_result: dict[str, Any]

class TicketMessageRequest(BaseModel):
    message:str
    