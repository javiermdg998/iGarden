<template>
  <div class="historic">
    <h1 class="historic-title">Monitorizacion del invernadero</h1>
    <v-row class="row">
        <Chart color="#e8e810"  title="Luminosidad" dataSource="http://localhost:5000/luminity"/>
        <Chart color="#e86e10" title="Temperatura" dataSource="http://localhost:5000/temperature"/>
        <Chart color="#3259a8" title="Humedad" dataSource="http://localhost:5000/humidity"/>
         
    </v-row>
  
  </div>
</template>
<script>
import Chart from "@/components/Chart.vue"

export default {
  components:{Chart}
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