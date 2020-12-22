<template>
  <div class="hello"> 
    <v-row class="row">   
<VueSvgGauge
  :start-angle="-110"
  :end-angle="110"
  :value="random"
  :separator-step="20"
  :scale-interval="10"
  :inner-radius="80"
>
  <span class="inner-text">
    <span>Temperatura</span>
  </span>
</VueSvgGauge>
<VueSvgGauge
  :start-angle="-110"
  :end-angle="110"
  :value="random"
  :separator-step="20"
  :scale-interval="10"
  :inner-radius="80"
>
  <span class="inner-text">
    <span>Temperatura</span>
  </span>
</VueSvgGauge>
<VueSvgGauge
  :start-angle="-110"
  :end-angle="110"
  :value="random"
  :separator-step="20"
  :scale-interval="10"
  :inner-radius="80"
>
  <span class="inner-text">
    <span>Temperatura</span>
  </span>
</VueSvgGauge>
</v-row>
  </div>
</template>

<script>
import io from 'socket.io-client';
import { VueSvgGauge } from 'vue-svg-gauge'
 

  

export default {
  components: {
    VueSvgGauge,
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
    color: red;
    
  }
</style>
