<template>
  <header :class="{ 'scrolled-nav': scrolledNav }">
    <nav>
        <ul class="navigationVue">
            <li><router-link class="link" :to="{name:''}">Inicio</router-link></li>
            <li><router-link class="link" :to="{name:''}">Dinosaurios</router-link></li>
            <li><router-link class="link" :to="{name:''}">Todoterrenos</router-link></li>
            <li><router-link class="link" :to="{name:''}">Recintos</router-link></li>
        </ul>
    </nav>
  </header>
</template>

<script>
    export default {
        name:"navigationVue",
        data(){
            return {
                scrolledNav: null,
                mobile: null,
                mobileNav: null,
                windowWidth: null,
            };  
        },
        created(){
            window.addEventListener("resize", this.checkScreen);
            this.checkScreen();
        },
        
        mounted(){
            window.addEventListener('scroll', this.updateScroll);
        },

        methods:{
            checkScreen(){
                this.windowWidth = window.innerWidth;
                
            }
        }
    };
</script>

<style lang="scss" scoped>
    header{
        background: rgb(255, 255, 255);
        z-index: 100%;
        width: 100%;
        position: fixed;  
        transition: 0.5s ease all;
        color:rgb(0, 0, 0);
        width: 100%;

        nav{
            border: darkred 2px double;
            display: auto;
            position: fixed;
            flex-direction: row;
            transition: 0.5s ease all;
            width:100%;
            margin:0 auto;
            left: 0;
            right: 0;
            @media(min-width: 100%){
                max-width:100%;
            }
            ul,
            .link{
                font-weight: 500;
                color: rgb(0, 0, 0);
                list-style: none;
                text-decoration: none;
            }
            li{
                text-transform: uppercase;
                padding:16px;
                margin-left: 16px;
            }
            .link{
                font-size: 14px;
                transition: 0.5s ease all;
                padding-bottom: 4px;
                border-bottom: 1px solid transparent;

                &:hover{
                    color:darkgreen;
                    border-color: darkgreen;
                }
            }
            .menu{
                display: flex;
                align-items: center;
            }

           
            .navigationVue{
                display: flex;
                align-items: center;
                flex: 20;
                justify-content: flex-end;
                position: center;
                
                
            }   
        }
    }
</style>