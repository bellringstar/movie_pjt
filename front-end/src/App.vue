<template>
  <div id="app" data-app>
    <nav>
    </nav>
    <router-view/>
  </div>
</template>

<script>
// const secretKey = process.env.VUE_APP_SECRET_KEY
export default {



  beforeDestroy() {
    localStorage.removeItem('encryptedToken'); // 로컬 스토리지 아이템 삭제
    localStorage.removeItem('encryptedUsername'); // 로컬 스토리지 아이템 삭제
    localStorage.removeItem('encryptedId'); // 로컬 스토리지 아이템 삭제

  },




}




</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

html,body {height: 100%;}
.wrap {height: 100%; display: flex; flex-direction: column;}
</style>
