# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeMatch: Content-Based Music Recommender**

---

## 2. Intended Use  

**Goal:** Predict the five songs in the catalog a listener is most likely to enjoy, based on their stated genre, mood, energy, and acoustic preferences. VibeMatch is for classroom exploration, not real listeners. Do not use it to make decisions about artists or to judge anyone's taste.

---

## 3. How the Model Works  

### Algorithm Summary

A song earns 4 points for matching the user's favorite genre and 3 points for matching their favorite mood. It can earn up to 2 points for having energy close to the user's target and up to 1 point for matching their acousticness preference. The points are added into a score out of 10, and songs are ranked from highest score to lowest. The recommender returns the top-ranked songs with brief reasons for their scores.

It compares genre, mood, energy, and acousticness with the listener's preferences.

---

## 4. Data  

The catalog has 18 example songs, 15 genres, and 12 mood labels. It includes energy, tempo, valence, danceability, and acousticness. The recommender scores energy and acousticness. The catalog is small and has no lyrics, listener history, or user feedback.

---

## 5. Strengths  

The system gives intuitive results when a profile's genre and mood match songs in the catalog. Deep Intense Rock puts “Storm Runner” first, while Chill Lofi puts “Library Rain” first.

---

## 6. Limitations and Bias 

The catalog is small and uneven: lofi has three songs, while most genres have one. Genre and mood are worth 7 of 10 points, so matching labels can outweigh a mismatch in sound. Exact label matching also treats related moods such as “sad” and “melancholy” as different. The model ignores tempo, valence, danceability, lyrics, context, and listening behavior.

Testing exposed a specific weakness: the Conflicted profile says it likes acoustic music, but songs ranked 2–5 all have low acousticness (0.05–0.35). Acousticness is worth only 1 point, while energy is worth 2, so those songs' high energy can outweigh the acoustic preference.

---

## 7. Evaluation  

I ran the recommender for High-Energy Pop, Chill Lofi, Deep Intense Rock, and Conflicted profiles. I checked whether the rankings matched each profile and inspected the score explanations.

**Pair comparisons**

- **Pop vs. Lofi:** The top song changes from high-energy, low-acoustic “Sunrise City” to low-energy, high-acoustic “Library Rain.” That fits the opposite sound preferences.
- **Pop vs. Rock:** Four of the five recommendations overlap. Both profiles want high-energy, non-acoustic songs; their genre and mood preferences distinguish the rankings.
- **Pop vs. Conflicted:** Both want high energy. Conflicted's ranks 2–5 all have low acousticness (0.05–0.35), despite its acoustic preference.
- **Lofi vs. Rock:** The top-five lists do not overlap. These profiles favor opposite energy and acousticness levels.
- **Lofi vs. Conflicted:** Both prefer acoustic music. Lofi's three matching songs fill its top three; Conflicted has only one folk song, then scores drop to about 2.
- **Rock vs. Conflicted:** Both target high energy. “Storm Runner” scores 9.88 for Rock, while “Pine Smoke Letters” scores 5.73 for Conflicted. No song is labeled “sad,” so Conflicted gets no mood-match points.

“Gym Hero” ranked second for both Pop and Rock for different reasons. For Pop, it earns 4 genre points as a pop song, even though its intense mood does not match happy. Its high energy helps keep it near the top. For Rock, its intense mood earns 3 points, and its high energy also suits that profile.

The adversarial profiles revealed more surprises. “Winter Hall Etude” ranked first for Extreme Energy (7.39) even though its energy is only 0.18 and its acousticness is 0.97; its classical genre and melancholy mood earned 7 points. With “Pop” capitalized, Sunrise City lost its exact genre match and fell from 9.76 to 5.76. For Genre Not in Catalog, no song earned genre points; three chill songs filled the top three (5.76, 5.68, and 5.67), and the recommender did not indicate that the requested genre was missing.

I also tried halving the genre weight from 4 to 2 and doubling the energy weight from 2 to 4, keeping the maximum score at 10. The results changed, but were not clearly better: Pop's “Rooftop Lights” moved from third to second, and “Concrete Crown” entered the top five. Lofi's “Spacewalk Thoughts” moved from fourth to third. Rock kept the same top-five order, while Conflicted replaced “Rooftop Lights” with “Pulse Garden.” “Pine Smoke Letters” stayed first for Conflicted, but its score fell from 5.73 to 4.53. The higher energy weight did not fix the Conflicted profile's acousticness mismatch.

**Terminal output for all seven profiles**

