<template>
  
  <div class="wrap">
    <div class="bg_gradient"></div>
    <img :src="bg_img" alt="bg_img" class="bg_img">
    
    <!-- <LogoItem/> -->
    <!-- <SearchFrom/> -->
    <div class="content">
      <DetailItem :detail="this.detail" :is_liked="this.detail.is_liked.includes(userId)" :bg_img="bg_img"/>
      <button @click="tohome">홈으로 가기</button>

    <div class="info">

    <!-- Smr -->
    <p class="sim_tit">🎬 이 영화와 비슷한 영화</p>
    
    <div class="row row-cols-2 row-cols-lg-5 g-2 g-l g-1 card_smr smr">
      <div class= "col"
               v-for="movie in similar" :key="movie.id">
                <SimilarItem :similar="movie" class="movies" />
              </div>
            </div>

    <!-- Tag -->
    <p class="sim_tit">👏 이런 점이 좋았어요!</p>
    <p></p>
    <TagForm :renewTag="clicked_tag"
    :username="username"
    :movie_id="movieIdx"
    :tag="tag" 
    v-for="tag in tags"
    :key="tag.id"/>
    
    <!-- Ytb -->
    <p class="sim_tit"> 📺 관련 영상 찾아보기</p>

    <div class="carousel-container" v-if="videos.length > 0">
        <carousel :item="4" :autoplay="true" :center="true" :nav="true" class="centered-carousel" :loop="true" :autoplayHoverPause="true" >
          <YoutubeItem 
            :video="video"
            v-for="video in videos.slice(0,5)"
            :key="video.id"
            class="ytb"/>
        </carousel>
      </div>


    <p class="sim_tit">🎬 {{ detail.title }} 감상평</p>

    <CreatereView :review="this.review" :movie_id="movieIdx" :user="userId" class="CreaterePage"/>
    <router-link :to="'/moreview/' + id">해당 영화 리뷰 더보기</router-link>
    </div></div>

</div>
</template>

<script>
const secretKey = process.env.VUE_APP_SECRET_KEY
import carousel from 'vue-owl-carousel'

import axios from 'axios'
// import LogoItem from '@/components/LogoItem.vue'
// import SearchFrom from '@/components/SearchFrom.vue'

import SimilarItem from '@/components/Detail/SimilarItem.vue'
import TagForm from '@/components/Detail/TagForm.vue'
import YoutubeItem from '@/components/Detail/YoutubeItem.vue'
import DetailItem from '@/components/Detail/DetailItem.vue'


import CreatereView from '../../components/Review/CreatereView.vue'

