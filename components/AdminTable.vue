<template>
  <b-table striped hover :items="applications" :fields="tableFields">
    <template #cell(actions)="data">
      <i class="fas fa-trash-alt" @click="$emit('delete', data.item.id)"></i>
    </template>
  </b-table>
</template>

<script>
export default {
  props: { applications: { required: true, type: Array } },
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
        {
          key: 'actions',
          label: '',
        },
      ],
    }
  },
}
</script>
