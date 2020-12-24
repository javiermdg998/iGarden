<template>
  <div class="small">
    <h2>{{title}}</h2>
    <line-chart :chart-data="datacollection"></line-chart>
    <button @click="fillData()">Randomize</button>
     <button @click="add()">Add data</button>
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
        points:[this.getRandomInt(), this.getRandomInt()],
        labels:[this.getRandomInt(), this.getRandomInt()]
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
        let labels_=[]
        let datas_=[]
        data.forEach(element => {
            let date=new Date(element.time)            
            labels_.push(`${date.getDay()}-${date.getMonth()}`)
            datas_.push(element.value)
        });


        this.datacollection = {
          labels: labels_,
          datasets: [
            {
              label: 'Data One',
              backgroundColor: this.color,
              data: datas_
            }, 
          ]
        }
        
      })
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