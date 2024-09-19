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
            class="btn-add-comments q-mr-sm"
            color="white"
            text-color="primary"
            label="Share your experience"
            @click="showAddCommentForm = true"
          />

          <q-dialog v-model="showAddCommentForm">
            <AddCommentForm @cancel="showAddCommentForm = false" />
          </q-dialog>
        </div>
      </header>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { computed, onBeforeMount, ref } from "vue";
import AddCommentForm from "components/AddCommentForm.vue";

const showAddCommentForm = ref(false);

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
