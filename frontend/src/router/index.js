import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import DisponibilidadeView from '../views/DisponibilidadeView.vue'
import DisponibilidadeExcecaoView from '../views/ExcecaoView.vue'
import EditDisponibilidadeView from '../views/EditDisponibilidadeView.vue'
import EditExcecaoView from '../views/EditExcecaoView.vue'
import EntregaView from '../views/EntregaView.vue'

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
    },
    {
      path: '/disponibilidadeExcecao',
      name: 'disponibilidadeExcecao',
      component: DisponibilidadeExcecaoView
    },
    {
      path: '/edit-dispon-excecao/',
      name: 'EditDisponExcecao',
      component: EditExcecaoView,
    },
    {
      path: '/entrega',
      name: 'Entrega',
      component: EntregaView,
    }

  ]
})

export default router
