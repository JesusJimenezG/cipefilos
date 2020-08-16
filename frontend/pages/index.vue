<template>
  <section class="section">
    <h2 class="title">
      Películas
    </h2>
    <!-- Empieza la parte de la búsqueda -->
    <div class="columns">
      <div class="column">
        <form action="" @submit.prevent="search">
          <b-input
            id="searchInput"
            v-model="searchText"
            type="text"
            placeholder="Filtro por título"
            required
          />
        </form>
      </div>
      <div class="column">
        <a class="button is-primary" @click="search">Buscar</a> &nbsp;
        <a class="button is-info" @click="clear">Limpiar</a>
      </div>
    </div>
    <br>
    <!-- Fin de la búsqueda -->
    <div class="columns is-mobile is-multiline">
      <Peli
        v-for="peli in pelis"
        :key="peli.id"
        :peli="peli"
      />
    </div>
  </section>
</template>

<script>
import Peli from '~/components/Peli'

export default {
  components: {
    Peli
  },
  asyncData ({ $axios }) {
    return $axios.get('api/pelicula/')
      .then((res) => {
        return {
          pelis: res.data
        }
      })
  },
  data () {
    return {
      searchText: ''
    }
  },
  methods: {
    search () {
      this.pelis = []
      this.$el.querySelector('#searchInput').blur() // esconder teclado
      return this.$axios.get('api/pelicula/', {
        params: {
          search: this.searchText,
          ordering: 'titulo'
        }
      })
        .then((res) => {
          this.pelis = res.data
        })
    },
    clear () {
      this.searchText = ''
      this.search()
    }
  }
}
</script>
