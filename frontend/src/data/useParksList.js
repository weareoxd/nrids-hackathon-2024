// useParks.js
import slugify from "slugify";
import { api } from "src/boot/axios";
import { ref } from "vue";

export function useParksList() {
  const parksList = ref([]);
  const isLoading = ref(false);
  const error = ref(null);

  // Function to fetch parks from the API
  async function fetchParks() {
    // If parks data is already loaded, don't fetch again
    if (parksList.value.length) {
      return;
    }

    isLoading.value = true;
    try {
      const response = await api.get("/park/park/");

      // add url slugs to park data
      parksList.value = response.data.map((park) => {
        const slug = slugify(park.name, { lower: true });

        return {
          ...park,
          slug,
        };
      });
    } catch (err) {
      console.error(err);
      error.value = err.message;
    } finally {
      isLoading.value = false;
    }
  }

  // Fetch parks only if they haven't been fetched yet
  fetchParks();

  function getParkBySlug(slug) {
    return parksList.value.find((park) => park.slug === slug);
  }

  return { parksList, isLoading, error, getParkBySlug };
}
