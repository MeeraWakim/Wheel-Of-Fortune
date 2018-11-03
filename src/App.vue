<template>
  <v-app>
    <!-- Toolbars -->
    <v-toolbar>
      <v-toolbar-side-icon></v-toolbar-side-icon>
      <v-toolbar-title>Title</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-sm-and-down">
        <v-btn flat>Link One</v-btn>
        <v-btn flat>Link Two</v-btn>
        <v-btn flat>Link Three</v-btn>
      </v-toolbar-items>
    </v-toolbar>

    <!-- Main container -->
    <v-container fluid fill-height>
      <v-layout justify-center align-center>
        <v-flex shrink>
          <v-tooltip right>
            <v-btn
              slot="activator"
              :href="source"
              icon
              large
              target="_blank"
            >
              <v-icon large>code</v-icon>
            </v-btn>
            <span>Source</span>
          </v-tooltip>
          <v-tooltip right>
            <v-btn slot="activator" icon large href="https://codepen.io/johnjleider/pen/qxQWda" target="_blank">
              <v-icon large>mdi-codepen</v-icon>
            </v-btn>
            <span>Codepen</span>
          </v-tooltip>
        </v-flex>
      </v-layout>
    </v-container>
    
    <!--Footer-->
    <v-footer app fixed>
      <span>A Summer Knight Project</span>
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
