from pydantic import BaseModel, Field
from typing import Optional

import uuid

class Todo(BaseModel):
    title: str
    description: str
    completed: bool

