<template>
  <div>
    <header>
      <img @click="tohome" class="img_logo" src="@/assets/logo.png" alt="메인">
    </header>
  </div>
</template>

<script>
export default {
  methods:{
    tohome(){
      this.$router.push({'name':'home'}).catch(()=>{location.reload()})
    }
  }
}
</script>

<style>

header {height: 170px; background-color: #f3f3f3; display: flex; align-items: center; justify-content:center; border-top:30px solid #000}
header > .img_logo {display:inline-block;}

</style>