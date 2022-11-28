<template>
    <div class="about">
      <h1>Todoterrenos</h1>
            <li><p>Código del todoterreno: <input v-model="newTodoterreno" type="text" placeholder="Código todoterreno" @keyup.enter="saveTodoterreno"></p></li>
                      
            <p>¿Está en ruta el todoterreno?:
            <select v-model="selected">
              <option disabled selected="">¿Está en ruta el todoterreno?</option>
              <option>Si</option>
              <option>No</option>
            </select> </p>
            
            <p>Número de visitantes:
            <select v-model="selected">
              <option disabled selected="">Número de visitantes</option>
              <option>1</option>
              <option>2</option>
              <option>3</option>
              <option>4</option>
              <option>5</option>
            </select> </p>

            <p>Sistema de seguridad:
            <select v-model="selected">
              <option disabled selected="">Sistema de seguridad</option>
              <option>Activado</option>
              <option>Desactivado</option>
            </select> </p>
            <br>
            <button @click="saveTodoterreno">Agregar nuevo todoterreno</button>
        </div>
</template>




	
<script>
import axios from "axios";
export default {
  data: () => ({
    result: null
  }),
  created() {
    axios.get("http://localhost:8000/todoterrenos").then((result) => {
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
