<template>
    <div class="about">
      <h1>Todoterrenos</h1>
      <h2>¿Desea añadir un nuevo todoterreno?</h2>
      <router-link to="/agregarTodoterreno"><button @click="saveDinosaurio">Agregar nuevo todoterreno</button></router-link> 
      <h2>Todoterrenos disponibles en el parque:</h2>
      <div v-for="todoterreno in result" class="content">
        <p>Todoterreno: {{todoterreno.codigo}} </p>
        <p> Sistema de seguridad: {{todoterreno.sis_seg}}</p>
          <button v-on:click="deleteTodoterrenos(todoterreno.codigo)">Eliminar</button> 
      </div>

    </div>
</template>


<script>
import axios from "axios";
export default {
  data: () => ({
    result: []
  }),
  created() {
    this.getTodoterrenos()
  },
  methods: {
    getTodoterrenos: function () {
      axios.get("http://localhost:8000/todoterrenos").then((result) => {
        this.result = result.data;
      }
      )
    },
    deleteTodoterrenos: function (codigo) {
      console.log("Dentro de delete")
      axios.delete("http://localhost:8000/todoterreno/" + codigo)
        .then(response => {
          console.log("Deleted todoterrenos " + codigo, response);
          this.getTodoterrenos()
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
};
</script>

<style>

button{
  color:darkred
}
h2{
  font-size: medium;
  margin-top: 3%;
}

</style>

      