import {createRouter, createWebHistory} from 'vue-router';
import Home from "../pages/Home.vue";
import TaskLists from "../pages/TaskLists.vue"



const routes = [
  {path:"/", name: "TaskLists", component:TaskLists}
];

export default createRouter({
  history:createWebHistory(),
  routes
});