import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    }
  ]
})


router.beforeEach((to, from) => {
  console.log('to',to)
  console.log('from',from)
  if(!import.meta.env.DEV){

  }
})


export default router
