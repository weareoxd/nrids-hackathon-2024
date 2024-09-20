// useParks.js
import slugify from "slugify";
import { api } from "src/boot/axios";
import { ref, toValue } from "vue";

const parksList = ref([]);
const isLoading = ref(false);
const error = ref(null);

export default function useParksList() {
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
      parksList.value = addSlugs(response.data);
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
    return parksList.value.find(park => park.slug === slug);
  }

  function addSlugs(parks) {
    const parksArray = toValue(parks);
    return parksArray.map(park => {
      const slug = slugify(park.name, { lower: true });

      return {
        ...park,
        slug
      };
    });
  }

  return { parksList, isLoading, error, getParkBySlug, addSlugs };
}
