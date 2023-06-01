<template>
  <div>
    
    <!-- <img :src="bg_img" alt="bg_img" class="bg_img"> -->
    <div class="col">
      <div class="details">
        <div class="poster-info">
          <img :src="pos_img" alt="pos_img" class="pos_img">
          <div class="movie-info">
            <p class="title">{{ detail.title }} <button @click="like_movie" class="like_btn">{{!isLiked? '❤ 좋아요' : '❤ 좋아요 취소'}}</button> </p>
              <div class="movie-details">
                <p class="release_date">개봉일: {{ detail.release_date }}</p>
                <p class="runtime">상영 시간: {{ detail.runtime }}분</p> 
              </div>
            <p class="overview">{{ detail.overview_kr }}</p>
        
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const secretKey = process.env.VUE_APP_SECRET_KEY
export default {
  name: 'DetailItem',
  props: {
    detail: Object,
    is_liked: Boolean,
    bg_img: String
  },
  data(){
    return{
      isLiked:this.is_liked
    }
  },
  computed: {
    // bg_img() {
    //   return `https://image.tmdb.org/t/p/w600_and_h900_bestv2${this.detail.backdrop_path}`
    // },
    pos_img() {
    
      return `https://image.tmdb.org/t/p/w600_and_h900_bestv2${this.detail.poster_path}`
    },
    userid(){
      
      const id = localStorage.getItem('encryptedId')
      return parseInt(this.$decryptToken(id, secretKey), 10);
    },

  },
  methods: {
    like_movie() {
      if (this.$store.getters.isLogin) {    
        axios({
          method: 'POST',
          url: `http://127.0.0.1:8000/api/like_movie/${this.userid}/`,
          data: {
            movie_id: this.detail.movie_id
          },
          headers:{
            Authorization: `Token ${this.$decryptToken(localStorage.getItem('encryptedToken'), secretKey)}`
          }
        })
        .then((res) => {
          console.log(res.data)
          this.isLiked = (res.data.is_liked?.includes(this.userid))
        })
        .catch((err) => {
          console.log(err)
          console.log('좋아요 실패')
        })
      } else {
        alert("로그인 해주세요")
      }
    },
  },

}
</script>

<style scoped>
.col {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 20px;
}

.details {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  margin-bottom: 20px;
}

.poster-info {
  display: flex;
}

.pos_img {
  width: 190px;
  height: 280px;
  border-radius: 10px;
  margin-right: 20px;
}

.movie-info {
  text-align: left;
}

.title {
  font-size: 24px;
  font-weight: bold;
  margin-top: 0;
  margin-bottom: 10px;
}

.overview {
  margin-top: 0;
  margin-bottom: 20px;
}

.movie-details {
  display: flex;
  flex-wrap: wrap;
  
}

.release_date,.runtime {
  font-size: 16px;
  font-weight: 600;
  margin-right: 20px;
  color: #515050;
}

.bg_img {
  position: relative;
  width: 100%;
  max-height: 400px;
  object-fit: cover;
  margin-bottom: 20px;
}

.like_btn {
  position: relative;
  top: -4px;
  border: solid 1px #FF4081;
  color: #FF4081;
  /* border: none; */
  padding: 5px 10px;
  border-radius: 20px;
  margin-bottom: 5px;
  cursor: pointer;
  font-size: 13px;
}

.ok_like_btn {
  position: relative;
  top: -4px;
  background-color: #FF4081;
  color: white;
  border: none;
  padding: 5px 10px;
  border-radius: 20px;
  margin-bottom: 5px;
  cursor: pointer;
  font-size: 13px;
}

</style>
