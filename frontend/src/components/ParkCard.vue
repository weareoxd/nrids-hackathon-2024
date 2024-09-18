<template>
  <q-card class="my-card">
    <q-img :src="park.image" :alt="park.name" height="240px" />

    <q-card-section>
      <h5>{{ park.name }}</h5>
      <router-link :to="park.router.path"> View park > </router-link>
    </q-card-section>
  </q-card>
</template>

<script setup>
import { defineProps } from "vue";

const props = defineProps({
  park: {
    type: Object,
    required: true,
  },
});
</script>

<style lang="sass" scoped>
.my-card
  width: 100%
  max-width: 400px
  margin: 32px 0
</style>
