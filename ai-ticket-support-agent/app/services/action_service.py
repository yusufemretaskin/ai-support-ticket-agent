def execute_ticket_action(ticket: dict, analysis: dict) -> dict:
    selected_action = analysis["selected_action"]

    if selected_action == "create_ticket_record":
        return create_ticket_action(ticket)

    if selected_action == "assign_ticket_to_department":
        return assign_ticket_to_department(ticket)

    if selected_action == "escalate_ticket":
        return escalate_ticket(ticket)

    if selected_action == "request_more_information":
        return request_more_information(ticket)

    if selected_action == "provide_information":
        return provide_information(ticket)

    return {
        "action": selected_action,
        "status": "failed",
        "message": "Unknown action selected."
    }


def create_ticket_action(ticket: dict) -> dict:
    return {
        "action": "create_ticket_record",
        "status": "completed",
        "message": f"Ticket {ticket['ticket_id']} was created."
    }


def assign_ticket_to_department(ticket: dict) -> dict:
    return {
        "action": "assign_ticket_to_department",
        "status": "completed",
        "department": ticket["assigned_department"],
        "message": f"Ticket assigned to {ticket['assigned_department']}."
    }


def escalate_ticket(ticket: dict) -> dict:
    ticket["status"] = "Escalated"

    return {
        "action": "escalate_ticket",
        "status": "completed",
        "message": f"Ticket {ticket['ticket_id']} was escalated."
    }


def request_more_information(ticket: dict) -> dict:
    ticket["status"] = "Waiting for Customer"

    return {
        "action": "request_more_information",
        "status": "completed",
        "message": "More information requested from customer."
    }


def provide_information(ticket: dict) -> dict:
    ticket["status"] = "Information Provided"

    return {
        "action": "provide_information",
        "status": "completed",
        "message": "Information response prepared for customer."
    }