<template lang="pug">
  div
    NavBar
    h2 {{ pageTitle }}
    ColorStrip(:chartdata="nrcEmotionData")
    BarChart(:chartdata="emotionFreqData" :options="chartOptions")
    LineChart(:chartdata="vaderScoreData" :options="chartOptions")
</template>

<script>
import NavBar from "@/components/NavBar.vue"
import BarChart from "@/components/BarChart.vue"
import LineChart from "@/components/LineChart.vue" 
import PieChart from "@/components/PieChart.vue" 
import RadarChart from "@/components/RadarChart.vue" 
import ColorStrip from "@/components/ColorStrip.vue"

export default {
  components: {
    NavBar,
    BarChart,
    LineChart,
    PieChart,
    RadarChart,
    ColorStrip
  },
  data() {
    return {
      episodeIndex: 0,
      unfilteredChartData: require("@/assets/avatar-chart-data.json")
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
          return this.episodeIndex + 1;
        case "Two":
          return this.episodeIndex + 1;
        case "Three": 
          return this.episodeIndex + 1;
        default:
          return ""; 
      }
    },
    pageTitle() {
      return `${this.episode.bookTitle}, Episode ${this.episodeNumber}: ${this.episode.title}`
    },
    vaderScoreData() {
      let plot = this.episode.plots[0];
      return  {
          labels: plot.x,
          datasets: [
            {
              label: plot.name,
              borderColor: '#283646',
              borderWidth: 1,
              fill: false,
              data: plot.y
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
              backgroundColor: ['#af0000', '#fe6600', '#8c3c00', '#003200', '#fef8aa', '#dddddd', '#00d5dc', '#282828', '#950083', '#0065fe']
            }
          ],
        }
    },
    chartOptions() {
      return {
        scales: {
          xAxes: [ { ticks: { beginAtZero:true } } ]
        },
        responsive: true,
        maintainAspectRatio: false
      }
    }
  }
}
</script>

<style>

</style>