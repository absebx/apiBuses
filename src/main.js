import Vue from 'vue'
import App from './App.vue'
import 'materialize-css'
import 'materialize-css/dist/css/materialize.css'
import VueRouter from 'vue-router'
import Personas from './components/Personas.vue';
import Buses from './components/Buses.vue';
import Trayectos from './components/Trayectos.vue';
import Horarios from './components/Horarios';
import Pasajes from './components/Pasajes';
import TipoPersonas from './components/TipoPersonas';

Vue.use(VueRouter)

const routes = [
  { path: '/personas', component: Personas },
  { path: '/buses', component: Buses },
  { path: '/trayectos', component: Trayectos},
  { path: '/horarios/:idTrayecto', component: Horarios},
  { path: '/pasajes/:idHorario', component: Pasajes},
  { path: '/tipoPersonas', component: TipoPersonas }
]

const router = new VueRouter({
  routes
})

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
