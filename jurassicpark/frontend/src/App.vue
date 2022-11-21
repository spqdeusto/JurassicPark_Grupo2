<template>
  <div classs="body">
    <section class="head">
      <HeaderVue/>
      <div>
        <MenuVue/>
      </div>
    <section class="content">

    </section>
    <section class="foot">
      <FooterVue/>
    </section>
    </section>
  </div>
</template>

<script>
import HeaderVue from "./components/HeaderVue.vue"
import MenuVue from "./components/MenuVue.vue"
import FooterVue from "./components/FooterVue.vue"


export default {
  name: "App",
  components: {
    HeaderVue,
    MenuVue,
    FooterVue
  }
}


</script>

<style scoped lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Raleway:wght@400;500&display=swap");

*{
  margin:0;
  padding:0;
  box-sizing: border-box;
  font-family: Arial, Helvetica, sans-serif;
  font-weight: 400;

}

.body{
  display:flex;
  flex-direction:column;
  min-height: 100vh;
  max-width: 100%;
  margin: 0 auto;
  top: 0;
  left: 0;
  right: 0;
}

.head{
  flex-grow: 1;
}

.foot{
  flex-grow: 1;
  

}

</style>
