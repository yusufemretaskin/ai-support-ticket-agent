from fastapi import APIRouter
from app.schemas.ticket import TicketRequest, TicketResponse
from app.services.ai_ticket_analyzer import analyze_ticket_with_ai
from app.services.ticket_service import create_ticket_record, get_all_tickets
from app.services.action_service import execute_ticket_action

router=APIRouter()

@router.get("")
def get_tickets():
    return {
        "tickets": get_all_tickets()
    }

@router.post("", response_model=TicketResponse)
def create_ticket(request: TicketRequest):
    analysis = analyze_ticket_with_ai(
        title=request.title,
        description=request.description
    )

    ticket = create_ticket_record(
        title=request.title,
        description=request.description,
        analysis=analysis
    )

    action_result = execute_ticket_action(
        ticket=ticket,
        analysis=analysis
    )

    return {
        "ticket_id": ticket["ticket_id"],
        "title": request.title,
        "description": request.description,
        "analysis": analysis,
        "action_result": action_result
    }