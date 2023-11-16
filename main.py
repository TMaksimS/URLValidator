"""main file for starting webapp"""

import uvicorn
from fastapi import FastAPI, Response

from src.webapp import app as handlers
from settings import LOGER, APP_PORT, APP_HOST, APP_RELOAD

app = FastAPI(
    title="LeadHit app",
    description="Web-приложение для определения заполненных форм",
    version="0.1",
    contact={
        "name": "Tarkin Maksim",
        "email": "williamcano97@gmail.com"
    },
)
app.include_router(
    router=handlers
)


@app.get("/")
async def curl():
    """Default endpoint for healthcheck"""
    return Response(content="OK", status_code=200)


@LOGER.catch
def main(host: str, port: int, reload: bool) -> uvicorn:
    """Head func for starting application"""
    return uvicorn.run(
        "main:app",
        host=f"{host}",
        port=port,
        reload=reload
    )


if __name__ == "__main__":
    main(host=APP_HOST, port=APP_PORT, reload=APP_RELOAD)
