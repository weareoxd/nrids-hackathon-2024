<template>
  <q-layout view="hHh lpR fFf">
    <q-header bordered class="bg-primary text-white">
      <header>
        <div class="header-items q-pa-sm">
          <router-link class="site-title" :to="{ name: 'home' }">
            <img src="~assets/bcparks-logo-vertical-reversed.svg" height="96" />
          </router-link>

          <router-link
            class="site-title text-white text-bold"
            :to="{ name: 'home' }"
          >
            Accessible parks
          </router-link>

          <q-btn
            class="btn-add-comments"
            color="white"
            text-color="primary"
            label="Share your experience"
          />
        </div>

        <nav class="q-pa-sm">
          <router-link v-for="link in navLinks" :key="link.label" :to="link.to">
            {{ link.label }}
          </router-link>
        </nav>
      </header>
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
import Chatbot from "src/components/ChatbotModal.vue";
import parksList from "src/data/parksList";

const navLinks = [
  { label: "Home", to: { name: "home" } },
  ...parksList.map((park) => ({
    label: park.name,
    to: { name: park.router.name },
  })),
];

defineOptions({
  name: "MainLayout",
});
</script>

<style scoped lang="scss">
.q-page {
  padding: 1em;

  @media screen and (min-width: $breakpoint-md-min) {
    margin: 0 auto;
    max-width: $breakpoint-md-min;
  }
}

header {
  .header-items {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1em;

    .site-title {
      font-size: 1.5rem;
      text-decoration: none;
    }

    @media screen and (min-width: $breakpoint-sm-min) {
      flex-direction: row;

      .btn-add-comments {
        margin-left: auto;
      }
    }
  }
}

nav {
  font-size: 1.1em;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.25em;

  @media screen and (min-width: $breakpoint-sm-min) {
    flex-direction: row;
    gap: 1em;
  }

  a {
    text-decoration: none;
    color: $white;

    &:hover {
      color: $accent;
    }
  }
}
</style>
