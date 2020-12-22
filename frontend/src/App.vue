<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Wecome to Your Vue.js App"/>
    <Grafico/>
  </div>
</template>

<script>
import HelloWorld from './pages/HelloWorld.vue'
import Grafico from './components/Grafico.vue'
export default {
  name: 'App',
  components: {
    HelloWorld,
    Grafico
  },
  data:()=>({
  
  })
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
