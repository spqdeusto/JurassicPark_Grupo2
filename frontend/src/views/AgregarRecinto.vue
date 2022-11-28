<template>
    <div class="about">
      <h1>Recintos</h1>
        <p>Nombre del recinto:
            <select v-model="selected">
              <option disabled selected="">Nombre del recinto</option>
              <option>Recinto del Dilophosaurus</option>
              <option>Recinto del T-Rex</option>
              <option>Recinto del Velociraptor</option>
              <option>Recinto del Brachiosaurus</option>
              <option>Recinto del Parasaulophus</option>
              <option>Recinto del Triceratops</option>
            </select></p>
           
            <p>Sistema electrico:
            <select v-model="selected">
              <option disabled selected="">Sistema eléctrico</option>
              <option>Verdadero-Electricidad activada</option>
              <option>Falso-Electricidad desactivada</option>
            </select> </p>
            <br>
      <button @click="saveRecinto">Agregar nuevo recinto</button>
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

li{
    list-style: none;
}

</style>
