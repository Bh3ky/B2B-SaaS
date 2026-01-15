import uuid
from datetime import datetime
from sqlalchemy import Column, String, Text,  DateTime, Enum
import enum
from app.core.database import Base

# define task status enum
class TasksStatus(str, enum.Enum):
    PENDING = "pending"
    STARTED = "started"
    COMPLETED = "completed"


class Task(Base):
    __tablename__ = "tasks"

    # define the table schema for our tasks
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(Enum(TasksStatus), default=TasksStatus.PENDING, nullable=False)
    org_id = Column(String, nullable=False, index=True)
    created_by = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)