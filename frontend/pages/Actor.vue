<template>
  <section class="section">
    <h2 class="title">
      Actores
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
      <Actor
        v-for="actor in actors"
        :key="actor.id"
        :actor="actor"
      />
    </div>
  </section>
</template>

<script>
import Actor from '~/components/Actor'

export default {
  components: {
    Actor
  },
  asyncData ({ $axios }) {
    return $axios.get('api/actores/')
      .then((res) => {
        return {
          actors: res.data
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
      this.actors = []
      this.$el.querySelector('#searchInput').blur() // esconder teclado
      return this.$axios.get('api/actores/', {
        params: {
          search: this.searchText,
          ordering: 'nombre'
        }
      })
        .then((res) => {
          this.actors = res.data
        })
    },
    clear () {
      this.searchText = ''
      this.search()
    }
  }
}
</script>
