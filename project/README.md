# 1. Data: [Cornell Movie-Dialogs Corpus](https://convokit.cornell.edu/documentation/movie.html) & [Cinemagoer](https://cinemagoer.readthedocs.io/en/latest/index.html)

[Conell's Page on This](https://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html)

[Cinemagoer](https://cinemagoer.readthedocs.io/en/latest/index.html)

[Our Complied Data for Download](https://uillinoisedu-my.sharepoint.com/:f:/g/personal/mengyue4_illinois_edu/ErWZnueG65RPrwWrxzms3DUBWE5y55pf1IomDARFoBG02w?e=uuMaeg)

A large metadata-rich collection of fictional conversations extracted from raw movie scripts. (220,579 conversational exchanges between 10,292 pairs of movie characters in 617 movies).

Dataset details:
1. Speaker-level information:

speakers in this dataset are movie characters. We take speaker index from the original data release as the speaker name. For each character, the data further provide the following information as speaker-level metadata:

    speaker_id: speaker id

    character_name: name of the character in the movie

    movie_idx: index of the movie this character appears in

    movie_name: title of the movie

    gender: gender of the character (“?” for unlabeled cases)

    credit_pos: position on movie credits (“?” for unlabeled cases, converted to 0)

2. Utterance-level information:

For each utterance, the data provide:

    utterances_id: index of the utterance

    speaker: the speaker id of who authored the utterance

    belonging_id: id of the first utterance in the conversation this utterance belongs to

    reply_to: id of the utterance to which this utterance replies to (None if the utterance is not a reply)

    text: textual content of the utterance

    movie_idx: index of the movie from which this utterance occurs

3. Movie-level information:

Conversations are indexed by the id of the first utterance that make the conversation. For each conversation the data provide:

    movie_idx: index of the movie from which this utterance occurs

    movie_name: title of the movie

    release_year: year of movie release

    rating: IMDB rating of the movie

    votes: number of IMDB votes

    genre: a list of genres this movie belongs to

    Cinemagoer_id: id from Cinemagoer, scraped from IMDB

    multiple_plot: multiple versions of plot introduction from IMDB

# 2. This Part's Goal:

~~1. restrict the year range of our movies to only as early as 2000~~

2. from the scripts (plots) and conversations, try to gain some insights from their <mark>shared similarities</mark> or <mark>differences</mark> on topics and words, obtaining some comprehension on what makes a great movie in terms of the plot

3. we plan to use *Word Frequency Analysis* and *Text Similarity Analysis*. 
   The frequency analysis examines the most frequently used words or phrases to identify common elements in successful movie scripts.
   The similarity analysis measures the similarity between different movie scripts to find patterns or trends.