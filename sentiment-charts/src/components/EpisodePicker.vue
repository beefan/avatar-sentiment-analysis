<template lang="pug">
  div#table-o-contents
    h5 View Analysis for:

    h6.heading(@click="showBookOne = !showBookOne") Book One: Water <b-icon-arrow-bar-down v-if="!showBookOne"></b-icon-arrow-bar-down><b-icon-arrow-bar-up v-if="showBookOne"></b-icon-arrow-bar-up>
    div.episode(v-if="showBookOne")
      p(v-for="(ep,i) in bookOne" v-bind:key="i" @click="pickEpisode(ep.title)") {{ ep.title }}

    h6.heading(@click="showBookTwo = !showBookTwo") Book Two: Earth <b-icon-arrow-bar-down v-if="!showBookTwo"></b-icon-arrow-bar-down><b-icon-arrow-bar-up v-if="showBookTwo"></b-icon-arrow-bar-up>
    div.episode(v-if="showBookTwo")
      p(v-for="(ep,i) in bookTwo" v-bind:key="i" @click="pickEpisode(ep.title)") {{ ep.title }}

    h6.heading(@click="showBookThree = !showBookThree") Book Three: Fire <b-icon-arrow-bar-down v-if="!showBookThree"></b-icon-arrow-bar-down><b-icon-arrow-bar-up v-if="showBookThree"></b-icon-arrow-bar-up>
    div.episode(v-if="showBookThree")
      p(v-for="(ep,i) in bookThree" v-bind:key="i" @click="pickEpisode(ep.title)") {{ ep.title }}
</template>

<script>
export default {
  data() {
    return {
      showBookOne: false,
      showBookTwo: false,
      showBookThree: false
    }
  },
  props: {
    episodes: Array
  },
  methods: {
    pickEpisode(title) {
      let index = 0;
      for (let i = 0; i < this.episodes.length; i++) {
        if (this.episodes[i].title == title){
          index = i;
          break;
        }
      }

      this.$emit('update:episodeIndex', index)
    }
  },
  computed: {
    bookOne() {
      // get bookOne episodes while removing the commentary data
      return this.episodes.filter(x => (x.bookTitle.split(" ")[1] == "One:" && x.title.indexOf("commentary") < 0) )
    },
    bookOneSummary(){
      return ''
    },
    bookTwo(){
      return this.episodes.filter(x => (x.bookTitle.split(" ")[1] == "Two:" && x.title.indexOf("end-book") < 0 ) )
    },
    bookTwoSummary(){
      return ''
    },
    bookThree(){
      return this.episodes.filter(x => (x.bookTitle.split(" ")[1] == "Three:" && x.title.indexOf("end-book") < 0 ) )
    },
    bookThreeSummary() {
      return ''
    },
    finalAnalysis(){
      return ''
    }
  }
}
</script>

<style lang="sass">

</style>