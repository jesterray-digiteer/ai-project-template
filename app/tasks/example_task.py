from celery_app import celery
from app.core.logger import get_logger
from app.services.example_service import process_payload

logger = get_logger(__name__)


@celery.task(bind=True, max_retries=3)
def run_example_task(self, payload: str) -> str:
    try:
        result = process_payload(payload)
        logger.info(f"Processed payload: {payload}")
        return result
    except Exception as exc:
        logger.error(f"Task failed: {exc}")
        raise self.retry(exc=exc)
    finally:
        pass
