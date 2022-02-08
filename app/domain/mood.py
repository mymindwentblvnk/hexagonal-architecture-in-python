import uuid
from dataclasses import dataclass, field


@dataclass
class Mood:

    mood_id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def save(self, mood_repository: 'MoodRepository') -> 'Mood':
        return mood_repository.add(self)

    def __hash__(self):
        return hash(self.mood_id)
