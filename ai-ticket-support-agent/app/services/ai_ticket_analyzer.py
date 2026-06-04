import os
import json
from openai import OpenAI
from app.services.tool_definitions import TICKET_TOOLS
token = os.getenv("GITHUB_TOKEN")

client = OpenAI(
    base_url="https://models.github.ai/inference",
    api_key=token
)

model_name = "openai/gpt-4o-mini"


def analyze_ticket_with_ai(title: str, description: str) -> dict:
    prompt = f"""
You are an AI support ticket assistant.

Analyze the support ticket and choose the best backend tool.

Allowed priorities:
Low, Medium, High, Critical

Allowed categories:
Account Access, Billing, Technical Issue, Performance, Security, Feature Request, General Question

Allowed departments:
Identity Support, Finance Support, Engineering Support, Platform Support, Security Team, Product Team, Customer Support

Allowed selected_action values:
create_ticket_record, assign_ticket_to_department, escalate_ticket, request_more_information, generate_response_draft, mark_as_security_incident, suggest_knowledge_base_article, provide_information

Ticket title:
{title}

Ticket description:
{description}

"""

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "system",
                "content": "You analyze support tickets and choose the correct backend tool."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        tools=TICKET_TOOLS,
        tool_choice="required"
    )

    message=response.choices[0].message

    if not message.tool_calls:
        raise Exception("LLM did not return response from tool call.")
    
    tool_call=message.tool_calls[0]

    selected_action=tool_call.function.name

    arguments=json.loads(tool_call.function.arguments)

    return {
        "category": arguments["category"],
        "priority": arguments["priority"],
        "sentiment": arguments["sentiment"],
        "assigned_department": arguments["assigned_department"],
        "requires_escalation": arguments["requires_escalation"],
        "selected_action": selected_action,
        "summary": arguments["summary"],
        "response_draft": arguments["response_draft"],
        "reason": arguments["reason"]
    }