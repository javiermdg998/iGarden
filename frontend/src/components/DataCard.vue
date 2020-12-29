<template>
    <div class="variable-card">
        <v-row>
          <span class="icon" v-bind:style="{ background: color}" >
            <v-icon>{{icon}}</v-icon>
          </span>
          <span class="value">{{value}} {{unit}}</span>
        </v-row>       
          <div class="topic"> {{topic}}</div>        
      </div>
</template>
<script>
export default {
    props:{
        value: String,
        topic: String,
        unit: String,
        icon: String,
        color: String
    }
}
</script>
<style >
.variable-card{
  display: flex;
  flex-direction: column;
  margin: 15px 35px;
  position: relative;
  /* border: solid 1px black; */
  font-size:50px;
box-shadow: 0px 2px 4px -1px rgba(0, 0, 0, 0.30),
            0px 4px 5px 0px rgba(0, 0, 0, 0.34),
            0px 1px 10px 0px rgba(0, 0, 0, 0.32);
padding: 25px;
min-width: 500px;
border-radius: 5px;
}
 .icon{
  box-shadow: 0px 2px 4px -1px rgba(0, 0, 0, 0.60),
              0px 4px 5px 0px rgba(0, 0, 0, 0.64),
              0px 1px 10px 0px rgba(0, 0, 0, 0.62);
  background: red;
  min-height: 150px;
  transform: translate(0px, -65px);
  border-radius: 5px;
  position: absolute;
  left:24px
}
.variable-card i{
  font-size: 180px!important;
  color: aliceblue!important;
  
}
.variable-card .value{
  font-size: 60px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-left: 224px;
  margin-top: 10px;
  
}
.topic{
  margin-left: 5px;
  margin-top: 50px;
  text-align: left;
}
</style>