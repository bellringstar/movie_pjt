<template>
  <div class="Detail">
    <h1>Detail</h1>
    <SimilarItem/>
    <TagForm/>
    <YoutubeItem/>
  </div>
</template>

<script>
import SimilarItem from '@/components/Detail/SimilarItem.vue'
import TagForm from '@/components/Detail/TagForm.vue'
import YoutubeItem from '@/components/Detail/YoutubeItem.vue'

export default {
  components:{
    SimilarItem,
    TagForm,
    YoutubeItem,
  },
}
</script>

<style>

</style>
