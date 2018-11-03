<template>
  <v-app dark>
    <!-- Toolbar -->
    <v-toolbar dark color="primary">
      <v-toolbar-title>Ring of Fortune</v-toolbar-title>
    </v-toolbar>

    <!-- Main container -->
    <v-container fluid fill-height>
      <v-layout justify-center align-center>
        <div>
          <v-btn depressed small color="secondary">
            Spin the ring!
          </v-btn>
        </div>
      <!--Stuff goes in here (Wheel)-->
      </v-layout>
    </v-container>
    
    <!--Footer-->
    <v-footer app fixed>
      <span color="accent">A Summer Knight Project</span>
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
        
        
      }
    },


    methods: {

    },

    
};

</script>

<style>

</style>
