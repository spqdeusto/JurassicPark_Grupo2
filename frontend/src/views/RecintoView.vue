<template>
    <div class="about">
      <h1>Recinto</h1>
           
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
  }
};
</script>

<style>

button{
  color:darkred
}

</style>

      