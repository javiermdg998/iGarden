<template>
  <div class="small">
    <h2>{{title}}</h2>
    <line-chart :chart-data="datacollection"></line-chart>

    
  </div>
</template>

<script>
  import LineChart from './LineChart.js'
  import DataApi from "@/util/DataApi.js"
  export default {
    name:'Chart',
    components: {
      'line-chart':LineChart
    },
    props: {
    color: String,
    dataSource: String,
    title:String    
  },
    data () {
      return {
        datacollection: {},
        points:[],
        labels:[]
      }
    },
   
    mounted(){
      DataApi.fetchJSONUrl(this.dataSource).then((data)=>{
       
     
        data.forEach(element => {
            let date=new Date(element.time)            
            this.labels.push(`${date.getHours()}:${date.getMinutes()} ${date.getDay()}-${date.getMonth()+1}`)
            this.points.push(element.value)
        });


        this.datacollection = {
          labels: this.labels,
          datasets: [
            {
              label: 'Data One',
              backgroundColor: this.color,
              data: this.points
            }, 
          ]
        }
        
      })
    },
    methods: {
      

      add(x){
          let date=new Date()
          this.points.push(x)
          
          this.labels.push(`${date.getDay()}-${date.getMonth()}`)
          this.points.splice(0,1)//borramos el valor mas antiguo para no desbordar el grafico
          this.labels.splice(0,1)
          this.datacollection = {
          labels: this.labels,
          datasets: [
            {
              label: 'Data One',
              backgroundColor: this.color,
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