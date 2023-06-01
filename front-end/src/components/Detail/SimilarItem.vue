<template>
  <div class="col SimilarItem smr">
    <div class="card">
      <div class="card_in">
      <img :src="poster" class="card-img">
      <p smr_txt>{{ similar.title }}</p>
    </div></div>
  </div>
</template>

<script>
export default {
  props: {
    similar: Object
  },
  computed: {
    poster() {
      return `https://image.tmdb.org/t/p/w600_and_h900_bestv2${this.similar.poster_path}`
    }
  }
}
</script>

<style scoped>
.SimilarItem {
  margin: 10px auto; 
  background-color: #F5F5F5;
  border-radius: 10px;
  /* box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15); */
  width: 160px;
}

.card{
  border: none;
  justify-content: space-between;
}

.SimilarItem p {
  margin: 0; 
  padding: 10px;
  font-size: 14px;
  font-weight: 300;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.smr_txt{
  text-align: center;
}

.card_in img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}


</style>
