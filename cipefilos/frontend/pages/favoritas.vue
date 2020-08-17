<template>
  <section class="section">
    <h2 class="title">
      Favoritas
    </h2>
    <div class="columns is-multiline">
      <Peli
        v-for="favorita in favoritas"
        :key="favorita.pelicula.id"
        :peli="favorita.pelicula"
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
  fetch ({ store, redirect }) {
    if (!store.state.user) {
      return redirect('/')
    }
  },
  asyncData ({ store, $axios }) {
    if (store.state.user) {
      return $axios.get('api/favoritas/')
        .then((res) => {
          return {
            favoritas: res.data
          }
        })
    }
  }
}
</script>
