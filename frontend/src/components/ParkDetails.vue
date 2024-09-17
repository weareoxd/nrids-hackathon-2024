<template>
  <div class="park-details">
    <h1>{{ park.name }}</h1>
    <div>park details: {{ park }}</div>
    <div><FileUpload /></div>
  </div>
</template>

<script setup>
import { api } from "src/boot/axios";
import { onBeforeMount } from "vue";
import FileUpload from "components/FileUpload.vue";

defineOptions({
  name: "ParkDetails",
});

const { park } = defineProps({
  park: { required: true, type: Object },
});

onBeforeMount(() => {
  const { data: details } = api.get("/");
  console.log("details", details);
});
</script>
