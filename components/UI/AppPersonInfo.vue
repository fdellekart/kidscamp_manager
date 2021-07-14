<template>
  <div class="person-row">
    <p class="info">
      {{ personData.firstName }} {{ personData.lastName }}
      {{ ageToPrint }}
    </p>
    <button class="edit-button" @click="$emit('toggle-edit', personData)">
      <i class="fas fa-edit"></i>
    </button>
    <button
      v-if="showDeleteIcon"
      class="edit-button"
      @click="$emit('delete', personData)"
    >
      <i class="fas fa-trash"></i>
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
    showDeleteIcon: {
      type: Boolean,
      required: false,
      default: true,
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
  computed: {
    ageToPrint() {
      if (this.personData.age > 0) {
        return this.personData.age
      }
      return ''
    },
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
