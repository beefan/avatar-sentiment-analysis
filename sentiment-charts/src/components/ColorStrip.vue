<template lang="pug">
div#color-strip-wrapper
  p.chart-name {{ chartdata.name }}
  div#color-strip
    div.strip(v-for="(emotion,index) in chartdata.y" v-bind:key="index" :id="`strip${index}`" :style="{ backgroundColor: colorMap[emotion], width: width}")
      b-tooltip(:target="`strip${index}`" triggers="hover") {{ emotion }}
</template>

<script>
export default {
  data() {
    return {
      colorMap: {}
    }
  },
  props: {
    chartdata: Object,
    options: Array
  },
  computed: {
    width() {
      return "1%"; //`${Math.round(100 / (this.chartdata.y.length + 2))}%`;
    },
    style(emotion) {
      return `backgroundColor: '${this.colorMap[emotion]}'`;
    }
  },
  created() {
    console.log(this.chartdata)
  this.colorMap = {
        anger: this.options[0],
        anticipation: this.options[1],
        disgust: this.options[2],
        fear: this.options[3],
        joy: this.options[4],
        negative: this.options[5],
        positive: this.options[6],
        sadness: this.options[7],
        surprise: this.options[8],
        trust: this.options[9],
        none: "#fff"
      }
  }
}
</script>

<style lang="sass">
#color-strip
  width: 100%
  display: flex
  flex-flow: row
  flex-wrap: nowrap
  justify-content: stretch
  height: 350px
  border: 1px solid #6c6c6c
.chart-name
  font-size: .8rem
  color: #6c6c6c
#color-strip-wrapper
  margin: 1%
.strip:hover 
  border: 1px solid grey
</style>