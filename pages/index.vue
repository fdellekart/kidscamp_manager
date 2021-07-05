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
      <div v-else class="parent-row">
        <p class="info">{{ parentData.firstName }} {{ parentData.lastName }}</p>
        <button class="edit-button" @click="isParentSaved = false">
          <i class="fas fa-edit"></i>
        </button>
      </div>
    </div>
    <div class="children-container">
      <h3>Kinder</h3>
    </div>
  </div>
</template>

<script>
import InputForm from '@/components/input/InputForm'

export default {
  components: {
    InputForm,
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
.parent-row {
  display: flex;
  flex-direction: row;
}
.edit-button {
  background-color: white;
  border: 0px;
  margin-left: 10px;
}
.info {
  padding-top: 15px;
}
.parent-container {
  margin-top: 5%;
}
.heading {
  margin-top: 5%;
}
.children-container {
  margin-top: 5%;
}
.warning {
  color: red;
  font-weight: bold;
}
</style>
