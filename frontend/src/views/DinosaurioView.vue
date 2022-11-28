<template>
    <div class="about">
      <h1>Dinosaurio</h1>
      <router-link to="/agregarDinosaurio"><button @click="saveDinosaurio">Agregar nuevo dinosaurio</button></router-link> 
      
      <div v-for="dinosaurio in result" class="content">
        <p>Dinosaurio: {{dinosaurio.nombre}}</p>
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
    axios.get("http://localhost:8000/dinosaurios").then((result) => {
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
