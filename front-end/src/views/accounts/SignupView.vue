<template>
  <div class="signup">
    <br><br>
    <h2>회원가입</h2>
    <form @submit.prevent="signup">

      <div class="input-container">
        <label for="username">아이디:</label>
        <input type="text" id="username" v-model="username" required>
      </div>

      <div class="input-container">
        <label for="password1">비밀번호:</label>
        <input type="password" id="password1" v-model="password1" required>
      </div>

      <div class="input-container">
        <label for="password2">비밀번호확인:</label>
        <input type="password" id="password2" v-model="password2" required>
      </div>

      <div class="input-container">
        <label for="email">이메일:</label>
        <input type="email" id="email" v-model="email" required>
      </div>

      <!-- <div>
        <label for="profile-image">프로필 이미지:</label>
        <input type="file" id="profile-image" >
      </div> -->

      <button type="submit">회원가입</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: "",
      email: "",
      password1: "",
      password2: "",
      // profileImage: null,
    };
  },
  methods: {
    signup() {
      const userData = {
        Username: this.username,
        Password1: this.password1,
        Password2: this.password2,
        Email: this.email,
        // profileImage: this.profileImage, 
      };

      axios({
        method:"post",
        url:"http://127.0.0.1:8000/accounts/signup/",
        data: {
          'Username': this.username,
          'Password1': this.password1,
          'Password2': this.password2,
          'Email': this.email,
        }
      })
      .then((res) => {
        console.log(res.data)
      })
      .catch(error => {
        console.log(error);
      });

      console.log(userData);
    }
  }
}
</script>

<style scoped>
.signup {
  margin-top: 20px;
  max-width: 400px;
  margin: 0 auto;
}

h2 {
  text-align: center;
}

form {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
}

label {
  font-weight: bold;
}

.input-container {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.input-container label {
  margin-right: 10px;
}

input[type="text"],
input[type="password"],
input[type="email"],
input[type="file"] {
  padding: 8px;
  width: 100%;
  box-sizing: border-box;
}

input[type="file"]::-webkit-file-upload-button {
  padding: 5px 10px;
  background-color: #6c6c6c;
  color: white;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}

input[type="file"]::-webkit-file-upload-button:hover {
  background-color: #6c6c6c;
}

button {
  padding: 10px;
  background-color: #6c6c6c;
  color: white;
  border: none;
  border-radius: 3px;
  cursor: pointer;
  width: 100%;
  box-sizing: border-box;
}

button:hover {
  background-color: #6c6c6c;
}
</style>
