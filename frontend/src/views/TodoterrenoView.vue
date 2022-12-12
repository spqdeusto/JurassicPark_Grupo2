<template>
    <div class="about">
      <h1>Todoterrenos</h1>
      <h2>¿Desea añadir un nuevo todoterreno?</h2>
      <router-link to="/agregarTodoterreno"><button @click="saveDinosaurio">Agregar nuevo todoterreno</button></router-link> 
      <h2>Todoterrenos disponibles en el parque:</h2>
      <div v-for="todoterreno in result" class="content">
        <p>Todoterreno: {{todoterreno.codigo}}</p>
          <button>Eliminar</button> | <button>Modificar</button>
          <li v-for="l in languages">
          {{ l }}
          </li>
      </div>

    </div>
</template>


<script>
import axios from "axios";
export default {
  data: () => ({
    result: null
  }),
  created() {
    axios.get("http://localhost:8000/todoterrenos").then((result) => {
      this.result = result.data;
    })
  },
  delete() {
    axios.delete("http://localhost:8000/todoterrenos")
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

      