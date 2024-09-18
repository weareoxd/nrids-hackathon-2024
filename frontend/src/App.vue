<template>
  <router-view />
</template>

<script setup>
import { useParksList } from "./data/useParksList";

// fetch the parks list from the API when the app loads
const { parksList } = useParksList();

defineOptions({
  name: "App",
});
</script>
