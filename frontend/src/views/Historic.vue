<template>
  <div class="historic">
    <h1 class="historic-title">Monitorizacion del invernadero</h1>
    
    <v-row class="row">
        <Chart color="#e8e810"  title="Luminosidad" dataSource="http://localhost:5000/luminity" ref="chart_lumi"/>
        <Chart color="#e86e10" title="Temperatura" dataSource="http://localhost:5000/temperature" ref="chart_temp"/>
        <Chart color="#3259a8" title="Humedad" dataSource="http://localhost:5000/humidity" ref="chart_hum"/>
         
    </v-row>
  
  </div>
</template>
<script>
import Chart from "@/components/Chart.vue"
import DataApi from "@/util/DataApi.js"

export default {
  components:{Chart},
  data:()=>({
    interval:null,
    chart_lumi:null,
    chart_temp:null,
    chart_hum:null
  }),
  created(){
    this.interval=setInterval(()=>{DataApi.getState().then((state)=>{
      console.log(state)
       this.$refs.chart_lumi.add(state.luminity)
      this.$refs.chart_temp.add(state.temperature)
      this.$refs.chart_hum.add(state.humidity)
    })},3000)
  },
  beforeDestroy(){
      clearInterval(this.interval)
  }
}
</script>
<style  scoped>
.historic-title{
  margin:55px 0 0 0;
}
.small {
  margin:60px auto;
}
</style>