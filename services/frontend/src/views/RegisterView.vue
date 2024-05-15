<script>

import Navigation from "@/app/shared/components/app-header/NavigationBar.vue";
import FooterBar from "@/app/shared/components/app-footer/FooterBar.vue";

export default {
  name: 'RegisterView',
  components: {
    FooterBar,
    Navigation
  }
}

</script>

<template>
  <div class="container py-4 px-3 mx-auto">
    <Navigation />
    <FooterBar />
  </div>
</template>

<style scoped>

</style>