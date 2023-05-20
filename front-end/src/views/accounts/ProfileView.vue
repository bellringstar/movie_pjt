<template>
  <div class="Profile">
    <NavForm/>
    <SearchFrom/>
    <InfoView :user="user"/>
    <LikedItem/>
    <MyreviewItem/>
  </div>
</template>

<script>
import axios from 'axios'
import NavForm from '@/components/NavForm.vue'
import SearchFrom from '@/components/SearchFrom.vue'

import LikedItem from '@/components/Profile/LikedItem.vue'
import MyreviewItem from '@/components/Profile/MyreviewItem.vue'
import InfoView from '../../components/Profile/InfoView.vue'

export default {
  name: 'ProfileView',

  components:{
    NavForm,
    SearchFrom,
    InfoView,
    LikedItem,
    MyreviewItem,
  },

  data(){
    return{
      user: {}
    }
  },

  created(){
    const user_id = this.$route.params.id
    this.get_user(user_id)
  },

  // mounted(){
  //   this.get_user()
  // },

  methods: {
    get_user(user_id){
      axios({
        method:'get',
        url: `http://127.0.0.1:8000/api/${user_id}/`
      })
      .then((res)=>{
        console.log(res.data)
        this.user = res.data
      })
    },
}
}
</script>

<style>

</style>
