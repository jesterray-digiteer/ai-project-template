from pydantic import BaseModel


class ExampleRequest(BaseModel):
    payload: str


class ExampleTaskPayload(BaseModel):
    payload: str


class ExampleResponse(BaseModel):
    task_id: str
    status: str
