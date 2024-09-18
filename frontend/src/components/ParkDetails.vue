<template>
  <div class="park-details">
    <h1>park details page</h1>

    <q-btn v-if="park" color="primary" @click="showAddCommentForm = true"
      >Share your experience</q-btn
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

const { parkId } = defineProps({
  parkId: { required: true, type: Number },
});

const park = ref(null);
// @TODO: fetch park details

const showAddCommentForm = ref(false);
</script>
