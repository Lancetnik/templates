<template>
    <v-container>
        <h1>Chart</h1>
        <v-btn
        @click="changePoints()"
        >Поменять значения графика</v-btn>
        <Chart :chart-data="chartData"/>	
    </v-container>
</template>

<script>
import Chart from "../components/Chart.vue"

export default {
    components: {
        Chart
    },

    data() {
        return {
            chartData: {
                labels: ["1", "2", "3"],
                datasets: [
                    {
                        label: "Наименование графика",
                        borderColor: "yellow",
                        pointBackgroundColor: "black",
                        borderWidth: 1,
                        pointBorderColor: "white",
                        backgroundColor: {"r": 255, "g": 255, "b": 0},
                        data: [36, 54, 100]
                    }
                ]
            }
        }
    },

    methods: {
        changePoints() {
            this.chartData = {
                labels: [Math.random(), Math.random(), Math.random()],
                datasets: [
                    {
                        label: this.chartData.datasets[0].label,
                        borderColor: this.chartData.datasets[0].borderColor,
                        pointBackgroundColor: this.chartData.datasets[0].pointBackgroundColor,
                        borderWidth: 1,
                        pointBorderColor: this.chartData.datasets[0].pointBorderColor,
                        backgroundColor: this.chartData.datasets[0].backgroundColor,
                        data: [Math.random(), Math.random(), Math.random()]
                    }
                ]
            }
        }
    }
}
</script>