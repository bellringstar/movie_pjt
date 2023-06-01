<template>
  <div class="login-container">
    <div class="background-image"></div>
    <img src="@/assets/logo.png" alt="로고 이미지" class="logo_img">
    <h1 class="L">로그인</h1><br>
    <form @submit.prevent="login">
      <div class="form-group">
        <!-- <label for="username">아이디:</label> -->
        <input type="text" id="username" v-model="username" required placeholder="아이디">
      </div>
      <div class="form-group">
        <!-- <label for="password">비밀번호:</label> -->
        <input type="password" id="password" v-model="password" required placeholder="비밀번호">
      </div>
      <button type="submit">로그인</button>
      <button class="signup" @click="signup">계정이 없으신가요? 회원가입</button>
      
      <!-- <br><p v-if="this.$store.state.login_err">아이디 혹은 비밀번호를 확인 해 주세요</p> -->
    </form>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      username: '',
      password: ''
    };
  },

  methods: {
    showmessage(text){
      this.$toasted.show(text,{
        duration:1000,
        position: 'top-center',
        type:'error'
      })
    },
    login() {
      const username = this.username
      const password = this.password
      axios({
        method:'post',
        url:'http://127.0.0.1:8000/accounts/login/',
        data:{
          username, password
        }
      })
      .then((res) => {
        const data = {
          'username':username,
          'token':res.data.key
        }
        this.$store.dispatch('login', data)
      })
      .catch((err) => {
        // context.commit('ERROR_MESSAGE', err.response.data)
        console.log(err)
        this.showmessage('id 혹은 비밀번호를 확인 해 주세요')
      })
      
    },
    signup(){
      this.$router.push({'name':'signup'}).catch(()=>{location.reload()})
    }
  },
  created(){
    if(!localStorage.getItem('get_popular_movie')){
      this.$store.dispatch('get_popular_movie')
    }
    if(!localStorage.getItem('get_recent_movie')){
      this.$store.dispatch('get_recent_movie')
    }
    if(localStorage.getItem('get_recent_movie') && localStorage.getItem('get_popular_movie')){
      this.$store.dispatch('get_movie')
    }
    
  },
  mounted(){
    if(!localStorage.getItem('get_popular_movie')){
      this.$store.dispatch('get_popular_movie')
    }
    if(!localStorage.getItem('get_recent_movie')){
      this.$store.dispatch('get_recent_movie')
    }
    if(localStorage.getItem('get_recent_movie') && localStorage.getItem('get_popular_movie')){
      this.$store.dispatch('get_movie')
    }


  }
};
</script>

<style scoped>

.L{
font-family: 'Noto Sans';
font-style: normal;
font-weight: 600;
font-size: 24px;
line-height: 48px;
text-align: center;
margin: 10px 0 0 0;
color: #333;
}

.login-container {
  max-width: 400px;
  margin: 200px auto;
  padding: 20px;
  background: #F4F8FF;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
}


.form-group {
  margin-bottom: 20px;
}

/* label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
  color: #333;
} */

input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

input[type="text"]::placeholder {
  color: #9a9a9a; 
}

input[type="password"]::placeholder {
  color: #9a9a9a;
}

button[type="submit"] {
  display: block;
  width: 100%;
  padding: 10px;
  font-family: 'Roboto';
  font-style: normal;
  font-weight: 500;
  /* font-weight: 400; */
  font-size: 16px;
  line-height: 28px;
  border-radius: 5px;
  border: none;
  background: #6DFF8F;
  color: rgb(0, 0, 0);
  cursor: pointer;
}

.signup {
  margin-top: 10px;
  display: block;
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border-radius: 5px;
  border: none;
  background: #6dff8f00;
  font-family: 'Roboto';
  font-style: normal;
  font-weight: 700;
  font-size: 16px;
  line-height: 28px;

  color: #3A5FFF;
  cursor: pointer;
}

p {
  color: #fd5151;
  margin-top: -5px;
  text-align: center;
}

.logo_img {
  width: 300px;
  height: 80px;
  margin: 0 auto;
}

.background-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url('@/assets/login-bg.png');
  background-size: cover;
  background-position: center;
  opacity: 0.6;
  z-index: -1;
}

</style>
