from app.adapter.in_memory_mood_repository import InMemoryMoodRepository
from app.domain.mood import Mood


def main():
    mood_repository = InMemoryMoodRepository()

    Mood().save(mood_repository)
    Mood().save(mood_repository)

    print(mood_repository.all())
    print(f'Total votes: {mood_repository.total()}')


if __name__ == '__main__':
    main()
