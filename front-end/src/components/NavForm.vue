<template>
    <header>
        <h1 class="logo">Movie<br/>Web</h1>
        <div class="grp_login">
            <a class="txt_logout" @click="logout">LOGOUT</a>
            <a class="txt_profile" @click="to_profile">PROFILE </a>
            <a class="txt_myreview" @click="myreview">MyReview </a>
        </div>
    </header>
</template>

<script>
const secretKey = process.env.VUE_APP_SECRET_KEY

import axios from 'axios'
export default {
    computed:{
        isLogin(){
            console.log(this.$store.getters.isLogin)
            return this.$store.getters.isLogin
        }
    },
    methods:{
        logout(){
            axios({
                method:'post',
                url:'http://127.0.0.1:8000/accounts/logout/',
                headers:{
                    Authorization: `Token ${this.$decryptToken(localStorage.getItem('encryptedToken'), secretKey)}`
                }
            })
            .then((res)=>{
                console.log('로그아웃', res.data)
                localStorage.removeItem('encryptedUsername')
                localStorage.removeItem('encryptedToken')
                localStorage.removeItem('encryptedId')

                
            })
            .catch((err)=>{
                console.log('로그아웃 실패', err)
            })
        }
    }
}
</script>

<style>
.txt_logout{
    color: white;
}

/* .grp_login{
  position: fixed;
    top: 0;
    left: 0;
    right: 400px;
}

a{
  text-decoration: none ;
  color: #ffffff;
  margin: 0 5px;
} */

</style>