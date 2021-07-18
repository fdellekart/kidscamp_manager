import Vuex from 'vuex'
import Cookie from 'js-cookie'

const createStore = () => {
  return new Vuex.Store({
    state: {
      authToken: null,
      applications: null,
    },
    mutations: {
      setAuthToken(state, token) {
        state.authToken = token
      },
      clearAuthToken(state) {
        state.authToken = null
      },
      setApplications(state, applications) {
        state.applications = applications
      },
    },
    actions: {
      fetchApplications(vuexContext) {
        this.$axios
          .$get('/applications.json?auth=' + vuexContext.state.authToken)
          .then((res) => vuexContext.commit('setApplications', res))
          .catch((e) => {
            if (e.request.status === 401) {
              vuexContext.dispatch('clearAuthToken')
              this.$router.push('/login')
            }
          })
      },
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
      clearAuthToken(vuexContext) {
        if (process.client) {
          localStorage.removeItem('jwt')
          localStorage.removeItem('expirationDate')
        }
        Cookie.remove('jwt')
        Cookie.remove('expirationDate')
        vuexContext.commit('clearAuthToken')
      },
      initAuth(vuexContext, req) {
        let token
        let expirationDate
        if (req) {
          if (!req.headers.cookie) {
            return
          }
          const jwtCookie = req.headers.cookie
            .split(';')
            .find((c) => c.trim().startsWith('jwt='))
          if (!jwtCookie) {
            return
          }
          token = jwtCookie.split('=')[1]
          const expirationCookie = req.headers.cookie
            .split(';')
            .find((c) => c.trim().startsWith('expirationDate='))
          expirationDate = expirationCookie.split('=')[1]
        } else {
          token = localStorage.getItem('jwt')
          console.log('Got token', token)
          if (!token) {
            return
          }
          expirationDate = localStorage.getItem('expirationDate')
        }

        if (new Date().getTime() > +expirationDate || !token) {
          vuexContext.dispatch('clearAuthToken')
          return
        }
        vuexContext.commit('setAuthToken', token)
      },
    },
    getters: {
      authToken(state) {
        return state.authToken
      },
      isAuthenticated(state) {
        return state.authToken != null
      },
      applications(state) {
        return state.applications
      },
    },
  })
}

export default createStore
