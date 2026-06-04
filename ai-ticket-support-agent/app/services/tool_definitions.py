TICKET_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "assign_ticket_to_department",
            "description": "Assign the ticket to the correct support department.",
            "parameters": {
                "type": "object",
                "properties": {
                    "category": {"type": "string"},
                    "priority": {"type": "string"},
                    "sentiment": {"type": "string"},
                    "assigned_department": {"type": "string"},
                    "requires_escalation": {"type": "boolean"},
                    "summary": {"type": "string"},
                    "response_draft": {"type": "string"},
                    "reason": {"type": "string"}
                },
                "required": [
                    "category",
                    "priority",
                    "sentiment",
                    "assigned_department",
                    "requires_escalation",
                    "summary",
                    "response_draft",
                    "reason"
                ]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "escalate_ticket",
            "description": "Use when the issue is high priority, critical, urgent, or has strong business impact.",
            "parameters": {
                "type": "object",
                "properties": {
                    "category": {"type": "string"},
                    "priority": {"type": "string"},
                    "sentiment": {"type": "string"},
                    "assigned_department": {"type": "string"},
                    "requires_escalation": {"type": "boolean"},
                    "summary": {"type": "string"},
                    "response_draft": {"type": "string"},
                    "reason": {"type": "string"}
                },
                "required": [
                    "category",
                    "priority",
                    "sentiment",
                    "assigned_department",
                    "requires_escalation",
                    "summary",
                    "response_draft",
                    "reason"
                ]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "request_more_information",
            "description": "Use when the ticket does not contain enough details to route or solve the issue.",
            "parameters": {
                "type": "object",
                "properties": {
                    "category": {"type": "string"},
                    "priority": {"type": "string"},
                    "sentiment": {"type": "string"},
                    "assigned_department": {"type": "string"},
                    "requires_escalation": {"type": "boolean"},
                    "summary": {"type": "string"},
                    "response_draft": {"type": "string"},
                    "reason": {"type": "string"}
                },
                "required": [
                    "category",
                    "priority",
                    "sentiment",
                    "assigned_department",
                    "requires_escalation",
                    "summary",
                    "response_draft",
                    "reason"
                ]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "provide_information",
            "description": "Use when the ticket is a general question and can be answered directly.",
            "parameters": {
                "type": "object",
                "properties": {
                    "category": {"type": "string"},
                    "priority": {"type": "string"},
                    "sentiment": {"type": "string"},
                    "assigned_department": {"type": "string"},
                    "requires_escalation": {"type": "boolean"},
                    "summary": {"type": "string"},
                    "response_draft": {"type": "string"},
                    "reason": {"type": "string"}
                },
                "required": [
                    "category",
                    "priority",
                    "sentiment",
                    "assigned_department",
                    "requires_escalation",
                    "summary",
                    "response_draft",
                    "reason"
                ]
            }
        }
    }
]