<template>
  <div wrap>
    <div class="background-image"></div>
    <div class="bd">
      <p><img src="@/assets/logo_w.png" alt="Review" class="logo_w" @click="tohome"></p>
      <input class="reco_sh_input" size="60" type="text" @keyup.enter="recommendMovie" v-model="query" placeholder="지금 원하는 영화를 검색해보세요." >
      <p class="txt">더운 여름 어울리는 공포영화,신나는 영화, 디즈니같은 영화, 판타지 영화</p>
      <div class="recommend-container">
      <img :src="loading_img" alt="로딩중" v-if="this.loading" class="load">
      <RecommendItem :recommend="recommend" v-for="recommend in recommend_data" :key="recommend.movie_id"/>
      <img :src="err_img" alt="검색 실패" v-if="this.err || recommend_data.err">
    </div>
  </div></div>
</template>

<script>
const secretKey = process.env.VUE_APP_SECRET_KEY

import RecommendItem from '@/components/RecommendItem.vue';
import axios from 'axios';
export default {
  components:{
      RecommendItem,
  },
  data(){
    return{
      query:'',
      err:null,
      loading:false
    }
  },
  computed:{
    recommend_data(){
      return this.$store.state.recommend_data
    },
    err_img(){
      return require('@/assets/rc_err.gif')
    },
    loading_img(){
      return require('@/assets/road2.gif')
    }
  },
  methods:{
    tohome(){
      this.$router.push({'name':'home'})
    },
    recommendMovie(){
      this.$store.state.recommend_data = []
      this.loading = true
      axios({ 
        method:'post',
        url:`http://127.0.0.1:8000/api/movies/search/`,
        data:{
          query:this.query
        },
        headers:{
          Authorization: `Token ${this.$decryptToken(localStorage.getItem('encryptedToken'), secretKey)}`
      } 
      })
      .then((res)=>{
        console.log('추천영화', res.data)
        this.query=''
        this.loading = false
        this.$store.dispatch('recommendMovie', res.data)
      })
      .catch((err)=>{
        console.log('검색실패',err)
        this.err=err
      })
    }
  }

}
</script>

<style scope>
/* body */
.wrap {}

.bd {padding: 10px 350px;}

.recommend-container {
  display: flex;
  flex-wrap: wrap;
  /* gap: 10px; */
  justify-content: space-between;
}

.logo_w{
  object-fit: contain;
  width: 300px;
  height: 200px;
  margin-top: 50px;
}

.reco_sh_input{
  /* border: solid 1px #B8B8B8; */
  text-decoration: none; 
  border-radius: 50px;
  /* width: 100px; */
  height: 50px;
  margin-top: -30px;
  padding: 20px;
  color: #515050;
  background-color: white ;
  opacity: 80%;
}

.card {
  width: 200px !important;
}

.img_logo {
  /* display:inline-block; */
width: 220px;
height: 60px;
margin-bottom: 8px;
}

.load{
  display: inline-flex;
  justify-content: center;
  align-content: center;
  object-fit: contain;
}

.background-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url('@/assets/rc-bg.jpg');
  background-size: cover;
  background-position: center;
  /* opacity: 0.6; */
  z-index: -1;
}

.txt{
    color: rgb(150, 150, 150);
    text-align: center;
    font-weight: 400;
    margin-top: 20px;
}

</style>