<template>
  <div v-if="parkData" class="park-details">
    <h2 class="q-mt-md q-mb-lg">{{ parkData.name }}</h2>

    <div class="q-my-lg">
      <div v-if="parkData?.data?.location" class="two-columns">
        <div class="column">
          <img src="~assets/icons/location-dot.svg" height="24" />
        </div>
        <div class="column">
          {{ parkData.data.location }}
        </div>
      </div>
      <div v-if="parkData?.data?.status" class="two-columns">
        <div class="column">
          <img :src="getImageUrl(`${parkData.data.status}.svg`)" height="24" />
        </div>
        <div class="column">
          {{ toTitleCase(parkData.data.status) }}
        </div>
      </div>
      <div v-if="parkData?.data?.calendar" class="two-columns">
        <div class="column">
          <img src="~assets/icons/calendar.svg" height="24" />
        </div>
        <div class="column">
          {{ parkData.data.calendar }}
        </div>
      </div>
    </div>

    <div class="q-my-lg">
      <q-carousel
        v-model="slide"
        animated
        navigation
        infinite
        autoplay
        arrows
        transition-prev="slide-right"
        transition-next="slide-left"
        height="250px"
        @mouseenter="autoplay = false"
        @mouseleave="autoplay = true"
      >
        <q-carousel-slide
          v-for="(value, key) in parkData.data.gallery"
          :key="`gallery-${key}`"
          :name="key"
          :img-src="value"
        />
      </q-carousel>
    </div>

    <h4 class="q-my-lg">Highlights</h4>

    <p
      v-for="(value, key) in parkData.data.description"
      :key="`description-${key}`"
    >
      {{ value }}
    </p>

    <h4 class="q-my-lg">Experiences</h4>

    <q-btn
      v-if="parkData"
      icon="add_a_photo"
      color="primary"
      label="Share your experience"
      size="lg"
      class="q-mb-lg full-width-sm"
      @click="showAddCommentForm = true"
    />

    <div
      v-for="(value, key) in parkData.feedback"
      :key="`feedback-${key}`"
      class="comment"
    >
      <p>{{ value.comments }}</p>

      <div class="q-gutter-sm row items-start">
        <q-img
          v-for="(photo_value, photo_key) in value.photos"
          :key="`feedback-${key}-photo-${photo_key}`"
          :src="photo_value"
          style="max-width: 150px; height: 150px"
          fit="cover"
        >
        </q-img>
      </div>
    </div>

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
    if (!newParkId) {
      return;
    }

    const response = await api.get(`/park/park/${newParkId}`);
    parkData.value = response.data;
  },
  { immediate: true }
);

const showAddCommentForm = ref(false);

const slide = ref(1);

const toTitleCase = (str) => {
  return str.replace(/\w\S*/g, (txt) => {
    return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
  });
};

const getImageUrl = (str) => {
  return new URL(`../assets/icons/${str}`, import.meta.url);
};
</script>

<style lang="scss" scoped>
.two-columns {
  display: flex;
  align-items: center;
  margin-bottom: 1em;
  gap: 16px;

  .column {
    &:first-child {
      width: 32px;
      flex: none;
    }

    &:last-child {
      flex: 1;
    }
  }
}

@media (max-width: 600px) {
  .full-width-sm {
    width: 100%;
  }
}

.comment {
  margin-bottom: 1em;
  padding: 1em;
  border: 1px solid $primary;
  border-radius: 4px;

  img {
    margin-top: 1em;
    margin-right: 1em;
  }
}
</style>
