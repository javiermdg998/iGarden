<template>
  <div class="historic">
    <h1 class="historic-title">Monitorizacion del invernadero</h1>
    <v-row class="row">
        <Chart color="#e8e810"  title="Luminosidad" />
        <Chart color="#e86e10" title="Temperatura" />
        <Chart color="#3259a8" title="Humedad" />
         
    </v-row>
  
  </div>
</template>
<script>
import Chart from "@/components/Chart.vue"

export default {
  components:{Chart},
  data:()=>({
    
  }),
  created(){
    
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