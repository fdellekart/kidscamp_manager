<template>
  <div>
    <admin-table
      :applications="$store.getters.applications"
      @delete="handleDeletionClick"
    />
    <b-modal
      id="warn-delete"
      ok-title="Ja, Löschen"
      cancel-title="Abbrechen"
      @ok="deleteApplication"
      >Du bist dabei die Anmeldung von {{ deleteModalText }} zu löschen. Bist du
      dir sicher?</b-modal
    >
  </div>
</template>

<script>
import AdminTable from '~/components/AdminTable'

export default {
  name: 'AdminPage',
  components: { AdminTable },
  middleware: ['check-auth', 'auth'],
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
      const child = this.$store.getters.applications[this.applicationIdToDelete]
        .child
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
  },
}
</script>
