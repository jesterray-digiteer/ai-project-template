from celery import Celery

from app.core.config import get_settings

settings = get_settings()

celery = Celery(
    "worker",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
    include=["app.tasks.example_task"],
)

celery.conf.task_routes = {
    "app.tasks.example_task.*": {"queue": "default"},
}

celery.conf.update(
    task_acks_late=True,
    task_reject_on_worker_lost=True,
    worker_prefetch_multiplier=1,
    worker_max_tasks_per_child=10,
)
