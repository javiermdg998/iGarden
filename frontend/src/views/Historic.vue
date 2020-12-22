<template>
  <div class="historic">
    <h1 class="historic-title">Monitorizacion del invernadero</h1>
    <v-row class="row">
      <Grafico/>
        <Grafico/>
        <Grafico/>
                <Grafico/>
    </v-row>
    <v-row class="row">
            
                 </v-row>
  </div>
</template>
<script>
import Grafico from "@/components/Grafico.vue"

export default {
  components:{Grafico}
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