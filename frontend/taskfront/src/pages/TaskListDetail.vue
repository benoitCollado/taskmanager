<script setup lang="ts">
  import {useTaskListStore} from "../store/taskLists";
  import {useTaskStore} from "../store/task"
  import {onMounted,ref} from 'vue';
  import {useRoute} from 'vue-router';
  import type  {TaskListRead} from '../schemas/TaskList.schema';
  import type {TaskRead} from '../schemas/Task.schema';
  import TaskForm from '../components/TaskForm.vue';
  import ZodForm from '../components/ZodForm.vue'
  import {TaskReadSchema} from '../schemas/Task.schema'

  const taskStore = useTaskStore();
  const taskListStore = useTaskListStore();
  const route = useRoute();
  const id = route.params.id;
  const list = ref<TaskListRead>();
  const tasks = ref<TaskRead>();
  const newTask = ref('');

  function addTask(){
    console.log(newTask.value);
  }

  onMounted(async () => {
  await taskStore.fetchTasks();
  await taskListStore.fetchTaskList();
  console.log(taskStore.tasks);
  console.log(taskListStore.taskLists);
  const idNumber = Number(id);
  list.value = taskListStore.taskLists.find(list => list.id === idNumber);
  tasks.value = taskStore.tasks.filter(task => task.list_id === idNumber);
  console.log(tasks);
  //taskListStore.fetchTaskLists()
  });
</script>

<template>
  <div>
    <h1>Liste : {{ list?.name ?? 'chargement...' }}</h1>
    <div
      v-for="task in tasks"
      :key="task.id"
      style="margin:0.1rem; border-radius: 4px; border:1px solid #aaa; padding:0.1rem;">
        <h2 style="margin:0.1rem">
          {{ task.name }}
        </h2>
        <p style="margin:0.1rem;">{{ task.status }}</p>
    </div>
    <ZodForm :schema="TaskReadSchema" :store="taskStore" />
  </div>
</template>