<template>
  <div class="MyreviewItem">
    <p class="sub_tit">Profile Page</p>
    <p class="tit">프로필 페이지</p>

    <div class = "info">
      <!-- <img class="profile_img" src="profile_image" alt="profile_img"> -->
      <p class="name">{{ user.name }}</p>
      <!-- <p class="itd">{{ user.self_introduction }}</p> -->
    </div>
  </div>
</template>

<script>
export default {
  props:{
    user:Object,
    name:String,
    // self_introduction:String,
  },
}
</script>

<style>

</style>