<template lang="pug">
  div
    NavBar
    b-row
      b-col(sm="10")
        h2 {{ pageTitle }}
        ColorStrip(:chartdata="nrcEmotionData" :options="bgColors")
        BarChart(:chartdata="emotionFreqData" :options="chartOptions.emotionFreq")
        LineChart(:chartdata="vaderScoreData" :options="chartOptions.vaderScores")
        RadarChart(:chartdata="characterRadarData" :options="chartOptions.charRadar")
      b-col(sm="2") 
        EpisodePicker(:episodes="unfilteredChartData.pages"  v-on:update:episodeIndex="episodeIndex = $event")
</template>

<script>
import NavBar from "@/components/NavBar.vue"
import BarChart from "@/components/BarChart.vue"
import LineChart from "@/components/LineChart.vue" 
import PieChart from "@/components/PieChart.vue" 
import RadarChart from "@/components/RadarChart.vue" 
import ColorStrip from "@/components/ColorStrip.vue"
import EpisodePicker from "@/components/EpisodePicker.vue"

export default {
  components: {
    NavBar,
    BarChart,
    LineChart,
    PieChart,
    RadarChart,
    ColorStrip,
    EpisodePicker
  },
  data() {
    return {
      episodeIndex: 0,
      unfilteredChartData: require("@/assets/avatar-chart-data.json"),
      bgColors: ['rgb(255, 173, 173, 0.5)', 
                 'rgb(255, 214, 165, 0.5)', 
                 'rgb(253, 255, 182, 0.5)', 
                 'rgb(202, 255, 191, 0.5)', 
                 'rgb(155, 246, 255, 0.5)', 
                 'rgb(141, 153, 174, 0.5)',
                 'rgb(237, 242, 244, 0.5)',
                 'rgb(160, 196, 255, 0.5)', 
                 'rgb(189, 178, 255, 0.5)', 
                 'rgb(255, 198, 255, 0.5)'],
      lineColors: ['rgb(255, 173, 173)', 
                 'rgb(255, 214, 165)', 
                 'rgb(253, 255, 182)', 
                 'rgb(202, 255, 191)', 
                 'rgb(155, 246, 255)', 
                 'rgb(141, 153, 174)',
                 'rgb(237, 242, 244)',
                 'rgb(160, 196, 255)', 
                 'rgb(189, 178, 255)', 
                 'rgb(255, 198, 255)'],
      chartOptions: {
        emotionFreq: { 
          scales: { xAxes: [{ ticks: { beginAtZero:true } } ] },
          responsive: true,
          maintainAspectRatio: false },
        vaderScores: { 
          scales: { xAxes: [ { ticks: { beginAtZero:true } } ] },
          responsive: true,
          maintainAspectRatio: false },
        charRadar: { 
          title: { text: 'Character NRC Emotion Totals', display: true},
          responsive: true,
          maintainAspectRatio: false }
      }
    }
  },
  methods: {
    removeNeutrals(xData, yData) {
      xData = xData.filter( (v, i) => { 
        if (yData[i] !== 0) {
          return true;
        } 
        });
      yData = yData.filter( x => x != 0)
      return {x: xData, y: yData}
    }
  },
  computed: {
    episode() {
      return this.unfilteredChartData.pages[this.episodeIndex];
    },
    episodeNumber() {
      let book = this.episode.bookTitle.split(" ")[1];
      switch (book.substring(0, book.length - 1)) {
        case "One":
          if (this.episodeIndex > 19) {
            return this.episodeIndex - 1;
          } else if (this.episodeIndex > 17) {
            return this.episodeIndex;
          }
          return this.episodeIndex + 1;
        case "Two":
          return this.episodeIndex - 22;
        case "Three": 
          return this.episodeIndex - 44;
        default:
          return ""; 
      }
    },
    pageTitle() {
      return `${this.episode.bookTitle}, Episode ${this.episodeNumber}: ${this.episode.title}`
    },
    vaderScoreData() {
      let plot = this.episode.plots[0];
      let normalizedPlot = this.removeNeutrals(plot.x, plot.y)
      return  {
          labels: normalizedPlot.x,
          datasets: [
            {
              label: plot.name,
              borderColor: '#283646',
              borderWidth: 1,
              fill: false,
              data: normalizedPlot.y
            }
          ]
        }
    },
    nrcEmotionData() {
      let plot = this.episode.plots[1];
      return plot;
    },
    emotionFreqData() {
      let plot = this.episode.plots[2];
      return  {
          labels: plot.x,
          datasets: [
            {
              label: plot.name,
              data: plot.y,
              fill: 'false',
              borderWidth: 2,
              backgroundColor: this.bgColors,
              borderColor: this.lineColors
            }
          ],
        }
    },
    characterRadarData() {
      const characterData = this.characterEmotionTotals;
      let dataSets = [];
      if (characterData.length < 1) { return { title: 'NRC Emotion Data', labels: ['missing', 'data'], datasets: [{ label: 'none', data: ['missing', 'data'] }]} }
      characterData.forEach( (plot, index) => {
          dataSets.push(  {
              label: plot.name.split(" ")[0],
              data: plot.y,
              borderWidth: 1,
              backgroundColor: this.bgColors[5-index],
              borderColor: this.lineColors[5-index]
            } );
      });

      return  {
          title: 'NRC Emotion Data',
          labels: characterData[0].x,
          datasets: dataSets,
        }
    },
    characterEmotionTotals() {
      // filter to get the character plots with NRC Emotion Totals in the title
      const characterData = this.episode.plots.slice(3).filter( val => val.name.indexOf('NRC Emotion Totals') > 0);
      // sort characters by number of lines
      const sum = (arr) => arr.reduce( (acc, curr) => acc + curr);
      characterData.sort( (a, b) => sum(a.y) < sum(b.y))

      // only get the top 6 characters
      if (characterData.length > 5){
        return characterData.slice(0, 5);
      }

      return characterData;
    }
  }
}
</script>

<style>

</style>