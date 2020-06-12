# Avatar Sentiment Analysis

## The Project
Perform programmatic sentiment analysis of entire *Avatar: The Last Airbender* series. Create a blog with graphs and charts showing emotional arcs, character arcs, etc. derived from some natural language processing in python.

## The Approach
* Use **jupyter** to show story and process of code creation
* Part 1: **python** and **beautiful soup** to scrape the fan wiki for all the transcript data.
* Part 2: 
  * **nltk** and **vader sentiment** to derive vader scores for every line of every episode. Emotional lexicon lookup using 
  * **[NRC data](http://sentiment.nrc.ca/lexicons-for-research/)** to associte emotion with every line in every episode. 
* Part 3:
  * generation of analysis (using charts) for each episode including:
    * characters speaking in each episode and total words each.
    * emotional arc of episode
    * emotional arc of top 3 or 4 speaking characters
    * emotional arc of "narration" details