<template>
  <div>
    <h3>{{title}} para las {{this.horario.horaInicio}}</h3>
    <!-- lista de pasajes -->
    <div v-if="!formulario">
      <a class="waves-effect waves-light btn" v-on:click="openForm">
        Agregar<i class="material-icons left">add_box</i>
      </a>
      <br />
      <table>
          <thead>
            <tr>
              <th>persona</th>
              <th>número asiento</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="pasaje in pasajes" v-bind:key="pasaje.index">
              <td><strong>{{`${pasaje.pasajero.nombrePrimario} ${pasaje.pasajero.nombreSecundario}`}}</strong></td>
              <td>{{pasaje.numeroAsiento}}</td>
              <td>
                <a class="waves-effect waves-light btn ab-btn-edit tooltipped" v-on:click="getPasaje(pasaje.id)">
                  <i class="material-icons left ab-icon-action">edit</i>
                </a>
                <a class="waves-effect waves-light btn ab-btn-delete" v-on:click="borrar(pasaje.id)">
                  <i class="material-icons left ab-icon-action">delete</i>
                </a>
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
        <br />
        <br />
        <div class="row">
          <div class="col s12">
            <div class="row">
              <div class="input-field col s4">
                <select v-model="pasaje.pasajero" class="browser-default">
                  <option value="0" disabled selected>Selecciona un pasajero</option>
                  <option v-for="pasajero in pasajeros" 
                    v-bind:value="pasajero.idPersona"
                    v-bind:key="pasajero.idPersona"
                  >
                    {{`${pasajero.nombrePrimario} ${pasajero.apPaterno}`}}
                  </option>
                </select>
                <label for="pasajero" class="active">pasajero</label>
              </div>
              <div class="input-field col s4">
                <input  id="numeroAsiento" type="text" class="validate" v-model="pasaje.numeroAsiento">
                <label for="numeroAsiento" class="active">numero de asiento</label>
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
import moment from 'moment';

export default {
  name: 'pasajes',
  data: ()=>{
    return {
      title: 'Pasajes',
      formulario: false,
      editar: false,
      pasajes: [],
      pasajeros: [],
      pasaje: {
        id: 0,
        horario: 0,
        pasajero: 0,
        numeroAsiento: ''
      },
      horario: {
        idHorarioServicio: 0,
        horaInicio: '',
        horaFin: ''
      }
    }
  },
  mounted(){
    this.formulario = false;
    this.editar = false;
    this.horario.idHorarioServicio = this.$route.params.idHorario;
    this.getPasajes();
    this.getHorario();
    this.getPasajeros();
  },
  methods:{
    getPasajes: function(){
      let ruta= `http://localhost:8000/apiBuses/pasajesHorario/${this.horario.idHorarioServicio}`;
      axios.get(ruta)
      .then(res=>{
        this.pasajes = res.data;
        console.log('pasajes',this.pasajes)
      })
      .catch(err=>{
        console.log(err);
        alert('Error al cargar los pasajes');
      });
    },
    getPasaje: function(id){
      let ruta = `http://localhost:8000/apiBuses/pasajes/${id}`;
      axios.get(ruta)
      .then(res=>{
        this.pasaje.id = res.data.id;
        this.pasaje.horario = res.data.horario;
        this.pasaje.pasajero = res.data.pasajero.idPersona;
        this.pasaje.numeroAsiento = res.data.numeroAsiento;

        this.editar = true;
        this.formulario = true;
      })
      .catch(err=>{
        console.log(err);
        alert('Error al obtener el pasaje');
      })
    },
    getHorario: function(){
      let ruta = `http://127.0.0.1:8000/apiBuses/horarios/${this.horario.idHorarioServicio}`;
      axios.get(ruta)
      .then(res=>{
        this.horario.fechaServicio = res.data.fechaServicio;
        this.horario.horaInicio = moment(res.data.horaInicio,'HH:mm:ss').format("HH:mm");
        this.horario.horaFin = moment(res.data.horaFin,'HH:mm:ss').format("HH:mm");
      })
      .catch(err=>{
        console.log('ERROR:',err)
        alert('ERROR al obtener horario');
      })
    },
    getPasajeros: function(){
      let ruta='http://localhost:8000/apiBuses/personasPasajeros';
      axios.get(ruta)
      .then(res=>{
        this.pasajeros = res.data;      
      })
      .catch(err=>{
        console.log('ERROR: ',err);
        alert('Error al obtener pasajeros');
      })
    },
    sendIngresar(){
      let ruta = 'http://127.0.0.1:8000/apiBuses/pasajes/';
      let {pasajero,numeroAsiento} = this.pasaje;
      let pasajeSalida = {
        horario: this.horario.idHorarioServicio,
        pasajero,
        numeroAsiento
      };
      let config = {
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json"
        }
      }
      axios.post(ruta,pasajeSalida,config)
        .then(res=>{
          alert('Ingresado correctamente')
          this.formulario = false;
          this.editar = false;
          this.getPasajes();
        })
        .catch(err=>{
          console.log('ERROR: ',err);
          alert('Error al ingresar');
        });
    },
    sendEdit(){
      let idPasaje = this.pasaje.id;
      let ruta = `http://127.0.0.1:8000/apiBuses/pasajes/${idPasaje}/`;
      let {pasajero,numeroAsiento} = this.pasaje;
      let pasajeSalida = {
        horario: this.horario.idHorarioServicio,
        pasajero,
        numeroAsiento
      };
      let config = {
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json"
        }
      }
      axios.put(ruta,pasajeSalida,config)
        .then(res=>{
          alert('mnodificado correctamente')
          this.formulario = false;
          this.editar = false;
          this.getPasajes();
        })
        .catch(err=>{
          console.log('ERROR: ',err);
          alert('Error al modificar');
        });
    },
    sendBorrar: function(id){
      let ruta = `http://127.0.0.1:8000/apiBuses/pasajes/${id}/`;
      axios.delete(ruta)
      .then(res=>{
        if (res.status == 204){
          alert('eliminado correctamente');
          this.getPasajes();
        }
      })
      .catch(err=>{
        console.log('ERROR: ',err);
        alert('Error al eliminar');
      })
    },
    enviar: function(){
      if(this.editar){
        this.sendEdit()
      }else{
        this.sendIngresar()
      }
    },
    borrar: function(id){
      let borrar = confirm('¿Seguro que quiere borrar este registro?');
      if(borrar){
        this.sendBorrar(id);
      }
    },
    openForm: function(){
      this.formulario = true;
      // reset pasaje
      this.pasaje.horario = 0;
      this.pasaje.pasajero = 0;
      this.pasaje.numeroAsiento = '';
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
  .ab-icon-action{
    margin-right: 0px;
  }
</style>