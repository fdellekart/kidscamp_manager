<template>
  <div class="container">
    <h1 class="heading">Anmeldung KidsCamp {{ currentYear }}</h1>
    <div class="separator"></div>
    <div v-if="!applicationFinished" class="parent-container">
      <h2>Erziehungsberechtigter</h2>
      <InputForm
        v-if="!isParentSaved"
        :person="parentData"
        @save="onSaveParent($event)"
      />
      <AppPersonInfo
        v-else
        :first-name="parentData.firstName"
        :last-name="parentData.lastName"
        :mail="parentData.mail"
        :show-delete-icon="false"
        @toggle-edit="isParentSaved = false"
      />
    </div>
    <div v-if="!applicationFinished" class="separator"></div>
    <div v-if="!applicationFinished" class="children-container">
      <h2>Kinder</h2>
      <AppPersonInfo
        v-for="child in children"
        :key="child.firstName + child.lastName + child.age"
        :first-name="child.firstName"
        :last-name="child.lastName"
        :age="+child.age"
        @toggle-edit="onEditChild($event)"
        @delete="onDeleteChild($event)"
      />
      <AppButton
        v-if="showNewChildButton"
        class="add-button"
        @click="isAddingChild = true"
        >Kind Hinzufügen</AppButton
      >
      <InputForm
        v-if="showChildInputForm"
        :person="childToEdit"
        :show-age="true"
        :show-cancel-button="children.length > 0"
        @save="onSaveChild($event)"
        @cancel="onCancelChild"
      />
    </div>
    <div v-if="!applicationFinished" class="submit-button-container">
      <AppButton @click="onSend">Anmeldung absenden</AppButton>
    </div>
    <p v-if="applicationFinished">Vielen Dank für deine Anmeldung!</p>
  </div>
</template>

<script>
import InputForm from '@/components/input/InputForm'
import AppPersonInfo from '@/components/UI/AppPersonInfo'

export default {
  components: {
    InputForm,
    AppPersonInfo,
  },
  data() {
    return {
      parentData: null,
      isParentSaved: false,
      children: [],
      isAddingChild: false,
      isEditingChild: false,
      childToEditIndex: null,
      childToEdit: undefined,
      applicationFinished: false,
    }
  },
  computed: {
    currentYear() {
      return new Date().getFullYear()
    },
    showChildInputForm() {
      return (
        this.children.length === 0 || this.isAddingChild || this.isEditingChild
      )
    },
    showNewChildButton() {
      return (
        this.children.length > 0 && !this.isAddingChild && !this.isEditingChild
      )
    },
  },
  methods: {
    onSaveParent(parentData) {
      this.parentData = parentData
      this.isParentSaved = true
    },
    onSaveChild(childData) {
      if (this.isEditingChild) {
        this.$set(this.children, this.childToEditIndex, childData)
        this.isEditingChild = false
        this.childToEdit = undefined
        this.childToEditIndex = null
      } else {
        this.children.push(childData)
        this.isAddingChild = false
      }
    },
    getChildIndex(childData) {
      return this.children.findIndex(
        (e) =>
          e.firstName + e.lastName === childData.firstName + childData.lastName
      )
    },
    onEditChild(childData) {
      this.isEditingChild = true
      this.childToEditIndex = this.getChildIndex(childData)
      this.childToEdit = childData
    },
    onCancelChild() {
      this.isEditingChild = false
      this.isAddingChild = false
      this.childToEditIndex = null
      this.childToEdit = undefined
    },
    onDeleteChild(childData) {
      const index = this.getChildIndex(childData)
      this.children.splice(index, 1)
    },
    onSend() {
      this.children.forEach((child) => {
        this.$axios
          .$post('/applications.json', {
            parent: this.parentData,
            child,
          })
          .then(() => {
            this.applicationFinished = true
          })
      })
    },
  },
}
</script>

<style scoped>
.parent-container {
  margin-top: 5%;
}
.heading {
  margin-top: 5%;
}
.children-container {
  margin-top: 5%;
}
.separator {
  height: 2px;
  background-color: darkgray;
  margin-top: 5%;
}
.add-button {
  margin-top: 3%;
}
.container {
  margin-bottom: 5%;
}
.submit-button-container {
  margin-top: 5%;
}
</style>
