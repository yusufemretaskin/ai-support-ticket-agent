from fastapi import FastAPI
from app.api.v1 import health,tickets

app=FastAPI(
    title="AI Ticket Support Agent",
    version="1.0.0"
)

app.include_router(health.router,prefix="/api/v1")
app.include_router(tickets.router,prefix="/api/v1/tickets")