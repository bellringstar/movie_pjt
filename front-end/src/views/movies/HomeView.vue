<template>
  <div class="Home">
    <h1>Home</h1>
    <NavForm/>
    <div class="row row-cols-1 row-cols-md-3 g-4 center">
      <MovieItem v-for="movie in movies"
      :key="movie.id"
      :movie=movie
      />
    </div>

  </div>
</template>

<script>
import MovieItem from '@/components/Home/MovieItem.vue'
import NavForm from '@/components/NavForm.vue'
import axios from 'axios'

export default {

  name : 'HomeView',

  components:{
    MovieItem,
    NavForm,
  },

  data(){
    return{
      movies : []
    }
  },

  created(){
    this.get_movie()
  },
  mounted(){
    this.get_movie()
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
    }
  }






}
</script>

<style>
</style>