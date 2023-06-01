import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import vuetify from './plugins/vuetify'
import CryptoJS from 'crypto-js'
import VueCarousel from 'vue-carousel';
import axios from 'axios'
import Vuetify from 'vuetify'
import Toasted from 'vue-toasted'
Vue.use(vuetify)
Vue.use(Vuetify)
Vue.use(VueCarousel);
Vue.use(Toasted)

function errorHandler(error) {
  console.log(error);
  // alert("An error occurred: " + error.message);
}
Vue.config.productionTip = false;
Vue.config.errorHandler = errorHandler;


new Vue({
  mounted(){
    Vue.config.productionTip = false;
    axios.interceptors.response.use(
      (response) => response,
      (error) => {
        if (this.$route.path=== '/' || this.$route.path === '/signup'){
          return Promise.reject(error)
        }
        this.$router.push('/error');
        return Promise.reject(error);
      }
    );
  },
  created(){
    Vue.config.productionTip = false;
    Vue.prototype.$decryptToken = function (encryptedToken, secretKey) {
      const bytes = CryptoJS.AES.decrypt(encryptedToken, secretKey);
      const decryptedToken = bytes.toString(CryptoJS.enc.Utf8);
      return decryptedToken;
    };
  },
  store,
  router,
  VueCarousel,
  vuetify,
  render: h => h(App)
}).$mount('#app')











