<template>
  <q-page class="">
    <h4>Find a park</h4>
    <q-input filled label="Search for a park" class="q-mb-md" />

    <div class="park-cards">
      <!-- @TODO: temporarily broken - use parksList -->
      <!-- <ParkCard v-for="park in parksList" :key="park.name" :park="park" /> -->
    </div>
  </q-page>
</template>

<script setup>
import ParkCard from "src/components/ParkCard.vue";

defineOptions({
  name: "IndexPage",
});
</script>
