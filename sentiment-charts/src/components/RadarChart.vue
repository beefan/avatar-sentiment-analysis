<script>
import { Radar } from "vue-chartjs";

export default {
  extends: Radar,
  props: ["chartdata", "options"],
  mounted() {
    this.renderChart(this.chartdata, this.options);
  },
  watch: {
    chartdata () {
      this.renderChart(this.chartdata, this.options)
    }
  }
};
</script>

<style></style>
