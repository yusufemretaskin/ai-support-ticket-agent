from typing import Any
from pydantic import BaseModel

class TicketRequest(BaseModel):
    title:str
    description:str

class TicketAnalysis(BaseModel):
    category:str
    priority: str
    sentiment: str
    assigned_department: str
    requires_escalation: bool
    selected_action: str
    summary: str
    response_draft: str

class TicketResponse(BaseModel):
    title:str
    description:str
    analysis:str
    analysis: TicketAnalysis
    action_result: dict[str, Any]