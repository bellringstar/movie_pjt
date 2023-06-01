<template>
  <div class="siginup-container">
    <div class="background-image"></div>
    <img src="@/assets/logo.png" alt="로고 이미지" class="logo_img">

    <br><br>
    <h1 class="L">회원가입</h1>
    <form @submit.prevent="signup">

      <div class="form-group">
        <input type="text" id="username" v-model="username" required placeholder="아이디">
      </div>

      <div class="form-group">
        <input type="password" id="password1" v-model="password1" required placeholder="비밀번호">
      </div>

      <div class="form-group">

        <input type="password" id="password2" v-model="password2" required placeholder="비밀번호확인">

      </div>
      

      <div class="form-group">
        <input type="email" id="email" v-model="email" required placeholder="이메일">
      </div>


      <button type="submit">회원가입</button>
      <button class="signup" @click="tosignup">로그인</button>
      
    </form>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      username: "",
      email: "",
      password1: "",
      password2: "",
      // profileImage: null,

    }
  },

  methods: {
    showmessage(text){
      this.$toasted.show(text,{
        duration:1000,
        position: 'top-center',
        type:'error'
      })
    },
    signup() {
      const username = this.username
      const password1 = this.password1 
      const password2 = this.password2
      const email = this.eamil
      
      axios({
        method:'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data:{
          username, password1, password2, email
        }
      })
      .then((res) => {
        console.log("회원가입 성공")
        const data={
          'username':username,
          'token': res.data.key
        }
        this.$store.dispatch('signUp', data)
      })
      .catch((err)=>{
        console.log("회원가입 실패")
        if(err['response']['data'].username){
          this.showmessage('이미 존재하는 ID 입니다.')
        }
        if(err['response']['data'].password1){
          this.showmessage('비밀번호를 더 복잡하게 작성해주세요')
        }
        if(err['response']['data'].non_field_errors){
          this.showmessage('비밀번호가 일치하지 않습니다.')
        }
      })
    },
    tosignup(){
      this.$router.push({'name':'login'})
    }
  }
}
</script>

<style scoped>

.L{
font-family: 'Noto Sans';
font-style: normal;
font-weight: 600;
font-size: 20px;
line-height: 48px;
text-align: center;
margin: 0px 0 10px 0;
color: #333;
}

.siginup-container {
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
input[type="password"],
input[type="email"] {
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

</style>
