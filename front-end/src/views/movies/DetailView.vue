<template>
  <div class="Detail">
    <h1>Detail</h1>
    <NavForm/>
    <SearchFrom/>
<<<<<<< HEAD
    <DetailItem/>
=======
    <DetailItem :detail="this.detail"/>
>>>>>>> front
    <SimilarItem/>
    <TagForm/>
    <YoutubeItem/>
  </div>
</template>

<script>
import axios from 'axios'

import NavForm from '@/components/NavForm.vue'
import SearchFrom from '@/components/SearchFrom.vue'

import SimilarItem from '@/components/Detail/SimilarItem.vue'
import TagForm from '@/components/Detail/TagForm.vue'
import YoutubeItem from '@/components/Detail/YoutubeItem.vue'
import DetailItem from '@/components/Detail/DetailItem.vue'

export default {
  name : 'detailView',

  components:{
    NavForm,
    SearchFrom,
    DetailItem,
    SimilarItem,
    TagForm,
    YoutubeItem,
  },

  data(){
    return{
      detail : {},
    }
  },

  created(){
    const movieIdx = this.$route.params.id
    this.get_detail(movieIdx)
  },

  mounted(){
    this.get_detail
  },

  methods: {
    get_detail(movieIdx){
      axios({
        method:'get',
        url: `http://127.0.0.1:8000/api/movies/${movieIdx}/`
      })
      .then((res)=>{
        console.log(res.data)
        this.detail = res.data
      })
    }
  }
}

</script>

<style>

</style>
