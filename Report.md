## Comparison of text between the two files to find the average cosine similarity of the top k words:

| Sl no | Pretrained model | Toxic Words | Non-Toxic Words | k | Cosine similarity |
| --- | --- | --- | --- | --- | --- |
| 1. | Glove Twitter 25 | 'fu*k', 'sh*t', 'ni*ger', 'like', 'ass' | 'article', 'page', 'wikipedia', 'talk', 'would' | 5 | 0.5824 |
| 2. | Glove Twitter 25 | 'fu*k', 'sh*t', 'nig**ger', 'like', 'ass**', 'fuck**ing', 'wikipedia', 'u', 'suck', 'gay' | 'article', 'page', 'wikipedia', 'talk', 'would', 'please', 'one', 'like', 'see', 'also' | 10 | 0.6616 |
| 3. | Glove Twitter 25 | 'fu**ck', 'sh**it', 'ni**ger', 'like', 'ass', 'fu**king', 'wikipedia', 'u', 'suck', 'gay', 'go', 'die', 'get', 'hate', 'know', 'page', 'pig', 'cunt', 'bi**ch', 'fat' | 'article', 'page', 'wikipedia', 'talk', 'would', 'please', 'one', 'like', 'see', 'also', 'think', 'edit', 'know', 'use', 'people', 'articles', 'may', 'time', 'thanks', 'could' | 20 | 0.6625 |
| 4. | Glove Twitter 200 | 'fu**k', 'sh**it', 'nigge**r', 'like', 'ass' | 'article', 'page', 'wikipedia', 'talk', 'would' | 5 | 0.4511 |
| 5. | Glove Twitter 200 | 'fu**ck', 's**hit', 'ni**gger', 'like', 'ass', 'fucking', 'wikipedia', 'u', 'suck', 'gay' | 'article', 'page', 'wikipedia', 'talk', 'would', 'please', 'one', 'like', 'see', 'also' | 10 | 0.4974 |
| 6. | Glove Twitter 200 | 'fu**ck', 's**hit', 'nig**ger', 'like', 'ass', 'fucking', 'wikipedia', 'u', 'suck', 'gay', 'go', 'die', 'get', 'hate', 'know', 'page', 'pig', 'cu**nt', 'bit**ch', 'fat' | 'article', 'page', 'wikipedia', 'talk', 'would', 'please', 'one', 'like', 'see', 'also', 'think', 'edit', 'know', 'use', 'people', 'articles', 'may', 'time', 'thanks', 'could' | 20 | 0.4980 |
| 7. | Glove wiki Giga 50 | 'fu**ck', 'sh**it', 'n**igger', 'like', 'ass' | 'article', 'page', 'wikipedia', 'talk', 'would' | 5 | 0.2162 |
| 8. | Glove wiki Giga 50 | 'fuc**k', 'shit', 'nigg**er', 'like', 'ass', 'fuck**ing', 'wikipedia', 'u', 'suck', 'gay' | 'article', 'page', 'wikipedia', 'talk', 'would', 'please', 'one', 'like', 'see', 'also' | 10 | 0.2706 |
| 9. | Glove wiki Giga 50 | 'fu**ck', 'shi**t', 'nig**ger', 'like', 'ass', 'fuc**king', 'wikipedia', 'u', 'suck', 'gay', 'go', 'die', 'get', 'hate', 'know', 'page', 'pig', 'cu**nt', 'bitch', 'fat' | 'article', 'page', 'wikipedia', 'talk', 'would', 'please', 'one', 'like', 'see', 'also', 'think', 'edit', 'know', 'use', 'people', 'articles', 'may', 'time', 'thanks', 'could' | 20 | 0.3363 |
| 10. | Glove wiki Giga 100 | 'fuc**k', 's**hit', 'nig**ger', 'like', 'ass' | 'article', 'page', 'wikipedia', 'talk', 'would' | 5 | 0.1482 |
| 11. | Glove wiki Giga 100 | 'fuc**k', 'sh**it', 'ni**gger', 'like', 'ass', 'fuc**king', 'wikipedia', 'u', 'suck', 'gay' | 'article', 'page', 'wikipedia', 'talk', 'would', 'please', 'one', 'like', 'see', 'also' | 10 | 0.2155 |
| 12. | Glove wiki Giga 100 | 'fu**ck', 'sh**it', 'nig**ger', 'like', 'ass', 'fucki**ng', 'wikipedia', 'u', 'suck', 'gay', 'go', 'die', 'get', 'hate', 'know', 'page', 'pig', 'cu**nt', 'bitc**h', 'fat' | 'article', 'page', 'wikipedia', 'talk', 'would', 'please', 'one', 'like', 'see', 'also', 'think', 'edit', 'know', 'use', 'people', 'articles', 'may', 'time', 'thanks', 'could' | 20 | 0.2809 |


