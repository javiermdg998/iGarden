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

    <v-btn href="/#/about">
      <span>Historic</span>

      <v-icon>mdi-chart-line-variant</v-icon>
    </v-btn>    
  </v-bottom-navigation>
</template>
<script>
  export default {
    data: () => ({ value: 1 }),
  }
</script>
<style  scoped>
.navbar-container{
    align-items: center;
}
</style>