import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import OtherView from '../views/OtherView.vue'
import DisponibilidadeView from '../views/DisponibilidadeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/other',
      name: 'other',
      component: OtherView
    },
    {
      path: '/disponibilidade',
      name: 'disponibilidade',
      component: DisponibilidadeView
    },
  ]
})

export default router
