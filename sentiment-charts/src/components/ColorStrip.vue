<template lang="pug">
div#color-strip-wrapper
  p.chart-name {{ chartdata.name }}
  div#color-strip
    div(v-for="(emotion,index) in chartdata.y" v-bind:key="index" :id="`strip${index}`" :style="{ backgroundColor: colorMap[emotion], width: width}")
      b-tooltip(:target="`strip${index}`" triggers="hover") {{ emotion }}
</template>

<script>
export default {
  data() {
    return {
      colorMap: {
        anger: '#af0000',
        anticipation: '#fe6600',
        disgust: '#8c3c00',
        fear: '#003200',
        joy: '#fef8aa',
        negative: '#dddddd',
        positive: '#00d5dc',
        sadness: '#282828',
        surprise: '#950083',
        trust: '#0065fe',
        none: '#f8f8f8'
      }
    }
  },
  props: {
    chartdata: Object
  },
  computed: {
    width() {
      return `${Math.round(100 / (this.chartdata.y.length + 2))}%`;
    },
    style(emotion) {
      return `backgroundColor: '${this.colorMap[emotion]}'`;
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
</style>