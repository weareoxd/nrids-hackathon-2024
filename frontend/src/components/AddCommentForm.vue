<template>
  <!-- Content for the "Add Comment" modal dialog -->
  <div class="add-comment-form q-pa-md bg-white">
    <!-- example of a close button action -->
    <!-- <q-btn flat round dense icon="close" @click="emit('cancel')" /> -->

    <h4 class="q-mt-none">Share your experience</h4>

    <q-form class="q-gutter-md q-mt-lg" @submit="onSubmit">
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
        @update:model-value="onFilesSelected"
      >
        <template #prepend>
          <q-icon name="attach_file" />
        </template>
      </q-file>

      <!-- show thumbnails here -->
      <div>
        <q-img
          v-for="(file, index) in filePreviews"
          :key="index"
          :src="file"
          class="preview-image"
          :alt="'Preview ' + (index + 1)"
        />
      </div>

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
        :options="facilityOptions"
        :rules="[(val) => !!val || 'Please select a park facility']"
      />

      <q-input
        v-model="comments"
        name="comments"
        filled
        label="Comments"
        type="textarea"
        :rules="[(val) => val.length || 'Please tell us about your experience']"
      />

      <div class="form-buttons row">
        <q-btn
          class="btn-submit col-12 col-sm q-mt-sm q-mr-md"
          label="Submit"
          type="submit"
          color="primary"
        />
        <q-btn
          class="btn-cancel col-12 col-sm-2 q-mt-sm"
          label="Cancel"
          color="white"
          text-color="primary"
          @click="emit('cancel')"
        />
      </div>
    </q-form>
  </div>
</template>

<script setup>
import { computed, ref } from "vue";
import { api } from "src/boot/axios";
import useParksList from "src/data/useParksList";
import useFacilitiesList from "src/data/useFacilitiesList";
import { useQuasar } from "quasar";

const $q = useQuasar();

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

const { facilities } = useFacilitiesList();
const facilityOptions = facilities.map((facility) => ({
  // Use the facility name as the label and value
  label: facility.feature_name,
  value: facility.feature_name,
}));

const emit = defineEmits(["cancel"]);

const filesImages = ref([]);
const filePreviews = ref([]);

const parkId = ref(park ? park.id : null);
const facility = ref(null);
const comments = ref("");

function onFileRejected(files) {
  console.log("Rejected files", files);
}

async function onSubmit(submitEvent) {
  console.log("submitting form", submitEvent);

  const formData = new FormData(submitEvent.target);

  try {
    const response = await api.post("/park/feedback/", formData);
    console.log("response", response);

    // close the modal
    emit("cancel");

    $q.notify({
      type: "positive",
      message: "Thank you! Your feedback has been submitted.",
    });
  } catch (error) {
    console.error("error", error);
    $q.notify({
      type: "negative",
      message:
        "There was a problem submitting your feedback. Please try again.",
    });
  }
}

const onFilesSelected = (files) => {
  filePreviews.value = [];
  for (let file of files) {
    const reader = new FileReader();
    reader.onload = (e) => {
      filePreviews.value.push(e.target.result);
    };
    reader.readAsDataURL(file);
  }
};
</script>

<style scoped lang="scss"></style>
