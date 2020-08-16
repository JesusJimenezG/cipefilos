export const state = () => ({
  token: null,
  user: null
})

export const mutations = {
  saveUser (state, user) {
    state.user = user
  },
  saveToken (state, token) {
    state.token = token
  }
}
