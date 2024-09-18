const routes = [
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      {
        name: "home",
        path: "",
        component: () => import("pages/IndexPage.vue"),
      },
      {
        name: "golden-ears-park",
        path: "/details/golden-ears-park",
        component: () => import("pages/park/GoldenEars.vue"),
      },
      {
        name: "cultus-lake-park",
        path: "/details/cultus-lake-park",
        component: () => import("pages/park/CultusLake.vue"),
      },
      {
        name: "sasquatch-park",
        path: "/details/sasquatch-park",
        component: () => import("pages/park/Sasquatch.vue"),
      },
      {
        name: "tyhee-lake-park",
        path: "/details/tyhee-lake-park",
        component: () => import("src/pages/park/TyheeLake.vue"),
      },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes;
