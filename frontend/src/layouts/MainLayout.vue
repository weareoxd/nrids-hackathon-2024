<template>
  <q-layout view="hHh lpR fFf">
    <q-header bordered class="bg-primary text-white">
      <q-toolbar>
        <q-avatar class="no-border-radius">
          <img src="~assets/bcparks-logo-vertical-reversed.svg" />
        </q-avatar>
        <q-toolbar-title>
          <router-link :to="{ name: 'home' }">Hackathon 2024</router-link>
        </q-toolbar-title>
        <q-btn color="white" text-color="primary" label="Upload photo" />
      </q-toolbar>
      <nav>
        nav here:
        <router-link :to="{ name: 'golden-ears-park' }"
          >golden ears</router-link
        >
        /
        <router-link :to="{ name: 'sasquatch-park' }"
          >sasquatch (uploader demo)</router-link
        >
        /
        <router-link :to="{ name: 'cultus-lake-park' }"
          >cultus lake</router-link
        >
        /
        <router-link :to="{ name: 'tyhee-lake-park' }">tyhee lake</router-link>
      </nav>
    </q-header>

    <q-page-container>
      <router-view />
      <q-page-sticky position="bottom-right" :offset="[18, 18]">
        <Chatbot />
      </q-page-sticky>
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { ref } from "vue";
import EssentialLink from "components/EssentialLink.vue";
import Chatbot from "src/components/ChatbotModal.vue";

defineOptions({
  name: "MainLayout",
});

const linksList = [
  {
    title: "Docs",
    caption: "quasar.dev",
    icon: "school",
    link: "https://quasar.dev",
  },
  {
    title: "Github",
    caption: "github.com/quasarframework",
    icon: "code",
    link: "https://github.com/quasarframework",
  },
  {
    title: "Discord Chat Channel",
    caption: "chat.quasar.dev",
    icon: "chat",
    link: "https://chat.quasar.dev",
  },
  {
    title: "Forum",
    caption: "forum.quasar.dev",
    icon: "record_voice_over",
    link: "https://forum.quasar.dev",
  },
  {
    title: "Twitter",
    caption: "@quasarframework",
    icon: "rss_feed",
    link: "https://twitter.quasar.dev",
  },
  {
    title: "Facebook",
    caption: "@QuasarFramework",
    icon: "public",
    link: "https://facebook.quasar.dev",
  },
  {
    title: "Quasar Awesome",
    caption: "Community Quasar projects",
    icon: "favorite",
    link: "https://awesome.quasar.dev",
  },
];

const leftDrawerOpen = ref(false);

function toggleLeftDrawer() {
  leftDrawerOpen.value = !leftDrawerOpen.value;
}
</script>

<style scoped lang="scss">
.q-page {
  padding: 1em;
}

nav {
  a {
    color: lighten($color: $info, $amount: 25%);
  }
}
</style>
