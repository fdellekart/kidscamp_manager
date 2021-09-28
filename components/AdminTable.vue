<template>
  <b-table striped hover :items="applications" :fields="tableFields"></b-table>
</template>

<script>
export default {
  props: ['applications'],
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
}
</script>