```text
Loaded songs: 18

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

============================================================
Profile: Chill Lofi
============================================================
1. Library Rain by Paper Lanterns
   Score: 9.80 / 10
   Because: genre match (+4.0); mood match (+3.0); energy closeness (+1.94); acousticness fit (+0.86)

2. Midnight Coding by LoRoom
   Score: 9.63 / 10
   Because: genre match (+4.0); mood match (+3.0); energy closeness (+1.92); acousticness fit (+0.71)

3. Focus Flow by LoRoom
   Score: 6.74 / 10
   Because: genre match (+4.0); energy closeness (+1.96); acousticness fit (+0.78)

4. Spacewalk Thoughts by Orbit Bloom
   Score: 5.72 / 10
   Because: mood match (+3.0); energy closeness (+1.80); acousticness fit (+0.92)

5. Coffee Shop Stories by Slow Stereo
   Score: 2.87 / 10
   Because: energy closeness (+1.98); acousticness fit (+0.89)

============================================================
Profile: Deep Intense Rock
============================================================
1. Storm Runner by Voltline
   Score: 9.88 / 10
   Because: genre match (+4.0); mood match (+3.0); energy closeness (+1.98); acousticness fit (+0.90)

2. Gym Hero by Max Pulse
   Score: 5.93 / 10
   Because: mood match (+3.0); energy closeness (+1.98); acousticness fit (+0.95)

3. Pulse Garden by Kaleo Wave
   Score: 2.90 / 10
   Because: energy closeness (+1.94); acousticness fit (+0.96)

4. Iron Tide by Black Anvil
   Score: 2.87 / 10
   Because: energy closeness (+1.90); acousticness fit (+0.97)

5. Sunrise City by Neon Echo
   Score: 2.62 / 10
   Because: energy closeness (+1.80); acousticness fit (+0.82)

============================================================
Profile: Conflicted (edge case)
============================================================
1. Pine Smoke Letters by Willow Marsh
   Score: 5.73 / 10
   Because: genre match (+4.0); energy closeness (+0.80); acousticness fit (+0.93)

2. Storm Runner by Voltline
   Score: 2.08 / 10
   Because: energy closeness (+1.98); acousticness fit (+0.10)

3. Rooftop Lights by Indigo Parade
   Score: 2.07 / 10
   Because: energy closeness (+1.72); acousticness fit (+0.35)

4. Sunrise City by Neon Echo
   Score: 2.02 / 10
   Because: energy closeness (+1.84); acousticness fit (+0.18)

5. Gym Hero by Max Pulse
   Score: 1.99 / 10
   Because: energy closeness (+1.94); acousticness fit (+0.05)

============================================================
Profile: Genre Not in Catalog
============================================================
1. Library Rain by Paper Lanterns
   Score: 5.76 / 10
   Because: mood match (+3.0); energy closeness (+1.90); acousticness fit (+0.86)

2. Spacewalk Thoughts by Orbit Bloom
   Score: 5.68 / 10
   Because: mood match (+3.0); energy closeness (+1.76); acousticness fit (+0.92)

3. Midnight Coding by LoRoom
   Score: 5.67 / 10
   Because: mood match (+3.0); energy closeness (+1.96); acousticness fit (+0.71)

4. Coffee Shop Stories by Slow Stereo
   Score: 2.83 / 10
   Because: energy closeness (+1.94); acousticness fit (+0.89)

5. Focus Flow by LoRoom
   Score: 2.78 / 10
   Because: energy closeness (+2.00); acousticness fit (+0.78)

============================================================
Profile: Capitalized Genre
============================================================
1. Sunrise City by Neon Echo
   Score: 5.76 / 10
   Because: mood match (+3.0); energy closeness (+1.94); acousticness fit (+0.82)

2. Rooftop Lights by Indigo Parade
   Score: 5.47 / 10
   Because: mood match (+3.0); energy closeness (+1.82); acousticness fit (+0.65)

3. Gym Hero by Max Pulse
   Score: 2.79 / 10
   Because: energy closeness (+1.84); acousticness fit (+0.95)

4. Storm Runner by Voltline
   Score: 2.78 / 10
   Because: energy closeness (+1.88); acousticness fit (+0.90)

5. Pulse Garden by Kaleo Wave
   Score: 2.76 / 10
   Because: energy closeness (+1.80); acousticness fit (+0.96)

============================================================
Profile: Extreme Energy
============================================================
1. Winter Hall Etude by Clara Voss
   Score: 7.39 / 10
   Because: genre match (+4.0); mood match (+3.0); energy closeness (+0.36); acousticness fit (+0.03)

2. Pine Smoke Letters by Willow Marsh
   Score: 3.67 / 10
   Because: mood match (+3.0); energy closeness (+0.60); acousticness fit (+0.07)

3. Iron Tide by Black Anvil
   Score: 2.91 / 10
   Because: energy closeness (+1.94); acousticness fit (+0.97)

4. Pulse Garden by Kaleo Wave
   Score: 2.86 / 10
   Because: energy closeness (+1.90); acousticness fit (+0.96)

5. Gym Hero by Max Pulse
   Score: 2.81 / 10
   Because: energy closeness (+1.86); acousticness fit (+0.95)
```

The output above uses the original 4/3/2/1 weights. The weight-shift experiment used temporary weights; its results are summarized above.

---

## 8. Future Work  

Next, I would add tempo, valence, and danceability to the score. I would also test related mood labels and add variety limits so the top results do not overrepresent one artist or genre.

---

## 9. Personal Reflection  

I learned that a recommender turns chosen features and weights into a ranking; it does not know what someone will love. I was surprised that a song can rank first without matching every preference because strong matches in a few heavily weighted features can outweigh mismatches elsewhere. This helped me see why real recommendation apps need to balance many signals and why their recommendations can reflect design choices and catalog gaps.

**AI-use reflection:** AI helped me draft the scoring logic and explanations. I checked the profile key names and import path by running the app, and compared the energy and acousticness points in the output with the recipe. I reviewed the suggestions and adjusted them to fit my project.
