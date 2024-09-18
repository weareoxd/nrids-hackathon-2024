<template>
  <!-- Content for the "Add Comment" modal dialog -->
  <div class="q-pa-md bg-white" style="max-width: 400px">
    <!-- example of a close button action -->
    <q-btn flat round dense icon="close" @click="emit('cancel')" />

    <h1>this is the form</h1>

    <q-form class="q-gutter-md" @submit="onSubmit">
      <q-input
        v-model="name"
        filled
        label="Your name *"
        hint="Name and surname"
      />

      <q-input
        v-model="name"
        outlined
        label="Your name *"
        hint="Name and surname"
      />

      <!-- Custom input component from APL, if we want to use it -->
      <AplInput
        v-model="name"
        filled
        label="Your name *"
        hint="Name and surname"
      />

      <q-select
        v-model="selection"
        filled
        label="Park *"
        :options="[
          { label: 'Park 1', value: { name: 'Park 1' } },
          { label: 'Park 2', value: { name: 'Park 2' } },
        ]"
      />

      <!-- Custom select component from APL, if we want to use it -->
      <AplSelect
        v-model="selection"
        filled
        label="Park *"
        :options="[
          { label: 'Park 1', value: { name: 'Park 1' } },
          { label: 'Park 2', value: { name: 'Park 2' } },
        ]"
      />

      <FileUpload />

      <q-input v-model="foo" filled label="Another field *" />

      <div>
        <q-btn label="Submit" type="submit" color="primary" />
        <q-btn label="Cancel" color="secondary" @click="emit('cancel')" />
      </div>
    </q-form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import FileUpload from "components/FileUpload.vue";
import AplInput from "components/AplInput.vue";
import AplSelect from "components/AplSelect.vue";

defineOptions({
  name: "AddCommentForm",
});

const { park } = defineProps({
  park: { required: false, type: [Object, null], default: null },
});

const emit = defineEmits(["cancel"]);

const name = ref("");
const foo = ref("");
const selection = ref(null);

function onSubmit() {
  console.log("submitting form", name.value, foo.value, park.name);
}
</script>

<style scoped lang="scss">
h1 {
  color: red;
  font-style: italic;
}
</style>
