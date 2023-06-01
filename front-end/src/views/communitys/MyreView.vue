<template>
  <div class="MyReview">
    <LogoItem/>
    <SearchFrom/>
    <div class="content">
      <MyreviewItem v-for="review in reviews"
        :key="review.id"
        :review="review"
        @review-update="ReviewUpdate"
        />
      <h3 v-if="reviews.length===0">리뷰가 없어요. ㅠㅠ.</h3>
  </div></div>
</template>

<script>
const secretKey = process.env.VUE_APP_SECRET_KEY

import axios from 'axios'

import SearchFrom from '@/components/SearchFrom.vue'
import LogoItem from '@/components/LogoItem.vue'
import MyreviewItem from '@/components/Profile/MyreviewItem.vue'


export default {
  components:{
    LogoItem,
    SearchFrom,
    MyreviewItem,
  },
  data() {
    return {
      reviews: []
    }
  },
  created(){
    if(this.$store.getters.isLogin){
      this.get_reviews()
    }else{
      alert('로그인 필요')
    }
  },
  computed:{
    userid(){
      return this.$route.params.id
    }
  },
  methods: {
    get_reviews() {
      axios({
        method:'get',
        url: `http://127.0.0.1:8000/api/${this.userid}/user_review/`,
        headers:{
          Authorization: `Token ${this.$decryptToken(localStorage.getItem('encryptedToken'), secretKey)}`
      }  
      })
      .then((res)=>{
        console.log(res.data)
        this.reviews = res.data
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    ReviewUpdate(){
      console.log("변경 후 갱신")
      this.get_reviews()
    }
  }
}

</script>


<style scoped>
.review-board {
  margin-top: 20px;
}

.content {
  padding: 10px 500px;
}


</style>
