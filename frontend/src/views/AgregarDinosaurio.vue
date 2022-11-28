<template>
    <div class="about">
      <h1>Dinosaurio</h1>
        
            <li><input v-model="newLanguage" type="text" placeholder="Nombre dinosaurio" @keyup.enter="saveDinosaurio"></li>
            <br>
            <li><input v-model="newLanguage" type="text" placeholder="Especie dinosaurio" @keyup.enter="saveDinosaurio"></li>
            <br>
            <li><input v-model="newLanguage" type="text" placeholder="Edad dinosaurio" @keyup.enter="saveDinosaurio"></li>
            <br>
            <li><input v-model="newLanguage" type="text" placeholder="Peso dinosaurio" @keyup.enter="saveDinosaurio"></li>
            <br>
            <li><input v-model="newLanguage" type="text" placeholder="Sexo dinosaurio" @keyup.enter="saveDinosaurio"></li>
            <br>
            <li><input v-model="newLanguage" type="text" placeholder="Peligrosidad dinosaurio" @keyup.enter="saveDinosaurio"></li>
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
  },
methods:{
		saveDinosaurio: function(event){
			this.languages.push(this.newLanguage);
			this.newLanguage = ""
		}
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
