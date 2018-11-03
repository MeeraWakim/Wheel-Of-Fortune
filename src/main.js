import Vue from 'vue'
import App from './App.vue'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'


const VueScrollTo = require('vue-scrollto')

Vue.use(VueScrollTo)
Vue.use(Vuetify, {
  theme: {
    "primary": "#455a64",
    "secondary": "#5e35b1",
    "accent": "#aa00ff",
    "error": "#c62828",
    "info": "#78909c",
    "success": "#4caf50",
    "warning": "#fbc02d"
  }
})

new Vue({
  el: '#app',
  render: h => h(App)
})

