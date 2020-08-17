import Vue from 'vue'
import Router from 'vue-router'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _411cf1d4 = () => interopDefault(import('..\\pages\\Actor.vue' /* webpackChunkName: "pages/Actor" */))
const _27b6079c = () => interopDefault(import('..\\pages\\favoritas.vue' /* webpackChunkName: "pages/favoritas" */))
const _44c711a6 = () => interopDefault(import('..\\pages\\Series.vue' /* webpackChunkName: "pages/Series" */))
const _21b02f93 = () => interopDefault(import('..\\pages\\index.vue' /* webpackChunkName: "pages/index" */))

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
    component: _411cf1d4,
    name: "Actor"
  }, {
    path: "/favoritas",
    component: _27b6079c,
    name: "favoritas"
  }, {
    path: "/Series",
    component: _44c711a6,
    name: "Series"
  }, {
    path: "/",
    component: _21b02f93,
    name: "index"
  }],

  fallback: false
}

export function createRouter () {
  return new Router(routerOptions)
}
