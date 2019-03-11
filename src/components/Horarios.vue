<template>
  <div>
    <h4>Horarios para trayecto <strong>{{trayecto.nombre}}</strong></h4>

    <!-- lista de trayectos -->
    <div v-if="!formulario">
      <a class="waves-effect waves-light btn" v-on:click="openForm">
        Agregar<i class="material-icons left">add_box</i>
      </a>
      <br />
      <table>
        <thead>
          <tr>
            <th>Fecha</th>
            <th>Hora Inicio</th>
            <th>Hora fin</th>
            <th>Chofer</th>
            <th>modelo Bus</th>
            <th>patente</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="horario in horarios" v-bind:key="horario.idHorarioServicio">
            <td><strong>{{horario.fechaServicio}}</strong></td>
            <td>{{horario.horaInicio}}</td>
            <td>{{horario.horaFin}}</td>
            <td>{{`${horario.chofer.nombrePrimario} ${horario.chofer.apPaterno}`}}</td>
            <td>{{horario.bus.modelo}}</td>
            <td>{{horario.bus.patente}}</td>
            <td>
              <a class="waves-effect waves-light btn ab-btn-edit tooltipped" v-on:click="getHorario(horario.idHorarioServicio)" data-tooltip="I am a tooltip">
                <i class="material-icons left ab-icon-action">edit</i>
              </a>
              <a class="waves-effect waves-light btn ab-btn-delete" v-on:click="borrar(horario.idHorarioServicio)">
                <i class="material-icons left ab-icon-action">delete</i>
              </a>
              <router-link
                class="waves-effect waves-light btn ab-btn-pasajes"
                v-bind:to="`/pasajes/${horario.idHorarioServicio}`"
              >
                Pasajes
                <i class="material-icons right">local_mall</i>
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
              <input  id="fechaServicio" type="date" class="validate" v-model="horario.fechaServicio">
              <label for="fechaServicio" class="active">Fecha servicio</label>
            </div>
            <div class="input-field col s4">
              <input  id="horaInicio" type="time" class="validate" v-model="horario.horaInicio">
              <label for="horaInicio" class="active">Hora inicio</label>
            </div>
            <div class="input-field col s4">
              <input  id="horaFin" type="time" class="validate" v-model="horario.horaFin">
              <label for="horaFin" class="active">Hora fin</label>
            </div>
          </div>
          <div class="row">
            <div class="input-field col s4">
              <select v-model="horario.bus" class="browser-default">
                <option value="0" disabled selected>Selecciona el bus</option>
                <option v-for="bus in buses" 
                  v-bind:value="bus.idBus"
                  v-bind:key="bus.idBus"
                >
                  {{`${bus.patente}--${bus.modelo}`}}
                </option>
              </select>
              <label for="bus" class="active">bus</label>
            </div>
            <div class="input-field col s4">
              <select v-model="horario.chofer" class="browser-default">
                <option value="0" disabled selected>Selecciona el chofer</option>
                <option v-for="chofer in choferes" 
                  v-bind:value="chofer.idPersona"
                  v-bind:key="chofer.idPersona"
                >
                  {{`${chofer.nombrePrimario} ${chofer.nombreSecundario}`}}
                </option>
              </select>
              <label for="bus" class="active">bus</label>
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
  name: 'horarios',
  data: ()=>{
    return{
      title: 'horarios',
      formulario: false,
      editar: false,
      horarios: [],
      choferes: [],
      buses: [],
      trayecto: {
        idTrayecto: '',
        nombre: ''
      },
      horario: {
        idHorarioServicio: 0,
        fechaServicio: Date.now(),
        horaInicio: Date.now().toLocaleString(),
        horaFin: Date.now().toLocaleString(),
        bus: 0,
        chofer: 0,
        trayecto: 0
      }
    }
  },
  mounted(){
    let idTrayecto = this.$route.params.idTrayecto;
    this.formulario=false;
    this.editar=false;
    this.getHorarios(idTrayecto);
    this.getTrayecto(idTrayecto);
    this.getChoferes();
    this.getBuses();
  },
  methods:{
    getHorarios: function(idTrayecto){
      //id del trayecto
      let ruta = `http://localhost:8000/apiBuses/horariosTrayecto/${idTrayecto}`;
      axios.get(ruta)
      .then(res => {
        this.horarios = res.data;
      })
      .catch(err=>{
        console.log(err);
        alert('Ocurrió un error');
      });
    },
    getHorario: function(idHorarioServicio){
    let ruta = `http://127.0.0.1:8000/apiBuses/horarios/${idHorarioServicio}`;
    axios.get(ruta)
    .then(res=>{
      this.horario.idHorarioServicio = res.data.idHorarioServicio;
      this.horario.fechaServicio = res.data.fechaServicio;
      this.horario.horaInicio = moment(res.data.horaInicio,'HH:mm:ss').format("HH:mm");
      this.horario.horaFin = moment(res.data.horaFin,'HH:mm:ss').format("HH:mm");
      this.horario.bus = res.data.bus.idBus;
      this.horario.chofer = res.data.chofer.idPersona;
      this.horario.trayecto = res.data.trayecto;

      this.editar = true;
      this.formulario = true;
    })
    .catch(err=>{
      alert('ERROR al obtener horario');
      console.log('ERROR:',err)
    })
    },
    getTrayecto: function(idTrayecto){
      let ruta = `http://localhost:8000/apiBuses/trayectos/${idTrayecto}`;
      axios.get(ruta)
      .then(res => {
        this.trayecto.idTrayecto = res.data.idTrayecto;
        this.trayecto.nombre = `${res.data.ciudadSalida}-${res.data.ciudadLlegada}`;
      })
      .catch(err => {
        alert('Ocurrió un error');
        console.log('ERROR:', err);
      });
    },
    getChoferes: function(){
      let ruta = 'http://localhost:8000/apiBuses/personasChoferes';
      axios.get(ruta)
      .then(res=>{
        this.choferes = res.data;
      })
      .catch(err=>{
        alert('Ocurrió un error');
        console.log('ERROR: ',err);
      })
    },
    getBuses: function(){
      let ruta = 'http://localhost:8000/apiBuses/buses';
      axios.get(ruta)
      .then(res => {
        this.buses = res.data;
      })
      .catch(err=>{
        alert('Ocurrió un error');
        console.log('ERROR:', err);
      })
    },
    sendIngresar: function(){
      let ruta = 'http://127.0.0.1:8000/apiBuses/horarios/';
      let {fechaServicio,horaInicio,horaFin,bus,chofer,trayecto} = this.horario;
      let horarioSalida = {
        fechaServicio,
        horaInicio: `${horaInicio}:00`,
        horaFin: `${horaFin}:00`,
        bus,
        chofer,
        trayecto: this.trayecto.idTrayecto
      };
      let config = {
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json"
        }
      }
      axios.post(ruta,horarioSalida,config)
        .then(res=>{
          alert('Ingresado correctamente')
          this.formulario = false;
          this.editar = false;
          this.getHorarios(this.trayecto.idTrayecto);
        })
        .catch(err=>{
          alert('Ocurrio error')
          console.log('ERROR: ',err);
        });
    },
    sendEdit: function(){
      let ruta = `http://127.0.0.1:8000/apiBuses/horarios/${this.horario.idHorarioServicio}/`;
      let {fechaServicio,horaInicio,horaFin,bus,chofer,trayecto} = this.horario;

      let horarioSalida = {
        fechaServicio,
        horaInicio: `${horaInicio}:00`,
        horaFin: `${horaFin}:00`,
        bus,
        chofer,
        trayecto: this.trayecto.idTrayecto
      };
      let config = {
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json"
        }
      }
      axios.put(ruta,horarioSalida,config)
        .then(res=>{
          alert('Ingresado correctamente')
          this.formulario = false;
          this.editar = false;
          this.getHorarios(this.trayecto.idTrayecto);
        })
        .catch(err=>{
          alert('Ocurrio error')
          console.log('ERROR: ',err);
        });
    },
    sendBorrar: function(idHorarioServicio){
      let ruta = `http://127.0.0.1:8000/apiBuses/horarios/${idHorarioServicio}/`;
      axios.delete(ruta)
      .then(res=>{
        if (res.status == 204){
          alert('eliminado correctamente');
          this.getHorarios(this.trayecto.idTrayecto);
        }
      })
      .catch(err=>{
        alert('Ocurrió un error');
        console.log('ERROR: ',err);
      })
    },
    enviar: function(){
      if(this.editar){
        this.sendEdit()
      }else{
        this.sendIngresar()
      }
    },
    borrar: function(idHorarioServicio){
      let borrar = confirm('¿Seguro que quiere borrar este registro?');
      if(borrar){
        this.sendBorrar(idHorarioServicio);
      }
    },
    openForm: function(){
      this.formulario = true;
      // reset horario
      this.horario.idHorarioServicio = 0;
      this.horario.fechaServicio = '';
      this.horario.horaInicio = '';
      this.horario.horaFin = '';
      this.horario.bus = 0;
      this.horario.chofer = 0;
      this.horario.trayecto = this.trayecto.idTrayecto;
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
  .ab-btn-pasajes{
    background-color: #FFED66;
    color: black;
  }
  .ab-icon-action{
    margin-right: 0px;
  }
</style>


