<template>
  <div class="container">
    <h1 class="heading">Anmeldung KidsCamp {{ currentYear }}</h1>
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
    <div class="children-container">
      <h3>Kinder</h3>
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
    }
  },
  computed: {
    currentYear() {
      return new Date().getFullYear()
    },
  },
  methods: {
    onSaveParent(parentData) {
      this.parentData = parentData
      console.log(this.parentData)
      this.isParentSaved = true
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
</style>
