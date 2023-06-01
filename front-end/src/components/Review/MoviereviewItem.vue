<template>
  <div class="review-page">
    <div class="review-content">
      <div class="review-item">

        <p class="review-author" @click="toprofile">{{ review.username }}님이 작성한 리뷰</p>
        <p class="review-likes">👍 {{ like_cnt }} 명에게 이 리뷰가 도움이 됐어요.</p><hr>

        <div class="review-header">
          <!-- <p class="review-movie">영화:{{ review.movie_title }}</p> -->
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

        <div>
        <button class="edit-button" @click="toggleEditing" v-if="review.user === loginId">{{ editing ? '저장' : '수정' }}</button>
        <button class="delete-button" @click="delete_review" v-if="review.user === loginId">삭제</button> 
        </div>
      
      </div>  
        <div class="dt">
        <p class="review-data">작성일: {{ created }}</p>
        <p class="review-data">수정일: {{ updated }}</p>
        </div>
        
        <div class="review-details">
          <div class="review-info">
            
          </div>

          <div class="review-actions">
            <button class="like-button" @click="like" v-if="review.user != this.$store.state.userid">
              {{!isLiked? '❤' : 'X'}}
            </button>
            <button class="comment-button" @click="get_comments" >💬 {{ comments.length }} </button>
          


          <div class="comment-input" v-if="comment_editing">
            <input v-if="comment_editing" v-model="newComment" type="text" placeholder="댓글을 입력하세요">
            <button class="save-button" @click="saveComment">저장</button>| 
            <button class="cancel-button" @click="toggleCommentEditing">취소</button>
          </div>
            <button v-else @click="toggleCommentEditing" class="rp_upd" >댓글 작성</button>
        </div>
        <div class="comment-section" v-if="view_comment">
            <CommentItem @update_comment="update_comment" :comment="comment" v-for="comment in comments" :key="comment.id"/>
          </div>
      </div>



      
    </div>
  </div>    
</template>

<script>

