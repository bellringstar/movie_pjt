<template>
  <div class="Profile">
    <h1>Profile</h1>
    <LikedItem/>
    <MyreviewItem/>
  </div>
</template>

<script>
import LikedItem from '@/components/Profile/LikedItem.vue'
import MyreviewItem from '@/components/Profile/MyreviewItem.vue'

export default {
  components:{
    LikedItem,
    MyreviewItem,
  },
}
</script>

<style>

</style>
