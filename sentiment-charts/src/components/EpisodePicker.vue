<template lang="pug">
  div#table-o-contents
    h6.heading(@click="showBookOne = !showBookOne") Book One: Water <b-icon-arrow-bar-down v-if="!showBookOne"></b-icon-arrow-bar-down><b-icon-arrow-bar-up v-if="showBookOne"></b-icon-arrow-bar-up>
    div.episode(v-if="showBookOne")
      p(v-for="(ep,i) in bookOne" v-bind:key="i" @click="pickEpisode(ep.title)" :class="{active: ep.title === selectedTitle}") {{ ep.title }}

    h6.heading(@click="showBookTwo = !showBookTwo") Book Two: Earth <b-icon-arrow-bar-down v-if="!showBookTwo"></b-icon-arrow-bar-down><b-icon-arrow-bar-up v-if="showBookTwo"></b-icon-arrow-bar-up>
    div.episode(v-if="showBookTwo")
      p(v-for="(ep,i) in bookTwo" v-bind:key="i" @click="pickEpisode(ep.title)" :class="{active: ep.title === selectedTitle}") {{ ep.title }}

    h6.heading(@click="showBookThree = !showBookThree") Book Three: Fire <b-icon-arrow-bar-down v-if="!showBookThree"></b-icon-arrow-bar-down><b-icon-arrow-bar-up v-if="showBookThree"></b-icon-arrow-bar-up>
    div.episode(v-if="showBookThree")
      p(v-for="(ep,i) in bookThree" v-bind:key="i" @click="pickEpisode(ep.title)" :class="{active: ep.title === selectedTitle}") {{ ep.title }}
</template>

<script>
export default {
  data() {
    return {
      showBookOne: false,
      showBookTwo: false,
      showBookThree: false,
      selectedTitle: 'The Boy in the Iceberg'
    }
  },
  props: {
    episodes: Array
  },
  methods: {
    pickEpisode(title) {
      this.selectedTitle = title;
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
    bookTwo(){
      return this.episodes.filter(x => (x.bookTitle.split(" ")[1] == "Two:" && x.title.indexOf("end-book") < 0 ) )
    },
    bookThree(){
      return this.episodes.filter(x => (x.bookTitle.split(" ")[1] == "Three:" && x.title.indexOf("end-book") < 0 ) )
    }
  }
}
</script>

<style lang="sass">
#table-o-contents
  .heading
    font-size: 1.2rem
    text-decoration: underline
  .heading:hover
    opacity: 70%
  .active
    font-weight: bold
  .episode p:hover
    color: #41b883
</style>