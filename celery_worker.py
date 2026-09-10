from celery_app import celery
import app.tasks.example_task  # noqa: F401

if __name__ == "__main__":
    celery.worker_main()
