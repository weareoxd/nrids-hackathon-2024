<template>
  <!-- Content for the "Add Comment" modal dialog -->
  <div class="add-comment-form q-pa-md bg-white">
    <!-- example of a close button action -->
    <!-- <q-btn flat round dense icon="close" @click="emit('cancel')" /> -->

    <h4 class="q-mt-none">Share your experience</h4>

    <q-form v-if="!isLoading" class="q-gutter-md q-mt-lg" @submit="onSubmit">
      <q-file
        v-model="filesImages"
        label="Upload up to 4 photos"
        name="photos"
        multiple
        max-files="4"
        filled
        accept=".jpg, .jpeg, .webp, .jfif, .png, image/jpeg, image/webp, image/jfif, image/png"
        hint="Allowed file types: jpg, webp, png"
        @rejected="onFileRejected"
        @update:model-value="onFilesSelected"
      >
        <template #prepend>
          <q-icon name="attach_file" />
        </template>
      </q-file>

      <!-- show thumbnails here -->
      <div class="upload-thumbs">
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
        use-input
        hide-selected
        fill-input
        input-debounce="0"
        label="Park location"
        emit-value
        map-options
        :options="filteredParkOptions"
        :rules="[val => !!val || 'Please select a park location']"
        @filter="filterParks"
      />

      <q-select
        v-model="facility"
        name="facility"
        filled
        use-input
        hide-selected
        fill-input
        input-debounce="0"
        label="Facility"
        emit-value
        map-options
        :options="filteredFacilityOptions"
        :rules="[val => !!val || 'Please select a park facility']"
        @filter="filterFacilities"
      />

      <q-input
        v-model="comments"
        name="comments"
        filled
        label="Comments"
        type="textarea"
        :rules="[val => val.length || 'Please tell us about your experience']"
      />

      <div class="form-buttons row">
        <q-btn
          class="btn-submit col-12 col-sm q-mt-sm q-mr-md"
          label="Submit"
          type="submit"
          color="primary"
          :loading="isSubmitting"
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

    <div v-else class="row justify-center items-center" style="height: 300px">
      <q-spinner size="100px" color="secondary" />
    </div>
  </div>
</template>

<script setup>
import { computed, ref, watch } from "vue";
import { api } from "src/boot/axios";
import useParksList from "src/data/useParksList";
import useFacilitiesList from "src/data/useFacilitiesList";
import { useQuasar } from "quasar";

const $q = useQuasar();

defineOptions({
  name: "AddCommentForm"
});

const { park } = defineProps({
  park: { required: false, type: [Object, null], default: null }
});

const { parksList, isLoading } = useParksList();

const parkOptions = computed(() =>
  parksList.value.map(park => ({
    label: park.name,
    value: park.id
  }))
);
const filteredParkOptions = ref(parkOptions.value);

// update
watch(parksList, () => {
  filteredParkOptions.value = parkOptions.value;
});

const { facilities } = useFacilitiesList();
const facilityOptions = facilities.map(facility => ({
  // Use the facility name as the label and value
  label: facility.feature_name,
  value: facility.feature_name
}));
const filteredFacilityOptions = ref(facilityOptions);

const emit = defineEmits(["cancel"]);

const filesImages = ref([]);
const filePreviews = ref([]);

const parkId = ref(park ? park.id : null);
const facility = ref(null);
const comments = ref("");
const isSubmitting = ref(true);

function onFileRejected(files) {
  console.log("Rejected files", files);
}

async function onSubmit(submitEvent) {
  const formData = new FormData(submitEvent.target);

  try {
    isSubmitting.value = true;
    const response = await api.post("/park/feedback/", formData);

    // close the modal
    emit("cancel");
    isSubmitting.value = false;

    $q.notify({
      type: "positive",
      message: "Thank you! Your feedback has been submitted."
    });
  } catch (error) {
    isSubmitting.value = false;
    console.error("error", error);
    $q.notify({
      type: "negative",
      message: "There was a problem submitting your feedback. Please try again."
    });
  }
}

const onFilesSelected = files => {
  filePreviews.value = [];
  for (let file of files) {
    const reader = new FileReader();
    reader.onload = e => {
      filePreviews.value.push(e.target.result);
    };
    reader.readAsDataURL(file);
  }
};

function filterFacilities(val, update, abort) {
  update(
    () => {
      const needle = val.toLowerCase();
      filteredFacilityOptions.value = facilityOptions.filter(({ label }) => {
        return label.toLowerCase().indexOf(needle) > -1;
      });
    },

    // "ref" is the Vue reference to the QSelect
    ref => {
      if (val !== "" && ref.options.length > 0) {
        ref.setOptionIndex(-1); // reset optionIndex in case there is something selected
        ref.moveOptionSelection(1, true); // focus the first selectable option and do not update the input-value
      }
    }
  );
}

function filterParks(val, update, abort) {
  update(
    () => {
      const needle = val.toLowerCase();
      filteredParkOptions.value = parkOptions.value.filter(({ label }) => {
        return label.toLowerCase().indexOf(needle) > -1;
      });
    },

    // "ref" is the Vue reference to the QSelect
    ref => {
      if (val !== "" && ref.options.length > 0) {
        ref.setOptionIndex(-1); // reset optionIndex in case there is something selected
        ref.moveOptionSelection(1, true); // focus the first selectable option and do not update the input-value
      }
    }
  );
}
</script>

<style scoped lang="scss">
.add-comment-form {
  max-width: 500px;
}

.upload-thumbs {
  display: grid;
  grid-template-columns: repeat(4, auto);
  gap: 0.5rem;
}
</style>
