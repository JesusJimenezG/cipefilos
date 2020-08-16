<template>
  <div
    class="column is-full-mobile is-half-tablet
             is-one-third-desktop is-one-quarter-widescreen"
  >
    <div class="card">
      <header class="card-header">
        <p class="card-header-title">
          {{ serie.titulo }}
        </p>
      </header>
      <div class="card-image">
        <figure class="image" @click="isModalActive=true">
          <img :src="serie.imagen">
        </figure>
      </div>
      <footer class="card-footer">
        <a class="button is-light card-footer-item">
            <span>Temporadas: </span>
          <span>{{ serie.temporadas }}</span>
          <span>{{ }}</span>
          <b-icon icon="star" />
        </a>
      </footer>
      <b-modal :active.sync="isModalActive">
        <div class="card">
          <div class="card-content">
            <h2 class="title">
              {{ serie.titulo }}
              <small>({{ serie.estreno }})</small>
            </h2>
            <p>{{ serie.resumen }}</p>
          </div>
        </div>
      </b-modal>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    serie: {
      type: Object
    }
  },
  data () {
    return {
      isModalActive: false
    }
  }
}
</script>

<style>
.card-image,
.modal-background {
  cursor: pointer !important;
}
</style>
