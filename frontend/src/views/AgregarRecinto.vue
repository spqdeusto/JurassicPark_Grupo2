<template>
    <div class="about">
      <h1>Recintos</h1>
        
            <li><input v-model="newLanguage" type="text" placeholder="Nombre recinto" @keyup.enter="saveRecinto"></li>
            <br>
            <li><input v-model="newLanguage" type="text" placeholder="Estado sist.eléctrico" @keyup.enter="saveRecinto"></li>
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
