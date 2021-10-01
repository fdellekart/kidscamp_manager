<template>
  <div class="container">
    <span>Aktuell {{ numberApplications }} Anmeldungen</span>
  </div>
</template>

<script>
export default {
  props: {
    numberApplications: {
      type: Number,
      required: true,
    },
  },
}
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: row;
  margin: 15px;
}
span {
  font-size: 30px;
  font-weight: bold;
}
</style>
