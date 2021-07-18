import Vuex from 'vuex'
import Cookie from 'js-cookie'

const createStore = () => {
  return new Vuex.Store({
    state: {
      authToken: null,
    },
    mutations: {
      setAuthToken(state, token) {
        state.authToken = token
      },
      clearAuthToken(state) {
        state.authToken = null
      },
    },
    actions: {
      authenticateUser(vuexContext, userData) {
        console.log('User Data:', userData)
        return this.$axios
          .post(this.$config.authSignInURL + this.$config.authApiKey, {
            email: userData.email,
            password: userData.password,
            returnSecureToken: true,
          })
          .then((res) => {
            vuexContext.commit('setAuthToken', res.data.idToken)
            localStorage.setItem('jwt', res.data.idToken)
            Cookie.set('jwt', res.data.idToken)
            localStorage.setItem(
              'expirationDate',
              new Date().getTime() + +res.data.expiresIn * 1000
            )
            Cookie.set(
              'expirationDate',
              new Date().getTime() + +res.data.expiresIn * 1000
            )
          })
      },
    },
  })
}

export default createStore
