<template>
  <q-page class="">
    <h4>Find a park</h4>
    <q-input filled label="Search for a park" class="q-mb-md" />

    <div class="park-cards">
      <ParkCard v-for="park in parksList" :key="park.name" :park="park" />
    </div>
  </q-page>
</template>

<script setup>
import ParkCard from "src/components/ParkCard.vue";
import { useParksList } from "src/data/useParksList";

const { parksList } = useParksList();

defineOptions({
  name: "IndexPage",
});
</script>
