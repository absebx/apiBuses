<template>
  <nav>
    <div class="nav-wrapper">
      <a href="#" class="brand-logo center">{{title}}</a>
      <ul id="nav-mobile" class="left hide-on-med-and-down">
        <li><router-link to="/personas">Personas</router-link></li>
        <li><router-link to="/TipoPersonas">Tipos de personas</router-link></li>
        <li><router-link to="/buses">Buses</router-link></li>
        <li><router-link to="/trayectos">Trayectos</router-link></li>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'navBar',
  data: ()=>{
    return {
      title: 'AppBuses'
    }
  }
}
</script>