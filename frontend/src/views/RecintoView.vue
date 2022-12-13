<template>
  <div class="about">
    <h1>Recintos</h1>
    <h2>Recintos disponibles en el parque:</h2>
    <div v-for="recinto in result" class="content">
      <p>Recinto: {{ recinto.nombre }}</p>
      <p>Sistema eléctrico: {{ recinto.sis_elec }}</p>
      <button v-on:click="change_sis(recinto.codigo)">Cambiar sistema</button>

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
    this.get_recintos()
  },
  methods: {
    get_recintos: function () {
      axios.get("http://localhost:8000/recintos").then((result) => {
        this.result = result.data;
      })
    },
    change_sis: function (codigo) {
      axios.get("http://localhost:8000/changeelectricidad/" + codigo).then((result) => {
        this.get_recintos()
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

      