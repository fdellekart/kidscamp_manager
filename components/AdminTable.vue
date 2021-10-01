<template>
  <b-table striped hover :items="applications" :fields="tableFields">
    <template #cell(actions)="data">
      <div v-if="!isEditing(data.item.id)">
        <i class="fas fa-trash-alt" @click="$emit('delete', data.item.id)"></i>
        <i class="fas fa-edit" @click="rowIdToEdit = data.item.id"></i>
      </div>
      <i
        v-else
        class="fas fa-check"
        @click="handleUpdateComplete(data.item.id)"
      ></i>
    </template>
    <template #cell(firstName)="data">
      <b-form-input
        v-if="isEditing(data.item.id)"
        v-model="data.item.firstName"
        :value="data.item.firstName"
      ></b-form-input>
      <span v-else>{{ data.item.firstName }}</span>
    </template>
  </b-table>
</template>

<script>
export default {
  props: { applications: { required: true, type: Array } },
  data() {
    return {
      rowIdToEdit: null,
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
  methods: {
    isEditing(rowId) {
      return this.rowIdToEdit === rowId
    },
    handleUpdateComplete(rowId) {
      console.log('Updated: ', rowId)
      this.rowIdToEdit = null
    },
  },
}
</script>
