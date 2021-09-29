<template>
  <div>
    <admin-table
      :applications="$store.getters.applicationsToDisplay"
      @delete="deleteApplication"
    />
  </div>
</template>

<script>
import AdminTable from '~/components/AdminTable'

export default {
  name: 'AdminPage',
  components: [AdminTable],
  middleware: ['check-auth', 'auth'],
  mounted() {
    this.$store.dispatch('fetchApplications')
  },
  methods: {
    deleteApplication(applicationId) {
      this.$store.dispatch('deleteApplication', applicationId)
    },
  },
}
</script>
