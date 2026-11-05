# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeMatch: Content-Based Music Recommender**

---

## 2. Intended Use  

VibeMatch recommends songs from a small catalog by comparing song attributes with a listener's stated preferences for genre, mood, energy, and acoustic sound. It assumes these preferences are a useful description of what the listener wants.

---

## 3. How the Model Works  

### Algorithm Summary

A song earns 4 points for matching the user's favorite genre and 3 points for matching their favorite mood. It can earn up to 2 points for having energy close to the user's target and up to 1 point for matching their acousticness preference. The points are added into a score out of 10, and songs are ranked from highest score to lowest. The recommender returns the top-ranked songs with brief reasons for their scores.

It uses genre, mood, energy, and acousticness, along with matching preferences in the user profile. This replaces the starter placeholder logic with a weighted score for each song and a ranked top-five list with explanations.

---

## 4. Data  

The catalog contains 18 example songs, covering 15 genres and 12 mood labels. It includes numeric audio attributes such as energy, tempo, valence, danceability, and acousticness; the recommender currently scores only energy and acousticness from these. The catalog was expanded from the starter data, but it is small and does not represent every genre, mood, artist, culture, or style of music. It also has no real listener history, lyrics, or user feedback.

---

## 5. Strengths  

The system gives intuitive results when a profile's genre and mood match songs in the catalog. For example, the Deep Intense Rock profile puts “Storm Runner” first, while Chill Lofi puts “Library Rain” first. The explanations make it easy to see which preferences contributed to a result.

---

## 6. Limitations and Bias 

The catalog is tiny and uneven: lofi has three songs, while most genres have only one, so some tastes have fewer choices. Genre and mood together contribute 7 of 10 possible points, so a song with matching labels can rank well even when its energy is far from the user's target. Exact label matching misses related moods such as “sad” and “melancholy.” The model also ignores tempo, valence, danceability, lyrics, context, and listening behavior.

---

## 7. Evaluation  

I ran the recommender for High-Energy Pop, Chill Lofi, Deep Intense Rock, and Conflicted (folk, sad, high-energy, acoustic) profiles. I checked whether the top songs reflected the profile and inspected the score explanations. The first three profiles received intuitive matches. In the conflicted case, “Pine Smoke Letters” ranked first because it matched folk and acoustic preferences, despite missing the requested mood and energy; that illustrates how a strong genre match can outweigh other mismatches. I also compared the displayed scores and ranks across profiles.

---

## 8. Future Work  

I would experiment with reducing the genre weight and increasing the energy weight, then compare how the rankings change. I could also use tempo, valence, and danceability, add related-label matching, and limit repeated artists or genres in the top results. More varied listener profiles and a larger catalog would make evaluation more informative.

---

## 9. Personal Reflection  

I learned that a recommender turns chosen features and weights into a ranking; it does not know what someone will love. I was surprised that a song can rank first without matching every preference because strong matches in a few heavily weighted features can outweigh mismatches elsewhere. This helped me see why real recommendation apps need to balance many signals and why their recommendations can reflect design choices and catalog gaps.
