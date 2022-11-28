<template>
    <div class="about">
      <h1>Dinosaurio</h1>
            <li><p>Nombre del dinosaurio: <input v-model="newDino" type="text" placeholder="Nombre dinosaurio" @keyup.enter="saveDinosaurio"></p></li>
            <li><p>Edad del dinosaurio: <input v-model="newDino" type="text" placeholder="Edad dinosaurio" @keyup.enter="saveDinosaurio"></p></li>
            <li><p>Peso del dinosaurio:<input v-model="newDino" type="text" placeholder="Peso dinosaurio" @keyup.enter="saveDinosaurio"></p></li>
            <p>Especie del dinosaurio:
            <select v-model="selected">
              <option disabled selected="">Especie del dinosaurio</option>
              <option>Dilophosaurus</option>
              <option>T-Rex</option>
              <option>Velociraptor</option>
              <option>Brachiosaurus</option>
              <option>Parasaulophus</option>
              <option>Triceratops</option>
            </select></p>
            <p>Sexo del dinosaurio:
            <select v-model="selected">
              <option disabled selected="">Sexo del dinosaurio</option>
              <option>Macho</option>
              <option>Hembra</option>
            </select></p>
            <p>Peligrosidad del dinosaurio:
            <select v-model="selected">
              <option disabled selected="">Peligrosidad del dinosaurio</option>
              <option>Pacífico</option>
              <option>Agresivo</option>
            </select></p>
            <br>
      <button @click="saveDinosaurio">Agregar nuevo dinosaurio</button>
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

li{
    list-style: none;
}

</style>
