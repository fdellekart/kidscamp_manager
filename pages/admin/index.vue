<template>
  <div class="container">
    <div class="stats-container">
      <application-stats
        :number-applications="Object.keys($store.getters.applications).length"
      />
    </div>
    <admin-table
      :applications="$store.getters.applications"
      @delete="handleDeletionClick"
      @update-application="handleUpdate"
    />
    <b-modal
      id="warn-delete"
      ok-title="Ja, Löschen"
      cancel-title="Abbrechen"
      ok-variant="danger"
      @ok="deleteApplication"
      >Du bist dabei die Anmeldung von <b>{{ deleteModalText }}</b> zu löschen.
      Bist du dir sicher?</b-modal
    >
  </div>
</template>

<script>
import AdminTable from '~/components/AdminTable'
import ApplicationStats from '~/components/ApplicationStats'

export default {
  name: 'AdminPage',
  components: { AdminTable, ApplicationStats },
  layout: 'admin',
  middleware: ['auth'],
  data() {
    return {
      applicationIdToDelete: null,
    }
  },
  computed: {
    deleteModalText() {
      if (!this.applicationIdToDelete) {
        return ''
      }
      const child =
        this.$store.getters.applications[this.applicationIdToDelete].child
      return child.firstName + ' ' + child.lastName
    },
  },
  mounted() {
    this.$store.dispatch('fetchApplications')
  },
  methods: {
    handleDeletionClick(applicationId) {
      this.applicationIdToDelete = applicationId
      this.$bvModal.show('warn-delete')
    },
    deleteApplication() {
      this.$store.dispatch('deleteApplication', this.applicationIdToDelete)
      this.applicationIdToDelete = null
    },
    handleUpdate(data) {
      this.$store.dispatch('updateApplication', data)
    },
  },
}
</script>

<style scoped>
.stats-container {
  margin: 10%;
}
</style>
