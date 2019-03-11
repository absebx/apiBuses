<template>
  <div>
    <h3>
      Mantenedor {{title}}
    </h3>
    <!-- lista de buses -->
    <div v-if="!formulario">
      <a class="waves-effect waves-light btn" v-on:click="openForm">
        Agregar<i class="material-icons left">add_box</i>
      </a>
      <br />
      <table>
        <thead>
          <tr>
            <th>Patente</th>
            <th>Modelo</th>
            <th>Capacidad pasajeros</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="bus in buses" v-bind:key="bus.idBus">
            <td>{{bus.patente}}</td>
            <td>{{bus.modelo}}</td>
            <td>{{bus.capacidadPasajeros}}</td>
            <td>
              <a class="waves-effect waves-light btn ab-btn-edit tooltipped" v-on:click="getBus(bus.idBus)" data-tooltip="I am a tooltip">
                <i class="material-icons left ab-icon-action">edit</i>
              </a>
              <a class="waves-effect waves-light btn ab-btn-delete" v-on:click="borrar(bus.idBus)">
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
      <br/>
      <br/>
      <div class="row">
        <div class="col s12">
          <div class="row">
            <div class="input-field col s4">
              <input  id="patente" type="text" class="validate" v-model="bus.patente">
              <label for="patente" class="active">patente</label>
            </div>
            <div class="input-field col s4">
              <input  id="modelo" type="text" class="validate" v-model="bus.modelo">
              <label for="modelo" class="active">modelo</label>
            </div>
            <div class="input-field col s4">
              <input  id="capacidadPasajeros" type="number" class="validate" v-model="bus.capacidadPasajeros">
              <label for="capacidadPasajeros" class="active">cantidad pasajeros</label>
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
  name: 'buses',
  data: ()=>{
    return {
      title: 'buses',
      formulario: false,
      editar: false,
      buses: [],
      bus: {
        idBus: '',
        patente: '',
        modelo: '',
        capacidadPasajeros: 0
      }
    }
  },
  mounted(){
    this.formulario = false,
    this.editar = false,
    this.getBuses()
  },
  methods:{
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
    getBus: function(idBus){
      let ruta = `http://localhost:8000/apiBuses/buses/${idBus}`;
      axios.get(ruta)
      .then(res=>{

        this.bus.idBus = res.data.idBus;
        this.bus.patente = res.data.patente;
        this.bus.modelo = res.data.modelo;
        this.bus.capacidadPasajeros = res.data.capacidadPasajeros;        

        this.editar = true;
        this.formulario = true;
      })
      .catch(err=>{
        alert('Ocurrió un error');
        console.log('ERROR:', err);
      });
    },
    sendIngresar: function(){
      let ruta = 'http://localhost:8000/apiBuses/buses/';
      let {patente,modelo,capacidadPasajeros} = this.bus;
      let busSalida = {
        patente,
        modelo,
        capacidadPasajeros
      }
      let config = {
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json"
        }
      }
      axios.post(ruta,busSalida,config)
        .then(res=>{
          alert('Ingresado correctamente')
          this.formulario = false;
          this.editar = false;
          this.getBuses();
        })
        .catch(err=>{
          alert('Ocurrio error')
          console.log('ERROR: ',err);
        });
    },
    sendEdit: function(){
      let ruta = `http://localhost:8000/apiBuses/buses/${this.bus.idBus}/`;
      let {patente,modelo,capacidadPasajeros} = this.bus;
      let busSalida = {
        patente,
        modelo,
        capacidadPasajeros
      }
      let config = {
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json"
        }
      }
      axios.put(ruta,busSalida,config)
        .then(res=>{
          alert('Modificado correctamente')
          console.log(res.data);
          this.formulario = false;
          this.editar = false;
          this.getBuses();
        })
        .catch(err=>{
          alert('Ocurrio error')
          console.log('ERROR: ',err);
        });
    },
    sendBorrar: function(idBus){
      let ruta = `http://localhost:8000/apiBuses/buses/${idBus}/`;
      axios.delete(ruta)
      .then(res => {
        if (res.status == 204){
          alert('eliminado correctamente');
          this.getBuses();
        }
      })
      .catch(err=>{
        alert('Ocurrió un error');
        console.log('ERROR: ',err);
      });
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
      // resetar bus
      this.bus.idBus = 0;
      this.bus.patente = '';
      this.bus.modelo = '';
      this.bus.capacidadPasajeros = 0;
    },
    borrar: function(idBus){
      let borrar = confirm('¿Seguro que quiere borrar este registro?');
      if(borrar){
        this.sendBorrar(idBus);
      }
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
  }
  .ab-icon-action{
    margin-right: 0px;
  }
</style>
