<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link> | 
      <router-link to="/detail">detail</router-link> |
      <router-link to="/moreview">moreview</router-link> |
      <router-link to="/myreview">myreview</router-link> |
      <router-link to="/login">login</router-link> |
      <router-link to="/profile">profile</router-link> |
      <router-link to="/signup">signup</router-link> |
    </nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

html,body {height: 100%;}
.wrap {height: 100%; display: flex; flex-direction: column;}
</style>
