import Vue from 'vue'
import App from './App.vue'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'


const VueScrollTo = require('vue-scrollto')

Vue.use(VueScrollTo)
Vue.use(Vuetify)
new Vue({
  el: '#app',
  render: h => h(App)
})

