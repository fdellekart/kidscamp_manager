<template>
  <div class="header-container">
    <div class="logo">
      <img class="logo-image" src="~/assets/logo.gif" alt="Logo" />
    </div>
    <div class="spacer"></div>
    <div v-show="showLinkToForm" class="nav-item">
      <nuxt-link to="/">Anmeldeformular</nuxt-link>
      <i class="fas fa-arrow-right"></i>
    </div>
    <div v-show="showLinkToHomePage" class="nav-item">
      <a href="https://www.kidscamp.at">Zurück zur Homepage</a>
      <i class="fas fa-arrow-right"></i>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TheHeader',
  props: {
    showLinkToForm: {
      type: Boolean,
      required: false,
      default: true,
    },
    showLinkToHomePage: {
      type: Boolean,
      required: false,
      default: false,
    },
  },
}
</script>

<style scoped>
.header-container {
  height: 100px;
  margin: 20px;
  margin-bottom: 0;
  position: sticky;
  display: flex;
  flex-direction: row;
  align-items: center;
}
.logo {
  margin: 0 10px;
  font-size: 1.3rem;
  height: 100%;
  align-items: left;
}
.logo-image {
  height: 100%;
}
.spacer {
  flex: 1;
}
.nav-item {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.nav-item a {
  font-size: 20px;
  color: black;
  font-weight: bold;
}
.nav-item a:hover {
  font-size: 20px;
  color: darkgray;
  font-weight: bold;
}
i {
  margin: 5px;
}
.nav-item:hover {
  color: darkgray;
}
</style>
