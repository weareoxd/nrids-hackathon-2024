<template>
  <q-card class="park-card">
    <q-img
      :src="park.data.image || PLACEHOLDER_IMG_URL"
      :alt="park.name"
      height="240px"
    />

    <q-card-section>
      <h5>{{ park.name }}</h5>
      <p>{{ park.data.location }}</p>

      <p class="icons">
        <img
          v-for="(value, key) in park.data.features"
          :key="key"
          :alt="key"
          :src="getImageUrl(value)"
        />
      </p>

      <router-link :to="{ name: 'park-details', params: { slug: park.slug } }">
        View park >
      </router-link>
    </q-card-section>
  </q-card>
</template>

<script setup>
import { defineProps } from "vue";
import PLACEHOLDER_IMG_URL from "assets/bc-parks-placeholder.png";

const { park } = defineProps({
  park: {
    type: Object,
    required: true,
  },
});

const getImageUrl = (str) => {
  return new URL(`../assets/icons/${str}`, import.meta.url);
};
</script>

<style lang="scss" scoped>
.icons img {
  width: 32px;
  height: 32px;
  margin-right: 0.5rem;

  &:last-child {
    margin-right: 0;
  }
}
</style>
