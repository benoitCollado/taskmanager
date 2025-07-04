<script setup lang="ts">
  import {useTaskListStore} from "../store/taskLists";
  import {useTaskStore} from "../store/task"
  import {onMounted,ref} from 'vue';
  import {useRoute} from 'vue-router';
  import {TaskListRead} from '../schemas/TaskList.schema';
  import {TaskRead} from '../schemas/Task.schema';
  import TaskForm from '../components/TaskForm.vue';

  const taskStore = useTaskStore();
  const taskListStore = useTaskListStore();
  const route = useRoute();
  const id = route.params.id;
  const list = ref<TaskListRead>();
  const tasks = ref<TaskRead>()

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
    <TaskForm/>
    <v-list-item
      v-for="task in tasks"
      :key="task.id">
        <v-list-item-content>
          <v-list-item-title>
            {{ task.name }}
          </v-list-item-title>
          {{ task.status }}
        </v-list-item-content>
    </v-list-item>
  </div>
</template>