<template>
  <div class="col" >
    <div class="card">
      <img :src="poster" class="card-img-top">
      <div class="card-body d-flex flex-column">
        <p class="card-title"><b>{{ movie.title }}</b></p>
        <p class="mv_info">{{ movie.release_date.slice(0,4) }}</p>
      </div>
   </div>
  </div>
  </template>

<script>
export default {
  name:'MovieItem',
  props:{
    movie:Object
  },
  computed: {
        poster() {
        return `https://image.tmdb.org/t/p/w600_and_h900_bestv2${this.movie.poster_path}`
      }
    },
  
}
</script>

<style scoped>
.card{ margin: 40px 75px 40px 0px; border: white;}
/* .sec{margin-left: 40px ;} */

.card-title{
text-align: left; 

font-family: 'Roboto';
font-style: normal;
font-weight: 500;
font-size: 15px;
line-height: 18px;
color: #333333;

overflow: hidden;
text-overflow: ellipsis;
white-space: nowrap;

}

.mv_info{
text-align: left;
margin: 0;

font-family: 'Roboto';
font-style: normal;
font-weight: 400;
font-size: 12px;
line-height: 14px;
color: #616161;
}

.sec{

}

</style>


