<template>
  <div>
    <div class="col">
      <img :src="bg_img" alt="bg_img" class="bg_img">
      <img :src="pos_img" alt="pos_img" class="pos_img">
      <p class="title">{{ detail.title }}</p>
      <p class="overview">{{ detail.overview_kr }}</p>
      <div>
        <p class="release_date">{{ detail.release_date }}</p>
        <p class="runtime">{{ detail.runtime }}</p> 
      </div>
    </div>

  </div>
  </template>

<script>
export default {
  name:'DetailItem',
  props:{
    detail:Object
  },
  computed: {
    bg_img() {
<<<<<<< HEAD
      return `https://image.tmdb.org/t/p/w600_and_h900_bestv2${this.movie.backdrop_path}`
    },
    pos_img() {
      return `https://image.tmdb.org/t/p/w600_and_h900_bestv2${this.movie.poster_path}`
=======
      return `https://image.tmdb.org/t/p/w600_and_h900_bestv2${this.detail.backdrop_path}`
    },
    pos_img() {
      return `https://image.tmdb.org/t/p/w600_and_h900_bestv2${this.detail.poster_path}`
>>>>>>> front
    }
  },
}

</script>

<style scoped>
.bg_img{
  width: 1920px;
  height: 705px;
}

.pos_img{
  width: 328px;
  height: 491px;
}




</style>


