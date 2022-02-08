import abc
from typing import List

from app.domain.mood import Mood


class MoodRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def add(self, mood: Mood) -> Mood:
        raise NotImplementedError

    @abc.abstractmethod
    def all(self) -> List[Mood]:
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, mood_id: str) -> Mood:
        raise NotImplementedError

    @abc.abstractmethod
    def total(self) -> int:
        raise NotImplementedError
