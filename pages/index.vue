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
    }
  },
  methods: {
    onSubmit() {
      console.log(this.parentData)
      this.isSaved = true
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
</style>
