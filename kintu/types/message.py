from pydantic import BaseModel, ConfigDict
from kintu.types.content import Content
from kintu.types.role import Role

class Message(BaseModel):
    role: Role
    content: Content

    model_config = ConfigDict(arbitrary_types_allowed=True)