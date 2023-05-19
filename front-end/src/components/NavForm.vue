<template>
    <header>
        <h1 class="logo">Movie<br/>Web</h1>
        <ul class="menu">
            <li>
                <a href="" class="btn">home</a>            
            </li>
            <li>
                <a href="" class="btn">review</a>            
            </li>
            <li>
                <a href="" class="btn">search</a>            
            </li>
        </ul>
    </header>
</template>

<script>
export default {

}
</script>

<style>
header {height: 170px; background-color: #f3f3f3; padding: 0 350px; display: flex; align-items: center;}

header > .menu {display: flex; height: 100%; align-items: center;}
header > .logo {font-family: 'Noto Sans'; font-size: 24pt; font-weight: bold; text-align: center; display: inline-flex; align-items: center; } 
header > .logo:before {content:''; width: 48px; height: 48px; background: url(@/assets/logo.png); margin-left:14px; }
header > .menu > li{display: flex; align-items:center; margin-left: 60px; height: 100%;}
header > .menu > li > .btn {display: inline-block; font-family: 'Noto Sans'; font-weight: bold; font-size: 16pt; color: black; text-decoration: none;}
</style>