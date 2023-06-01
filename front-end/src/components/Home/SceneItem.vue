<template>
  <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="true">
  <div class="carousel-indicators">
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
  </div>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="@/assets/banner1.png" class="banner d-block"  alt="banner1"
      @click="handle_click1()">
    </div>
    <div class="carousel-item">
      <img src="@/assets/banner2.jpg" class="banner d-block" alt="banner2"
      @click="handle_click2()">
    </div>
    <div class="carousel-item">
      <img src="@/assets/banner3.jpg" class="banner d-block" alt="banner3"
      @click="handle_click3()">
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
</template>

<script>
export default {

  name : 'BannerItem',

  methods:{
  handle_click1(){
      this.$router.push('/detail/916224').catch(()=>{
        this.$router.push('/error')
      })
  },
  handle_click2(){
    this.$router.push('/detail/597').catch(()=>{
      this.$router.push('/error')
    })
  },
  handle_click3(){
    this.$router.push('/detail/8966').catch(()=>{
      this.$router.push('/error')
    })
    }
  }
}
</script>

<style>
.banner{
  /* width: 1200px; */
  /* align-items: center !important; */
  /* text-align: center !important; */
  /* justify-content: center !important;  */
}

.carousel-item-next, .carousel-item-prev, .carousel-item.active {
    /* display: inline-block; */
}

.carousel-inner{
  /* align-items: center !important; */
  /* text-align: center !important; */
  /* justify-content: center !important;  */
}

.carousel-item {
  /* float:none !important; */
  /* align-items: center !important; */
  /* text-align: center !important; */
  /* justify-content: center !important;  */
  /* margin-right: -32%; */
}

</style>