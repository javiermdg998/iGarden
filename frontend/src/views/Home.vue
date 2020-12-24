<template>
  <div class="monitoring"> 
   
    <v-row class="row-card">   
      <DataCard icon="mdi-thermometer" topic="Temperatura" value="18" unit="ºC" color="red"/>
       <DataCard icon="mdi-watering-can" topic="Hidratado" value="SI" unit="" color="green"/>
    </v-row>

    <v-row class="row-card">   
       <DataCard icon="mdi-water-percent" topic="Humedad " value="35" unit="%" color="blue"/>
       <DataCard icon="mdi-lightbulb" topic="Temperatura" value="23" unit="lux" color="orange"/>
    <!-- <VueSvgGauge
      :start-angle="-110"
      :end-angle="110"
      :value="56"
      :separator-step="20"
      :scale-interval="10"
      :inner-radius="80"
    >
      <span class="inner-text">
        <span>Humedad</span>
      </span>
    </VueSvgGauge> -->
</v-row>

  </div>
</template>

<script>
import io from 'socket.io-client';
// import { VueSvgGauge } from 'vue-svg-gauge'
import DataCard from "@/components/DataCard.vue"

  

export default {
  components: {
    // VueSvgGauge,
    DataCard
  },
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data:()=>({
    connection:null,
    value:0,
  }),
  created(){
    this.connection=io("ws://192.168.8.116:5000",{
      transports:["websocket"]
    })
    this.connection.on("message",(data)=>{
      console.log(data)
    })
  },
  mounted(){
    
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.gauge{
  width: 400px;
}

.inner-text {
  position: absolute;
  bottom: 25%;
  left: 0%;
  width: 100%;
 
  
}
.inner-text span {
    max-width: 100px;
    color: black;
    
  }
.row{
  display: flex;
  justify-content: space-around;
  align-self: center;
}

.row-card{
  justify-content: center;
  margin-bottom: 35px;
}
.row-card:nth-of-type(1){
  margin-top: 45px;
}

h1{
  margin: 15px 0 10px;
}


</style>
