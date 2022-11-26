<template>
    <div class="about">
      <h1>Dinosaurio</h1>
      <div v-if="result" class="content">
        <p>Dinosaurio nombre: {{result.nombre}}</p>
      </div>
    </div>
</template>

<script>
import axios from "axios";
export default {
  created() {
    axios.get("https://localhost:8000").then((result) => {
      console.log(result.data);
    })
  }
};
</script>
