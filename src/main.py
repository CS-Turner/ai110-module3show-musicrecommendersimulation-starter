"""Command line runner for the Music Recommender Simulation."""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    profiles = {
        "High-Energy Pop": {
            "favorite_genre": "pop",
            "favorite_mood": "happy",
            "target_energy": 0.85,
            "likes_acoustic": False,
        },
        "Chill Lofi": {
            "favorite_genre": "lofi",
            "favorite_mood": "chill",
            "target_energy": 0.38,
            "likes_acoustic": True,
        },
        "Deep Intense Rock": {
            "favorite_genre": "rock",
            "favorite_mood": "intense",
            "target_energy": 0.92,
            "likes_acoustic": False,
        },
        "Conflicted (edge case)": {
            "favorite_genre": "folk",
            "favorite_mood": "sad",
            "target_energy": 0.90,
            "likes_acoustic": True,
        },
    }

    for name, user_prefs in profiles.items():
        print("\n" + "=" * 60)
        print(f"Profile: {name}")
        print("=" * 60)

        for rank, (song, score, explanation) in enumerate(
            recommend_songs(user_prefs, songs, k=5), start=1
        ):
            print(f"{rank}. {song['title']} by {song['artist']}")
            print(f"   Score: {score:.2f} / 10")
            print(f"   Because: {explanation}")
            print()


if __name__ == "__main__":
    main()