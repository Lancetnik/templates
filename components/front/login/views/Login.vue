<template>
  <div class="hold-transition">
    <keep-alive>
      <router-view class="center"/>
    </keep-alive>
  </div>
</template>

<script>
export default {
  name: "Login",
};
</script>

<style scoped>
.center {
  width: 400px;
  margin: auto;
  margin-top: 200px;
}
</style>
