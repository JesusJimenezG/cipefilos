<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Cipéfilos</router-link> |
      <router-link to="/peliculas">Películas</router-link> |
      <router-link to="/series">Series</router-link> |
      <router-link to="/actores">Actores</router-link>
    </div>
    <router-view/>
  </div>
</template>

<script>
// src/plugins/vuetify.js

</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

#nav{
  position: relative;
  display: inline-block;
  padding: 30px 20px;
  text-decoration: none;
  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
