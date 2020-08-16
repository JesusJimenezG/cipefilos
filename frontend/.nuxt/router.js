import Vue from 'vue'
import Router from 'vue-router'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _fecc999c = () => interopDefault(import('..\\pages\\Actor.vue' /* webpackChunkName: "pages/Actor" */))
const _6272c5b8 = () => interopDefault(import('..\\pages\\favoritas.vue' /* webpackChunkName: "pages/favoritas" */))
const _6eb72dec = () => interopDefault(import('..\\pages\\Series.vue' /* webpackChunkName: "pages/Series" */))
const _7a4f48a2 = () => interopDefault(import('..\\pages\\index.vue' /* webpackChunkName: "pages/index" */))

// TODO: remove in Nuxt 3
const emptyFn = () => {}
const originalPush = Router.prototype.push
Router.prototype.push = function push (location, onComplete = emptyFn, onAbort) {
  return originalPush.call(this, location, onComplete, onAbort)
}

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  base: decodeURI('/'),
  linkActiveClass: 'nuxt-link-active',
  linkExactActiveClass: 'nuxt-link-exact-active',
  scrollBehavior,

  routes: [{
    path: "/Actor",
    component: _fecc999c,
    name: "Actor"
  }, {
    path: "/favoritas",
    component: _6272c5b8,
    name: "favoritas"
  }, {
    path: "/Series",
    component: _6eb72dec,
    name: "Series"
  }, {
    path: "/",
    component: _7a4f48a2,
    name: "index"
  }],

  fallback: false
}

export function createRouter () {
  return new Router(routerOptions)
}
