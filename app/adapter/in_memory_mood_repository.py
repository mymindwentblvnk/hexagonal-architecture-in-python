from typing import List

from app.domain.mood_repository import MoodRepository


class InMemoryMoodRepository(MoodRepository):

    def __init__(self):
        self.moods = list()

    def add(self, mood: 'Mood') -> 'Mood':
        self.moods.append(mood)
        return mood

    def all(self) -> List['Mood']:
        return self.moods

    def get(self, mood_id: str) -> 'Mood':
        [mood] = filter(lambda m: m.mood_id == mood_id, self.moods)
        return mood

    def total(self) -> int:
        return len(self.moods)
