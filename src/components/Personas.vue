<template>
  <div>
    <h3>Mantenedor {{title}}</h3>
    <br/>
    <div v-if="!formulario">
      <a class="waves-effect waves-light btn" v-on:click="openForm">
        Agregar<i class="material-icons left">add_box</i>
      </a>
      <br/>
      <table>
        <thead>
          <tr>
            <th>Identificador país</th>
            <th>Nombres</th>
            <th>Apellidos</th>
            <th>Tipo de usuario</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="persona in personas" v-bind:key="persona.idPersona">
            <td>{{persona.identificacionPais}}</td>
            <td>{{persona.nombrePrimario+' '+persona.nombreSecundario}}</td>
            <td>{{persona.apPaterno+' '+persona.apMaterno}}</td>
            <td>{{persona.tipoUsuarioDescripcion}}</td>
            <td>
              <a class="waves-effect waves-light btn ab-btn-edit tooltipped" v-on:click="getPersona(persona.idPersona)" data-tooltip="I am a tooltip">
                <i class="material-icons left ab-icon-action">edit</i>
              </a>
              <a class="waves-effect waves-light btn ab-btn-delete" v-on:click="borrar(persona.idPersona)">
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
              <input  id="idPais" type="text" class="validate" v-model="persona.identificacionPais">
              <label for="idPais" class="active">id País</label>
            </div>
            <div class="input-field col s4">
              <input  id="nombrePrimario" type="text" class="validate" v-model="persona.nombrePrimario">
              <label for="nombrePrimario" class="active">Primer nombre</label>
            </div>
            <div class="input-field col s4">
              <input  id="nombreSecundario" type="text" class="validate" v-model="persona.nombreSecundario">
              <label for="nombreSecundario" class="active">Segundo nombre</label>
            </div>
          </div>
          <div class="row">
            <div class="input-field col s4">
              <input  id="apPaterno" type="text" class="validate" v-model="persona.apPaterno">
              <label for="apPaterno" class="active">Apellido paterno</label>
            </div>
            <div class="input-field col s4">
              <input  id="apMaterno" type="text" class="validate" v-model="persona.apMaterno">
              <label for="apMaterno" class="active">Apellido materno</label>
            </div>
            <div class="input-field col s4">
              <select v-model="persona.tipoUsuario" class="browser-default">
                <option value="0" disabled selected>Selecciona tipo de usuario</option>
                <option v-for="tipo in tipoPersonas" 
                  v-bind:value="tipo.idTipoPersona"
                  v-bind:key="tipo.idPersona"
                >
                  {{tipo.descripcion}}
                </option>
              </select>
              
              <label for="tipoUsuario" class="active">Tipo Usuario</label>
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
  name: 'personas',
  data: ()=>{
    return {
      title: 'personas',
      personas: [],
      tipoPersonas: [],
      formulario: false,
      editar: false,
      persona: {
        idPersona: 0,
        identificacionPais: '',
        nombrePrimario: '',
        nombreSecundario: '',
        apPaterno: '',
        apMaterno: '',
        tipoUsuario: 2
      }
    }
  },
  mounted(){
    this.formulario = false
    this.getPersonas();
    this.getTipoUsuarios();
  },
  methods:{
    getPersonas: function(){
      let ruta='http://localhost:8000/apiBuses/personas/'
      axios.get(ruta)
      .then(res=>{
        this.personas = res.data;
      })
      .catch(err=>{
        console.log('ERROR: ',err)
      })
    },
    getTipoUsuarios: function(){
      let ruta='http://localhost:8000/apiBuses/tipoPersonas'
      axios.get(ruta)
      .then(res=>{
        this.tipoPersonas = res.data;
      })
      .catch(err=>{
        alert('Ocurrió un error durante la carga de tipos');
        console.log(err);
      })
    },
    getPersona: function(idPersona){
      let ruta='http://localhost:8000/apiBuses/personas/'+idPersona
      axios.get(ruta)
        .then(res=>{
          this.persona.idPersona = res.data.idPersona,
          this.persona.identificacionPais = res.data.identificacionPais,
          this.persona.nombrePrimario = res.data.nombrePrimario,
          this.persona.nombreSecundario = res.data.nombreSecundario,
          this.persona.apPaterno = res.data.apPaterno,
          this.persona.apMaterno = res.data.apMaterno,
          this.persona.tipoUsuario = res.data.tipoUsuario
          this.editar = true;
          this.formulario = true;
        })
        .catch(err=>{
          alert('ERROR al obtener persona');
          console.log('ERROR:',err)
        })
    },
    sendIngresar: function(){
      let ruta = 'http://localhost:8000/apiBuses/personas/';
      //datos de persona de salida
      let {identificacionPais,nombrePrimario,nombreSecundario,apPaterno,apMaterno,tipoUsuario} = this.persona;
      let personaSalida = {
        identificacionPais,
        nombrePrimario,
        nombreSecundario,
        apPaterno,
        apMaterno,
        tipoUsuario
      };
      let config = {
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json"
        }
      }
      axios.post(ruta,personaSalida,config)
        .then(res=>{
          alert('Ingresado correctamente')
          console.log(res.data);
          this.formulario = false;
          this.editar = false;
          this.getPersonas();
        })
        .catch(err=>{
          alert('Ocurrio error')
          console.log('ERROR: ',err);
        });
    },
    sendEdit: function(){
      let ruta = 'http://localhost:8000/apiBuses/personas/'+this.persona.idPersona+'/';
      //datos de persona de salida
      let {identificacionPais,nombrePrimario,nombreSecundario,apPaterno,apMaterno,tipoUsuario} = this.persona;
      let personaSalida = {
        identificacionPais,
        nombrePrimario,
        nombreSecundario,
        apPaterno,
        apMaterno,
        tipoUsuario
      };
      let config = {
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json"
        }
      }
      axios.put(ruta,personaSalida,config)
        .then(res=>{
          alert('modificado correctamente')
          console.log(res.data);
          this.formulario = false;
          this.editar = false;
          this.getPersonas();
        })
        .catch(err=>{
          alert('Ocurrio error')
          console.log('ERROR: ',err);
        });
    },
    sendBorrar: function(idPersona){
      let ruta = `http://localhost:8000/apiBuses/personas/${idPersona}/`;
       axios.delete(ruta)
        .then(res => {
          if (res.status == 204){
            alert('eliminado correctamente');
            this.getPersonas();
          }
        })
        .catch(err=>{
          alert('Ocurrió un error');
          console.log('ERROR: ',err);
        });
    },
    openForm: function(){
      this.formulario = true;
      this.persona.idPersona = 0;
      this.persona.identificacionPais ='';
      this.persona.nombrePrimario = '';
      this.persona.nombreSecundario = '';
      this.persona.apPaterno = '';
      this.persona.apMaterno = '';
      this.persona.tipoUsuario = 0;
    },
    enviar: function(){
      if(this.editar){
        this.sendEdit()
      }else{
        this.sendIngresar()
      }
    },
    borrar: function(idPersona){
      let borrar = confirm('¿Seguro que quiere borrar esta persona?');
      if(borrar){
        this.sendBorrar(idPersona);
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