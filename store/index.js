import Vuex from 'vuex'
import Vue from 'vue'
import Cookie from 'js-cookie'

const createStore = () => {
  return new Vuex.Store({
    state: {
      user: null,
      authToken: null,
      applications: {},
    },
    mutations: {
      setUser(state, user) {
        state.user = user
      },
      setAuthToken(state, token) {
        state.authToken = token
      },
      clearAuthToken(state) {
        state.authToken = null
      },
      setApplications(state, applications) {
        Vue.set(state, 'applications', applications)
      },
      deleteApplication(state, applicationId) {
        Vue.delete(state.applications, applicationId)
      },
      updateApplication(state, data) {
        Vue.set(state.applications, data.id, data.application)
      },
    },
    actions: {
      onAuthStateChangedAction(vuexContext, { authUser, claims }) {
        if (!authUser) {
          vuexContext.commit('setUser', null)
          this.$router.push('/login')
        } else {
          vuexContext.commit('setUser', authUser)
        }
      },
      deleteApplication(vuexContext, applicationId) {
        this.$axios
          .$delete(
            '/api/applications/' +
              applicationId +
              '.json?auth=' +
              vuexContext.state.authToken
          )
          .then(() => {
            vuexContext.commit('deleteApplication', applicationId)
          })
          .catch((e) => {
            if (e.request.status === 401) {
              vuexContext.dispatch('clearAuthToken')
              this.$router.push('/login')
            }
          })
      },
      updateApplication(vuexContext, data) {
        this.$axios
          .$put(
            '/api/applications/' +
              data.id +
              '.json?auth=' +
              vuexContext.state.authToken,
            data.application
          )
          .then(() => {
            vuexContext.commit('updateApplication', data)
          })
          .catch((e) => {
            if (e.request.status === 401) {
              vuexContext.dispatch('clearAuthToken')
              this.$router.push('/login')
            }
          })
      },
      fetchApplications(vuexContext) {
        const applicationsRef = this.$fire.database.ref('applications')
        applicationsRef.on('value', (snapshot) => {
          vuexContext.commit('setApplications', snapshot.val())
        })
      },
      authenticateUser(vuexContext, userData) {
        return this.$axios
          .post('/auth/', {
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
      user(state) {
        return state.user
      },
    },
  })
}

export default createStore
