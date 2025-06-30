import {createRouter, createWebHistory} from 'vue-router';
import TaskLists from "../pages/TaskLists.vue";
import TaskListDetail from "../pages/TaskListDetail.vue";



const routes = [
  {path:"/", name: "TaskLists", component:TaskLists},
  {path:"/tasklist/:id", name:'TaskListDetail', component: TaskListDetail}
];

export default createRouter({
  history:createWebHistory(),
  routes
});