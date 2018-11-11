<template>
  <v-app dark>
    <!-- Toolbar/Logo -->
    <v-toolbar dark color="primary" height="110">
        <img align="middle" 
             id="logo" 
             src="../Gearofluck.png" 
             height="90"
             width="150"
             >
    </v-toolbar>

    <!-- Main container -->
    <v-container fluid fill-height>
      <v-layout justify-center align-center>
        <div>
          <v-btn
            align="bottom"
            depressed
            large
            color="accent"
            @click="onClick()">
            Spin the Gear!
          </v-btn>
        </div>
      <!--Stuff goes in here (Wheel)-->
      </v-layout>
    </v-container>
    
    <!--Footer-->
    <v-footer app fixed>
      <span color="secondary">A Summer Knight Project</span>
    </v-footer>
  </v-app>
</template>

<script>
import * as axios from 'axios';

export default {
    name: 'app',
    
    components: {
      
    },

    data() {
      return {
        flaskdata: 'HelloBitches',
      }
    },
    methods: {    onClick(){
      console.log("FUNCTION RAN");
      axios.post('http://127.0.0.1:5000/uploads/data',{body: this.flaskdata})
    .then(response => {})
    .catch(e => {
      this.errors.push(e)
    })
    },
    },
};
</script>

<style>

</style>
