<template>
  <div class="Error">
    <LogoItem/>
    <br>
    <h1>존재하지 않는 페이지입니다</h1>
    <img :src="err_img" alt="검색 실패">

  </div>
</template>

<script>
import LogoItem from '@/components/LogoItem.vue';              
export default {
  components:{
    LogoItem
  },
  computed:{
    err_img(){
      return require('@/assets/rc_err.gif')
    },
  }

  }

</script>

<style>

</style>
