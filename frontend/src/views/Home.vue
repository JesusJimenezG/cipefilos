<template>
  <div id="nav">
    <router-link to="/register">Regístrate</router-link> |
    <router-link to="/login">Inicia Sesión</router-link>
  </div>
  <div class="home">
    <Peliculas/>
  </div>
</template>

<script>
// @ is an alias to /src
import Peliculas from '@/components/Peliculas.vue';

export default {
  name: 'Home',
  components: {
    Peliculas,
  },
};

</script>

<style lang="scss" scoped>
#nav{
  float: right;
  padding: 30px 20px;
  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
