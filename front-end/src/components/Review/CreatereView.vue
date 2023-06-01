<template>
  <div class="CreateReview">
    <div class="crv">
    <form @submit.prevent="submit_review">
      <label for="title">제목:</label>
      <input type="text" id="title" v-model="title" required placeholder="눈과 귀가 즐거움으로 가득한, 꼭 봐야 할 영화!">
      <br>
      <label for="content">내용:</label>
      <textarea id="content" v-model="content" required placeholder="이 영화는 영상미가 정말 좋네요. BGM선곡도 완벽 그 자체였습니다. 2시간동안 정말 행복한 경험이었어요^^."></textarea>
      <br>
      <button type="submit">등록하기</button>
    </form>
  </div></div>
</template>
<script>
import axios from 'axios'
const secretKey = process.env.VUE_APP_SECRET_KEY

export default {
  name: 'CreateReview',

  data() {
    return {
      review: 0,
      title: '',
      content: ''
    }
  },

  props: {
    movie_id: String,
    user: Number
  },

  methods: {
    submit_review() {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/api/${this.movie_id}/reviews/`,
        data: {
          userid: this.user,
          title: this.title,
          content: this.content
        },
        headers:{
            Authorization: `Token ${this.$decryptToken(localStorage.getItem('encryptedToken'), secretKey)}`
          }
      })
        .then((res) => {
          console.log('리뷰생성',res.data)
          // console.log(this.movie_id)
          // console.log(this.review, res.data)
          this.title=''
          this.content=''
          this.$router.push({'name':'moreview', params:{'id':this.movie_id}})
        })
        .catch((err) => {
          console.log('리뷰 생성 실패', err)
        })
    }
  }
}
</script>
<style scoped>

.CreateReview {
  /* max-width: 400px; */
  /* margin: 0 20px; */

  padding: 10px;
  padding-right: 100px;
  display: inline-flex;
  /* justify-content: space-between; */
  gap: 15px;
}

.crv{
  display:flex;
  justify-content:flex-start;
  text-align: left;
  /* background: #ccc; */
  border-radius: 10px;
  width: 400px;
  height: 300px;
}


h1 {
  margin-bottom: 20px;
  text-align: center;
}

label {
  font-weight: bold;
  margin-left: 10px;
  margin-top: 5px;
}

#title {
    background: #f8f8f8;
  }

#content {
  background: #f8f8f8;
  margin-bottom: 10px;
  }

input,
textarea {
  margin-top: 5px;
  margin-left: 10px;
  width: 500px;
  margin-bottom: 10px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

button {
  display: block;
  margin: 0 auto;
  padding: 10px 20px;
  background-color: #3a5effb2;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #3A5FFF;
}
</style>