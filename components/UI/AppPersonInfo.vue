<template>
  <div class="person-row">
    <p class="info">{{ personData.firstName }} {{ personData.lastName }}</p>
    <button class="edit-button" @click="$emit('toggle-edit')">
      <i class="fas fa-edit"></i>
    </button>
  </div>
</template>

<script>
export default {
  props: {
    firstName: {
      type: String,
      required: true,
    },
    lastName: {
      type: String,
      required: true,
    },
    age: {
      type: Number,
      required: false,
      default: -1,
    },
  },
  data() {
    return {
      personData: {
        firstName: this.firstName,
        lastName: this.lastName,
        age: this.age,
      },
    }
  },
}
</script>

<style scoped>
.person-row {
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
</style>
