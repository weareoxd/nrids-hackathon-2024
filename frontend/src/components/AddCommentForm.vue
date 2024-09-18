<template>
  <!-- Content for the "Add Comment" modal dialog -->
  <div class="add-comment-form q-pa-md bg-white">
    <!-- example of a close button action -->
    <!-- <q-btn flat round dense icon="close" @click="emit('cancel')" /> -->

    <h4 class="q-mt-none">Share your experience</h4>

    <q-form class="q-gutter-md" @submit="onSubmit">
      <q-file
        v-model="filesImages"
        label="Upload up to 4 photos"
        name="photos"
        multiple
        max-files="4"
        filled
        accept=".jpg, .jpeg, .webp, image/jpeg, image/webp"
        hint="Allowed file types: jpg, webp"
        @rejected="onFileRejected"
      >
        <template #prepend>
          <q-icon name="attach_file" />
        </template>
      </q-file>

      <!-- @TODO: show thumbnails here -->

      <q-select
        v-model="parkId"
        name="park"
        filled
        label="Park location"
        emit-value
        map-options
        :options="parkOptions"
        :rules="[(val) => !!val || 'Please select a park location']"
      />

      <q-select
        v-model="facility"
        name="facility"
        filled
        label="Facility"
        emit-value
        map-options
        :options="[
          // @TODO: get facilities list or change to plain text input?
          { label: 'Parking lot', value: 'Parking lot' },
          { label: 'Campgrounds', value: 'Campgrounds' },
        ]"
        :rules="[(val) => !!val || 'Please select a park facility']"
      />

      <q-input
        v-model="comments"
        name="comments"
        filled
        type="textarea"
        :rules="[(val) => val.length || 'Please tell us about your experience']"
      />

      <div class="form-buttons row">
        <q-btn
          class="btn-submit col q-mr-md"
          label="Submit"
          type="submit"
          color="primary"
        />
        <q-btn
          class="btn-cancel col-2"
          label="Cancel"
          color="secondary"
          @click="emit('cancel')"
        />
      </div>
    </q-form>
  </div>
</template>

<script setup>
import { computed, ref } from "vue";
import { api } from "src/boot/axios";
import { useParksList } from "src/data/useParksList";

defineOptions({
  name: "AddCommentForm",
});

const { park } = defineProps({
  park: { required: false, type: [Object, null], default: null },
});

const { parksList } = useParksList();

const parkOptions = computed(() =>
  parksList.value.map((park) => ({
    label: park.name,
    value: park.id,
  }))
);

const emit = defineEmits(["cancel"]);

const filesImages = ref(null);

const parkId = ref(park ? park.id : null);
const facility = ref(null);
const comments = ref("");

function onFileRejected(files) {
  console.log("Rejected files", files);
}

async function onSubmit(submitEvent) {
  console.log("submitting form", submitEvent);

  const formData = new FormData(submitEvent.target);

  const response = await api.post("/park/feedback/", formData);

  console.log("response", response);
}
</script>

<style scoped lang="scss"></style>
