<template>
  <div>
    <Header />
    <Navbar />
    <v-container>
      <keep-alive>
        <router-view class="main"/>
      </keep-alive>
    </v-container>
    <Footer />
  </div>
</template>

<script>
import Header from "@/components/main/Header.vue";
import Footer from "@/components/main/Footer.vue";
import Navbar from "@/components/main/Navbar.vue";

export default {
  name: "Main",
  components: {
    Header,
    Footer,
    Navbar,
  },
};
</script>


<style lang="scss">
.main {
  margin-bottom: 60px;
  z-index: 3;
}
</style>