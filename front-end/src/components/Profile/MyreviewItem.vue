<template>
  <div class="review-page">
    <div class="review-content">
      <div class="review-item">
        <div class="review-header">
          <p class="review-movie">영화:{{ review.movie_title }}</p>
          <p class="review-title" v-if="!editing" >{{ review.title }}</p>
          <div>
            <span class="review-title" v-if="editing">제목 </span>
            <input class="review-title" v-if="editing" v-model="title" type="text" placeholder="제목">
          </div>
          <div class="review-body">
            <p v-if="!editing" class="review-content">{{ review.content }}</p>
            <span v-if="editing" class="review-con">내용 </span>
            <textarea v-if="editing" v-model="content" class="edit-content" placeholder="내용"></textarea>
          </div>
        </div>
        <div class="review-details">
          <div class="review-info">
            <!-- <p class="review-author" @click="toprofile">작성자: {{ review.username }}</p> -->
            <!-- <p class="review-data">작성일: {{ created }}</p> -->
            <!-- <p class="review-data">수정일: {{ updated }}</p> -->
            <p class="review-likes"> ❤ {{ like_cnt }}</p>
          </div>
          <!-- <div class="review-actions">
            <button class="comment-button" @click="get_comments" >댓글:{{ comments.length }} </button>
          </div> -->
        </div>

        <!-- <div class="comment-section" v-if="view_comment">
          <CommentItem @update_comment="update_comment" :comment="comment" v-for="comment in comments" :key="comment.id"/>
        </div> -->
        <div class="bt_edit">
        <button class="edit-button" @click="toggleEditing" v-if="review.user === loginId">{{ editing ? '완료' : '수정' }}</button>
        <button class="delete-button" @click="delete_review" v-if="review.user === loginId">삭제</button> 
        </div>
      </div>
    </div>
  </div>    
</template>

<script>
import axios from 'axios'


const secretKey = process.env.VUE_APP_SECRET_KEY
// import CommentItem from '../Review/CommentItem.vue'
export default {
  props: {
    review: Object
  },
  components:{
    // CommentItem,
  },
  data() {
    return {
      title:this.review.title,
      content:this.review.content,
      editing: false,
      like_cnt:this.review.is_liked.length,
    }
  },
  created(){
    // this.get_comments()
  },
  computed:{
    created() {
      const date = new Date(this.review.created_at)
      const year = date.getFullYear()
      const month = (date.getMonth() + 1).toString().padStart(2, '0')
      const day = date.getDate().toString().padStart(2, '0')
      const hours = date.getHours().toString().padStart(2, '0')
      const minutes = date.getMinutes().toString().padStart(2, '0')
      const seconds = date.getSeconds().toString().padStart(2, '0')
      return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`
    },
    updated() {
      const date = new Date(this.review.updated_at)
      const year = date.getFullYear()
      const month = (date.getMonth() + 1).toString().padStart(2, '0')
      const day = date.getDate().toString().padStart(2, '0')
      const hours = date.getHours().toString().padStart(2, '0')
      const minutes = date.getMinutes().toString().padStart(2, '0')
      const seconds = date.getSeconds().toString().padStart(2, '0')
      return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`
    },
    loginId(){
      return parseInt(this.$decryptToken(localStorage.getItem('encryptedId'), secretKey),10)
    },
  },
  methods: {

    toggleEditing() {
      if(this.title.trim() === '' && this.editing) {
        this.$toasted.show('제목을 입력해 주세요',{
          duration:1000,
          position: 'top-center',
          type:'error'
        })
        return        
      }
      if(this.content.trim() === '' && this.editing){
        this.$toasted.show('내용을 입력해 주세요',{
          duration:1000,
          position: 'top-center',
          type:'error'
        })
        return
      }
      if (this.editing) {
        axios({
          method: 'put',
          url: `http://127.0.0.1:8000/api/review/${this.review.id}/`,
          data: {
            title: this.title,
            content: this.content
          },
          headers:{
            Authorization: `Token ${this.$decryptToken(localStorage.getItem('encryptedToken'), secretKey)}`
          }
        })
          .then((res) => {
            console.log(res.data)
            console.log("변경성공")
            this.$emit('review-update')
          })
          .catch((err) => {
            console.log(err)
            
          })
      }
      this.editing = !this.editing
    },
    get_comments(){
        axios({
          method:'get',
          url:`http://127.0.0.1:8000/api/${this.review.id}/comment/`,
          headers:{
            Authorization: `Token ${this.$decryptToken(localStorage.getItem('encryptedToken'), secretKey)}`
          }
        })
        .then((res)=>{
          console.log("댓글목록", res.data)
          this.comments = res.data
          this.view_comment = !this.view_comment
        })
        .catch((err)=>{
          console.log(err)
        })
      },
    delete_review(){
      axios({
        method:'delete',
        url: `http://127.0.0.1:8000/api/review/${this.review.id}/`,
        headers:{
            Authorization: `Token ${this.$decryptToken(localStorage.getItem('encryptedToken'), secretKey)}`
          }
      })
      .then(()=>{
        console.log('삭제성공')
        this.$emit('review-update')
        
      })
      .then((err)=>{
        console.log(err)
      })
    },
    toprofile(){
      this.$router.push({'name':'profile' ,params:{'username':this.review.username}}).catch(()=>{location.reload()})
    },
  }
}
</script>

