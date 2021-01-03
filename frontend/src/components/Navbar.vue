<template>
  <v-bottom-navigation
    :value="value"
    color="#442bcf"
    grow 
    class="navbar-container"
  >
    <v-btn href="/#/">
      <span>Monitoring</span>

      <v-icon>mdi-gauge</v-icon>
    </v-btn >

    <v-btn href="/#/historic">
      <span>Historic</span>

      <v-icon>mdi-chart-line-variant</v-icon>
    </v-btn>    
  </v-bottom-navigation>
</template>
<script>
  export default {
    data: () => ({ value: 1 }),
    created(){
      let location =  window.location
      let loc_array= location.toString().split("/")
      switch(loc_array[loc_array.length - 1]){
        case "":
          this.value=0
          break;
        case "historic":
          this.value=1
          break;
      }
    }
  }

</script>
<style  scoped>
.navbar-container{
    align-items: center;
}
</style>