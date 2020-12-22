<template>
  <div class="small">
    <chart :chart-data="datacollection"></chart>
    <button @click="fillData()">Randomize</button>
     <button @click="add()">Add data</button>
  </div>
</template>

<script>
  import Chart from './Chart.js'

  export default {
    name:'Grafico',
    components: {
      'chart':Chart
    },
    data () {
      return {
        datacollection: null,
        points:[this.getRandomInt(), this.getRandomInt()],
        labels:[this.getRandomInt(), this.getRandomInt()]
      }
    },
    mounted () {
      this.fillData()
    },
    methods: {
      fillData () {
        this.datacollection = {
          labels: this.labels,
          datasets: [
            {
              label: 'Data One',
              backgroundColor: '#f87979',
              data: this.points
            }, 
          ]
        }
      },
      add(){
          this.points.push(this.getRandomInt())
          this.labels.push(this.getRandomInt())
           this.datacollection = {
          labels: this.labels,
          datasets: [
            {
              label: 'Data One',
              backgroundColor: '#f87979',
              data: this.points
            }, 
          ]
        }
      },
      getRandomInt () {
        return Math.floor(Math.random() * (50 - 5 + 1)) + 5
      }
    }
  }
</script>

<style>
  .small {
    max-width: 400px;
    margin:  150px auto;
  }
</style>