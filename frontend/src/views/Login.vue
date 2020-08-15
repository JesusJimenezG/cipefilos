<template>
  <div id="nav">
    <router-link to="/register">Regístrate</router-link>
  </div>
  <div class="login">
    <h1 class="title">Login in the page</h1>
    <form action class="form">
      <label class="form-label" for="#username">Usuario:</label>
      <input class="form-input" type="username" id="username" required placeholder="Usuario">
      <label class="form-label" for="#password">Password:</label>
      <input class="form-input" type="password" id="password" placeholder="Password">
      <input class="form-submit" type="submit" value="Login">
    </form>
  </div>
</template>

<script>
export default {
  data: () => ({
    username: '',
    password: '',
    error: false,
  }),
  methods: {
    login() {
      console.log(this.user);
      console.log(this.password);
    },
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
.login {
  padding: 2rem;
}
.title {
  text-align: center;
}
.form {
  margin: 3rem auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 20%;
  min-width: 350px;
  max-width: 100%;
  background: rgba(19, 35, 47, 0.9);
  border-radius: 5px;
  padding: 40px;
  box-shadow: 0 4px 10px 4px rgba(0, 0, 0, 0.3);
}
.form-label {
  margin-top: 2rem;
  color: white;
  margin-bottom: 0.5rem;
  &:first-of-type {
    margin-top: 0rem;
  }
}
.form-input {
  padding: 10px 15px;
  background: none;
  background-image: none;
  border: 1px solid white;
  color: white;
  &:focus {
    outline: 0;
    border-color: #1ab188;
  }
}
.form-submit {
  background: #1ab188;
  border: none;
  color: white;
  margin-top: 3rem;
  padding: 1rem 0;
  cursor: pointer;
  transition: background 0.2s;
  &:hover {
    background: #0b9185;
  }
}
</style>
