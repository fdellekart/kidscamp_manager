<template>
  <div class="admin-auth-page">
    <div class="auth-container">
      <form @submit.prevent="onSubmit">
        <p v-if="showWarning" class="unauthenticated-warn" style="color: red">
          Login not Possible
        </p>
        <app-control-input v-model="email" type="email"
          >E-Mail Addresse</app-control-input
        >
        <app-control-input v-model="password" type="password"
          >Passwort</app-control-input
        >
        <app-button type="submit">Einloggen</app-button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AdminAuthPage',
  middleware: 'auth',
  data() {
    return {
      email: '',
      password: '',
      showWarning: false,
    }
  },
  methods: {
    onSubmit() {
      this.$fire.auth
        .signInWithEmailAndPassword(this.email, this.password)
        .catch((e) => {
          this.showWarning = true
        })
        .then((user) => {
          this.$router.push('/admin')
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
