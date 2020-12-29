<template>
  <div class="monitoring"> 
   
    <v-row class="row-card">   
      <DataCard icon="mdi-thermometer" topic="Temperatura" :value="this.temperature+''" unit="ºC" color="red"/>
       <DataCard icon="mdi-watering-can" topic="Hidratado" :value="this.humid?'SI':'NO'" unit="" color="green"/>
    </v-row>

    <v-row class="row-card">   
       <DataCard icon="mdi-water-percent" topic="Humedad " :value="this.humidity+''" unit="%" color="blue"/>
       <DataCard icon="mdi-lightbulb" topic="Temperatura" :value="this.luminity+''" unit="lux" color="orange"/>

</v-row>

  </div>
</template>

<script>
// import io from 'socket.io-client';
// import { VueSvgGauge } from 'vue-svg-gauge'
import DataCard from "@/components/DataCard.vue"
import DataApi from "@/util/DataApi.js"
  

export default {
  components: {
    // VueSvgGauge,
    DataCard
  },
  name: 'HelloWorld',
  props: {
    msg: String,
    data: String
  },
  data:()=>({
    connection:null,
    value:0,
    humidity:0,
    temperature:0,
    humid:false,
    luminity:0,
    interval:null
  }),
  created(){
  
    // this.connection=io("ws://127.0.0.1:5000",{
    //   transports:["websocket"]
    // })
    // this.connection.on("message",(data)=>{
    //   console.log(data)
    
    this.interval=setInterval(()=>{
        DataApi.getState().then(data=>{
          console.log(data)
          this.humidity=data.humidity
          this.temperature=data.temperature
          this.luminity=data.luminity
          this.humid=data.humid
        })},1000)

  
 
  },
  beforeDestroy(){

  },
  methods:{
   
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
