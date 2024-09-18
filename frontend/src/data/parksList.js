export default [
  {
    name: "Golden Ears Park",
    image:
      "https://nrs.objectstore.gov.bc.ca/kuwyyf/RS_7390_Golden_Ears_gal_e622f8f345.jpg",

    router: {
      name: "golden-ears-park",
      path: "/details/golden-ears-park",
      component: () => import("pages/park/GoldenEars.vue"),
    },
  },

  {
    name: "Cultus Lake Park",
    image:
      "https://nrs.objectstore.gov.bc.ca/kuwyyf/cultus_lake_park_41_gal_RS_10712_62d974466e.jpg",

    router: {
      name: "cultus-lake-park",
      path: "/details/cultus-lake-park",
      component: () => import("pages/park/CultusLake.vue"),
    },
  },

  {
    name: "Sasquatch Park",
    image:
      "https://nrs.objectstore.gov.bc.ca/kuwyyf/RS_7782_Sasquatch_Iain_Robert_Reid_46_gal_e77a88ffd1.jpg",

    router: {
      name: "sasquatch-park",
      path: "/details/sasquatch-park",
      component: () => import("pages/park/Sasquatch.vue"),
    },
  },

  {
    name: "Tyhee Lake Park",
    image:
      "https://nrs.objectstore.gov.bc.ca/kuwyyf/dbc_131246_dbc_1200_px_Tyhee_9ade1cba78.jpg",

    router: {
      name: "tyhee-lake-park",
      path: "/details/tyhee-lake-park",
      component: () => import("src/pages/park/TyheeLake.vue"),
    },
  },
];
