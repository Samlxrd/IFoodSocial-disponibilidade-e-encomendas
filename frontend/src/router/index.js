import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import DisponibilidadeView from '../views/DisponibilidadeView.vue'
import EditDisponibilidadeView from '../views/EditDisponibilidadeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/disponibilidade',
      name: 'disponibilidade',
      component: DisponibilidadeView
    },
    {
      path: '/edit-disponibilidade/',
      name: 'EditDisponibilidade',
      component: EditDisponibilidadeView,
      props: true
    }
  ]
})

export default router
