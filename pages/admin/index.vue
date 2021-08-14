<template>
  <div><b-table :items="$store.getters.applicationsToDisplay"></b-table></div>
</template>

<script>
export default {
  name: 'AdminPage',
  middleware: ['check-auth', 'auth'],
  mounted() {
    this.$store.dispatch('fetchApplications')
  },
}
</script>
