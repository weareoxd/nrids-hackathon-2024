<template>
  <q-page class="">
    <h4>Find a park</h4>
    <div>
      <ParkCard />
    </div>
  </q-page>
</template>

<script setup>
import ParkCard from "src/components/ParkCard.vue";

defineOptions({
  name: "IndexPage",
});
</script>
