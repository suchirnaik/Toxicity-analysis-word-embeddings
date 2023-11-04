
| Sl no | Pretrained Model    | Toxic Words | Non-Toxic Words | k  | Cosine Similarity |
|-------|---------------------|-------------|-----------------|----|-------------------|
| 1     | Glove Twitter 25   | 'fuck', 'shit', 'nigger', 'like', 'ass'19)
          |'article', 'page', 'wikipedia', 'talk', 'would'
              | 5  | 0.5824            |
| 2     | Glove Twitter 25   | 'fuck', 'shit', 'nigger', 'like', 'ass', 'fucking', 'wikipedia', 'u', 'suck', 'gay'
           | 'article', 'page', 'wikipedia', 'talk', 'would', 'please', 'one', 'like', 'see', 'also'


               | 10 | 0.6616            |
| 3     | Glove Twitter 25   | 'fuck', 'shit', 'nigger', 'like', 'ass', 'fucking', 'wikipedia', 'u', 'suck', 'gay', 'go', 'die', 'get', 'hate', 'know', 'page', 'pig', 'cunt', 'bitch', 'fat'
           | 'article', 'page', 'wikipedia', 'talk', 'would', 'please', 'one', 'like', 'see', 'also', 'think', 'edit', 'know', 'use', 'people', 'articles', 'may', 'time', 'thanks', 'could'

              | 20 | 0.6625            |
| 4     | Glove Twitter 200  | 5           | 5               | 5  | 0.4511            |
| 5     | Glove Twitter 200  | 5           | 5               | 10 | 0.4974            |
| 6     | Glove Twitter 200  | 5           | 5               | 20 | 0.4980            |
| 7     | Glove Wiki Giga 50 | 5           | 5               | 5  | 0.2162            |
| 8     | Glove Wiki Giga 50 | 5           | 5               | 10 | 0.2706            |
| 9     | Glove Wiki Giga 50 | 5           | 5               | 20 | 0.3363            |
| 10    | Glove Wiki Giga 100| 5           | 5               | 5  | 0.1482            |
| 11    | Glove Wiki Giga 100| 5           | 5               | 10 | 0.2155            |
| 12    | Glove Wiki Giga 100| 5           | 5               | 20 | 0.2809            |
