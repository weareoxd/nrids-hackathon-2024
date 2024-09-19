<template>
  <q-card class="my-card">
    <q-img
      :src="park.image || PLACEHOLDER_IMG_URL"
      :alt="park.name"
      height="240px"
    />

    <q-card-section>
      <h5>{{ park.name }}</h5>
      <router-link :to="{ name: 'park-details', params: { slug: park.slug } }">
        View park >
      </router-link>
    </q-card-section>
  </q-card>
</template>

<script setup>
import { defineProps } from "vue";

// @TODO: Add BC parks images to parks data
// @TODO: Use BC Parks branded placeholder, if needed
const PLACEHOLDER_IMG_URL = "https://via.placeholder.com/400";

const { park } = defineProps({
  park: {
    type: Object,
    required: true,
  },
});

console.log("park!", park);
</script>

<style lang="sass" scoped>
.my-card
  width: 100%
  max-width: 400px
  margin: 32px 0
</style>
