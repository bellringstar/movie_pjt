<template>
<v-autocomplete
  class="home_srh"
  v-if="searching"
  :search-input.sync="search"
  label="🔎영화제목을 입력해주세요"
  :items="filteredMovies"
  item-text="title"
  item-value="id"
  @input="filterItems"
  @change="select"
  @keydown.enter="toDetail"
  variant="solo-filled"
>
  <template #item="{ item }">
    <div class="autocomplete-item">{{ item.title }}</div>
  </template>

  <template #no-data>
  <div class="v-list-item__title">검색어를 입력해보세요</div>
  </template>

</v-autocomplete>

</template>

<script>
// import axios from 'axios';

export default {
  data() {
    return {
      search:'',
      searching:true,
      selected:false
    }
  },
  computed: {
  movies() {
    return this.$store.state.movies.map(movie => ({
      title: movie.title,
      movie_id: movie.movie_id
      }))
    },
    filteredMovies() {
      if(this.search){
        if (this.search.trim() === '') {
        return [];
      } 
      }

      // Apply your custom filtering logic here if needed
      return this.movies;
    }
  },

  methods: {
    filterItems(item, queryText, itemText) {
    const normalizedQuery = queryText.toLowerCase().replace(/\s/g, '');
    const normalizedItem = itemText.toLowerCase().replace(/\s/g, '');

    return normalizedItem?.includes(normalizedQuery);
  },
    select(item){
      this.search = item
      const selectedMovie = this.$store.state.movies.find(movie => movie.title === item)
      this.movieId = selectedMovie ? selectedMovie.movie_id : null;
      this.$router.push({name:'detail', params:{id:this.movieId}})
      console.log(this.search, this.movieId)
      
    },
    toDetail(){
      console.log("to Detail")
      const selectedMovie = this.$store.state.movies.find(movie => movie.title === this.search)
      this.movieId = selectedMovie ? selectedMovie.movie_id : null;
      if(this.movieId){
          this.$router.push({name:'detail', params:{id:this.movieId}})
   
       }
    }
  }
};
</script>

<style>

.home_srh {
  color: #f3f3f3;
  display: block;
  width: 100%;
  padding: 0 50px;
  margin-top: 20px !important;
  margin-bottom: 30px !important;
}

.home_srh label {
  text-align: center;
  font-family: 'Roboto';
  font-style: normal;
  font-weight: 500;
  font-size: 16px;
  line-height: 38px;
  color: #B8B8B8;
}

.home_srh input {
  border: none !important;
  color: inherit;
  font-size: 16px;
  outline: none !important;
  width: 100%;
  text-align: center;
}

@media (min-width: 576px) {
  .home_srh {
    width: 1200px;
    margin: 0 auto;
  }
}

.autocomplete-item {
  padding: 8px 16px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  color:rgb(0, 0, 0);
}

.autocomplete-item:hover{
  /* color:chartreuse; */
  font-weight: bold;
}

.v-list-item__title {
  font-size: 16px;
  color: #B8B8B8;
  text-align: left;
  padding: 15px 8px 8px 8px;
}

</style>

