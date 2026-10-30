from dataclasses import dataclass, field
from uuid import UUID
from .ids import new_id
from .messages import Message

@dataclass(slots=True)
class Session:
    id: UUID = field(default_factory=new_id)
    messages: list[Message] = field(default_factory=list)

    def add(self, message: Message) -> None:
        self.messages.append(message)
