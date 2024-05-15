<template>
  <div class="container py-4 px-3 mx-auto">
    <Navigation />
    <HelloWorld msg="Welcome to Your Vue.js App" />
    <ButtonCounter />
    <div class="opacity-75"> <img alt="Regimo logo" src="../assets/regimo.png"> </div>

    <FooterBar />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/app/shared/components/HelloWorld.vue'
import ButtonCounter from '@/app/shared/components/ButtonCounter.vue'
import Navigation from '@/app/shared/components/app-header/NavigationBar.vue'
import FooterBar from "@/app/shared/components/app-footer/FooterBar.vue";

export default {
  name: 'HomeView',
  components: {
    FooterBar,
    Navigation,
    ButtonCounter,
    HelloWorld
  }
}
</script>
