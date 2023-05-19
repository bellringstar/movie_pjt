<template>
  <div class="MyreviewItem">
    <p class="sub_tit">Profile Page</p>
    <p class="tit">프로필 페이지</p>

    <div class = "info">
      <img class="user_img" src="" alt="user.img">
      <p class="name">{{ user.name }}</p>
      <p class="itd">{{ user.itd }}</p>
    </div>
  </div>
</template>

<script>
export default {
  props:{
    user:Object
  },
}
</script>

<style>

</style>