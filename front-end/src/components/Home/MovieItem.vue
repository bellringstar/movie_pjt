<template>
  <div class="col" >
    <div class="card h-100">
      <!-- <img :src="poster" class="card-img-top"> -->
      <div class="card-body d-flex flex-column">
        <h5 class="card-title"><b>{{ movie.title }}</b></h5>
        <!-- <h1>a</h1> -->
      </div>
   </div>
  </div>
  </template>

<script>
export default {
  name:'MovieCard',
  props:{
    movie:Object
  },
  computed: {
        poster() {
        return `https://image.tmdb.org/t/p/w600_and_h900_bestv2${this.movie.poster_path}`
      }
    }
}

</script>

<style scoped>

</style>


