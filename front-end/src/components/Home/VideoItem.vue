<template>
  <div class="col" >
    <div class="card h-100">
      <div class="card-body d-flex flex-column">
        <iframe width="560" height="315" :src="youtube" frameborder="0" allowfullscreen></iframe>
      </div>
   </div>
  </div>
  </template>

<script>
export default {
  name:'VideoItem',
  props:{
    video: Object,
    videoId: String,
  },
  computed: {
    youtube() {
      return `https://www.youtube.com/embed/${this.videoId}`
    },
      }
}

</script>

<style scoped>

</style>


