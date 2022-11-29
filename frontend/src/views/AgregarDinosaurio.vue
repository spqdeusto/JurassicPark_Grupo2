<template>
    <div class="about">
      <h1>Dinosaurio</h1>
      <form v-on:submit.prevent="submitForm">
            <li><p>Nombre del dinosaurio: <input v-model="nombre" type="text" placeholder="Nombre dinosaurio"></p></li>
            <li><p>Edad del dinosaurio: <input v-model="edad" type="text" placeholder="Edad dinosaurio"></p></li>
            <li><p>Peso del dinosaurio:<input v-model="peso" type="text" placeholder="Peso dinosaurio"></p></li>
            <p>Especie del dinosaurio:
            <select v-model="especie">
              <option disabled selected="">Especie del dinosaurio</option>
              <option value=1>Dilophosaurus</option>
              <option value=2>T-Rex</option>
              <option value=3>Velociraptor</option>
              <option value=4>Brachiosaurus</option>
              <option value=5>Parasaulophus</option>
              <option value=6>Galliminus</option>
              <option value=7>Triceratops</option>
            </select></p>
            <p>Sexo del dinosaurio:
            <select v-model="sexo">
              <option disabled selected="">Sexo del dinosaurio</option>
              <option value="M">Macho</option>
              <option value="H">Hembra</option>
            </select></p>
            <p>Peligrosidad del dinosaurio:
            <select v-model="es_agresivo">
              <option disabled selected="">Peligrosidad del dinosaurio</option>
              <option value="false">Pacífico</option>
              <option value="true">Agresivo</option>
            </select></p>
            <br>
            <div class="form-group">
              <button class="btn btn-primary">Submit</button>
            </div>
          </form>
 </div>
</template>




	
<script>
import axios from "axios";
export default {
  data () {
    return {
      nombre: "",
      edad: "",
      peso: "",
      especie: "",
      sexo: "",
      es_agresivo: ""
    }
  },
  methods:{
    submitForm(){
    
      axios.post("http://localhost:8000/dinosaurio/create",{
        nombre: this.nombre,
        edad: this.edad,
        peso: this.peso,
        especie: this.especie,
        sexo: this.sexo,
        es_agresivo: this.es_agresivo

      }).then(response =>{
        this.success="Data saved successfully";
        this.response=JSON.stringify(response, null, 2);
      }).catch(error=> {
        this.response="Error: " + error.response.status
      })
      this.nombre="";
      this.edad="";
      this.peso="";
    }
  },

  created() {
    axios.get("http://localhost:8000/dinosaurios").then((result) => {
      this.result = result.data;
    })
  }
}
</script>

<style>

button{
  color:darkred
}

li{
    list-style: none;
}

</style>
