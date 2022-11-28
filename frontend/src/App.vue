<template>
  <img src="@/assets/logo.png" alt="" />
  <nav>
    <router-link to="/">Inicio</router-link> |
    <router-link to="/dinosaurios">Dinosaurios</router-link> |
    <router-link to="/recintos">Recintos</router-link> |
    <router-link to="/todoterrenos">Todoterrenos</router-link> 
  </nav>
  <router-view/>
<div class="footer">
  <h1>&copy;  Grupo 2: Proceso de software y calidad </h1>
</div>
</template>





<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 300vh;
}

img{
  width: 20%;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: darkred;
}

.footer{
      
      background:darkred;
      text-align: center;
      color: white;
      position: fixed;
      left:0;
      bottom: 0;
      width: 100%;
      font-size: 60%;
}
</style>
