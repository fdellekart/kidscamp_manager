<template>
  <div class="admin-auth-page">
    <div class="auth-container">
      <form @submit.prevent="onSubmit">
        <p v-if="showWarning" class="unauthenticated-warn" style="color: red">
          Login not Possible
        </p>
        <AppControlInput v-model="email" type="email"
          >E-Mail Addresse</AppControlInput
        >
        <AppControlInput v-model="password" type="password"
          >Passwort</AppControlInput
        >
        <AppButton type="submit">Einloggen</AppButton>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AdminAuthPage',
  data() {
    return {
      email: '',
      password: '',
      showWarning: false,
    }
  },
  methods: {
    onSubmit() {
      this.$store
        .dispatch('authenticateUser', {
          email: this.email,
          password: this.password,
        })
        .then(() => this.$router.push('/admin'))
        .catch((e) => {
          console.log(e)
          this.showWarning = true
        })
    },
  },
}
</script>

<style scoped>
.admin-auth-page {
  padding: 20px;
}

.auth-container {
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 2px 2px #ccc;
  width: 300px;
  margin: auto;
  padding: 10px;
  box-sizing: border-box;
}
</style>
