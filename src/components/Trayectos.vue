<template>
  <div>
    <h3>Mantenedor {{title}}</h3>
    <!-- lista de trayectos -->
    <div v-if="!formulario">
      <a class="waves-effect waves-light btn" v-on:click="openForm">
        Agregar<i class="material-icons left">add_box</i>
      </a>
      <br />
      <table>
        <thead>
          <tr>
            <th>ciudad salida</th>
            <th>Ciudad llegada</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="trayecto in trayectos" v-bind:key="trayecto.idTrayecto">
            <td>{{trayecto.ciudadSalida}}</td>
            <td>{{trayecto.ciudadLlegada}}</td>
            <td>
              <a class="waves-effect waves-light btn ab-btn-edit tooltipped" v-on:click="getTrayecto(trayecto.idTrayecto)" data-tooltip="I am a tooltip">
                <i class="material-icons left ab-icon-action">edit</i>
              </a>
              <a class="waves-effect waves-light btn ab-btn-delete" v-on:click="borrar(trayecto.idTrayecto)">
                <i class="material-icons left ab-icon-action">delete</i>
              </a>
              <router-link
                class="waves-effect waves-light btn ab-btn-horarios"
                v-bind:to="`horarios/${trayecto.idTrayecto}`"
              >
                Horarios
                <i class="material-icons right">access_time</i>
              </router-link>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div v-if="formulario">
      <a class="waves-effect waves-light btn" v-on:click="formulario = false, editar = false">
        <span v-if="!editar">Agregar</span>
        <span v-if="editar">Editar</span>
        <i class="material-icons left">remove</i>
      </a>
      <br/>
      <br/>
      <div class="row">
        <div class="col s12">
          <div class="row">
            <div class="input-field col s4">
              <input  id="patente" type="text" class="validate" v-model="trayecto.ciudadSalida">
              <label for="patente" class="active">Ciudad Salida</label>
            </div>
            <div class="input-field col s4">
              <input  id="modelo" type="text" class="validate" v-model="trayecto.ciudadLlegada">
              <label for="modelo" class="active">Ciudad Llegada</label>
            </div>
          </div>
          <div class="row">
            <div class="col-s12">
              <button class="waves-effect waves-light btn" v-on:click='enviar'>
                <span v-if="!editar">Ingresar</span>
                <span v-if="editar">Modificar</span>
                <i v-if="!editar" class="material-icons left">add_box</i>
                <i v-if="editar" class="material-icons left">edit</i>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>


  </div>
</template>


<script>
import axios from 'axios';

export default {
  name: 'trayectos',
  data: ()=>{
    return {
      title: 'Trayectos',
      formulario: false,
      editar: false,
      trayectos: [],
      trayecto: {
        idTrayecto: 0,
        ciudadSalida: '',
        ciudadLlegada: ''
      }
    }
  },
  mounted(){
    this.formulario = false;
    this.editar = false;
    this.getTrayectos();
  },
  methods:{
    getTrayectos: function(){
      let ruta = 'http://localhost:8000/apiBuses/trayectos/';
      axios.get(ruta)
      .then(res => {
        this.trayectos = res.data;
        console.log(res.data);
      })
      .catch(err=>{
        alert('Ocurrió un error');
        console.log('ERROR:', err);
      })
    },
    getTrayecto: function(idTrayecto){
      let ruta = `http://localhost:8000/apiBuses/trayectos/${idTrayecto}`;
      axios.get(ruta)
      .then(res => {
        this.trayecto.idTrayecto = res.data.idTrayecto,
        this.trayecto.ciudadSalida = res.data.ciudadSalida,
        this.trayecto.ciudadLlegada = res.data.ciudadLlegada

        this.editar = true;
        this.formulario = true;
      })
      .catch(err => {
        alert('Ocurrió un error');
        console.log('ERROR:', err);
      });
    },
    sendEdit: function(){
      let ruta = `http://localhost:8000/apiBuses/trayectos/${this.trayecto.idTrayecto}/`
      let {ciudadSalida,ciudadLlegada} = this.trayecto;
      let trayectoSalida = {
        ciudadSalida,
        ciudadLlegada
      };
      let config = {
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json"
        }
      };
      axios.put(ruta,trayectoSalida,config)
      .then(res=>{
        alert('Registro modificado');
        this.formulario = false;
        this.editar = false;
        this.getTrayectos();
      })
      .catch(err=>{
        alert('Ocurrio un error')
          console.log('ERROR: ',err);
      });

    },
    sendIngresar: function(){
      let ruta = 'http://localhost:8000/apiBuses/trayectos/'
      let {ciudadSalida,ciudadLlegada} = this.trayecto;
      let trayectoSalida = {
        ciudadSalida,
        ciudadLlegada
      };
      let config = {
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json"
        }
      };
      axios.post(ruta,trayectoSalida,config)
      .then(res=>{
        alert('Ingresado correctamente');
        this.formulario = false;
        this.editar = false;
        this.getTrayectos();
      })
      .catch(err=>{
        alert('Ocurrio un error')
          console.log('ERROR: ',err);
      });
    },
    sendBorrar: function(idTrayecto){
      let ruta = `http://localhost:8000/apiBuses/trayectos/${idTrayecto}/`
      axios.delete(ruta)
      .then(res => {
        if (res.status == 204){
          alert('eliminado correctamente');
          this.getTrayectos();
        }
      })
      .catch(err=>{
        alert('Ocurrió un error');
        console.log('ERROR: ',err);
      })
    },
    borrar: function(idTrayecto){
      let borrar = confirm('¿Seguro que quiere borrar este registro?');
      if(borrar){
        this.sendBorrar(idTrayecto);
      }
    },
    enviar: function(){
      if(this.editar){
        this.sendEdit()
      }else{
        this.sendIngresar()
      }
    },
    openForm: function(){
      this.formulario = true;
      this.trayecto.idTrayecto = 0;
      this.trayecto.ciudadSalida = '';
      this.trayecto.ciudadLlegada = '';
    }
  }
}
</script>

<style scoped>
    .ab-btn-edit{
    margin-right: 10px;
  }
  .ab-btn-delete{
    background-color: #ee6e73;
    margin-right: 10px;
  }
  .ab-btn-horarios{
    background-color: #FFED66;
    color: black;
  }
  .ab-icon-action{
    margin-right: 0px;
  }
</style>
