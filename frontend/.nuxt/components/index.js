export { default as Actor } from '../..\\components\\Actor.vue'
export { default as Logo } from '../..\\components\\Logo.vue'
export { default as Peli } from '../..\\components\\Peli.vue'
export { default as Serie } from '../..\\components\\Serie.vue'

export const LazyActor = import('../..\\components\\Actor.vue' /* webpackChunkName: "components_Actor" */).then(c => c.default || c)
export const LazyLogo = import('../..\\components\\Logo.vue' /* webpackChunkName: "components_Logo" */).then(c => c.default || c)
export const LazyPeli = import('../..\\components\\Peli.vue' /* webpackChunkName: "components_Peli" */).then(c => c.default || c)
export const LazySerie = import('../..\\components\\Serie.vue' /* webpackChunkName: "components_Serie" */).then(c => c.default || c)