# Word Vector Pre-trained Models Analysis

## Analysis

- I first chose the Twitter pre-trained models to find the similarity between the k pre-trained words. But then I found out that the Twitter pre-trained models were not performing too well.
- As you can see from the above tables, the Twitter pre-trained models give a high similarity score between the toxic and non-toxic words.
- Therefore, I checked the Kaggle link for the source of the dataset.
- I found that the description said that the Kaggle dataset contained Wikipedia comments which have been labeled by human raters for toxic behavior.
- Therefore, I used the Wiki Giga pre-trained models to check if I would obtain a better score.
- The Wiki Giga pre-trained models gave a better result with a low similarity score between the toxic and non-toxic datasets.
- From the above observations, it can be seen that the score increases slightly from the top 5 to the top 20. This is probably because the top 5 toxic words have higher toxicity compared to the words which come after the top 5 words. Therefore, they are less similar.
- The pre-trained models are able to pick this up in all cases and increase the score gradually from the top 5 to the top 20.
- It can also be observed that as the dimensions of the pre-trained models increase, they give a smaller score for the similarity between the toxic and non-toxic words. This is true both in the case of the Twitter pre-trained model and the Wiki Giga pre-trained model. It is probably because the higher-dimension pre-trained models are able to capture finer semantic information.

Below are the observations for the top k frequent words and their similar words. You can skip to the analysis and come back here for reference.

### glove-twitter-25:

**world_of_war.txt:**
We found the top 5 frequent words and their 5 similar words:

| Sl no | Word      | Similar Words                    |
|-------|-----------|---------------------------------|
| 1.    | one       | 'all', 'only', 'there', 'every', 'have'   |
| 2.    | upon      | 'within', 'lives', 'through', 'presence', 'faith' |
| 3.    | said      | 'told', 'she', 'did', 'asked', 'knew' |
| 4.    | martians  | 'wombats', 'hares', 'maccabees', 'pattycake', 'fratellis' |
| 5.    | people    | 'other', 'those', 'ones', 'especially', 'reason' |

**on_liberty.txt:**
We found the top 5 frequent words and their 5 similar words:

| Sl no | Word      | Similar Words                            |
|-------|-----------|-----------------------------------------|
| 1.    | one       | 'all', 'only', 'there', 'every', 'have' |
| 2.    | may       | 'promise', 'least', 'close', 'cannot', 'which' |
| 3.    | opinion   | 'compare', 'difference', 'honest', 'answers', 'sense' |
| 4.    | would     | 'could', 'should', 'have', "n't", 'does' |
| 5.    | society   | 'influence', 'based', 'culture', 'freedom', 'education' |

**kingarthur.txt:**
We found the top 5 frequent words and their 10 similar words:

| Sl no | Word   | Similar Words                                             |
|-------|--------|----------------------------------------------------------|
| 1.    | sir    | 'mark', 'ryan', 'mrs', 'ms.', 'phil', 'tom', 'brad', 'mr', 'sarah', 'boss' |
| 2.    | king   | 'prince', 'queen', 'aka', 'lady', 'jack', "'s", 'stone', 'mr.', 'the', 'star' |
| 3.    | said   | 'told', 'she', 'did', 'asked', 'knew', 'called', 'saying', 'thought', 'knows', 'thinks' |
| 4.    | knight | 'bowie', 'dawn', 'stone', 'gatsby', 'castle', 'spider-man', 'wolf', 'maiden', 'sherlock', 'king' |
| 5.    | though | 'chil', 'shall', 'bcuz', 'enuff', 'wud', 'thee', 'therefore', 'becuz', 'treat', 'neither' |

### glove-twitter-200:

**world_of_war.txt:**
We found the top 5 frequent words and their 5 similar words:

| Sl no | Word   | Similar Words                         |
|-------|--------|--------------------------------------|
| 1.    | one    | 'thousand', 'the', 'another', 'two'  |
| 2.    | upon   | 'universe', 'before', 'toward', 'once', 'lord' |
| 3.    | said   | 'told', 'did', 'asked', 'saying', 'thought' |
| 4.    | martians | 'goblins', 'cults', 'minotaur', 'sleepwalk', 'lemurs' |
| 5.    | people   | 'ppl', 'other', 'when', 'they', "n't" |

**on_liberty.txt:**
We found the top 5 frequent words and their 5 similar words:

| Sl no | Word   | Similar Words                        |
|-------|--------|-------------------------------------|
| 1.    | one    | 'thousand', 'the', 'another', 'two' |
| 2.    | may    | 'might', 'will', 'yun', 'could', 'sure' |
| 3.    | opinion | 'opinions', 'disagree', 'honest', 'agree', 'decision' |
| 4.    | would  | 'could', 'should', "'d", 'did', 'think' |
| 5.    | society | 'culture', 'politics', 'humanity', 'community', 'education' |

