<template>
  <div class="Home">
    <!-- <h1>Home</h1> -->
    <NavForm/>
    <SearchFrom/>
    <div class="row row-cols-1 row-cols-md-3  g-4 center">
      <MovieItem v-for="movie in movies.slice(0,10)"
      :key="movie.id"
      :movie="movie"
      />
    </div><br><br>

    <div class="row row-cols-1 row-cols-md-3 g-4 center">
      <MovieItem v-for="movie in movies.slice(0,10)"
      :key="movie.id"
      :movie="movie"
      />
    </div>

    <div class="row row-cols-1 row-cols-md-3 g-4 center">
      <VideoItem :videoId="videoId" />
    </div>


  </div>
</template>

<script>
import axios from 'axios'
import NavForm from '@/components/NavForm.vue'
import SearchFrom from '@/components/SearchFrom.vue'

import MovieItem from '@/components/Home/MovieItem.vue'
import VideoItem from '@/components/Home/VideoItem.vue'

export default {

  name : 'HomeView',

  components:{
    NavForm,
    SearchFrom,
    MovieItem,
    VideoItem,
  },

  data(){
    return{
      movies : [],
      videoTitle: '',
      videoId: '',
      query:'영화추천'
    }
  },

  created(){
    this.get_movie()
    this.get_youtube()
  },
  mounted() {
  this.get_movie()
  this.get_youtube()
  },

  methods: {
    get_movie(){
      axios({
        method:'get',
        url: 'http://127.0.0.1:8000/api/movies/' 
      })
      .then((res)=>{
        // console.log(res.data)
        this.movies = res.data
        // console.log(this.movies)
      })
    },
    get_youtube() {
    const apiKey = process.env.VUE_APP_YOUTUBE_API_KEY;
    
      axios({
          method: 'get',
          url: 'https://www.googleapis.com/youtube/v3/search',
          params: {
            key: apiKey,
            type: 'video',
            part: 'snippet',
            q: this.query,
          }
        })
      .then((res) => {
        console.log(res.data.items[0].id.videoId)
        this.videoTitle = res.data.items[0].snippet.title
        this.videoId = res.data.items[0].id.videoId
      })
      .catch(error => {
        console.log(error);
      });
    }
  }
  }

</script>

<style>
</style>