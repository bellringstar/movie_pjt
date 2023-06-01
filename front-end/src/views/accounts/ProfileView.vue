<template>
  <div class="Profile">
    <LogoItem/>
      <SearchFrom/>
      <InfoView :username="username" @profile_update="update"/>
      <h4>찜한 영화</h4>
      <div class="carousel-container" v-if="movies.length > 0">
        <carousel :autoplay="true" :center="true" :nav="true" class="centered-carousel" :loop="true" :autoWidth="true">
          <LikedItem :movie="movie" v-for="movie in movies" :key="movie.movie_id" />
        </carousel>
      </div>
      <!-- <MyreviewItem/> -->
  </div>
</template>

<script>
// import { Carousel, slide } from 'vue-carousel'
import carousel from 'vue-owl-carousel'

import LogoItem from '@/components/LogoItem.vue'
import SearchFrom from '@/components/SearchFrom.vue'

import LikedItem from '@/components/Profile/LikedItem.vue'
// import MyreviewItem from '@/components/Profile/MyreviewItem.vue'
import InfoView from '../../components/Profile/InfoView.vue'
import axios from 'axios'
const secretKey = process.env.VUE_APP_SECRET_KEY

export default {
  name: 'ProfileView',

  components:{
    LogoItem,
    SearchFrom,
    InfoView,
    LikedItem,
    carousel
    // slide
    // MyreviewItem,
  },

  data(){
    return{
      user: {},
      movies: {},
      username:this.$route.params.username
    }
  },
  computed:{
    slideWidth(){
      return `${100 / 3}%`
    }
  },
  

  created(){
    this.get_user()
  },

  mounted(){
    this.get_user()
  },
  methods: {
    get_user(){
      axios({
        method:'get',
        url: `http://127.0.0.1:8000/api/${this.username}/`,
        headers:{
            Authorization: `token ${this.$decryptToken(localStorage.getItem('encryptedToken'), secretKey)}`
        }
      })
      .then((res)=>{
        console.log(res.data)
        this.user = res.data
        console.log(this.user)
      })
      .then(()=>{
        axios({
          method:'GET',
          url:`http://127.0.0.1:8000/api/like_movie/${this.user.id}/`,
          headers:{
            Authorization: `token ${this.$decryptToken(localStorage.getItem('encryptedToken'), secretKey)}`
        }
        })
        .then((res)=>{
          console.log(res.data)
          this.movies = res.data
        })
      })
    },
    update(){
      this.get_user(this.user.username)
    }

  }}
</script>

<style scoped>

.carousel-container {
  width: 50%;
  margin: 0 auto;
}

.centered-carousel {
  display: flex;
  justify-content: center;
  align-items: center;
}

.grp_nav{
  text-decoration: none;
  margin: 10 0px;
  display:flex;
  justify-content:flex-end;
}

html,body {height: 100%;}
.wrap {height: 100%; display: flex; flex-direction: column;}
.content {padding: 10px 350px;}


</style>