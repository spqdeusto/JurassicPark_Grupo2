<template>
    <div class="about">
      <h1>Dinosaurios</h1>
      <h2>¿Desea añadir un nuevo dinosaurio?</h2>
      <router-link to="/agregarDinosaurio"><button @click="saveDinosaurio">Agregar nuevo dinosaurio</button></router-link> 
      <h2>Dinosaurios disponibles en el parque:</h2>
      <div v-for="dinosaurio in result" class="content">
        <p>Dinosaurio: {{dinosaurio.nombre}}</p>
          <button onClick = delete>Eliminar</button> | <router-link to="/modificarDinosaurio"><button @click="modifyDinosaurio">Modificar</button></router-link>
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
  },
  delete(){
    axios.delete("http://localhost:8000/dinosaurio/{nombre}")
    .then(response => {
      console.log("deleted", response);
      setData(response.data);
    })
    .catch(error =>{
      console.log(error)
    })
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
