<template>
  <div class="Profile">
    <NavForm/>
    <SearchFrom/>
    <InfoView/>
    <LikedItem/>
    <MyreviewItem/>
  </div>
</template>

<script>
// import axios from 'axios'
import NavForm from '@/components/NavForm.vue'
import SearchFrom from '@/components/SearchFrom.vue'

import LikedItem from '@/components/Profile/LikedItem.vue'
import MyreviewItem from '@/components/Profile/MyreviewItem.vue'
import InfoView from '../../components/Profile/InfoView.vue'

export default {
  components:{
    NavForm,
    SearchFrom,
    InfoView,
    LikedItem,
    MyreviewItem,
  },
}
</script>

<style>

</style>
