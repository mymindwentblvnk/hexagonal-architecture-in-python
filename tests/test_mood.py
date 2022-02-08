import uuid
from app.domain.mood import Mood


def test_vote_existing_vote_id():
    mood_id = str(uuid.uuid4())
    assert Mood(mood_id).mood_id == mood_id


def test_vote_defaults():
    mood_id = str(uuid.uuid4())
    assert Mood().mood_id != mood_id