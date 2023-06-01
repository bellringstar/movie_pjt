<template>
    <div class="wrap">
        <div class="rc_item">
        <div class="card"  @click="update_modal">
        <img :src="poster" class="card-img" alt="Movie Poster">
            <div class="card-body">
                <h5 class="card-title">{{ this.detail.title }}</h5>
                <!-- <p class="card-text overflow-ellipsis">{{ this.detail.overview_kr }}</p> -->
                <p>{{ this.detail.release_date.substring(0, 4) }}</p>
            </div>
        </div>
    
        <!-- Modal -->
        <div :class="{modal : showModal}" v-show="showModal">
            <div class="modal-background" ><img :src="poster" class="card-img-top" alt="Movie Poster"></div>
            <div class="modal-content">
            <div class="box">
                <DetailItem :detail="this.detail" :is_liked="this.detail.is_liked?.includes(userId)" :bg_img="poster"/>
                <button @click="todetail">상세페이지로</button>
                <button class="modal-close is-large" @click="update_modal">닫기</button>
            </div>
            </div>

        </div>
    </div></div>
</template>

<script>
import axios from 'axios'
import DetailItem from './Detail/DetailItem.vue'
const secretKey = process.env.VUE_APP_SECRET_KEY

export default {
    components:{
        DetailItem
    },  
    props:{
        recommend:Object
    },
    computed:{
        poster(){
            if(this.detail.poster_path){
                return `https://image.tmdb.org/t/p/original/${this.detail.poster_path}`
            }else{
                return ''
            }
        },
        userId(){
            return parseInt(this.$decryptToken(localStorage.getItem('encryptedId'), secretKey),10)
        }
    },  
    data(){
        return{
            movie_id:this.recommend.movie_id,
            detail:{},
            showModal: false
        }
    },
    mounted(){
        this.get_recommend_movie()
        console.log(this.detail)
    },
    methods:{
        get_recommend_movie(){
            axios({
                method:'get',
                url:`http://127.0.0.1:8000/api/movies/${this.movie_id}/`,
                headers:{
                    Authorization: `Token ${this.$decryptToken(localStorage.getItem('encryptedToken'), secretKey)}`
                }
            })
            .then((res)=>{
                console.log(res.data)
                this.detail = res.data
            })
            .catch((err)=>{
                console.log(err)
            })
        },
        update_modal(){
            this.showModal = !this.showModal
        },
        todetail(){
            this.$router.push({'name':'detail', params:{'id':this.movie_id}})
        }
    }
}
</script>


<style scoped>

/* body */
.wrap{
    margin-top: 100px;
}

.rc_item{
    margin-top: 30px;}

/* movie_card */

.overflow-ellipsis {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  cursor: pointer;
}

.card {
    border: 0;
}

.card-body{
    background-color: black;
}

.card-body p{
    color: white;
}

.card-img {
    width: 200px;
    height: 300px;
    align-items: center;
}

.card-title {
    font-weight: 600;
    color: white;
}

/* modal */
.modal {
  transition: opacity 0.5s;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;

}

.modal-background {
  position: fixed;
  inset: 0;
  background-color: rgba(0, 0, 0, 0.5);
}

.modal-content {
  max-width: 800px;
  margin: 20px;
  background-color: rgba(255, 255, 255, 0.8);
  border-radius: 6px;
  padding: 20px;
}

.modal-close {
  position: absolute;
  top: 10px;
  right: 10px;
  z-index: 2;
  background-color: transparent;
  border: none;
  cursor: pointer;
}

.txt{
    color: white;
}

</style>