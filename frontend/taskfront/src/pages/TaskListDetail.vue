<script setup lang="ts">
  import {useTaskListStore} from "../store/taskLists";
  import {useTaskStore} from "../store/task"
  import {onMounted,ref} from 'vue';
  import {useRoute} from 'vue-router';
  import {TaskListRead} from '../schemas/TaskList.schema';
  import {TaskRead} from '../schemas/Task.schema';

  const taskStore = useTaskStore();
  const taskListStore = useTaskListStore();
  const route = useRoute();
  const id = route.params.id;
  const list = ref<TaskListRead>();
  const tasks = ref<TaskRead>()

  onMounted(async () => {
  console.log(id);
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
  <div class="p-4">
    <h1>Liste : {{ list?.name ?? 'chargement...' }}</h1>
    <div v-for="task in tasks" :key="task.id">
      {{task.name}} - status : {{ task.status }} 
    </div>
  </div>
</template>