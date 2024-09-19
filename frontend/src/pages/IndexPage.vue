<template>
  <q-page class="">
    <div class="squatchy-wrap bg-white">
      <div class="squatchy">
        <q-avatar><img src="~assets/squatchy.svg" /></q-avatar>

        <p class="q-ma-none">
          {{ squatchyText }}
        </p>
      </div>
    </div>

    <q-input
      v-model="squatchyQuery"
      outlined
      label="Search by feature"
      color="primary"
      bg-color="white"
      class="q-ma-md q-mb-lg"
      @keydown.enter="squatchySearch"
    >
      <template #append>
        <q-icon name="search" />
      </template>
    </q-input>

    <div class="park-cards q-px-md">
      <ParkCard
        v-for="park in visibleParksList"
        :key="park.name"
        :park="park"
      />
    </div>
  </q-page>
</template>

<script setup>
import ParkCard from "src/components/ParkCard.vue";
import useParksList from "src/data/useParksList";
import { computed, ref, toValue } from "vue";

defineOptions({
  name: "IndexPage",
});

const { parksList } = useParksList();

const visibleParksList = computed(() => {
  if (!searchResults.value) {
    return parksList.value;
  }

  return searchResults.value;
});

const squatchyWelcomeText = ref(
  "Hi, I'm Squatchy. I'm here to help you find your next adventure. What accessibility feature best describes what you are looking for?"
);

const squatchyText = ref(squatchyWelcomeText);

const squatchyQuery = ref("");

const searchResults = ref(null);

function squatchySearch() {
  squatchyText.value = "Let me get that for you!";

  // @TODO: Implement search functionality

  // @TODO: update

  squatchyQuery.value = "";
}
</script>

<style lang="scss" scoped>
.park-cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1rem;
}

.squatchy-wrap {
  margin: -1rem -1rem 1.5rem;
  display: flex;
}

.squatchy {
  width: 100%;
  margin: 0.25rem 0.25rem 0.75rem;
  border: 1px solid $primary;
  background: $tertiary;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 1em;
  padding: 1em;
  box-shadow: 0px 0.6px 1.8px 0px rgba(0, 0, 0, 0.1),
    0px 3.2px 7.2px 0px rgba(0, 0, 0, 0.13);
  border-radius: 4px;
}
</style>
