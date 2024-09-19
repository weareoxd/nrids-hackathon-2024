<template>
  <div class="park-details">
    <h1>park details page</h1>

    <p>parkData:</p>
    <pre>{{ parkData }}</pre>

    <q-btn
      v-if="parkData"
      icon="add_a_photo"
      color="primary"
      label="Share your experience"
      size="lg"
      @click="showAddCommentForm = true"
    />

    <q-dialog v-model="showAddCommentForm">
      <AddCommentForm :park="parkData" @cancel="showAddCommentForm = false" />
    </q-dialog>
  </div>
</template>

<script setup>
import { api } from "src/boot/axios";
import { onBeforeMount, ref, watch } from "vue";
import AddCommentForm from "components/AddCommentForm.vue";

defineOptions({
  name: "ParkDetails",
});

const { parkId } = defineProps({
  parkId: { required: true, type: Number },
});

const parkData = ref(null);
// Fetch park details from the API
watch(
  () => parkId,
  async (newParkId) => {
    console.log("parkId changed", newParkId);

    if (!newParkId) {
      return;
    }

    const response = await api.get(`/park/park/${newParkId}`);
    parkData.value = response.data;
  },
  { immediate: true }
);

const showAddCommentForm = ref(false);
</script>
