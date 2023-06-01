import Vue from 'vue'
import VueRouter from 'vue-router'

import HomeView from '@/views/movies/HomeView.vue'
import DetailView from '@/views/movies/DetailView.vue'
import RecommendView from '@/views/movies/RecommendView.vue'
import ErrorView from '@/views/errors/ErrorView.vue'

import MoreView from '@/views/communitys/MoreView.vue'
import MyreView from '@/views/communitys/MyreView.vue'

import LoginView from '@/views/accounts/LoginView.vue'
import ProfileView from '@/views/accounts/ProfileView.vue'
import SignupView from '@/views/accounts/SignupView.vue'

Vue.use(VueRouter)



const routes = [
  {
    path: '/',
    name:'login',
    component: LoginView,
    beforeEnter: (to, from, next) => {
      if(!localStorage.getItem('encryptedToken')){
        next()
      }else{
        localStorage.removeItem('encryptedToken')
        localStorage.removeItem('encryptedUsername')
        localStorage.removeItem('encryptedId')
        location.reload()
      }
    }
    
  },
  // movies

  {
    path: '/home',
    name: 'home',
    component: HomeView,
    beforeEnter: (to, from, next) => {
      if(localStorage.getItem('encryptedToken')){
        next()
      } else {
        next('/')
      }
    },
    beforeRouteUpdate(to, from, next) {
      if (from !== to) {
        next()
      } else {
        location.reload()
      }
    }
  },
  {
    path: '/detail/:id',
    name: 'detail',
    component: DetailView,
    beforeEnter: (to, from, next) => {
      if(localStorage.getItem('encryptedToken')){
        next()
      } else {
        next('/')
      }
    },
    beforeRouteUpdate(to, from, next) {
      if (from.params.id !== to.params.id) {
        next()
      } else {
        next(false)
      }
    }
  },
  {
    path:'/recommend',
    name:'recommend',
    component: RecommendView,
    beforeEnter: (to, from, next) => {
      if(localStorage.getItem('encryptedToken')){
        next()
      } else {
        next('/')
      }
    },

  },

  // errors
  {
    path: '/error',
    name: 'error',
    component: ErrorView
  },

  // communitys
  {
    path: '/moreview/:id',
    name: 'moreview',
    component: MoreView,
    beforeEnter: (to, from, next) => {
      if(localStorage.getItem('encryptedToken')){
        next()
      } else {
        next('/')
      }
    },
    beforeRouteUpdate(to, from, next) {
      if (from.params.id !== to.params.id) {
        next()
      } else {
        next(false)
      }
    }
    
  },
  {
    path: '/myreview/:id',
    name: 'myreview',
    component: MyreView,
    beforeEnter: (to, from, next) => {
      if(localStorage.getItem('encryptedToken')){
        next()
      } else {
        next('/')
      }
    },
    beforeRouteUpdate(to, from, next) {
      if (from.params.id !== to.params.id) {
        next()
      } else {
        next(false)
      }
    }
  },

  // accounts

  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },

  {
    path: '/profile/:username',
    name: 'profile',
    component: ProfileView,
    beforeEnter: (to, from, next) => {
      if(localStorage.getItem('encryptedToken')){
        next()
      } else {
        next('/')
      }
    },
    beforeRouteUpdate(to, from, next) {
      if (from.params.username !== to.params.username) {
        next()
      } else {
        next(false)
      }
    }

  },
  {
    path: '*',
    redirect: '/error'
  }
]



const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
