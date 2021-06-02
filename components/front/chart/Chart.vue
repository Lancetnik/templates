<script>
import { Line, mixins } from "vue-chartjs" // You can also import "Bar, Pie, Radar"
const { reactiveProp } = mixins

export default {
  extends: Line, 
  mixins: [reactiveProp],
  props: ['options'],

  data() {
    return {
      gradient: null,
    }
  },
  mounted() {
    this.gradient = this.$refs.canvas
      .getContext("2d")
      .createLinearGradient(0, 0, 0, 450);

    this.gradient.addColorStop(0, 
      `rgba(${this.chartData.datasets[0].backgroundColor["r"]}, 
            ${this.chartData.datasets[0].backgroundColor["g"]},
            ${this.chartData.datasets[0].backgroundColor["b"]}, 0.5)`
            )
    this.gradient.addColorStop(0.5, 
      `rgba(${this.chartData.datasets[0].backgroundColor["r"]}, 
            ${this.chartData.datasets[0].backgroundColor["g"]},
            ${this.chartData.datasets[0].backgroundColor["b"]}, 0.25)`
            )
    this.gradient.addColorStop(1, 
      `rgba(${this.chartData.datasets[0].backgroundColor["r"]}, 
            ${this.chartData.datasets[0].backgroundColor["g"]},
            ${this.chartData.datasets[0].backgroundColor["b"]}, 0.0)`
            )
            
    this.chartData.datasets[0].backgroundColor = this.gradient

    this.renderChart(this.chartData, {
      responsive: true,
      maintainAspectRatio: false,
      
      onClick: function(event, pointsArray) {
        if(pointsArray.length === 1) {
          var pointPosition = pointsArray[0]._index
          var pointValue = this.tooltip._data.datasets[0].data[pointPosition]
          console.log(pointValue)
        } else {
            console.log("You selected the background!")            
        }  
      }
    })
  }
}
</script>