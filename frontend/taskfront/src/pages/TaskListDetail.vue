<script setup lang="ts">
  import {useTaskListStore} from "../store/taskLists";
  import {useTaskStore} from "../store/task"
  import {onMounted,ref,watch, computed} from 'vue';
  import {useRoute} from 'vue-router';
  import type  {TaskListRead} from '../schemas/TaskList.schema';
  import type {TaskRead} from '../schemas/Task.schema';
  import ZodForm from '../components/ZodForm.vue'
  import {TaskCreateSchema} from '../schemas/Task.schema'

  const taskStore = useTaskStore();
  const taskListStore = useTaskListStore();
  const route = useRoute();
  const id = route.params.id;

  const list = computed (()=>{
    return taskListStore.taskLists.find(list => list.id === Number(id));
  })
  const tasks = computed(()=>{
    return taskStore.tasks.filter(task => task.list_id === Number(id));
  })

  onMounted(async () => {
    await taskStore.fetch(true);
    await taskListStore.fetch(true);
  });
</script>

<template>
  <div class="p-4">
    <h1>Liste : {{ list?.name ?? 'chargement...' }}</h1>
    <div v-for="task in tasks" :key="task.id">
      {{task.name}} - status : {{ task.status }} 
    </div>
    <ZodForm :schema="TaskCreateSchema" :store="{save:taskStore.save, fetch:taskStore.fetch}" :initial-data="{list_id : Number(id), status:'pending'}" @saved="taskStore.fetch(true)" />
  </div>
</template>