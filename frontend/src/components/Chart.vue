<template>
  <div class="small">
    <h2>{{title}}</h2>
    <line-chart :chart-data="datacollection"></line-chart>

  </div>
</template>

<script>
  import LineChart from './LineChart.js'

  export default {
    name:'Chart',
    components: {
      'line-chart':LineChart
    },
    props: {
    color: String,
    dataSource: String,
    title:String,
    dataPoints:Object,
    dataLabels:Object    
  },
    data () {
      return {
        datacollection: {},
        points:[],
        labels:[]
      }
    },
   
    mounted(){    
        this.datacollection = {
          labels: this.dataLabels,
          datasets: [
            {
              label: 'Data One',
              backgroundColor: this.color,
              data: this.dataPoints
            }, 
          ]
        }
        
      },
      methods: {
        load_data () {
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
      
    }
  }
</script>

<style>
  .small {
    max-width: 400px;
    margin:  150px auto;
  }
</style>