import uvicorn
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.core.config import get_settings
from app.core.logger import get_logger
from app.routes.example import example_router

settings = get_settings()
logger = get_logger(__name__)

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    logger.error(f"Validation error on {request.url}: {exc.errors()}")
    return JSONResponse(status_code=422, content={"error": exc.errors(), "body": exc.body})


origins = [settings.LOCALHOST_URL, settings.STAGING_URL, settings.PROD_URL]
origins = [origin for origin in origins if origin]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(example_router)


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"message": "API is Running"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
