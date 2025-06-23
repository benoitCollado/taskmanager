<script setup lang="ts">
  import {useTaskListStore} from "../store/taskLists";
  import {onMounted} from 'vue';

  const store = useTaskListStore()

  onMounted(()=>{
    store.fetchTaskList()
  })
</script>

<template>
  <div class="p-4">
    <h1>Listes de tâches </h1>
    <div v-for="list in store.taskLists" :key="list.id">
      {{list.name}}
    </div>
  </div>
</template>