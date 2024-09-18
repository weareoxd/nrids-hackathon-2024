<template>
  <div class="park-details">
    <h1>{{ park.name }}</h1>
    <div>park details: {{ park }}</div>

    <q-btn color="primary" @click="showAddCommentForm = true"
      >Show comment form</q-btn
    >

    <q-dialog v-model="showAddCommentForm">
      <AddCommentForm :park="park" @cancel="showAddCommentForm = false" />
    </q-dialog>
  </div>
</template>

<script setup>
import { api } from "src/boot/axios";
import { onBeforeMount, ref } from "vue";
import AddCommentForm from "components/AddCommentForm.vue";

defineOptions({
  name: "ParkDetails",
});

const { park } = defineProps({
  park: { required: true, type: Object },
});

const showAddCommentForm = ref(false);

onBeforeMount(() => {
  const { data: details } = api.get("/");
  console.log("details", details);
});
</script>
