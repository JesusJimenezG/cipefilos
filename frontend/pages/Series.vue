<template>
  <section class="section">
    <h2 class="title">
      Series
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
      <Serie
        v-for="serie in series"
        :key="serie.id"
        :serie="serie"
      />
    </div>
  </section>
</template>

<script>
import Serie from '~/components/Serie'

export default {
  components: {
    Serie
  },
  asyncData ({ $axios }) {
    return $axios.get('api/series/')
      .then((res) => {
        return {
          series: res.data
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
      this.series = []
      this.$el.querySelector('#searchInput').blur() // esconder teclado
      return this.$axios.get('api/series/', {
        params: {
          search: this.searchText,
          ordering: 'titulo'
        }
      })
        .then((res) => {
          this.series = res.data
        })
    },
    clear () {
      this.searchText = ''
      this.search()
    }
  }
}
</script>