**kingarthur.txt:**
We found the top 5 frequent words and their 10 similar words:

| Sl no | Word   | Similar Words                                   |
|-------|--------|------------------------------------------------|
| 1.    | sir    | 'madam', 'boss', "ma'am", 'mr', 'mr.', 'ferguson', 'john', 'sure', 'david', 'well' |
| 2.    | king   | 'prince', 'queen', 'aka', 'kings', 'burger', 'the', "'s", 'legend', 'john', 'jack' |
| 3.    | said   | 'told', 'did', 'asked', 'saying', 'thought', 'she', 'says', 'say', 'knew', 'think' |
| 4.    | knight | 'rises', 'batman', 'tdkr', 'dark', 'avengers', 'dawn', 'joker', 'ghost', 'nolan', 'bane' |
| 5.    | though | ‘shall', 'thy', 'shalt', 'though', 'tho', 'fool', 'thoo', 'thoe', 'foreal', 'forreal' |

### glove-wiki-gigaword-50:

**world_of_war.txt:**
We found the top 5 frequent words and their 5 similar words:

| Sl no | Word   | Similar Words                   |
|-------|--------|--------------------------------|
| 1.    | one    | 'another', 'only', 'same', '.', 'but' |
| 2.    | upon   | 'latter', 'thus', 'given', 'taken', 'however' |
| 3.    | said   | 'told', 'says', 'spokesman', 'saying', 'asked' |
| 4.    | martians | 'skrulls', 'extraterrestrials', 'orcs', 'colonize', 'philistines' |
| 5.    | people   | 'others', 'least', 'some', 'those', 'there' |

**on_liberty.txt:**
We found the top 5 frequent words and their 5 similar words:

| Sl no | Word   | Similar Words                   |
|-------|--------|--------------------------------|
| 1.    | one    | 'another', 'only', 'same', '.', 'but' |
| 2.    | may    | 'however', '.', 'to', 'likely', 'although' |
| 3.    | opinion | 'opinions', 'nonetheless', 'contrary', 'poll', 'argued' |
| 4.    | would  | 'could', 'should', 'not', 'will', 'if' |
| 5.    | society | 'societies', 'institution', 'culture', 'social', 'established' |

**kingarthur.txt:**
We found the top 5 frequent words and their 10 similar words:

| Sl no | Word   | Similar Words                                      |
|-------|--------|---------------------------------------------------|
| 1.    | sir    | 'edward', 'henry', 'hugh', 'william', 'charles', 'arthur', 'francis', 'james', 'john', 'george' |
| 2.    | king   | 'prince', 'queen', 'ii', 'emperor', 'son', 'uncle', 'kingdom', 'throne', 'brother', 'ruler' |
| 3.    | said   | 'told', 'says', 'saying', 'added', 'asked', 'spokesman', ',', 'that', 'adding', 'but' |
| 4.    | knight | 'knights', 'parker', 'hunter', 'chevalier', 'noble', 'star', 'dragon', 'johnson', 'henry', 'named' |
| 5.    | though | 'shalt', 'unto', 'thee', 'didst', 'thy', 'hast', 'wherefore', 'holier', 'xfx', 'al-shafi' |

### glove-wiki-gigaword-100:

**world_of_war.txt:**
We found the top 5 frequent words and their 5 similar words:

| Sl no | Word   | Similar Words                       |
|-------|--------|------------------------------------|
| 1.    | one    | 'only', 'another', 'this', 'same', 'two' |
| 2.    | upon   | 'same', 'thus', 'given', 'before', 'rather' |
| 3.    | said   | 'told', 'says', 'saying', 'added', 'asked' |
| 4.    | martians | 'extraterrestrials', 'cylons', 'skrulls', 'orcs', 'terrans' |
| 5.    | people   | 'others', 'those', 'many', 'some', 'they' |

**on_liberty.txt:**
We found the top 5 frequent words and their 5 similar words:

| Sl no | Word   | Similar Words                      |
|-------|--------|-----------------------------------|
| 1.    | one    | 'only', 'another', 'this', 'same', 'two' |
| 2.    | may    | 'could', 'likely', 'might', 'would', 'not' |
| 3.    | opinion | 'opinions', 'poll', 'polls', 'conservative', 'voters' |
| 4.    | would  | 'could', 'will', 'not', 'should', 'be' |
| 5.    | society | 'societies', 'institution', 'community', 'culture', 'institute' |

**kingarthur.txt:**
We found the top 5 frequent words and their 10 similar words:

