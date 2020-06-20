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
    * emotional arc of episode (vader scores and NRC lexicon lookup)
    * emotional frequency of episode
    * emotions of speaking characters
* Part 4:
  * Vue.js/Chart.js/Boostrap-vue on the frontend
    * Custom ColorStrip chart to show emotion line by line using color representation. 
    * Chart Js Bar chart to show frequency of emotion per episode
    * Chart Js Line graph to plot Vader scores (positivity/negativity) by line
    * Chart Js Radar chart to show emotion frequency by top 6 characters
    * Episode picker with reactiviy in charts to show chosen episode.