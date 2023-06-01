<template>
  <div class="banner">
      <img src="@/assets/ban.png" class="d-block"  alt="banner1"
      @click="handle_click1()">
</div>
</template>

<script>
export default {

  name : 'BannerItem',

  methods:{
  handle_click1(){
      this.$router.push({"name":"recommend"})
  },
  }
}
</script>

<style scoped>
.banner{
  width: 1200px;
  display: flex;
  align-items: center !important;
  text-align: center !important;
  justify-content: center !important; 
  margin-bottom: 100px;
  /* border-radius: 5%; */

}

img{
  width: 1100px;
  align-items: center !important;
  text-align: center !important;
  justify-content: center !important; 
  /* border-radius: 5%; */
}

/* .carousel-item-next, .carousel-item-prev, .carousel-item.active {
    display: inline-block;
} */

/* .carousel-inner{
  align-items: center !important;
  text-align: center !important;
  justify-content: center !important; 
}

.carousel-item {
  margin-right: -32%;
} */

</style>