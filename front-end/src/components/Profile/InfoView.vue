<template>
  <div class="InfoItem">
    <div class="content" style="padding-right: 0px; padding-left: 0px">

      <!-- <p class="tit">{{ user.username }} </p> -->
      <h3 class="main_tit">{{ username }} 님의 프로필페이지</h3>

      <!-- 프로필 이미지 -->
      <div class="pf_ctn">
        <img :src="profile_user.profile_image?'http://127.0.0.1:8000' + profile_user.profile_image: default_profile_image" alt="프로필 이미지" class="pf_img"/>
      </div>


      <!-- 프로필이미지 업로드 -->
      <div class="pf_up">
        <div v-if="isEditingProfileImage">
          <input type="file" @change="uploadProfileImage" />
          <button @click="cancelEditingProfileImage">취소</button>
        </div>
        <div v-else>
          <button @click="startEditingProfileImage" v-if="user.username === this.loginUser">프로필 이미지 수정</button>
        </div>
      </div>
      

      <!-- 자기소개 -->
      <div class="introduction-contatiner" >
        <div v-if="!isEditingIntroduction">
          <h3 data-v-cf794c2e="" class="introduction-heading" style="margin-right: 0px;border-right-width: 10px; width: 20%;">자기소개</h3>
          <div class="introduction-content introduction-box" v-if="user.self_introduction">{{ user.self_introduction }}</div>
          <div v-else class="introduction-box">자기소개를 입력해 주세요</div>
          <button @click="startEditingIntroduction" class="itd_btn" v-if="user.username === this.loginUser">자기소개 수정</button>
        </div>
      
        <div v-else>
          <p>
            <textarea class="introduction-box" v-model="introduction" :placeholder="user.self_introduction"/>
          </p>
          <button @click="saveIntroduction">저장</button>
        </div>
      </div>
        


        <!-- 리뷰 보러가기 -->
        <div>
          <button class="review-btn" @click="myreview">리뷰 더 보기</button>
        </div>
        
    </div>
  </div>
</template>

<script>
const secretKey = process.env.VUE_APP_SECRET_KEY

import axios from 'axios';

export default {
  props: {
    username: String,
  },
  data() {
    return {
      introduction: '',
      isEditingProfileImage: false,
      isEditingIntroduction: false,
      loginUser:'',
      user:{}
    }
  },
  created(){
    this.get_profile_info()

    this.loginUser = this.$decryptToken(localStorage.getItem('encryptedUsername'), secretKey)
  },
  computed:{
    profile_user(){
      return this.$store.state.profile_user
    },
    default_profile_image(){
        // return 'http://127.0.0.1:8000' + this.user.profile_image

        return require('@/assets/1.png')
      }
    }   
  ,

  mounted() {
    const randomChars = ['😘', '🥰', '😎', '😋', '😍'];
    const randomChar = randomChars[Math.floor(Math.random() * randomChars.length)]
    document.querySelector('.tit')?.setAttribute('data-random-char', randomChar)

    if (this.user) {
      this.introduction = this.user.self_introduction;
      // this.profile_image = 'http://127.0.0.1:8000' + this.user.profile_image;
    }
  },

  methods: {
    uploadProfileImage(event) {
      const file = event.target.files[0];
      const formData = new FormData();
      formData.append('profile_image', file);

      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/api/${this.user.username}/`,
        data: formData,
        headers: {
          'Content-Type': 'multipart/form-data',
          Authorization: `token ${this.$decryptToken(localStorage.getItem('encryptedToken'), secretKey)}`
        },

      })
        .then((res) => {
          console.log(res.data)
          this.profile_image = 'http://127.0.0.1:8000' + res.data.profile_image;
          this.isEditingProfileImage = false;
          this.get_profile_info()
        })
        .catch((err) => {
          console.error('프로필 사진 업로드 에러 발생', err);
        });
    },
    startEditingIntroduction() {
      this.isEditingIntroduction = !this.isEditingIntroduction;
    },
    startEditingProfileImage() {
      this.isEditingProfileImage = true;
    },
    cancelEditingProfileImage() {
      this.isEditingProfileImage = false;
    },
    saveIntroduction() {
      axios({
        method:'put',
        url: `http://127.0.0.1:8000/api/${this.user.username}/`,
        data:{
          self_introduction: this.introduction,
        },
        headers:{
            Authorization: `Token ${this.$decryptToken(localStorage.getItem('encryptedToken'), secretKey)}`
          }
      })
        .then((res) => {
          console.log('자기소개 수정 완료', res.data);
          this.isEditingIntroduction = !this.isEditingIntroduction;
          this.get_profile_info()
        })
        .catch((err) => {
          console.error('자기소개 수정 에러 발생', err);
        });
    },
    myreview(){
      this.$router.push({'name':'myreview', params:{'id':this.user.id}}).catch(()=>{location.reload()})
    },
    get_profile_info(){
      axios({
        method:'get',
        url:`http://127.0.0.1:8000/api/${this.username}/`,
        headers:{
            Authorization: `Token ${this.$decryptToken(localStorage.getItem('encryptedToken'), secretKey)}`
        }
      })
      .then((res)=>{
        this.$store.dispatch('get_profile_user', res.data)
        this.user = res.data
      })
      .catch((err)=>{
        console.log('정보가져오기 싪패',err)
      })
    }
  }}