<style scoped>
.review-page {
  padding: 20px;
  text-align: left;
}

.review-header {
  /* text-align: center; */
  margin-bottom: 20px;
}

.page-title {
  font-size: 24px;
  font-weight: bold;
}

.review-item {
  display: flex;
  flex-direction: column;
  /* text-align: left; */
  border: 1px solid #ccc;
  border-radius: 10px;
  padding: 30px;
  margin-bottom: 20px;
  width: fit-content;
  max-width: 100%;
}

.review-title {
  display: flex;
  text-align: left;
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 10px;
}

.review-movie {
  margin-right: 10px;
  font-weight: 500;
  /* padding: 10px; */
  text-align: left;
  font-size: 20px;
  font-weight: bold;
  color: #333333;
}

.review-details {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
  flex-direction: column;
}

.review-info {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.review-author {
  font-size: 14px;
  color: #888;
  margin-right: 10px;
}

.review-date {
  font-size: 14px;
  color: #888;
  margin-right: 10px;
}

.review-likes {
  font-size: 14px;
  color: #888;
}

.review-actions {
  display: flex;
  align-items: center;
}

.like-button,
.comment-button {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 8px 12px;
  margin-right: 10px;
  cursor: pointer;
}

.like-button:hover,
.comment-button:hover {
  background-color: #0056b3;
}

.review-body {
  margin-top: 30px;
  margin-bottom: 10px;
}

.review-content {
  font-size: 16px;
}

.comment-section {
  margin-top: 20px;
}

.comment-input {
  margin-top: 20px;
}

.comment-input input {
  width: 200px;
  padding: 8px;
  border: 1px solid #ccc;
  margin-right: 10px;
}

.save-button,
.cancel-button {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 8px 12px;
  cursor: pointer;
}

.save-button:hover,
.cancel-button:hover {
  background-color: #0056b3;
}


.bt_edit{
  display: flex;
}

.edit-button,
.delete-button {
  color: #007bff;
  margin-top: 10px;
  cursor: pointer;
  border-radius: 10px;
  display:inline-flex ;
  justify-content:flex-end ;
  align-items: flex-end;
}

.edit-button +
.delete-button {
    padding: 0px 20px;
   }


.edit-button:hover,
.delete-button:hover {
  font-weight: bold;
}

input{
  border: 1px solid #ccc;
}

.comment-input input {
  width: 200px;
  padding: 8px;
  border: 1px solid #ccc;
  margin-right: 10px;
}

input,textarea{
width: 300px;
padding: 8px;
border-radius: 5px;
border: solid 1px  #B8B8B8;
}

.review-con{
font-size: 20px;
font-weight: bold;
display: flex;
text-align: center;
justify-content: flex-start;
}

</style>