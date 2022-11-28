<template>
    <div class="about">
      <h1>Todoterrenos</h1>
        
            <li><input v-model="newLanguage" type="text" placeholder="Código todoterreno" @keyup.enter="saveRecinto"></li>
            <br>
            <li><input type="radio" id="true" value="Está en ruta" v-model="picked" @keyup.enter="saveRecinto"></li>
              <label for="true">Está en ruta</label>
            <li><input type="radio" id="false" value="No está en ruta" v-model="picked" @keyup.enter="saveRecinto"></li>
              <label for="false">No está en ruta</label>
            <br>
            <br>
            <li><input v-model="newLanguage" type="text" placeholder="Número de visitantes" @keyup.enter="saveRecinto"></li>
            <br>
            <li><input v-model="newLanguage" type="text" placeholder="Sistema de seguridad" @keyup.enter="saveRecinto"></li>
            <br>
      <button @click="saveRecinto">Agregar nuevo todoterreno</button>
    </div>
</template>




	
<script>
import axios from "axios";
import { vModelCheckbox } from "vue";
export default {
  data: () => ({
    result: null
  }),
  created() {
    axios.get("http://localhost:8000/todoterrenos").then((result) => {
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
