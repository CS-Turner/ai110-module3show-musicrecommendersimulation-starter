# 🎵 Music Recommender Simulation

## Project Summary

This project builds a content-based music recommender for an 18-song catalog. It scores songs against a listener's genre, mood, energy, and acousticness preferences, then ranks the top five. The project tests several listener profiles and explores how changing feature weights affects recommendations.

---

## How The System Works

Collaborative filtering recommends songs based on patterns in what listeners with similar tastes enjoy. Content-based filtering recommends songs with attributes (genre, mood, or tempo) that are similar to songs a user already likes. Real platforms typically combine both and incorporate user signals such as likes, skips, and replays. Mine will be content-based only, since there is no user behavior data to work with.

### Features Used
**Song features:** genre, mood, energy, acousticness
**UserProfile preferences:** favorite_genre, favorite_mood, target_energy, likes_acoustic
**Not used for scoring:** id, title, artist (identifiers only)

### Algorithm Recipe
Each song gets a score out of 10.0:
- +4.0 if genre matches the user's favorite genre
- +3.0 if mood matches the user's favorite mood
- Up to +2.0 for energy closeness: 2.0 × (1 - |song energy - target energy|)
- Up to +1.0 for acousticness: if the user likes acoustic, 1.0 × acousticness; otherwise 1.0 × (1 - acousticness)

Scoring judges one song. Ranking scores every song, sorts highest to lowest, and returns the top k with reasons.

### Expected Biases
Genre and mood together are worth 7 of 10 points, while energy—the feature that describes how a song sounds—gets only 2. A song with the right genre and mood labels but very different energy can still rank high. Genre is weighted 4 points to mood's 3, rather than the project's suggested 2:1 starting ratio; I weighted mood close to genre because mood reflects what the listener wants right now. Lofi has 3 of 18 songs, so lofi fans get more variety than jazz fans. Exact matches for mood and genre give no credit to near matches, such as "chill" and "relaxed".

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:

   ```bash
   python -m src.main
   ```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

```
============================================================
Profile: High-Energy Pop
============================================================
1. Sunrise City by Neon Echo
   Score: 9.76 / 10
   Because: genre match (+4.0); mood match (+3.0); energy closeness (+1.94); acousticness fit (+0.82)

2. Gym Hero by Max Pulse
   Score: 6.79 / 10
   Because: genre match (+4.0); energy closeness (+1.84); acousticness fit (+0.95)

3. Rooftop Lights by Indigo Parade
   Score: 5.47 / 10
   Because: mood match (+3.0); energy closeness (+1.82); acousticness fit (+0.65)

4. Storm Runner by Voltline
   Score: 2.78 / 10
   Because: energy closeness (+1.88); acousticness fit (+0.90)

5. Pulse Garden by Kaleo Wave
   Score: 2.76 / 10
   Because: energy closeness (+1.80); acousticness fit (+0.96)
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

I tested the recommender with several profiles. Chill Lofi ranked “Library Rain” first (9.80/10), while Deep Intense Rock ranked “Storm Runner” first (9.88/10). The Conflicted profile ranked the folk song “Pine Smoke Letters” first (5.73/10), even though it wanted a sad, high-energy, acoustic song.

I also halved the genre weight and doubled the energy weight. Pop's “Rooftop Lights” moved from third to second, and “Concrete Crown” entered the top five; Lofi's “Spacewalk Thoughts” moved from fourth to third. Rock's top-five order stayed the same. The change did not fix the Conflicted profile's acousticness mismatch.

In stress tests, “Pop” still matched “pop” after case-insensitive comparison. A genre missing from the catalog earned no genre points, and the recommender did not warn that it was missing. “Winter Hall Etude” ranked first for the maximum-energy profile because its genre and mood matches outweighed its low energy.

---

## Limitations and Risks

The catalog is small and uneven, with only 18 songs and most genres represented once. Genre and mood account for 7 of 10 points, so label matches can outweigh a mismatch in sound; acousticness contributes only 1 point. The recommender ignores tempo, valence, danceability, lyrics, listening history, and context, and it has no variety step to encourage discovery beyond the highest-scoring matches.

---

## Reflection

I learned that a recommender's results depend on the features and weights chosen by its designer. A strong genre or mood match can outweigh a mismatch in sound, as the Extreme Energy test showed. Testing different profiles and weights helped me see how these choices can narrow recommendations or favor some preferences over others.

See the [**Model Card**](model_card.md) for the full evaluation and limitations.
