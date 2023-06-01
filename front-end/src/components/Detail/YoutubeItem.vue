<template>
  <div class="YoutubeItem">
    <iframe :src="videos_url"></iframe>
  </div>
</template>

<script>
export default {
  props: {
    video: Object,
  },
  computed: {
    videos_url() {
      return `https://www.youtube.com/embed/${this.video.key}?autoplay=0`
    }
  }
}
</script>

<style>

.YoutubeItem {
  position: relative;
  width: 100%;
  overflow: hidden;
  border-radius: 5px;
  height: 200px;
}

.YoutubeItem iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border: 0;
  object-fit: cover;
}

@media (max-width: 768px) {
  .YoutubeItem {
    padding-bottom: 75%; /* 4:3 비율 */
  }
}
</style>
