<template>
  <div class="container">
    <input-form
      v-if="!isSaved"
      :person="child"
      :show-age="true"
      :show-cancel-button="true"
      @save="onSaveChild($event)"
      @cancel="onCancelChild"
    />
    <app-person-info
      v-if="isSaved"
      :first-name="child.firstName"
      :last-name="child.lastName"
      :age="+child.age"
      @toggle-edit="onEditChild"
      @delete="$emit('delete', idx)"
    />
  </div>
</template>

<script>
import InputForm from '@/components/input/InputForm'
import AppPersonInfo from '@/components/UI/AppPersonInfo'

export default {
  components: {
    InputForm,
    AppPersonInfo,
  },
  props: {
    idx: {
      type: String,
      default: '',
    },
  },
  data() {
    return {
      child: { firstName: null, lastName: null, age: null },
      isSaved: false,
    }
  },
  methods: {
    onSaveChild(child) {
      this.child = child
      this.isSaved = true
      this.$emit('save', { idx: this.idx, child })
    },
    onEditChild() {
      this.isSaved = false
    },
    onCancelChild(idx) {
      if (!this.child.firstName & !this.child.lastName & !this.child.age) {
        this.$emit('delete', this.idx)
      } else {
        this.isSaved = true
      }
    },
  },
}
</script>
