<template>

  <div class="wrap">
    <div class="bg_gradient"></div>
    <div class="MoReview">
      <!-- <LogoItem/> -->
      <!-- <SearchFrom/> -->
      <!-- <CreatereView/> -->
      <!-- <MoviereviewItem/> -->
      <img :src="bg_img" alt="bg_img" class="bg_img">
      <div class="content">
      <DetailItem :detail="this.detail" :is_liked="this.detail.is_liked?.includes(userId)" :bg_img="bg_img"/>
      <button @click="todetail">디테일로 가기</button>

      <br>
      
      <!-- <p class="sub_tit">REVIEW&COMMENT</p> -->
      <p v-if="reviews"><img src="@/assets/review.png" alt="Review" class="rv_img"></p>
      <p v-if="reviews.length === 0">리뷰가 없습니다. ㅜㅜ</p>
      <MoviereviewItem @review-updated="get_reviews" v-for="review in reviews"
        :key="review.id"
        :review="review"
        :is_liked="review.is_liked?.includes(userId)"
        />
  </div></div></div>
</template>

<script>
const secretKey = process.env.VUE_APP_SECRET_KEY

import axios from 'axios'

// import SearchFrom from '@/components/SearchFrom.vue'
// import LogoItem from '@/components/LogoItem.vue'
import MoviereviewItem from '@/components/Review/MoviereviewItem.vue'
// import CreatereView from '@/components/Review/CreatereView.vue'
import DetailItem from '@/components/Detail/DetailItem.vue'
export default {
  components:{
    // LogoItem,
    // SearchFrom,
    MoviereviewItem,
    DetailItem,
    // CreatereView,  
  },

  data() {
    return {
      reviews: {},
      movie_id : this.$route.params.id,
      detail:{}
    }
  },


  created(){
    this.get_reviews()
    this.get_detail()
  },
  computed:{
    userId(){
      const id = localStorage.getItem('encryptedId')
      return parseInt(this.$decryptToken(id, secretKey), 10);
    },
    bg_img() {
      return `https://image.tmdb.org/t/p/original/${this.detail.backdrop_path}`
    },
  },

  methods: {
    todetail(){
      this.$router.push({'name':'detail', params:{'id': this.movie_id}})
    },
    get_detail(){
      axios({
        method:'get',
        url: `http://127.0.0.1:8000/api/movies/${this.movie_id}/`,
        headers:{
          Authorization: `token ${this.$decryptToken(localStorage.getItem('encryptedToken'), secretKey)}`
        } 
      })
      .then((res)=>{
        // console.log(res.data)
        this.detail = res.data
      })
    },
    get_reviews() {
      axios({
        method:'get',
        url: `http://127.0.0.1:8000/api/${this.movie_id}/movie_review/`,
        headers:{
          Authorization: `Token ${this.$decryptToken(localStorage.getItem('encryptedToken'), secretKey)}`
      }  
      })

      .then(res => {
        this.reviews = res.data
        console.log("리뷰가져오기")
      })
      .catch(err => {
        this.reviews = []
        console.error('get_review 에러발생',err);
      })
    
  }
  }
}

</script>


<style scoped>
button {
  display: block;
  width: 100%;
  padding: 10px;
  font-family: 'Roboto';
  font-style: normal;
  font-weight: 500;
  /* font-weight: 400; */
  font-size: 16px;
  line-height: 28px;
  border-radius: 5px;
  border: none;
  background: #6DFF8F;
  color: rgb(0, 0, 0);
  cursor: pointer;
}
.content {
  padding: 10px 500px;
}
.bg_gradient {
  position: absolute;
  width: 100%;
  height: 200px;
  background-image: linear-gradient(to bottom, black,rgba(255, 255, 255, 0));
  margin-bottom: 20px;
  opacity: 0.8;
}
.bg_img {
  width: 100%;
  max-height: 350px;
  object-fit: cover;
  margin-bottom: 20px;
}
.review-board {
  margin-top: 20px;
}

.rv_img{
  object-fit: contain;
  width: 300px;
  height: 200px;
    /* text-align: left; */
  /* margin-left: 0; */
  /* margin-right: auto;  */
}

p {
  display: flex;
  margin-bottom: -30px;
  margin-left: 10px;
}

p.rv_img{
  justify-content:start;
  
}

</style>
