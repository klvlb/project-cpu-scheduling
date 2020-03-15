import Vue from 'vue';
import VueRouter from 'vue-router';

import Home from '../components/Home.vue';
import About from '../components/About.vue';

import Scheduling from '../components/os/Scheduling.vue';
import Multithreading from '../components/os/Multithreading.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/about',
    name: 'About',
    component: About,
  },
  {
    path: '/cpu-scheduling',
    name: 'Scheduling',
    component: Scheduling,
  },
  {
    path: '/multithreading-add',
    name: 'Multithreading',
    component: Multithreading,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
