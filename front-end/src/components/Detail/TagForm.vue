<template>
  <div class="TagForm">
    <p class= "Tagbox" @click="changeTag">#{{ tag.title }} <span class="TagCount"> {{ all_tag_count }}</span></p>
    <!-- <p class="smt">이 태그를 선택한 사람</p> -->
    <!-- <p>{{ all_tag_count }}</p> -->
  </div>
</template>

<script>
import axios from 'axios'
const secretKey = process.env.VUE_APP_SECRET_KEY
export default {
  props: {
    tag: Object,
    movie_id: {
      type: [String, Number],
      required: true
    },
    username: String,
    renewTag: {
      type: Function,
      required: true
    }
  },
  created(){
    console.log(this.$store.state.tag_info)
  },
  computed: {
    tag_data() {
      return this.$store.state.tag_info
    },
    userid() {
      const secretKey = process.env.VUE_APP_SECRET_KEY
      const id = localStorage.getItem('encryptedId')
      const decryptedId = parseInt(this.$decryptToken(id, secretKey), 10);
      return decryptedId
    },
    all_tag_count() {
      return this.$store.state.tag_info.filter(tag => tag.tag_id === this.tag.id).length
    },
    my_tag_count() {
      return this.$store.state.tag_info.filter(tag => tag.tag_id === this.tag.id && tag.user === this.userid).length
    }
  },
  methods: {
    changeTag() {
      const isClicked = this.tag_data.some(item => item.tag_id === this.tag.id && item.user === this.userid)
      if (!this.$store.getters.isLogin) {
        console.log("로그인 필요")
      } else if (!isClicked) {
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/api/${this.movie_id}/tag/`,
          data: {
            tag_id: this.tag.id,
            username: this.username
          },
          headers:{
            Authorization: `token ${this.$decryptToken(localStorage.getItem('encryptedToken'), secretKey)}`
          }
        })
          .then(() => {
            console.log("태그 추가")
          })
          .then(() => {
            this.renewTag()
          })
      } else {
        axios({
          method: 'delete',
          url: `http://127.0.0.1:8000/api/${this.movie_id}/tag/`,
          data: {
            tag_id: this.tag.id,
            username: this.username
          },
          headers:{
            Authorization: `token ${this.$decryptToken(localStorage.getItem('encryptedToken'), secretKey)}`
          }
        })
          .then(() => {
            console.log("태그 삭제")
          })
          .then(() => {
            this.renewTag()
          })
      }
      this.renewTag()
    },
  }
}
</script>

<style scoped>
.Tagbox {
  text-align:none !important;
  margin: 20px;
  padding: 10px 10px 10px 10px;
  border-radius: 50px;
  display: flex;
  /* width: 120px; */
  text-align: center;
  /* align-items:; */
  /* justify-content: space-between; */
  /* background-color: #F5F5F5; */
  border: solid 1px #515050;
}

.TagCount {
  margin-left: 15px;
  /* display: flex; */
  /* justify-content:flex-end; */
  color: #B8B8B8;

}


.TagForm {
  padding: 5px;
  display: inline-flex;
  /* justify-content: space-between; */
  gap: 20px;
  /* display:flex !important; */
  /* justify-content:flex-start !important; */
  /* text-align: left !important; */
  /* margin-left: 5px; */
  /* padding: 10px; */
  /* width: 300px; */
}

.TagForm p {
  margin: 0;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
}

.TagForm p:first-child {
  color: #515050;
  font-weight: 500;
}

.smt {
  color: rgb(99, 99, 99);
  font-size: 12px !important;
}


</style>
