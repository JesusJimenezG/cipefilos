<template>
  <div id="nav">
    <router-link to="/register">Regístrate</router-link> |
    <router-link to="/login">Inicia Sesión</router-link>
  </div>
</template>

<script>
// @ is an alias to /src
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
