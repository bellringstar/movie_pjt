<template>
  <div class="login-container">
    <h1>Login</h1><br>
    <form @submit.prevent="login">
      <div class="form-group">
        <label for="username">아이디:</label>
        <input type="text" id="username" v-model="username" required>
      </div>
      <div class="form-group">
        <label for="password">비밀번호:</label>
        <input type="password" id="password" v-model="password" required>
      </div>
      <button type="submit">Log in</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    login() {
      // 로그인 로직을 구현합니다.
      // this.username과 this.password 변수를 사용하여 서버로 인증 요청을 보낼 수 있습니다.
      // 성공 또는 실패에 따라 알맞은 동작을 수행합니다.
      const username = this.username
      const password = this.password
      const payload = {
        username, password
      }
      this.$store.dispatch('LOGIN', payload)
    }
  }
};
</script>

<style>
.login-container {
  max-width: 400px;
  margin: 30px auto;
  padding: 20px;
  background: #f4f4f4;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
}

h1 {
  text-align: center;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  font-weight: bold;
}

input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

button[type="submit"] {
  display: block;
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border-radius: 5px;
  border: none;
  background-color: #6c6c6c;
  color: white;
  cursor: pointer;
}
</style>
