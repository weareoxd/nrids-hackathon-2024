export default [
  {
    name: "Golden Ears Park",

    router: {
      name: "golden-ears-park",
      path: "/details/golden-ears-park",
      component: () => import("pages/park/GoldenEars.vue"),
    },
  },

  {
    name: "Cultus Lake Park",

    router: {
      name: "cultus-lake-park",
      path: "/details/cultus-lake-park",
      component: () => import("pages/park/CultusLake.vue"),
    },
  },

  {
    name: "Sasquatch Park",

    router: {
      name: "sasquatch-park",
      path: "/details/sasquatch-park",
      component: () => import("pages/park/Sasquatch.vue"),
    },
  },

  {
    name: "Tyhee Lake Park",

    router: {
      name: "tyhee-lake-park",
      path: "/details/tyhee-lake-park",
      component: () => import("src/pages/park/TyheeLake.vue"),
    },
  },
];
