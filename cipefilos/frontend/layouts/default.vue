<template>
  <div>
    <nav
      class="navbar header has-shadow is-primary"
      role="navigation"
      aria-label="main navigation"
    >
      <div class="navbar-brand">
        <a class="navbar-item" href="/">Cipéfilos</a>
        <div class="navbar-burger" @click="isActive = !isActive">
          <span />
          <span />
          <span />
        </div>
      </div>
      <div class="navbar-menu" :class="{ active: isActive }">
        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <a v-if="!user" class="button" @click="isRegisterActive=true">
                <strong>Registro</strong>
              </a>
              <a v-else class="button is-primary">
                Bienvenido {{ user }} 😄
              </a>
              <a v-if="!user" class="button is-light" @click="isLoginActive=true">
                Acceder
              </a>
              <a v-else class="button is-light" @click="logout">
                Salir
              </a>
              <!--login -->
              <b-modal :active.sync="isLoginActive">
                <form action @submit.prevent="login">
                  <div class="modal-card" style="width: auto">
                    <header class="modal-card-head">
                      <p class="modal-card-title">
                        Identificación
                      </p>
                    </header>
                    <section class="modal-card-body">
                      <b-field label="email">
                        <b-input
                          v-model="loginEmail"
                          type="email"
                          placeholder="Usuario"
                          required
                        />
                      </b-field>
                      <b-field label="Contraseña">
                        <b-input
                          v-model="loginPassword"
                          type="password"
                          password-reveal
                          placeholder="Tu contraseña"
                          required
                        />
                      </b-field>
                    </section>
                    <footer class="modal-card-foot">
                      <button class="button is-primary">
                        Acceder
                      </button>
                    </footer>
                  </div>
                </form>
              </b-modal>
              <!-- Modal para el registro -->
              <b-modal :active.sync="isRegisterActive">
                <form action="" @submit.prevent="register">
                  <div class="modal-card" style="width: auto">
                    <header class="modal-card-head">
                      <p class="modal-card-title">
                        Registro
                      </p>
                    </header>
                    <section class="modal-card-body">
                      <b-field label="Nombre">
                        <b-input
                          v-model="registerFirstName"
                          type="firstName"
                          placeholder="Nombre"
                          required
                        />
                      </b-field>
                      <b-field label="Apellido">
                        <b-input
                          v-model="registerLastName"
                          type="lastName"
                          placeholder="Apellido"
                          required
                        />
                      </b-field>
                      <b-field label="Usuario">
                        <b-input
                          v-model="registerUsername"
                          type="username"
                          placeholder="Usuario"
                          required
                        />
                      </b-field>
                      <b-field label="Email">
                        <b-input
                          v-model="registerEmail"
                          type="email"
                          placeholder="email"
                          required
                        />
                      </b-field>
                      <b-field label="Contraseña">
                        <b-input
                          v-model="registerPassword"
                          type="password"
                          password-reveal
                          placeholder="Contraseña"
                          required
                        />
                      </b-field>
                      <b-field label="Repite la contraseña">
                        <b-input
                          v-model="registerPasswordConf"
                          type="password"
                          password-reveal
                          placeholder="Contraseña"
                          required
                        />
                      </b-field>
                    </section>
                    <footer class="modal-card-foot">
                      <button class="button is-primary">
                        Registrarse
                      </button>
                    </footer>
                  </div>
                </form>
              </b-modal>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <section class="main-content columns">
      <aside class="column is-3 section">
        <!-- 3 en lugar de 2 y 9 por 10 -->
        <p class="menu-label is-hidden-touch">
          General
        </p>
        <ul class="menu-list">
          <li>
            <nuxt-link to="/" exact-active-class="is-active">
              <b-icon icon="video" />
              Películas
            </nuxt-link>
          </li>
          <li>
            <nuxt-link to="/series" exact-active-class="is-active">
              <b-icon icon="" />
              Series
            </nuxt-link>
          </li>
          <li>
            <nuxt-link to="/actor" exact-active-class="is-active">
              <b-icon icon="star" />
              Actores
            </nuxt-link>
          </li>
          <li v-if="user">
            <nuxt-link to="/favoritas" exact-active-class="is-active">
              <b-icon icon="star" />
              Favoritas
            </nuxt-link>
          </li>
        </ul>
      </aside>

      <div class="container column is-10">
        <nuxt />
      </div>
    </section>
  </div>
</template>

<script>
export default {
  data () {
    return {
      // login
      isActive: false,
      isLoginActive: false,
      loginEmail: 'postman@test.com',
      loginPassword: '159post753',
      // registro
      isRegisterActive: false,
      isRegisterSuccessful: false,
      registerFirstName: '',
      registerLastName: '',
      registerUsername: '',
      registerEmail: '',
      registerPassword: '',
      registerPasswordCond: ''
    }
  },
  computed: {
    user () {
      return this.$store.state.user
    }
  },
  methods: {
    login () {
      return this.$axios.post('users/login/', {
        email: this.loginEmail,
        password: this.loginPassword
      }).then((res) => {
        if (res.data.access_token) {
          this.$store.commit('saveToken', res.data.access_token)
          this.$store.commit('saveUser', this.loginEmail.split('@')[0])
          // Reiniciamos los campos
          this.loginEmail = ''
          this.loginPassword = ''
          // Escondemos la modal
          this.isLoginActive = false
        }
      }).catch((error) => { alert(Object.values(error.response.data)) })
    },
    logout () {
      this.$store.commit('saveToken', null)
      this.$store.commit('saveUser', null)
      this.$router.replace({ path: '/' })
    },
    register () {
      return this.$axios.post('users/signup/', {
        email: this.registerEmail,
        username: this.registerUsername,
        password: this.registerPassword,
        password_confirmation: this.registerPasswordConf,
        first_name: this.registerFirstName,
        last_name: this.registerLastName
      })
        .then((res) => {
          if (res.data.first_name) {
            this.$buefy.dialog.alert('Bienvenido! ' + res.data.first_name + ' ' + res.data.last_name)
          }
          // this.$store.commit('saveToken', res.data.access_token)
          this.$store.commit('saveUser', this.registerEmail)
          // Reiniciamos los campos
          this.registerEmail = ''
          this.registerPassword1 = ''
          this.registerPassword2 = ''
          // Escondemos la modal
          this.isRegisterActive = false
        })
        .catch((error) => {
          alert(Object.values(error.response.data))
        })
    }
  }
}
</script>

<style>
.active{
  display: block !important;
}
</style>
