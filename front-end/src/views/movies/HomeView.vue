<template>
  <div class="Home wrap">
  <LogoItem/>

  <div class="content">
    <div class="grp_login">
      <a class="txt_logout" @click="logout">LOGOUT</a> |
      <a class="txt_profile" @click="to_profile">PROFILE </a> |
      <!-- <a class="txt_myreview" @click="myreview">My R </a> | -->
      <a class="txt_myreview" @click="recommend"> Flick AI </a>
    </div>
      
    <div class="menu">
      <SearchFrom/>
    </div>

    <BannerItem />

    <div class="txt">
    <p class="sub_txt">HOT MOVIE</p>
    <p class="main_txt">인기영화 순위</p>
    </div>

    <div class="row row-cols-2 row-cols-lg-5 g-2 g-lg-3 mv-for">
      <div class= "col"
      v-for="movie in popular_movies.slice(0,5)" :key="movie.id" 
      @click="handle_click(movie.movie_id)">
        <MovieItem :movie="movie" class="movies"/>
      </div>
    </div>

    <div class="row row-cols-2 row-cols-lg-5 g-2 g-lg-3 mv-for lst">
      <div class= "col"
      v-for="movie in popular_movies.slice(5,10)" :key="movie.id" 
      @click="handle_click(movie.movie_id)">
        <MovieItem :movie="movie" class="movies"/>
      </div>
    </div>

    <div class="txt">
    <p class="sub_txt">RECENT MOVIE</p>
    <p class="main_txt">최신영화 순위</p>
    </div>

    <div class="row row-cols-2 row-cols-lg-5 g-2 g-lg-3 mv-for">
      <div class= "col p-1"
      v-for="movie in recent_movies.slice(0,5)" :key="movie.id" 
      @click="handle_click(movie.movie_id)">
        <MovieItem :movie="movie" class="movies"/>
      </div>
    </div>

    <div class="row row-cols-2 row-cols-lg-5 g-2 g-lg-3 mv-for">
      <div class= "col p-1"
      v-for="movie in recent_movies.slice(5,10)" :key="movie.id" 
      @click="handle_click(movie.movie_id)">
        <MovieItem :movie="movie" class="movies"/>
      </div>
    </div>

    <!-- <div class="txt">
    <p class="sub_txt">YOUTUBE MOVIE</p>
    <p class="main_txt">유튜브 추천영화</p>
    </div> -->

    <div class="row row-cols-1 row-cols-md-3 g-4 center lst">
      <!-- <VideoItem :videoId="videoId"/> -->
      <VideoItem v-for="video in videos"
      :key="video.videoId"
      :videoId="video.id.videoId"
      :videoTitle="video.snippet.title"/>
    </div>

    <div class="txt sce">
    <p class="sub_txt">WELLMADE MOVIE</p>
    <p class="main_txt">명장면으로 보는 영화</p>
    </div>

    <SceneItem class="scene"/>

  </div>
  </div>
</template>

<script>
const secretKey = process.env.VUE_APP_SECRET_KEY

import axios from 'axios'
import LogoItem from '@/components/LogoItem.vue'
// import NavForm from '@/components/NavForm.vue'
import SearchFrom from '@/components/SearchFrom.vue'

import MovieItem from '@/components/Home/MovieItem.vue'
import VideoItem from '@/components/Home/VideoItem.vue'
import BannerItem from '@/components/Home/BannerItem.vue'
import SceneItem from '@/components/Home/SceneItem.vue'

export default {

  name : 'HomeView',

  components:{
    // NavForm,
    SearchFrom,
    BannerItem,
    MovieItem,
    VideoItem,
    LogoItem,
    SceneItem
  },

  data(){
    return{
      videos: [],
      query:'영화추천'
    }
  },
  computed:{
    // movies(){
    //   return this.$store.state.movies
    // },
    recent_movies(){
      return JSON.parse(localStorage.getItem('recent_movies')) || []
    },
    popular_movies(){
      return JSON.parse(localStorage.getItem('popular_movies')) || []
    },
    username(){
      const encryptedToken = localStorage.getItem('encryptedUsername')
      return this.$decryptToken(encryptedToken, secretKey)
    },
    userid(){
      return parseInt(this.$decryptToken(localStorage.getItem('encryptedId'), secretKey),10)
    }
  },
  created(){
    if(this.$store.state.movies.length === 0){
      this.get_movie()
    }
    if(!localStorage.getItem('recent_movies')){
      this.get_popular_movie(),
      this.get_recent_movie()
    }
  },

  methods: {
    to_profile(){
      this.$router.push({'name':'profile', 'params':{'username':this.username}})
    },
    logout(){
      axios({
        method:'post',
        url:`http://127.0.0.1:8000/accounts/logout/`,
        headers:{
          Authorization: `Token ${this.$decryptToken(localStorage.getItem('encryptedToken'), secretKey)}`
      } 
      })
      .then((res)=>{
        console.log(res)
        window.localStorage.removeItem('encryptedUsername')
        window.localStorage.removeItem('encryptedToken')
        window.localStorage.removeItem('encryptedId')
        this.$router.push({'name':'login'}).catch((err)=>{console.log('로그아웃 오류',err)})
      })
    },
    myreview(){
      this.$router.push({'name':'myreview' ,params:{'id':this.userid}}).catch(()=>{location.reload()})
    },
    get_movie(){
      this.$store.dispatch('get_movie')
    },
    get_popular_movie(){
      this.$store.dispatch('get_popular_movie')
      
    },
    get_recent_movie(){
      this.$store.dispatch('get_recent_movie')
    },

    handle_click(movie_id){
      this.$router.push(`/detail/${movie_id}`).catch(()=>{location.reload()})
    },
    recommend(){
      this.$router.push('/recommend')
    }
  }
  }

</script>

<style>
.wrap {height: 100%; display: flex; flex-direction: column;}

.srh_mv {display:block;}

.content {padding: 10px 350px;}

.grp_login {display:flex; justify-content:flex-end;}
.txt_login {margin-right: 30px; text-decoration:none;}
.txt_signup {margin-right: 10px; text-decoration:none;}

.movies {
  width: 290px;
  height: 390px;
  display: flex;
  justify-content:center;
  /* align-items: center; */
}

.txt {text-align: left; margin: 50px 0 -30px 0;}
.main_txt {
  font-style: normal;
  font-weight: 600;
  font-size: 45px;
  line-height: 59px;
  color: #333333;
}

.sub_txt {margin: 5px 0; font-style: normal; font-weight: 500; font-size: 28px; line-height: 38px; color: #B8B8B8;}
.sub_txt::after {content: ' 🚀 '; font-size: 22px;}

.lst {
  margin-bottom:150px;
}
.scene {
  margin: 50px 0 20px 0;
  padding: 0;
}

a{
  text-decoration: none ;
  color: #3A5FFF;
  margin: 0 5px;
  
}


/* .sec{padding-left: 40px;} */

/* bs-gutter-x{
  1rem;
}  */

</style>
