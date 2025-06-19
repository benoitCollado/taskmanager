<template>
  <div class="p-4">
    <h1 class="text-xl font-bold mb-4">Liste des tâches</h1>
    <div v-for="task in store.tasks" :key="task.id" class="mb-2 p-2 border rounded">
      {{task.name}} - <strong>{{task.status}}</strong>
    </div>
  </div>
</template>

<script setup lang="ts">
  import {onMounted} from 'vue';
  import {useTaskStore} from "../store/task";

  const store = useTaskStore();

  onMounted(()=>{
    store.fetchTasks();
  });
</script>