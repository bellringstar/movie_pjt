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
        <label for="password">비밀번호:</label>
        <input type="password" id="password" v-model="password" required>
      </div>

      <!-- <div class="input-container">
        <label for="password">비밀번호확인:</label>
        <input type="password" id="password" v-model="password" required>
      </div> -->

      <div class="input-container">
        <label for="email">이메일:</label>
        <input type="email" id="email" v-model="email" required>
      </div>

      <div>
        <label for="profile-image">프로필 이미지:</label>
        <input type="file" id="profile-image" @change="handleFileChange">
      </div>

      <button type="submit">회원가입</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      email: '',
      profileImage: null,
    };
  },
  methods: {
    signup() {
      const userData = {
        username: this.username,
        password: this.password,
        email: this.email,
        profileImage: this.profileImage, 
      };

      // axios.post('/api/signup', userData)
      //   .then(response => {
      //   })
      //   .catch(error => {
      //     console.error(error);
      //   });

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
