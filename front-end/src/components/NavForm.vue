<template>
    <nav class="navbar">
      <div class="nav_logo">
        <i class="fa-solid fa-star"></i>
        <a href=""> <img src="@/assets/logo.png" alt="logo" class="nav_logo"> logo </a>
      </div>
      <ul class="nav_menu">
        <li><a href="">Home</a></li>
        <li><a href="">Review</a></li>
        <li><a href="">Search</a></li>
      </ul>
      <ul class="nav_account">
        <li><a href="">Login</a></li>
        <li><a href="">Signup</a></li>
      </ul>
      <a href="#" class="navbar_toggleBtn">
        <i class="fa-solid fa-bars"></i>
      </a>
    </nav>
</template>

<script>
export default {

}
</script>

<style>

:root {
  --accent-color: #f3ff87;
  --text-color: #f0f4f5;
  --background-color: #0b002b;}

.body {
  margin: 0;
  font-family: 'Montserrat';}

a {
  text-decoration: none;
  color: var(--text-color);}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: var(--background-color);
  padding: 8px 12px;}


.nav_logo {
font-size: 24px;
color: var(--text-color);
width: 64px;
height: 64px;
}


.nav_logo i {
  color: var(--accent-color);}

.nav_logo span {
  color: var(--accent-color);}

.nav_menu {
  display: flex;
  list-style: none;
  padding-left: 0;}

.nav_menu li {
  padding: 8px 12px;}

.nav_menu li:hover {
  color: var(--background-color);
  background-color: var(--accent-color);
  border-radius: 4px;}

.nav_menu li a:hover {
  color: var(--background-color);}

.nav_icons {
  display: flex;
  color: #7dc0ff;
  list-style: none;
  padding-left: 0;}

.nav_icons li {
  padding: 8px 5px;}

.navbar_toggleBtn {
  display: none;
  color:var(--text-color);
  position: absolute;
  right: 32px;
  font-size: 24px;}
</style>