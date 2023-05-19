import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/movies/HomeView.vue'
import DetailView from '@/views/movies/DetailView.vue'

import ErrorView from '@/views/errors/ErrorView.vue'

import MoreView from '@/views/communitys/MoreView.vue'
import MyreView from '@/views/communitys/MyreView.vue'

import LoginView from '@/views/accounts/LoginView.vue'
import ProfileView from '@/views/accounts/ProfileView.vue'
import SignupView from '@/views/accounts/SignupView.vue'

Vue.use(VueRouter)

const routes = [
  // movies
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/detail',
    name: 'detail',
    component: DetailView
  },

  // errors
  {
    path: '/error',
    name: 'error',
    component: ErrorView
  },

  // communitys
  {
    path: '/moreview',
    name: 'moreview',
    component: MoreView
  },
  {
    path: '/myreview',
    name: 'myreview',
    component: MyreView
  },

  // accounts
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView
  },

  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