const secretKey = process.env.VUE_APP_SECRET_KEY
import axios from 'axios'
import CommentItem from './CommentItem.vue'
export default {
  name: 'MoviereviewItem',
  props:{
    review:Object,
    is_liked:Boolean,
  },
  components:{
    CommentItem,
  },
  data(){
    return{
      like_cnt:this.review.is_liked.length,
      editing: false,
      comments:[],
      view_comment:true,
      comment_editing:false,
      newComment:'',
      isLiked:this.is_liked,
      title:this.review.title,
      content:this.review.content
    }
  },
  created(){
    this.get_comments()
  },
  computed:{
    loginId(){
      return parseInt(this.$decryptToken(localStorage.getItem('encryptedId'), secretKey),10)
    },
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
    userid(){
      if(localStorage.getItem('encryptedId')){
        return parseInt(this.$decryptToken(localStorage.getItem('encryptedId'), secretKey),10)
      }
      return null
    },

  },
  
      
  methods:{
    toprofile(){
      this.$router.push({'name':'profile', params:{'username':this.review.username}})
    },
    toggleCommentEditing() {
        this.comment_editing = !this.comment_editing;
        this.newComment = ''; 
      },
      saveComment(){
        axios({
          method:'post',
          url:`http://127.0.0.1:8000/api/${this.review.id}/comment/`,
          data:{
            userid:this.loginId,
            content:this.newComment
          },
          headers:{
            Authorization: `Token ${this.$decryptToken(localStorage.getItem('encryptedToken'), secretKey)}`
          }
        })
        .then((res)=>{
          console.log("댓글 생성")
          this.content = res.data.content
          this.newComment = ''
          this.comment_editing = false
          this.view_comment = !this.view_comment
          this.get_comments()
        })
        .catch((err)=>{
          console.log("실패", err)
        })
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
    like(){
      if(this.$store.getters.isLogin){    
        axios({
          method:'POST',
          url:`http://127.0.0.1:8000/api/like_review/${this.review.id}/`,
          data:{
            user_id: this.loginId
          },
          headers:{
            Authorization: `Token ${this.$decryptToken(localStorage.getItem('encryptedToken'), secretKey)}`
          }
        })
        .then((res)=>{
          console.log("성공")
          this.isLiked = (res.data.is_liked?.includes(this.userid))
          return res.data.movie_id
        })
        .then((movieIdx)=>{
          axios({
            method:'GET',
            url: `http://127.0.0.1:8000/api/${movieIdx}/movie_review/`,
            headers:{
              Authorization: `Token ${this.$decryptToken(localStorage.getItem('encryptedToken'), secretKey)}`
          } 
          })
          .then((res)=>{
            const review_data = res.data.filter(item=>item.id === this.review.id)
            console.log(review_data)
            this.like_cnt = review_data[0].is_liked.length
          })
        })
        .catch((err)=>{
          console.log(err)
        })
      }
      else{
        alert("로그인 해주세요")
      }
    },
    showmessage(text){
      this.$toasted.show(text,{
        duration:1000,
        position: 'top-center',
        type:'error'
      })
    },
    toggleEditing() {
      if(this.title.trim() === '' && this.editing){
        this.showmessage('제목을 입력해주세요')
        return
      }
      if(this.content.trim() === '' && this.editing){
        this.showmessage('내용을 입력해주세요')
        return
      }
      if (this.editing) {
        axios({
          method: 'put',
          url: `http://127.0.0.1:8000/api/${this.review.movie_id}/reviews/`,
          data: {
            id: this.review.id,
            title: this.title,
            content: this.content
          },
          headers:{
            Authorization: `Token ${this.$decryptToken(localStorage.getItem('encryptedToken'), secretKey)}`
          }
        })
          .then(() => {
            console.log('수정성공')
            this.$emit('review-updated')
          })
          .catch((err) => {
            console.log('수정실패',err)
          })
      }
      this.editing = !this.editing
    },
    delete_review(){
      axios({
        method:'delete',
        url: `http://127.0.0.1:8000/api/${this.review.movie_id}/reviews/`,
        data:{
          id: this.review.id
        },
        headers:{
            Authorization: `Token ${this.$decryptToken(localStorage.getItem('encryptedToken'), secretKey)}`
          }
      })
      .then(()=>{
        console.log('삭제성공')
        this.$emit('review-updated')
      })
      .catch((err)=>{
        console.log('삭제실패',err)
      })
    },
    update_comment(){
      this.get_comments()
      this.view_comment = !this.view_comment
    }
  },


}

</script>

<style scoped>
.review-page {
  padding: 20px;
}

.review-header {
  /* text-align: center; */
  margin-bottom: 20px;
}

.page-title {
  font-size: 24px;
  font-weight: bold;
}

.dt p{
  display: inline;
  /* text-align: right; */
}

.dt{
  text-align: end;
  color: #B8B8B8;
  margin-bottom: 10px;
}

.review-data + .review-data {
  margin-left: 20px;
}

.rp_upd{
  display: flex;
  justify-content: end;
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 8px 12px;
  cursor: pointer;
  border-radius: 7px;
}

.rp_upd:hover {
  background-color: #0056b3;
}

.review-item {
  text-align: left;
  border: 1px solid #ccc;
  border-radius: 10px;
  padding: 30px;
  margin-bottom: 20px;
}

.review-title{
  display: flex;
  font-size: 20px;
  font-weight: bold;
}

.review-con{
font-size: 20px;
font-weight: bold;
display: flex;
text-align: center;
justify-content: flex-start;
}

.review-movie {
  font-size: 16px;
  color: #888;
  margin-bottom: 10px;
}

.review-details {
  display: block;
  /* justify-content: space-between; */
  align-items: center;
  margin-bottom: 10px;
}

.review-info {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.review-author {
  margin-right: 10px;
  font-weight: 500;
  /* padding: 10px; */
  text-align: left;
  font-size: 20px;
  font-weight: bold;
  color: #333333;
}

.review-date {
  font-size: 14px;
  color: #888;
  margin-right: 10px;
}

.review-likes {
  margin-top: -7px;
  font-size: 14px;
  color: #888;
}

.review-actions {
  display: flex;
  align-items: center;
  justify-content: flex-end;
}

.like-button{
  background-color: #FF4081;
  color: #fff;
  border: none;
  padding: 8px 12px;
  margin-right: 10px;
  cursor: pointer;
  border-radius: 5px;
}

.comment-button {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 8px 12px;
  margin-right: 10px;
  cursor: pointer;
  border-radius: 5px;
}

.like-button:hover{
  background-color: #ff105f;
}
.comment-button:hover {
  background-color: #0056b3;
}

.review-body {
  margin-top: 10px;
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

.edit-button,
.delete-button {
  /* background-color: #dc3545; */
  color: #007bff;
  /* border: none; */
  /* padding: 8px 12px; */
  margin-top: 10px;
  cursor: pointer;
  border-radius: 10px;
  /* margin-left: 10px; */
  display:inline-flex !important;
  justify-content:flex-end !important;
  /* padding: 10px; */
}

.edit-button +
.delete-button {
    padding: 0px 20px;
   }


.edit-button:hover,
.delete-button:hover {
  /* background-color: #a51c2d; */
  /* border: #007bff solid 1px; */
  /* border-radius: 20px; */
  /* padding: 10px; */
  font-weight: bold;
}

input.review-title,textarea.edit-content{
padding: 5px;
border-radius: 10px;
border: solid 1px  #B8B8B8;
}

input{
  border: 1px black solid;
}

</style>