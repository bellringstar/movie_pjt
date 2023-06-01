import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '../router'
import CryptoJS from 'crypto-js'

const secretKey = process.env.VUE_APP_SECRET_KEY
const encryptToken = (token, secretKey) => {
  const encryptedToken = CryptoJS.AES.encrypt(String(token), secretKey).toString();
  return encryptedToken;
};



Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token:null,
    movies : [],
    recent_movies:[],
    popular_movies:[],
    username: "",
    userid:null,
    tag_info:[],
    login_err:'',
    recommend_data:[],
    profile_user:{},
    detail:{},


  },
  getters: {
    isLogin(){
      return localStorage.getItem('encryptedToken') ? true : false
    }
  },

  mutations: {
    SAVE_TOKEN(state, data){
      const token = data.token
      
      const encryptedToken = encryptToken(token, secretKey)
      const encryptedUsername = encryptToken(data.username, secretKey)
      localStorage.setItem('encryptedUsername',encryptedUsername)
      localStorage.setItem('encryptedToken', encryptedToken)

      axios({
        method:'get',
        url:`http://127.0.0.1:8000/api/${data.username}/`
      })
      .then((res)=>{
        const encryptedId = encryptToken(res.data.id, secretKey)
        localStorage.setItem('encryptedId',encryptedId)
        if (!localStorage.getItem('recent_movies') || !localStorage.getItem('popular_movies')) {
          setTimeout(() => {
            router.push({ name: 'home' });
          }, 4000);
        } else {

          router.push({ name: 'home' });
        }
        
      })
      
    },
    ERROR_MESSAGE(state, err){
      state.login_err = err
    },
    GET_MOVIE(state){
      axios({
        method:'get',
        url: 'http://127.0.0.1:8000/api/movies/' 
      })
      .then((res)=>{
        // console.log(res.data)
        state.movies = res.data
      })
      .catch((err)=>{
        console.log(err)
      })
      
    },
    GET_RECENT_MOVIE(){
      axios({
        method:'get',
        url:'http://127.0.0.1:8000/api/get_recent_movie/',
      })
      .then((res)=>{
        localStorage.setItem('recent_movies', JSON.stringify(res.data))
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    GET_POPULAR_MOVIE(){
      axios({
        method:'get',
        url: 'http://127.0.0.1:8000/api/get_popularity_movie/',
        
      })
      .then((res) => {
         localStorage.setItem('popular_movies', JSON.stringify(res.data))
      })
      .catch((err)=>{
        console.log(err)
      })

    },
    CLICKED_TAG(state, data){
      state.tag_info = data
    },
    RECOMMEND_MOVIE(state,data){
      state.recommend_data = data

    },
    GET_PROFILE_USER(state,data){
      state.profile_user = data
    },
    GET_DETAIL(state,data){
      state.detail = data
    },


    
  },
  
  actions: {
    get_detail(context, data){
      context.commit('GET_DETAIL', data)
    },
    signUp(context, data){
      context.commit("SAVE_TOKEN", data)
    },
    login(context, data){
      context.commit('SAVE_TOKEN', data)

    },
    get_movie(context){
      context.commit('GET_MOVIE')
    },
    
    get_recent_movie(context){
      context.commit('GET_RECENT_MOVIE')
    },
    get_popular_movie(context){
      context.commit('GET_POPULAR_MOVIE')
    },
    clicked_tag(context, data){
      context.commit('CLICKED_TAG', data) 
    },
    recommendMovie(context, data){
      context.commit('RECOMMEND_MOVIE', data)
    },
    get_profile_user(context, data){
      context.commit('GET_PROFILE_USER', data)
    }

  },
  
  modules: {
  }
})
