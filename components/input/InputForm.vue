<template>
  <form @submit.prevent="onSubmit">
    <app-control-input v-model="personData.firstName"
      >Vorname</app-control-input
    >
    <app-control-input v-model="personData.lastName"
      >Nachname</app-control-input
    >
    <app-control-input
      v-if="showAge"
      v-model="personData.age"
      :show-child-age-placeholder="true"
      >Alter</app-control-input
    >
    <app-control-input v-if="!showAge" v-model="personData.mail"
      >E-Mail Adresse</app-control-input
    >
    <p v-show="showWarning" class="warning">Bitte Daten vollständig angeben!</p>
    <p v-show="showAgeNumericWarning" class="warning">
      Bitte für das Alter eine Zahl angeben!
    </p>
    <p v-show="showAgeOutOfBoundsWarning" class="warning">
      Eine Teilnahme ist nur für Kinder zwischen 8 und 14 Jahren möglich. Bitte
      gib das Alter deines Kindes zu Beginn der Lagerwoche an.
    </p>
    <p v-show="showMailWarning" class="warning">Bitte gültige Mail angeben!</p>
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
    // showAge == false implicitly asumes that showMail == true
    // therefore it is only possible to choose between mail or age
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
      personData: this.showAge
        ? {
            firstName: this.person ? this.person.firstName : '',
            lastName: this.person ? this.person.lastName : '',
            age: this.person ? this.person.age : '',
          }
        : {
            firstName: this.person ? this.person.firstName : '',
            lastName: this.person ? this.person.lastName : '',
            mail: this.person ? this.person.mail : '',
          },
      showWarning: false,
      showAgeNumericWarning: false,
      showMailWarning: false,
      showAgeOutOfBoundsWarning: false,
    }
  },
  methods: {
    onSubmit() {
      if (!this.personData.firstName || !this.personData.lastName) {
        this.showWarning = true
        return
      }
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
      if (
        this.showAge &&
        (this.personData.age < 8 || this.personData.age > 14)
      ) {
        this.showAgeOutOfBoundsWarning = true
        return
      }
      if (!this.showAge && !this.isEmailValid(this.personData.mail)) {
        this.showMailWarning = true
        return
      }
      this.showWarning = false
      this.showAgeNumericWarning = false
      this.showMailWarning = false
      this.$emit('save', this.personData)
    },
    isEmailValid(mail) {
      if (
        /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(
          mail
        )
      ) {
        return true
      }
      return false
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
