import { createRouter, createWebHistory } from 'vue-router'


const routes = [
  {
    path: '/',
    name: 'inicio',
    component: () => import(/* webpackChunkName: "about" */ '../views/InicioView.vue')
  },
  {
    path: '/dinosaurios',
    name: 'dinosaurios',
    component: () => import(/* webpackChunkName: "about" */ '../views/DinosaurioView.vue')
  },
  {
    path: '/recintos',
    name: 'recintos',
    component: () => import(/* webpackChunkName: "about" */ '../views/RecintoView.vue')
  },
  {
    path: '/todoterrenos',
    name: 'todoterrenos',
    component: () => import(/* webpackChunkName: "about" */ '../views/TodoterrenoView.vue')
  },
  {
    path: '/agregarDinosaurio',
    name: 'agregarDinosaurio',
    component: () => import(/* webpackChunkName: "about" */ '../views/AgregarDinosaurio.vue')
  },
  {
    path: '/agregarTodoterreno',
    name: 'agregarTodoterreno',
    component: () => import(/* webpackChunkName: "about" */ '../views/AgregarTodoterreno.vue')
  },

 
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
