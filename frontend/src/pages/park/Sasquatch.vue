<template>
  <q-page class="park">
    <h1>Sasquatch Park</h1>

    <ParkDetails
      :park="{
        name: 'Sasquatch Park',
        id: 1234,
      }"
    />
  </q-page>
</template>

<script setup>
import ParkDetails from "components/ParkDetails.vue";

defineOptions({
  name: "SasquatchPark",
});
</script>
