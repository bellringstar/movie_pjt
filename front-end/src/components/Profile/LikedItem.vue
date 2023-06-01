<template>
  <div class="carousel-slide-container">
    <div class="col" @click="todetail">
      <div class="card" @click="todetail">
        <img :src="poster_path" class="card-img-top">
        <div class="card-body d-flex flex-column">
          <h5 class="card-title"><b>{{ movie.title }}</b></h5>
          <br>
          <p class="card-text"><small class="text-body-secondary">{{ movie.release_date }}</small></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props:{
    movie:Object
  },
  computed:{
    poster_path(){
      
      return `https://image.tmdb.org/t/p/original/${this.movie.poster_path}`
    }
  },
  methods:{
    todetail(){
      this.$router.push({'name':'detail',params:{'id':this.movie.movie_id}})
    }
  },
  created(){
    
  }
  

}
</script>


<style scoped>
.col {
  width: 50%;
  margin: auto;
  margin-left: 30%;
}

.card {
  width: 80%; /* 이미지 크기에 맞게 조정 */
  position: relative;
}

.card img {
  width: 100%; /* 이미지 크기에 맞게 조정 */
  height: auto;
  object-fit: cover;
}

.card-body {
  margin-top: 5%;
  width: 100%;
}

</style>