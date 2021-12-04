<template>
  <div>
    <b-table
      striped
      hover
      :items="applicationsToDisplay"
      :fields="tableFields"
      role="applications-table"
    >
      <template #cell(actions)="data">
        <div v-if="!isEditing(data.item.id)" class="actions-container">
          <i
            :id="'button-delete-' + data.item.id"
            class="fas fa-trash-alt"
            @click="$emit('delete', data.item.id)"
          ></i>
          <b-tooltip :target="'button-delete-' + data.item.id"
            >Löschen</b-tooltip
          >
          <i
            :id="'button-edit-' + data.item.id"
            class="fas fa-edit"
            @click="handleEdit(data.item)"
          ></i>
          <b-tooltip :target="'button-edit-' + data.item.id"
            >Bearbeiten</b-tooltip
          >
        </div>
        <div v-else class="actions-container">
          <i
            :id="'button-edit-complete-' + data.item.id"
            class="fas fa-check"
            @click="handleEditComplete(data.item.id)"
          ></i>
          <b-tooltip :target="'button-edit-complete-' + data.item.id"
            >Speichern</b-tooltip
          >
          <i
            :id="'button-edit-abort-' + data.item.id"
            class="fas fa-times"
            @click="handleEditAbort()"
          ></i>
          <b-tooltip :target="'button-edit-abort-' + data.item.id"
            >Abbrechen</b-tooltip
          >
        </div>
      </template>
      <template #cell(created)="data">
        <span>{{ data.item.created }}</span>
      </template>
      <template #cell(firstName)="data">
        <b-form-input
          v-if="isEditing(data.item.id)"
          v-model="rowToEdit.firstName"
          :value="data.item.firstName"
        ></b-form-input>
        <span v-else>{{ data.item.firstName }}</span>
      </template>
      <template #cell(lastName)="data">
        <b-form-input
          v-if="isEditing(data.item.id)"
          v-model="rowToEdit.lastName"
          :value="data.item.lastName"
        ></b-form-input>
        <span v-else>{{ data.item.lastName }}</span>
      </template>
      <template #cell(age)="data">
        <b-form-input
          v-if="isEditing(data.item.id)"
          v-model="rowToEdit.age"
          :value="data.item.age"
        ></b-form-input>
        <span v-else>{{ data.item.age }}</span>
      </template>
      <template #cell(parent)="data">
        <b-form-input
          v-if="isEditing(data.item.id)"
          v-model="rowToEdit.parent"
          :value="data.item.parent"
        ></b-form-input>
        <span v-else>{{ data.item.parent }}</span>
      </template>
      <template #cell(mail)="data">
        <b-form-input
          v-if="isEditing(data.item.id)"
          v-model="rowToEdit.mail"
          :value="data.item.mail"
        ></b-form-input>
        <a v-else :href="'mailto:' + data.item.mail">{{ data.item.mail }}</a>
      </template>
    </b-table>
  </div>
</template>

<script>
export default {
  props: { applications: { required: true, type: Object } },
  data() {
    return {
      rowToEdit: {},
      tableFields: [
        {
          key: 'created',
          label: 'Datum',
          sortable: true,
        },
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
  computed: {
    applicationsToDisplay() {
      if (!this.applications) {
        return []
      }
      return Object.keys(this.applications).map((applicationId) => {
        const application = this.applications[applicationId]
        const date = new Date(application.created)
        return {
          parent:
            application.parent.firstName + ' ' + application.parent.lastName,
          mail: application.parent.mail,
          firstName: application.child.firstName,
          lastName: application.child.lastName,
          age: application.child.age,
          created: date.toLocaleDateString('de'),
          id: applicationId,
        }
      })
    },
  },
  methods: {
    isEditing(rowId) {
      return this.rowToEdit.id === rowId
    },
    handleEdit(row) {
      this.rowToEdit = { ...row }
    },
    handleEditComplete(rowId) {
      this.$emit('update-application', {
        id: this.rowToEdit.id,
        application: {
          created: this.applications[this.rowToEdit.id].created,
          parent: {
            firstName: this.rowToEdit.parent.split(' ')[0],
            lastName: this.rowToEdit.parent.split(' ')[1],
            mail: this.rowToEdit.mail,
          },
          child: {
            firstName: this.rowToEdit.firstName,
            lastName: this.rowToEdit.lastName,
            age: this.rowToEdit.age,
          },
        },
      })
      this.rowToEdit = {}
    },
    handleEditAbort() {
      this.rowToEdit = {}
    },
  },
}
</script>

<style scoped>
.actions-container {
  display: flex;
  flex-direction: row-reverse;
}
.fas {
  padding: 4px;
  margin: 2px;
  border-radius: 3px;
}
.fas:hover {
  background-color: gray;
}
</style>