</script>


<style scoped>

/* 영역 */
html,body {height: 100%;}
.wrap {height: 100%; display: flex; flex-direction: column; align-items: center;}

.InfoItem {
  /* background-color: #f1f1f1; */
  padding: 0 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* 타이틀 */

/* .tit {
  font-size: 24px;
  font-weight: bold;
  color: #333;
  margin-bottom: 20px;
} */

.tit {margin: 5px 0; font-style: normal; font-weight: 500; font-size: 28px; line-height: 38px; color: #3A5FFF;}
.tit::after {
  content: attr(data-random-char);
  font-size: 22px;
}

/* 정보 */
.pf_ctn .pf_up {
  /* margin-left: 50px; */
  margin-bottom: 10px;
  width: 150px;
  height: 150px;
  overflow: hidden;
  border-radius: 50%;
  border: solid 5px black;
  align-content: center;
  object-fit: cover;
}
.pf_img {
  width: 150px;
  height: 150px;
  overflow: hidden;
  border-radius: 50%;
  align-content: center;
  text-align: center;
  justify-content: center;
  align-items: center;
  justify-items: center;
  object-fit: cover;
}

.InfoItem-introduction-container {
  width: 80%;
  height: 20%;
  border: 1px solid black;
  padding: 10px;
  margin-top: 20px;
  display: flex;
  flex-direction: column;
}

.introduction-box {
  border: 1px solid black;
  padding: 10px;
  width: 400px;
  height: 200px;
  text-align: left;
  margin: 10px;
}

.introduction-heading {
  font-size: 16px;
  margin-bottom: 10px;
}

.introduction-content {
  font-size: 14px;
}

textarea {
  width: 100%;
  height: 100%;
  resize: none;
  padding: 5px;
  margin-bottom: 10px;
}

button {
  padding: 10px 20px;
  background-color: #333;
  color: #fff;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
}


.itd_btn{
  border: solid 1px black;
}


.input_field {
  margin-bottom: 10px;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 14px;
}

.btn {
  padding: 10px 20px;
  background-color: #333;
  color: #fff;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
}

button{
  margin: 5%;
}

.review-btn{
  margin-top: 1%;
}



@media screen and (max-width: 768px) {
  .MyreviewItem {
    padding: 10px;
  }

  .info {
    flex-direction: column;
    align-items: flex-start;
  }

  .input_field {
    width: 100%;
  }

  .btn {
    width: 100%;
    margin-top: 10px;
  }
}


</style>
