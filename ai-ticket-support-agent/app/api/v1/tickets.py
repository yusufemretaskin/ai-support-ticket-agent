from fastapi import APIRouter, HTTPException
from app.schemas.ticket import TicketRequest, TicketResponse, TicketMessageRequest
from app.services.ai_ticket_analyzer import analyze_ticket_with_ai
from app.services.ticket_service import create_ticket_record, get_all_tickets, add_customer_message, build_ticket_context
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


@router.post("/{ticket_id}/messages")
def add_ticket_message(ticket_id: str, request: TicketMessageRequest):
    ticket = add_customer_message(
        ticket_id=ticket_id,
        message=request.message
    )
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    updated_analysis = analyze_ticket_with_ai(
        title=ticket["title"],
        description=build_ticket_context(ticket)
    )
    ticket["analysis"] = updated_analysis

    action_result = execute_ticket_action(
        ticket=ticket,
        analysis=updated_analysis
    )

    return {
        "ticket_id": ticket_id,
        "analysis": updated_analysis,
        "action_result": action_result
    }