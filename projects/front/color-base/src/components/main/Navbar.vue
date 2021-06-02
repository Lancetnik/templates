<template>
  <div class="mb-6">
    <v-toolbar dark :style="'background: ' + $route.meta.theme">
      <v-tabs fixed-tabs>
        <v-tab :to="{ name: 'page1' }"> page1 </v-tab>
        <v-tab :to="{ name: 'page2' }"> page2 </v-tab>
        <v-tab :to="{ name: 'page3' }"> page3 </v-tab>
        <v-tab :to="{ name: 'page4' }"> page4 </v-tab>
      </v-tabs>
    </v-toolbar>

    <div
      class="color-row"
      :style="'background: ' + $route.meta.theme"
    ></div>
  </div>
</template>


<script>
export default {
  name: "Navbar",

  created() {
  }
};
</script>


<style scoped lang="scss">
.color-row {
  height: 400px;
  width: 100%;
  position: absolute;
}
</style>