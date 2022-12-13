<template>
  <div class="about">
    <h1>Dinosaurios</h1>
    <h2>¿Desea añadir un nuevo dinosaurio?</h2>
    <router-link to="/agregarDinosaurio"><button @click="saveDinosaurio">Agregar nuevo dinosaurio</button></router-link>
    <h2>Dinosaurios disponibles en el parque:</h2>
    <div v-for="dinosaurio in result" class="content">
      <p>Dinosaurio: {{ dinosaurio.nombre }}</p>
      <button v-on:click="deleteDinosaurio(dinosaurio.nombre)">Eliminar</button>

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
    this.getDinosaurios()
  },
  methods: {
    getDinosaurios: function () {
      axios.get("http://localhost:8000/dinosaurios").then((result) => {
        this.result = result.data;
      }
      )
    },
    deleteDinosaurio: function (nombre) {
      console.log("Dentro de delete")
      axios.delete("http://localhost:8000/dinosaurio/" + nombre)
        .then(response => {
          console.log("Deleted dinosario " + nombre, response);
          this.getDinosaurios()
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
};
</script>

<style>
button {
  color: darkred
}

h2 {
  font-size: medium;
  margin-top: 3%;
}
</style>
