from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from app.models.task import TasksStatus


# schemas are Python classes that use Pydantic to help validate data (information)
# that gets send to and from the API.

class TaskCreate(BaseModel):
    title: str
    description: Optional[str]
    status: TasksStatus = TasksStatus.PENDING


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TasksStatus] = None


class TaskStatusUpdate(BaseModel):
    status: TasksStatus


# Response schema for returning task data which is slimmed down as we
# don't want to return everything stored in the database.
class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: TasksStatus
    org_id: str
    created_by: str
    created_at: datetime
    updated_at: datetime


    class Config:
        from_attributes = True