# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

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

2. Install dependencies

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

I ran the recommender with three other profiles:

- **Chill Lofi:** Library Rain ranked first (9.80/10), followed by Midnight Coding (9.63/10).
- **Deep Intense Rock:** Storm Runner ranked first (9.88/10), followed by Gym Hero (5.93/10).
- **Conflicted (edge case):** Pine Smoke Letters ranked first (5.73/10). It matched the folk genre and acoustic preference, but not the requested sad mood and was much lower energy than the 0.90 target.

- Phase 4 experiment to try: halve the genre weight (from 4 to 2) and double the energy weight (from 2 to 4), then compare how the recommendations change.

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions

- about where bias or unfairness could show up in systems like this
