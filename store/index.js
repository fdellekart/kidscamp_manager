import Vuex from 'vuex'
import Vue from 'vue'

const createStore = () => {
  return new Vuex.Store({
    state: {
      user: null,
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
        this.$fire.database
          .ref('/applications/' + applicationId)
          .remove()
          .then(() => {
            vuexContext.commit('deleteApplication', applicationId)
          })
          .catch((e) => {
            console.log('Error:', e)
          })
      },
      updateApplication(vuexContext, data) {
        const updates = {}
        updates['/applications/' + data.id] = data.application
        this.$fire.database
          .ref()
          .update(updates)
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
          const val = snapshot.val()
          if (!val) {
            vuexContext.commit('setApplications', {})
          } else {
            vuexContext.commit('setApplications', val)
          }
        })
      },
    },
    getters: {
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
