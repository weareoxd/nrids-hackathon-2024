<template>
  <div class="q-pa-md q-gutter-sm">
    <q-btn color="tertiary" round @click="fullHeight = true">
      <q-avatar size="64px">
        <img src="~assets/squatchy.svg" />
      </q-avatar>
    </q-btn>

    <q-dialog v-model="fullHeight" full-height>
      <q-card class="column full-height" style="width: 300px">
        <q-card-section>
          <div class="text-h6">Full Height</div>
        </q-card-section>

        <q-card-section class="col q-pt-none">
          Click/Tap on the backdrop.
        </q-card-section>

        <q-card-actions align="right" class="bg-white text-teal">
          <q-btn v-close-popup flat label="OK" />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </div>
</template>

<script>
import { ref } from "vue";

export default {
  setup() {
    return {
      fullHeight: ref(false),
    };
  },
};
</script>
