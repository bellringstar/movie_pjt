<template>
  <div class="MoReview">
    <NavForm/>
    <SearchFrom/>
    <MoviereviewItem v-for="review in reviews.slice(0,10)"
      :key="review.id"
      :review="review"
      />
  </div>
</template>

<script>
import axios from 'axios'
import NavForm from '@/components/NavForm.vue'
import SearchFrom from '@/components/SearchFrom.vue'

import MoviereviewItem from '@/components/Review/MoviereviewItem.vue'


export default {
  components:{
    NavForm,
    SearchFrom,
    MoviereviewItem,
  },
  data() {
    return {
      reviews: []
    }
  },
  mounted(){
    this.get_reviews()
  },
  methods: {
    get_reviews() {
      axios.get('<int:movie_pk>/movie_review/') 
        .then(res => {
          this.reviews = res.data;
        })
        .catch(err => {
          console.error(err);
        });
    }
  }
}

</script>


<style scoped>
.review-board {
  margin-top: 20px;
}
</style>
