<template>
    <div class="about">
      <h1>Todoterreno</h1>
      <router-link to="/agregarTodoterreno"><button @click="saveRecinto">Agregar nuevo todoterreno</button></router-link> 
      
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
  }
};
</script>

<style>

button{
  color:darkred
}

</style>

      