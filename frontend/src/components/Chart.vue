<template>
  <div class="small">
    <h2>{{title}}</h2>
    <line-chart :chart-data="datacollection"></line-chart>

     <button @click="add(4)">Add data</button>
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
      fetch(this.dataSource).then((res)=>{
        if (res.ok){
          return res.text()
        }else{
          alert("error")
        }
      }).then((data)=>{
        data=JSON.parse(data)
     
        data.forEach(element => {
            let date=new Date(element.time)            
            this.labels.push(`${date.getDay()}-${date.getMonth()}`)
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
          this.points.push(x)
          this.labels.push(new Date())
            
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