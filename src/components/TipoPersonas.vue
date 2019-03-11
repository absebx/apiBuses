<template>
  <div>
    <h3>Mantenedor {{title}}</h3>
    <!-- lista de tipos -->
    <div v-if="!formulario">
      <a class="waves-effect waves-light btn" v-on:click="openForm">
        Agregar<i class="material-icons left">add_box</i>
      </a>
      <br />
      <table>
        <thead>
          <tr>
            <th>Descripocion</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="tipo in tipos" v-bind:key="tipo.idTipoPersona">
            <td>{{tipo.descripcion}}</td>
            <td>
              <a class="waves-effect waves-light btn ab-btn-edit tooltipped" v-on:click="getTipo(tipo.idTipoPersona)">
                <i class="material-icons left ab-icon-action">edit</i>
              </a>
              <a class="waves-effect waves-light btn ab-btn-delete" v-on:click="borrar(tipo.idTipoPersona)">
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
              <input  id="patente" type="text" class="validate" v-model="tipo.descripcion">
              <label for="patente" class="active">descripcion</label>
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
  name: 'tipoPersonas',
  data: ()=>{
    return{
      title: 'tipo personas',
      formulario: false,
      editar: false,
      tipos: [],
      tipo: {
        idTipoPersona: 0,
        descripcion: ''
      }
    }
  },
  mounted(){
    this.formulario = false,
    this.editar = false,
    this.getTipos()
  },
  methods:{
    getTipos: function(){
      let ruta = 'http://127.0.0.1:8000/apiBuses/tipoPersonas';
      axios.get(ruta)
      .then(res => {
        this.tipos = res.data;
      })
      .catch(err=>{
        console.log('ERROR:', err);
        alert('Error al cargar tipos');
      })
    },
    getTipo: function(idTipoPersona){
      let ruta = `http://127.0.0.1:8000/apiBuses/tipoPersonas/${idTipoPersona}`;
      axios.get(ruta)
      .then(res=>{

        this.tipo.idTipoPersona = res.data.idTipoPersona;
        this.tipo.descripcion = res.data.descripcion;
        this.editar = true;
        this.formulario = true;
      })
      .catch(err=>{
        alert('Ocurrió un error');
        console.log('ERROR:', err);
      });
    },
    sendIngresar: function(){
      let ruta = 'http://127.0.0.1:8000/apiBuses/tipoPersonas/';
      let descripcion = this.tipo.descripcion;
      let tipoPersonaSalida = {
        descripcion
      };
      let config = {
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json"
        }
      }
      axios.post(ruta,tipoPersonaSalida,config)
      .then(res=>{
        alert('Ingresado correctamente')
        this.formulario = false;
        this.editar = false;
        this.getTipos();
      })
      .catch(err=>{
        console.log('ERROR: ',err);
        alert('Error al ingresar tipoPerona')
      });
    },
    sendEdit: function(){
      let ruta = `http://127.0.0.1:8000/apiBuses/tipoPersonas/${this.tipo.idTipoPersona}/`;
      let descripcion = this.tipo.descripcion;
      let tipoPersonaSalida = {
        descripcion
      };
      let config = {
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json"
        }
      };

      axios.put(ruta,tipoPersonaSalida,config)
      .then(res=>{
        alert('Modificado correctamente')
        this.formulario = false;
        this.editar = false;
        this.getTipos();
      })
      .catch(err=>{
        alert('Ocurrio error')
        console.log('ERROR: ',err);
      });
    },
    sendBorrar: function(idTipoPersona){
      let ruta = `http://127.0.0.1:8000/apiBuses/tipoPersonas/${idTipoPersona}/`;
      axios.delete(ruta)
      .then(res => {
        if (res.status == 204){
          alert('eliminado correctamente');
          this.getTipos();
        }
      })
      .catch(err=>{
        console.log('ERROR: ',err);
        alert('Error al eliminar tipo persona');
      });
    },
    enviar: function(){
      if(this.editar){
        this.sendEdit()
      }else{
        this.sendIngresar();
      }
    },
    openForm: function(){
      this.formulario = true;
      // resetear campos
      this.tipo.idTipoPersona = 0;
      this.tipo.descripcion = ''; 
    },
    borrar: function(idTipoPersona){
      let borrar = confirm('¿Seguro que quiere borrar este registro?');
      if(borrar){
        this.sendBorrar(idTipoPersona);
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
