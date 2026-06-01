# AI Ticket Support Agent

This is a FastAPI project that uses AI/NLP to analyze support tickets.

The project classifies tickets, detects priority and sentiment, assigns department, selects an action/function, executes backend action and returns response draft.

## What It Does

- Create support ticket
- Analyze ticket text with LLM
- Detect category
- Detect priority
- Detect sentiment
- Assign department
- Select action/function
- Execute backend action
- Create response draft
- Continue ticket conversation with follow-up messages

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Pydantic
- OpenAI compatible API / GitHub Models
- GitHub Codespaces

## Flow

```text
POST /api/v1/tickets
↓
FastAPI receives ticket
↓
LLM analyzes ticket with NLP
↓
LLM returns category, priority, sentiment, department and selected action
↓
Backend creates ticket record
↓
Backend executes selected function/action
↓
API returns analysis, action result and response draft
```

## Follow-up Flow

```text
LLM asks for more information
↓
Ticket status becomes Waiting for Customer
↓
User sends new message with ticket_id
↓
Backend adds message to same ticket
↓
LLM analyzes full ticket context again
↓
Backend executes new selected action
↓
API returns updated result
```

## Priority Types

```text
Low
Medium
High
Critical
```

## Categories

```text
Account Access
Billing
Technical Issue
Performance
Security
Feature Request
General Question
```

## Departments

```text
Identity Support
Finance Support
Engineering Support
Platform Support
Security Team
Product Team
Customer Support
```

## Actions / Functions

```text
create_ticket_record
assign_ticket_to_department
escalate_ticket
request_more_information
generate_response_draft
mark_as_security_incident
suggest_knowledge_base_article
provide_information
```

## Project Structure

```text
app/
  main.py
  api/v1/
    health.py
    tickets.py
  schemas/
    ticket.py
  services/
    ai_ticket_analyzer.py
    ticket_service.py
    action_service.py

requirements.txt
README.md
```

## Health

```http
GET /api/v1/health
```

## Create Ticket

```http
POST /api/v1/tickets
```

Example body:

```json
{
  "title": "Cannot login to my account",
  "description": "I cannot access my account after resetting my password. This is urgent."
}
```

Example response:

```json
{
  "ticket_id": "generated-ticket-id",
  "title": "Cannot login to my account",
  "description": "I cannot access my account after resetting my password. This is urgent.",
  "analysis": {
    "category": "Account Access",
    "priority": "High",
    "sentiment": "Frustrated",
    "assigned_department": "Identity Support",
    "requires_escalation": true,
    "selected_action": "escalate_ticket",
    "summary": "Customer cannot access the account and needs urgent support.",
    "response_draft": "Thank you for contacting support. We have escalated this issue to the Identity Support team."
  },
  "action_result": {
    "action": "escalate_ticket",
    "status": "completed",
    "message": "Ticket was escalated."
  }
}
```

## Get Tickets

```http
GET /api/v1/tickets
```

## Add Follow-up Message

```http
POST /api/v1/tickets/{ticket_id}/messages
```

Example body:

```json
{
  "message": "The error code is 504 and it affects all users."
}
```

## Install Packages

```bash
pip install -r requirements.txt
```

## Set Token

```bash
export GITHUB_TOKEN="your-token"
```

or if using OpenAI directly:

```bash
export OPENAI_API_KEY="your-token"
```

## Run API

```bash
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Swagger

After running the API, open:

```text
/docs
```


## Project Summary

This project shows an AI support ticket agent.

The LLM analyzes the ticket and selects the best action.  
The backend validates and executes the action.  
This keeps AI as the decision layer and backend as the trusted execution layer.