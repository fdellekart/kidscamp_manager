import Vuex from 'vuex'
import Cookie from 'js-cookie'

const createStore = () => {
  return new Vuex.Store({
    state: {},
    mutations: {},
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
            localStorage.setItem('authToken', res.data.idToken)
            Cookie.set('jwt', res.data.idToken)
            localStorage.setItem(
              'authTokenExpiresIn',
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
