<template>
  <q-page class="park">
    <!-- loading indicator -->
    <template v-if="isLoading">
      <div class="row justify-center items-center" style="height: 100vh">
        <q-spinner size="100px" color="secondary" />
      </div>
    </template>
    <template v-else>
      <ParkDetails v-if="parkId" :park-id="parkId" />
      <p v-else>Park not found.</p>
    </template>
  </q-page>
</template>

<script setup>
import ParkDetails from "components/ParkDetails.vue";
import useParksList from "src/data/useParksList";
import { computed, ref, watchEffect } from "vue";
import { useRoute, useRouter } from "vue-router";

const router = useRouter();

// get park id from the url slug
// get slug param from route
const route = useRoute();
const urlSlug = computed(() => route.params.slug);

const { getParkBySlug, isLoading } = useParksList();

const parkId = computed(() => {
  const park = getParkBySlug(urlSlug.value);

  return park ? park.id : null;
});

// if park not found, redirect to 404 page
watchEffect(() => {
  if (!isLoading.value && parkId.value === null) {
    console.error("Park not found for slug", urlSlug.value);

    // redirect to error page
    router.push({
      name: "not-found",
      params: { catchAll: "park-not-found" }
    });
  }
});

defineOptions({
  name: "ParkDetailsPage"
});
</script>
