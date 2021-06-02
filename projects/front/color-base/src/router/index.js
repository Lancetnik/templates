import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@/store'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    component: () => import('../views/Login.vue'),
    redirect: {name: 'SignIn'},
    children: [
        {
          path: 'sign-in',
          name: 'SignIn',
          component: () => import('../components/login/sign-in.vue'),
        },
        {
          path: 'sign-up/',
          name: 'SignUp',
          component: () => import('../components/login/sign-up.vue'),
        }
    ]
  },
  {
    path: '/main',
    component: () => import('../views/Main.vue'),
    redirect: {name: 'page1'},
    name: 'main',
    children: [
      {
        path: '/page1',
        component: () => import('../views/Main/Page1.vue'),
        name: 'page1',
        meta: { theme: '#55884F' }
      },
      {
        path: '/page2',
        component: () => import('../views/Main/Page2.vue'),
        name: 'page2',
        meta: { theme: '#544F88' }
      },  
      {
        path: '/page3',
        component: () => import('../views/Main/Page3.vue'),
        name: 'page3',
        meta: { theme: '#37889A' }
      },  
      {
        path: '/page4',
        component: () => import('../views/Main/Page4.vue'),
        name: 'page4',
        meta: { theme: '#374D9A' }
      }  
    ]
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  linkActiveClass: 'common-is-active',
  routes
})

export default router
