<template>
  <form @submit.prevent="onSubmit">
    <AppControlInput v-model="personData.firstName">Vorname</AppControlInput>
    <AppControlInput v-model="personData.lastName">Nachname</AppControlInput>
    <AppControlInput v-if="showAge" v-model="personData.age"
      >Alter</AppControlInput
    >
    <p v-show="showWarning" class="warning">Bitte Daten vollständig angeben!</p>
    <p v-show="showAgeNumericWarning" class="warning">
      Bitte für das Alter eine Zahl angeben!
    </p>
    <AppButton type="submit">Speichern</AppButton>
    <AppButton v-if="showCancelButton" @click="$emit('cancel')"
      >Abbrechen</AppButton
    >
  </form>
</template>

<script>
export default {
  props: {
    person: {
      type: Object,
      default: undefined,
    },
    showAge: {
      type: Boolean,
      required: false,
      default: false,
    },
    showCancelButton: {
      type: Boolean,
      required: false,
      default: false,
    },
  },
  data() {
    return {
      personData: {
        firstName: this.person ? this.person.firstName : '',
        lastName: this.person ? this.person.lastName : '',
        age: this.person ? this.person.age : '',
      },
      showWarning: false,
      showAgeNumericWarning: false,
    }
  },
  methods: {
    onSubmit() {
      const isFirstNameShort = this.personData.firstName.length < 2
      const isLastNameShort = this.personData.lastName.length < 2
      if (isFirstNameShort || isLastNameShort) {
        this.showWarning = true
        return
      }
      if (this.showAge && isNaN(this.personData.age)) {
        this.showAgeNumericWarning = true
        return
      }
      this.showWarning = false
      this.showAgeNumericWarning = false
      this.$emit('save', this.personData)
    },
  },
}
</script>

<style scoped>
.warning {
  color: red;
  font-weight: bold;
}
</style>
