import uuid

from app.adapter.in_memory_mood_repository import InMemoryMoodRepository
from app.domain.mood import Mood


def test_mood_save():
    mood = Mood()
    mood_repository = InMemoryMoodRepository()

    assert mood.save(mood_repository).mood_id == mood.mood_id


def test_mood_repository_all():
    mood_repository = InMemoryMoodRepository()
    mood_1 = Mood().save(mood_repository)
    mood_2 = Mood().save(mood_repository)

    assert set(mood_repository.all()) == {mood_1, mood_2}


def test_mood_repository_total():
    mood_repository = InMemoryMoodRepository()
    Mood().save(mood_repository)
    Mood().save(mood_repository)

    assert mood_repository.total() == 2


def test_mood_repository_get():
    mood_repository = InMemoryMoodRepository()

    mood_id = str(uuid.uuid4())
    expected_mood = Mood(mood_id=mood_id)
    expected_mood.save(mood_repository)
    actual_mood = mood_repository.get(mood_id)

    assert expected_mood == actual_mood
