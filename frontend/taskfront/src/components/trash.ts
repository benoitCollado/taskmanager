/// FICHIER: src/store/task.ts
import { defineStore } from 'pinia'
import axios from 'axios'

export interface Task {
  id: number
  name: string
  status: string
  list_id: number
}

export const useTaskStore = defineStore('task', {
  state: () => ({
    tasks: [] as Task[],
  }),
  actions: {
    async fetchTasks() {
      const res = await axios.get<Task[]>('http://localhost:8000/tasks')
      this.tasks = res.data
    },
  },
})


/// FICHIER: src/App.vue
<template>
  <router-view />
</template>

<script setup lang="ts">
</script>

