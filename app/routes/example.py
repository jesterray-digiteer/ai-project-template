from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.core.logger import get_logger
from app.core.security import verify_api_key
from app.schemas.example import ExampleRequest, ExampleResponse
from app.tasks.example_task import run_example_task

logger = get_logger(__name__)

example_router = APIRouter(prefix="/example", tags=["example"])


@example_router.post("/", response_model=ExampleResponse, dependencies=[Depends(verify_api_key)])
async def submit_example(request: ExampleRequest) -> ExampleResponse | JSONResponse:
    try:
        task = run_example_task.apply_async(args=[request.payload])
        return ExampleResponse(task_id=task.id, status="queued")
    except Exception as exc:
        logger.error(f"Failed to queue example task: {exc}")
        return JSONResponse({"error": str(exc)}, status_code=500)
