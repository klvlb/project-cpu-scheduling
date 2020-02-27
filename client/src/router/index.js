import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../components/Home.vue";
import Scheduling from "../components/CPUScheduling.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/cpu-scheduling",
    name: "Scheduling",
    component: Scheduling,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
