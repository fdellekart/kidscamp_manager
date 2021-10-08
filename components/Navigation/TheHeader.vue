<template>
  <div class="header-container">
    <header class="the-header">
      <div class="logo">
        <img class="logo-image" src="~/assets/logo.gif" alt="" />
      </div>
    </header>
  </div>
</template>

<script>
export default {
  name: 'TheHeader',
}
</script>

<style scoped>
.header-container {
  height: 100px;
  margin: 20px;
  margin-bottom: 0;
}
.the-header {
  width: 100%;
  position: fixed;
  height: 100px;
  display: flex;
  justify-content: space-around;
  align-items: center;
  z-index: 100;
  box-sizing: border-box;
  padding: 0 20px;
  flex-direction: row;
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
</style>
