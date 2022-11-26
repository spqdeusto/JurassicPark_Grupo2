<template>
    <div class="about">
      <h1>Dinosaurio</h1>
      <div v-for="dinosaurio in result" class="content">
        <p>Dinosaurio nombre: {{dinosaurio.nombre}}</p>
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
