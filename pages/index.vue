<template>
  <div class="container">
    <h1 class="heading">Anmeldung KidsCamp {{ currentYear }}</h1>
    <div class="separator"></div>
    <div class="parent-container">
      <h3>Erziehungsberechtigter</h3>
      <InputForm
        v-if="!isParentSaved"
        :person="parentData"
        @save="onSaveParent($event)"
      />
      <AppPersonInfo
        v-else
        :first-name="parentData.firstName"
        :last-name="parentData.lastName"
        @toggle-edit="isParentSaved = false"
      />
    </div>
    <div class="separator"></div>
    <div class="children-container">
      <h3>Kinder</h3>
      <AppPersonInfo
        v-for="child in children"
        :key="child.firstName + child.lastName + child.age"
        :first-name="child.firstName"
        :last-name="child.lastName"
        :age="+child.age"
        @toggle-edit="onEditChild($event)"
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
        :is-child="true"
        :show-cancel-button="children.length > 0"
        @save="onSaveChild($event)"
        @cancel="onCancelChild"
      />
    </div>
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
      console.log(this.parentData)
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
      console.log(childData)
    },
    onEditChild(childData) {
      this.isEditingChild = true
      this.childToEditIndex = this.children.findIndex(
        (e) =>
          e.firstName + e.lastName === childData.firstName + childData.lastName
      )
      this.childToEdit = childData
    },
    onCancelChild() {
      this.isEditingChild = false
      this.isAddingChild = false
      this.childToEditIndex = null
      this.childToEdit = undefined
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
</style>
