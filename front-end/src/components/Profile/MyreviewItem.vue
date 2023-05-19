<template>
  <div class="MyreviewItem">
    <p class="sub_tit">REVIEW&COMMENT</p>
    <p class="tit">리뷰&코멘트</p>

    <div class = review>
      <p class="title">{{ review.title }}</p>
      <p class="content">{{ review.content }}</p>
      <p class="user">작성자 : {{ review.user }}</p>
      <p class="liked">이 리뷰가 도움이 됐어요 {{ is_liked }}</p>
    </div>
  </div>
</template>

<script>
export default {
  props:{
    review:Object
  },
}

</script>

<style>
.review {
  border: 1px solid #ccc;
  padding: 10px;
  margin-bottom: 10px;
}
</style>