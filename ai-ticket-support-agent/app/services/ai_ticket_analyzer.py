import os
import json
from openai import OpenAI

token = os.getenv("GITHUB_TOKEN")

client = OpenAI(
    base_url="https://models.github.ai/inference",
    api_key=token
)

model_name = "openai/gpt-4o-mini"


def analyze_ticket_with_ai(title: str, description: str) -> dict:
    prompt = f"""
You are an AI support ticket assistant.

Analyze the ticket and return JSON only.

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

Return this JSON structure only:
{{
  "category": "...",
  "priority": "...",
  "sentiment": "Neutral | Frustrated | Angry",
  "assigned_department": "...",
  "requires_escalation": true,
  "selected_action": "...",
  "summary": "...",
  "response_draft": "..."
}}
"""

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "system",
                "content": "You analyze support tickets and return valid JSON only."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response.choices[0].message.content.strip()

    if content.startswith("```"):
        content = content.replace("```json", "").replace("```", "").strip()

    return json.loads(content)