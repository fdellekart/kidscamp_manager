<template>
  <div>
    <admin-table
      :applications="$store.getters.applicationsToDisplay"
      @delete="handleDeletionClick"
    />
    <b-modal id="warn-delete" @ok="deleteApplication"
      >Du bist dabei {{ applicationIdToDelete }} zu löschen. Bist du dir
      sicher?</b-modal
    >
  </div>
</template>

<script>
import AdminTable from '~/components/AdminTable'

export default {
  name: 'AdminPage',
  components: [AdminTable],
  middleware: ['check-auth', 'auth'],
  data() {
    return {
      applicationIdToDelete: null,
    }
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
