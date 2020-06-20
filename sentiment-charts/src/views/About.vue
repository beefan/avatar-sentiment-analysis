
<template lang="pug">
  div
    NavBar
    br
    h4 About the Avatar Sentiment Analysis Project
    div.cast
      img(src="@/assets/aang.jpeg")
      img(src="@/assets/iroh.png")
      img(src="@/assets/katara.jpeg")
      img(src="@/assets/sokka.jpeg")
      img(src="@/assets/zuko.png")
      img(src="@/assets/toph.jpeg")
    div.about-text
      h6 Inspiration
      p {{ inspiration }}
      p {{ inspiration2 }}
      h6 Technologies
      p To get the data:
        ul 
          li Python 
          li BeautifulSoup
          li NLTK
          li VaderSentiment
          li NRC Emotion Lexicon
      p To display the data: 
        ul 
          li Javascript
          li ChartJS
          li Vue.js 
          li Bootstrap 
      p {{ technologies2 }}
      h6 Process
      ul 
        li Start with the fandom wiki and look at the html code for the transcripts page to see which elements to target with code.
        li Use the BeautifulSoup library to parse through the DOM and extract the transcripts for each episode.
        li Use raw python, NLTK to clean up the transcript data and create a JSON file with an array of all the data by episode.
        li Use VaderSentiment and the NRC Emotion Lexicon to classify each line with an emotion and vader score. Export JSON files with that data.
        li Use raw python to compile plot data for each episode in a format that will be easy to parse in javascript and feed to chartJS.
        li Create a Vue.js frontend. Create chart components. 
        li Import the Json chart data compiled in Python and feed proper data to chart components. 
        li Create episode picker and reactivity which updates charts when a new episode is picked. 
        li Use bootstrap and css to make the frontend look decent and easily navigable. 
      h6 Notes/Reflection
      p {{ reflection }}
      p {{ reflection2 }}
      p {{ reflection3 }}
      p {{ reflection4 }}
      h6 Check out <a href="https://github.com/beefan/avatar-sentiment-analysis">the code</a> on Github.
</template>
<script>
import NavBar from "@/components/NavBar.vue"

export default {
  components: {
    NavBar
  },
  data() {
    return {
      inspiration: `Text processing and analysis using computers is becoming more and more common. 
                    Pretty much every modern tech company is using computer programming to analyze
                    text data. Using modern Natural Language Processing (NLP) libraries, text data
                    can help us determine the emotion behind the text, the meaning of the text, or 
                    find general patterns across large quantities of text.`,
      inspiration2: `Having not done much NLP, I was curious about what the process would look like.
                    I've been watching a lot of Avatar lately and seeing as it just came out on US
                    Netflix, I thought it was a great target of this kind of text anaylsis. I wanted
                    specifically to delve into the world of sentiment analysis and see if I could 
                    point to emotional patterns in the "Avatar: The Last Airbender" series.`,
    reflection: `One thing that is immediately evident when browsing the charts is that some episodes
                 do not have character data. As this data was generated auto-magically, it is possible
                 that there was an error in the extraction code. However, I think it is more likely that
                 the emotion extraction algorithms have failed. I determine emotion by looking up characters
                 words in the NRC emotion lexicon. This is one of the dumbest emotion detection algorithms
                 someone could implement and so it would make sense if it did not create robust results.`,
    reflection2: `Another note is that I removed all neutral data points from the vader score data. The Vader scores
                  are a simple positivity measure with 1 being most positive and -1 most negative. The
                  line graph representing Vader Scores had a lot of neutral data. Once again, is this really neutral
                  or just improperly detected by the algorithm? Remove neutral data makes the line graph much smoother
                  and I hope easier to witness trends.`,
    reflection3: `This was a really fun project and a great introduction to natural language processing and sentiment
                  analysis. The quality of this analysis is yet to be determined, but I hope to spend some time looking
                  through the charts and watching episodes to get a sense of the data quality. At that point, I may add
                  my reflections to this blog. That's the real value in sentiment analysis anyway, right? It's not enough
                  to build the charts. What do the charts tell us about trends in the data? Avatar is a cult classic. What
                  do these specific trends tell us about the character and plot composition in show that has capitivated
                  the imagination of the entire world? `,
    reflection4: `Though I didn't no perform this analysis for Nickolodeon, I wouldn't be surprised if Nickolodeon was
                  performing similar analysis internally. Not only could it help to identify a "formula" of a successful
                  show, but attributes of a great writer and insight into how such attributes might be promoted.`
    }
  }
}
</script>

<style lang="sass">
.cast
  display: flex
  flex-flow: row
  margin: 3%
  img
    border-radius: 3px
.about-text
  p, li
    margin-left: 8%
    margin-right: 8%
    text-align: left
  h6
    font-weight: bold
    text-decoration: underline
</style>