import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '../router'
import CryptoJS from 'crypto-js'

const encryptToken = (token, secretKey) => {
  const encryptedToken = CryptoJS.AES.encrypt(token, secretKey).toString();
  return encryptedToken;
}

const decryptToken = (encryptedToken, secretKey) => {
  const bytes = CryptoJS.AES.decrypt(encryptedToken, secretKey)
  const decryptedToken = bytes.toString(CryptoJS.enc.Utf8)
  return decryptedToken
}



Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token:null
  },
  getters: {
    isLogin(state){
      return state.token ? true : false
    }
  },

  mutations: {
    SAVE_TOKEN(state, token){
      const secretKey = "tokensecretkey93728"
      const encryptedToken = encryptToken(token, secretKey)
      localStorage.setItem('encryptedToken', encryptedToken)
      state.token = decryptToken(encryptedToken, secretKey)
      router.push({name:'home'})
    }
  },
  
  actions: {
    signUp(context, data){
      const username = data.username
      const password1 = data.password1
      const password2 = data.password2
      const email = data.email
      axios({
        method:'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data:{
          username, password1, password2, email
        }
      })
      .then((res) => {
        console.log("성공")
        console.log(res.data)
        context.commit("SAVE_TOKEN", res.data)
      })
      .catch((err)=>{
        console.log("실패")
        console.log(err['response']['data'])
      })
    },
    LOGIN(context, data){
      const username = data.username
      const password = data.password
      axios({
        method:'post',
        url:'http://127.0.0.1:8000/accounts/login/',
        data:{
          username, password
        }
      })
      .then((res) => {
        context.commit('SAVE_TOKEN', res.data.key)
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
  
  modules: {
  }
})
