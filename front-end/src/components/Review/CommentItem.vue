
<template>
  <div class="review-page">
    <div class="review-content">
      <div class="review-item">
        <p class="review-author" @click="toprofile">{{ this.username }}님이 작성한 댓글</p>

        <div class="review-header">
          <!-- <p class="review-movie">영화:{{ review.movie_title }}</p> -->
          <p class="review-title" v-if="!editing" >{{ this.content }}</p>
          <div v-if="editing">
            <input v-model="content" type="text" placeholder="수정할 댓글을 입력하세요">
          </div>
        </div>

        <div>
        <button class="edit-button" v-if="loginUser === this.user" @click="toggleEditing">{{ editing ? '저장' : '수정' }}</button>
        <button class="delete-button" v-if="loginUser === this.user" @click="deleteComment">삭제</button> 
        </div>
      
      </div>  
        <div class="dt">
        <p class="review-data">작성일: {{ created }}</p>
        <p class="review-data">수정일: {{ updated }}</p>
        </div>
        
        <div class="review-details">
          <div class="review-info">
            
          </div>

          
      </div>



      
    </div>
  </div>    
</template>

<script>
const secretKey = process.env.VUE_APP_SECRET_KEY
import axios from 'axios'
export default {
    name:'CommentItem',
    props:{
      comment:Object
    },
    created(){
      this.get_user()
    },
    data(){
      return{
        commentId : this.comment.id,
        content: this.comment.content,
        created_at: this.comment.created_at,
        updated_at: this.comment.updated_at,
        review_id: this.comment.review_id,
        user: this.comment.user,
        username:'',
        editing: false,
      }
    },
    computed:{
      loginUser(){
        return parseInt(this.$decryptToken(localStorage.getItem('encryptedId'), secretKey),10)
      },
      created() {
        const date = new Date(this.created_at)
        const year = date.getFullYear()
        const month = (date.getMonth() + 1).toString().padStart(2, '0')
        const day = date.getDate().toString().padStart(2, '0')
        const hours = date.getHours().toString().padStart(2, '0')
        const minutes = date.getMinutes().toString().padStart(2, '0')
        const seconds = date.getSeconds().toString().padStart(2, '0')
        return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`
      },
      updated() {
        const date = new Date(this.updated_at)
        const year = date.getFullYear()
        const month = (date.getMonth() + 1).toString().padStart(2, '0')
        const day = date.getDate().toString().padStart(2, '0')
        const hours = date.getHours().toString().padStart(2, '0')
        const minutes = date.getMinutes().toString().padStart(2, '0')
        const seconds = date.getSeconds().toString().padStart(2, '0')
        return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`
      }
    },
    methods:{
      toggleEditing() {
        this.editing = !this.editing;
        this.newComment = this.content;
    },

    showmessage(text){
      this.$toasted.show(text,{
        duration:1000,
        position: 'top-center',
        type:'error'
      })
    },
      
      updateComment(){
        if(this.content.trim()==='' && this.editing){
          this.showmessage('내용을 입력해주세요')
          return
        }
        axios({
          method:'put',
          url:`http://127.0.0.1:8000/api/${this.review_id}/comment/`,
          data:{
            userid: this.loginUser,
            content:this.content,
            commentid: this.commentId
          },
          headers:{
            Authorization: `token ${this.$decryptToken(localStorage.getItem('encryptedToken'), secretKey)}`
          }
        })
        .then((res)=>{
            console.log("수정 성공")
            this.content = res.data.content
            this.editing = false;
          })
          .catch((err)=>{
            console.log("수정실패", err)
          })
      },
      deleteComment(){
        axios({
          method:'delete',
          url:`http://127.0.0.1:8000/api/${this.review_id}/comment/`,
          data:{
            userid: this.loginUser,
            commentid: this.commentId
          },
          headers:{
            Authorization: `token ${this.$decryptToken(localStorage.getItem('encryptedToken'), secretKey)}`
          }
        })
        .then((res)=>{
          console.log("삭제 성공", res)
          this.$emit('update_comment')
        })
        .catch((err)=>{
          console.log(err)
        })
      },
      get_user(){
        axios({
          method:'get',
          url: `http://127.0.0.1:8000/api/${this.user}/`,
          headers:{
            Authorization: `token ${this.$decryptToken(localStorage.getItem('encryptedToken'), secretKey)}`
          }
        })
        .then((res)=>{
          console.log(res.data)
          this.username = res.data.username
          console.log(this.user)
        })        
      },
      toprofile(){
      this.$router.push({'name':'profile', params:{'username':this.username}})
    },   
    }
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
  font-weight: 100;
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