<template>
  <div class="container">
    <div class="parent-container">
      <h3>Erziehungsberechtigter</h3>
      <form v-if="!isSaved" @submit.prevent="onSubmit">
        <AppControlInput v-model="parentData.firstName"
          >Vorname</AppControlInput
        >
        <AppControlInput v-model="parentData.lastName"
          >Nachname</AppControlInput
        >
        <p v-if="showParentWarning" class="warning">
          Bitte Daten vollständig angeben!
        </p>
        <AppButton type="submit">Speichern</AppButton>
      </form>
      <div v-else class="parent-row">
        <p class="info">{{ parentData.firstName }} {{ parentData.lastName }}</p>
        <button class="edit-button" @click="isSaved = false">
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
import AppControlInput from '@/components/UI/AppControlInput'

export default {
  components: {
    AppControlInput,
  },
  data() {
    return {
      parentData: {
        firstName: '',
        lastName: '',
      },
      isSaved: false,
      showParentWarning: false,
    }
  },
  methods: {
    onSubmit() {
      const firstNameShort = this.parentData.firstName.length < 2
      const lastNameShort = this.parentData.lastName.length < 2
      if (firstNameShort || lastNameShort) {
        this.showParentWarning = true
      } else {
        console.log(this.parentData)
        this.isSaved = true
        this.showParentWarning = false
      }
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
.children-container {
  margin-top: 5%;
}
.warning {
  color: red;
  font-weight: bold;
}
</style>
