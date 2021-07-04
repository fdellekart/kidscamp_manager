<template>
  <div class="container">
    <form>
      <AppControlInput v-model="parentData.firstName">Vorname</AppControlInput>
      <AppControlInput v-model="parentData.lastName">Nachname</AppControlInput>
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
    thingy() {
      return 'Stuff to print'
    },
  },
}
</script>

<style>
.container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.title {
  font-family: 'Quicksand', 'Source Sans Pro', -apple-system, BlinkMacSystemFont,
    'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}

.links {
  padding-top: 15px;
}
</style>
