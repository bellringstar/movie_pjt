<template>
    <div class="CreatereView">
      <h1>Create Review</h1>
      <form @submit.prevent="submitReview">
        <label for="title">Title:</label>
        <input type="text" id="title" v-model="review.title" required>
        <br>
        <label for="content">Content:</label>
        <textarea id="content" v-model="review.content" required></textarea>
        <br>
        <button type="submit">Submit</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios'

  export default {
    name : 'CreatereView',

    components:{
    },

    data(){
      return{
        // review : {},
      }
    },

    methods: {
      submit_review() {
            axios({
              method:'get',
              url: `http://127.0.0.1:8000/api/comment/`
            })
            .then((res)=>{
              console.log(res)
              this.review = res.data
              this.$router.push('/reviews/' + res.data.id);
            })
    }
  }
}


  </script>
  
  <style scoped>
  h1 {
    margin-bottom: 20px;
  }
  label {
    font-weight: bold;
  }
  input, textarea {
    width: 100%;
    margin-bottom: 10px;
  }
  button {
    padding: 10px 20px;
  }
  </style>
  