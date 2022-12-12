<template>
    <div class="about">
      <h1>Recintos</h1>
      <h2>Recintos disponibles en el parque:</h2>     
      <div v-for="recinto in result" class="content">
        <p>{{recinto.nombre}}</p>
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
    axios.get("http://localhost:8000/recintos").then((result) => {
      this.result = result.data;
    })
  },
  delete() {
    axios.delete("http://localhost:8000/recintos")
  }
};
</script>

<style>

button{
  color:darkred
}

</style>

      