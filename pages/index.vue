<template>
  <div class="container">
    <form @submit.prevent="onSubmit">
      <AppControlInput v-model="parentData.firstName">Vorname</AppControlInput>
      <AppControlInput v-model="parentData.lastName">Nachname</AppControlInput>
      <AppButton type="submit">Senden</AppButton>
    </form>
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
    }
  },
  methods: {
    onSubmit() {
      console.log(this.parentData)
    },
  },
}
</script>

<style></style>
