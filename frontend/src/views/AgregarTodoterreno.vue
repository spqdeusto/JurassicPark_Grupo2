<template>
    <div class="about">
      <h1>Todoterrenos</h1>
      <form v-on:submit.prevent="submitForm">
            <li><p>Código del todoterreno: <input v-model="form.codigo" type="text" placeholder="Código todoterreno"></p></li>
                      
            <p>¿Está en ruta el todoterreno?:
            <select v-model="form.ruta">
              <option disabled selected="">¿Está en ruta el todoterreno?</option>
              <option value="true">Si</option>
              <option value="false">No</option>
            </select> </p>
            
            <p>Número de visitantes:
            <select v-model="form.pasajeros">
              <option disabled selected="">Número de visitantes</option>
              <option value=1>1</option>
              <option value=2>2</option>
              <option value=3>3</option>
              <option value=4>4</option>
              <option value=5>5</option>
            </select> </p>

            <p>Sistema de seguridad:
            <select v-model="form.sis_seg">
              <option disabled selected="">Sistema de seguridad</option>
              <option value="true">Activado</option>
              <option value="false">Desactivado</option>
            </select> </p>
            <p>Recinto del todoterreno:
              <select v-model="form.recinto">
              <option disabled selected="">Recinto</option>
              <option value=1>Recinto del Dilophosaurus</option>
              <option value=2>Recinto del T-Rex</option>
              <option value=3>Recinto de los Velociraptores</option>
              <option value=4>Recinto de Brachiosaurus y de Parasaulophus</option>
              <option value=5>Recinto de Galliminus</option>
              <option value=6>Recinto de Triceraptops</option>
            </select> </p>
            <div class="form-group">
              <button class="btn btn-primary">Submit</button>
            </div>
          </form>
        </div>
</template>


<script>
import axios from "axios";
export default {
  data() {
    return {
      form: {
        codigo: 0,
        ruta: false,
        pasajeros: 0,
        sis_seg: false,
        recinto:0
      }
    }
  },
  methods: {
    submitForm() {
      axios.post("http://localhost:8000/todoterreno/create", this.form
      ).then(response => {
        this.success = "Data saved successfully";
        this.response = JSON.stringify(response, null, 2);
      }).catch(error => {
        this.response = "Error: " + error.response.status
      })
    },
  }
}
</script>

<style>
button {
  color: darkred
}

li {
  list-style: none;
}
</style>