export default {
  name : 'detailView',

  components:{
    // LogoItem,
    // SearchFrom,
    DetailItem,
    SimilarItem,
    TagForm,
    YoutubeItem,
    CreatereView,
    carousel

  },

  data(){
    return{
      detail : {},
      id : this.$route.params.id,
      review : {},
      movieIdx:this.$route.params.id,
      similar: [],
      tags: [],
      videos:[],
      backdrop:[],
      backdropwidth:[]
      
    }
  },
  computed:{
    username(){
      // console.log(this.$store.state.username)
      if(localStorage.getItem('encryptedUsername')){
        return this.$decryptToken(localStorage.getItem('encryptedUsername'), secretKey)
      }
      return null
    },
    userId(){
      if(localStorage.getItem('encryptedId')){
        return parseInt(this.$decryptToken(localStorage.getItem('encryptedId'), secretKey),10)
      }
      return null
    },
    bg_img() {
      return `https://image.tmdb.org/t/p/original/${this.detail.backdrop_path}`
    },

  },  

  created(){
   
  },
  
  mounted(){
    this.clicked_tag()
    this.get_detail()
    this.get_similar()
    this.get_tags()
    this.get_videos()

  },

  


  methods: {
    tohome(){
      this.$router.push({'name':'home'})
    },

    get_detail(){
      axios({
        method:'get',
        url: `http://127.0.0.1:8000/api/movies/${this.movieIdx}/`,
        headers:{
          Authorization: `token ${this.$decryptToken(localStorage.getItem('encryptedToken'), secretKey)}`
        } 
      })
      .then((res)=>{
        // console.log(res.data)
        this.detail = res.data
      })
    },
    get_similar(){
      axios({
        method:'get',
        url: `https://api.themoviedb.org/3/movie/${this.movieIdx}/recommendations?language=ko-KR&page=1`,
        headers:{
          Authorization: process.env.VUE_APP_TMDB_KEY
        }
      })
      .then((res)=>{
        const similarMovies = res.data.results.slice(0, 5)
        this.similar = similarMovies
      })
      .catch((err)=>{
        console.log("추천실패",err)
      })
    },
    get_tags(){
      axios({
        method:'get',
        url: `http://127.0.0.1:8000/api/movies/tag/`,
        headers:{
          Authorization: `token ${this.$decryptToken(localStorage.getItem('encryptedToken'), secretKey)}`
      } 
      })
      .then((res)=>{
        // console.log(res.data)
        this.tags = res.data
      })
    },
    clicked_tag(){
      axios({
        method:'get',
        url:`http://127.0.0.1:8000/api/${this.movieIdx}/tag/`,
        headers:{
          Authorization: `token ${this.$decryptToken(localStorage.getItem('encryptedToken'), secretKey)}`
      } 
      })
      .then((res)=>{
        const data = []
        for(const movieTag of res.data){
          if(movieTag.movie_id == this.movieIdx){
            data.push(movieTag)
          }
        }
        this.$store.dispatch('clicked_tag', data)
      })
    },
    get_videos(){
      axios({
        method:'get',
        url:`https://api.themoviedb.org/3/movie/${this.movieIdx}/videos`,
        headers: {
          accept: 'application/json',
          Authorization: process.env.VUE_APP_TMDB_KEY
        }
      })
      .then((res)=>{
        // console.log(res.data.results)
        this.videos = res.data.results
      })
      .catch((err)=>{
        console.log(err)
      })
    }
  }
}

</script>

<style scoped>

button {
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
.CreaterePage{
  width:100%;
  justify-content: center;
}
.carousel-container {
  width: 70%;
  margin: 0 auto;
  height: 100%;
}

.centered-carousel {
  display: flex;
  justify-content: center;
  align-items: center;
}
.wrap {
  height: 100%;
  display: flex;
  flex-direction: column;
}

.content {
  padding: 10px 500px;
}

.info {
  margin: 20px 0;
  width: 100%;
  height: 100%;
  border-radius: 10px;
  border: 1px solid rgb(166, 166, 166);
  padding: 10px;
}

.sim_tit {
  text-align: left;
  margin: 10px 20px 20px 20px;
  font-weight: 600;
  padding: 10px;
  text-align: left;
  font-size: 20px;
  font-weight: bold;
  color: #333333;
}


.bg_gradient {
  position: absolute;
  width: 100%;
  height: 200px;
  background-image: linear-gradient(to bottom, black,rgba(255, 255, 255, 0));
  margin-bottom: 20px;
  opacity: 0.8;
}

.bg_img {
  width: 100%;
  max-height: 350px;
  object-fit: cover;
  margin-bottom: 20px;
}

.movies {
  width: 160px;
  height: 260px;
  display: flex;
  justify-content:center;
  align-items: center;
}

.card_smr{
  justify-content: space-between;
  margin: 20px;
}


.ytb {
  width: 100%;
  height: 100%;
  max-height: 200px;
  max-width: 320px; /* 최대 가로 크기를 설정 */
  aspect-ratio: 16/9; /* 가로:세로 비율을 설정 */
  margin: 20px;
  object-fit: cover; /* 영상을 잘리지 않고 적절히 표시 */
}

@media (max-width: 768px) {
  /* 원하는 반응형 크기에 따라 미디어 쿼리를 추가 */
  .ytb {
    max-width: 100%; /* 가로 크기를 100%로 설정 */
    aspect-ratio: auto; /* 비율을 유지하지 않고 자동으로 조정 */
  }
}

</style>
