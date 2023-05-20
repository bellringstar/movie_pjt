<template>
  <div>
    <div class="col">
      <img :src="bg_img" alt="bg_img" class="bg_img">
      <img :src="pos_img" alt="pos_img" class="pos_img">
      <p class="title">{{ detail.title }}</p>
      <p class="overview">{{ detail.overview_kr }}</p>
      <div>
        <p class="release_date"> {{ detail.release_date }}</p>ㅣ
        <p class="runtime">{{ detail.runtime }}분</p> 
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
      return `https://image.tmdb.org/t/p/w600_and_h900_bestv2${this.detail.backdrop_path}`
    },
    pos_img() {
      return `https://image.tmdb.org/t/p/w600_and_h900_bestv2${this.detail.poster_path}`
    }
  },
}

</script>

<style scoped>
/* .bg_img{
  width: 1920px;
  height: 705px;
}

.pos_img{
  width: 328px;
  height: 491px;
} */

.col {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 20px;
}

.bg_img {
  width: 100%;
  max-height: 400px;
  object-fit: cover;
}

.pos_img {
  width: 164px;
  height: 246px;
  margin-top: -100px;
}

.title {
  font-size: 24px;
  font-weight: bold;
  margin-top: 20px;
}

.overview {
  margin-top: 10px;
}

.details {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}

.release_date,
.runtime {
  font-size: 14px;
  font-weight: bold;
}

</style>


