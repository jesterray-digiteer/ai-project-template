# fastapi-template

Starter folder structure for Digiteer AI projects: FastAPI + Celery/Redis, with the
layering convention used across projects like funtastic-ai. Copy this folder to start
a new project, then rename it and fill in the example route/task/service with real
business logic.

## Layering convention

- `app/routes/` — HTTP layer only: parse input, check auth, dispatch to a Celery task
  or service, return a response. No business logic here.
- `app/tasks/` — Celery task wrappers: (de)serialize payloads, call into `app/services/`,
  log, retry/report failures.
- `app/services/` — actual business/domain logic.
- `app/schemas/` — all Pydantic request/response/payload models.
- `app/core/` — settings (`config.py`), logging (`logger.py`), auth (`security.py`).
- `app/utils/` — generic shared helpers not tied to one domain concept.

## Using this template

1. Copy this folder to a new project directory and `git init`.
2. Rename `name` in `pyproject.toml`.
3. `cp .env.example .env` and fill in real values.
4. `uv sync`
5. Run the API: `uv run uvicorn main:app --reload`
6. Run the worker (separate terminal): `uv run python celery_worker.py`
7. Run tests: `uv run pytest`
8. Replace `app/routes/example.py`, `app/tasks/example_task.py`,
   `app/services/example_service.py`, and `app/schemas/example.py` with your project's
   actual routes/tasks/services/schemas, following the same layering.

If a project doesn't need async background processing, drop `celery_app.py`,
`celery_worker.py`, `app/tasks/`, and the `celery`/`redis` dependencies.
