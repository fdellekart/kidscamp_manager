<template>
  <div>
    <b-table
      striped
      hover
      :items="$store.getters.applicationsToDisplay"
      :fields="tableFields"
    ></b-table>
  </div>
</template>

<script>
export default {
  name: 'AdminPage',
  middleware: ['check-auth', 'auth'],
  data() {
    return {
      tableFields: [
        {
          key: 'firstName',
          label: 'Vorname',
          sortable: true,
        },
        {
          key: 'lastName',
          label: 'Nachname',
          sortable: true,
        },
        {
          key: 'age',
          label: 'Alter',
          sortable: true,
        },
        {
          key: 'parent',
          label: 'Erziehungsberechtigter',
          sortable: true,
        },
        {
          key: 'mail',
          label: 'E-Mail',
          sortable: true,
        },
      ],
    }
  },
  mounted() {
    this.$store.dispatch('fetchApplications')
  },
}
</script>
