"""Buffer for connecting endpoints"""

from fastapi import APIRouter

from src.webapp.handbook_router import app as hb_handler

app = APIRouter(prefix="/api")
app.include_router(hb_handler)
