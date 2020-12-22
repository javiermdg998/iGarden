<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <div>Moisture value: <span>{{value}}</span></div>
    
  </div>
</template>

<script>
import io from 'socket.io-client';

export default {
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
</style>