| Sl no | Word   | Similar Words                                  |
|-------|--------|-----------------------------------------------|
| 1.    | sir    | 'william', 'edward', 'henry', 'hugh', 'charles', 'lord', 'arthur', 'francis', 'john', 'george' |
| 2.    | king   | 'prince', 'queen', 'son', 'brother', 'monarch', 'throne', 'kingdom', 'father', 'emperor', 'ii' |
| 3.    | said   | 'told', 'says', 'saying', 'added', 'asked', 'spokesman', ',', 'that', 'adding', 'but' |
| 4.    | knight | 'knights', 'parker', 'hunter', 'chevalier', 'noble', 'star', 'dragon', 'johnson', 'henry', 'named' |
| 5.    | though | 'shalt', 'didst', 'thy', 'hast', 'thee', 'wherefore', 'ye', 'commandment', 'unto', 'canst' |

I have scored each of the pre-trained word vectors models for similar words. The score is just based on my personal preference, and I have listed my analysis below.

| Text File | Glove-Twitter-25 | Glove-Twitter-200 | Glove-Wiki-Gigaword-50 | Glove-Wiki-Gigaword-100 |
|-----------|-------------------|-------------------|------------------------|-------------------------|
| world_of_war.txt (Martian)   | 3   | 4   | 4   | 4.5 |
| on_liberty.txt (Society)    | 3   | 3.5 | 4.5 | 5   |
| kingarthur.txt (Knight)     | 3   | 4   | 3.5 | 4.5 |

Above, Glove-Wiki-Gigaword-100 gave the best similar words, with Glove-Wiki-Gigaword-100 giving the best results. I also found Glove-Twitter-200 to perform better than Glove-Twitter-25.

I have taken a couple of examples for comparison below. The word "Society" is from on_liberty.txt, "Knight" is from kingarthur.txt, and "Martians" is from world_of_war.txt. The below examples have the top k most common words for the selected example words from the three text files.

#### Examples for Comparison:

**Glove-Twitter-25:**
- Society: ['influence', 'based', 'culture', 'freedom', 'education']
- Knight: ['bowie', 'dawn', 'stone', 'gatsby', 'castle', 'spider-man', 'wolf', 'maiden', 'sherlock', 'king']
- Martians: ['wombats', 'hares', 'maccabees', 'pattycake', 'fratellis']

**Glove-Twitter-200:**
- Society: ['culture', 'politics', 'humanity', 'community', 'education']
- Martians: ['goblins', 'cults', 'minotaur', 'sleepwalk', 'lemurs']
- Knight: ['rises', 'batman', 'tdkr', 'dark', 'avengers', 'dawn', 'joker', 'ghost', 'nolan', 'bane']

**Glove-Wiki-Gigaword-50:**
- Society: ['societies', 'institution', 'culture', 'social', 'established']
- Martians: ['skrulls', 'extraterrestrials', 'orcs', 'colonize', 'philistines']
- Knight: ['james', 'parker', 'smith', 'john', 'captain', 'burke', 'knights', 'william', 'walker', 'henry']

**Glove-Wiki-Gigaword-100:**
- Society: ['societies', 'institution', 'community', 'culture', 'institute']
- Martians: ['extraterrestrials', 'cylons', 'skrulls', 'orcs', 'terrans']
- Knight: ['knights', 'parker', 'hunter', 'chevalier', 'noble', 'star', 'dragon', 'johnson', 'henry', 'named']

# Observations and Analysis

## Observations and Analysis using the above examples:

- Considering the example word "Society" (from the most frequent list) from on_liberty.txt, Glove-Wiki-Gigaword-100 has the best similar words. The other sets have one or two words that are not very related to society. For example, Glove-Wiki-Gigaword-50 has the word "established," which is not very related to the word society in my perspective.

- Next, considering the example word "Martians" for the world_of_war.txt file, I have rated Glove-Twitter-25 the least since it had the word "hares," which is not related to Martians. The other sets had mythical creatures and 'extraterrestrials,' which made me give them a higher score. I found the other sets to have more similar words to Martians.

- Lastly, considering the word "Knight" for kingarthur.txt, Glove-Twitter-200 had more references to the movie Batman. 'Rises,' 'Batman,' 'TDKR,' 'Dark,' 'Avengers,' 'Dawn,' 'Joker,' 'Ghost,' 'Nolan,' 'Bane.' I found this observation to be interesting. Dark Knight Rises, Joker the villain, Christopher Nolan the filmmaker of Batman are some interesting examples of why the pre-trained model might have picked up these words. Although Batman is one of my favorite superheroes, I did not give it a perfect score since the similar words were not very diverse and were more tilted toward the movie Batman. However, I found Glove-Wiki-Gigaword-100 to have the best similar words, which were also diverse in context.

