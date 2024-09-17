<template>
  <q-page class="park">
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
