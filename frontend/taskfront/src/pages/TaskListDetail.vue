<script setup lang="ts">
  import {useTaskListStore} from "../store/taskLists";
  import {useTaskStore} from "../store/task"
  import {onMounted, computed,reactive, ref} from 'vue';
  import {useRoute} from 'vue-router';
  import ZodForm from '../components/ZodForm.vue'
  import {TaskCreateSchema, TaskReadSchema} from '../schemas/Task.schema'
import ZodCart from "../components/ZodCart.vue";

   interface Alerte {
    type:"info"|"warning"|"error"
    title:string
    message:string
  }

  const taskStore = useTaskStore();
  const taskListStore = useTaskListStore();
  const route = useRoute();
  const id = route.params.id;
  const alerts = reactive<Alerte[]>([])
  const isAdding = ref(false)

 

  const list = computed (()=>{
    return taskListStore.taskLists.find(list => list.id === Number(id));
  })
  const tasks = computed(()=>{
    return taskStore.tasks.filter(task => task.list_id === Number(id));
  })

  const eraseTask = async (id:number)=>{
    const success = await taskStore.erase(id);
    if(success){
      taskStore.fetch(true)
    }else{
      const alert : Alerte = {type:"error", title:"Suppression Error", message:"The task Suppression doesn't work retry later or contact support"}
      alerts.push(alert)
      setTimeout(()=>{
        const index = alerts.indexOf(alert);
        if(index !== -1){
          alerts.splice(index, 1)
        }
      }, 3000)
    }
  }

  onMounted(async () => {
    await taskStore.fetch(true);
    await taskListStore.fetch(true);
  });

  function openCloseForm(){
    isAdding.value = !isAdding.value;
  }
</script>

<template>
  <div class="pa-4">
    <div v-for="alert in alerts" :class:="alert.type" class="alert">
      <h4>{{ alert.title }}</h4>
      <p>{{ alert.message }}</p>
    </div>

    <h1>Liste : {{ list?.name ?? 'chargement...' }}</h1>
    <div v-for="task in tasks" class="task-cart" :key="task.id">
      <ZodCart :data="task" :schema-mod="TaskCreateSchema" :schema-read="TaskReadSchema" :store="{save:taskStore.save}" @saved="taskStore.fetch(true)"/>
      <!--<h4>{{task.name}}</h4> 
      <span :class="task.status"> {{  task.status  }} </span>
      <span @click="eraseTask(task.id)" class="close-button">X</span>-->
      <span @click="eraseTask(task.id)" class="close-button">X</span>
    </div>

    <button v-if="!isAdding" @click="openCloseForm">Ajouter une Tâche</button>
    <ZodForm v-if="isAdding" :schema="TaskCreateSchema" :store="{save:taskStore.save}" :initial-data="{list_id : Number(id), status:'pending'}" @saved="()=>{taskStore.fetch(true); openCloseForm();}" @canceled="openCloseForm()" />
  </div>
</template>

<style scoped>
.task-cart{
position:relative;
display:block; 
border: 1px solid #CCC; 
border-radius:4px; 
margin:6px; 
padding:4px;
background-color: rgba(200,200,200,0.2);
}
.task-cart:hover{
  border: 1px solid #a0d;
  /*box-shadow: 1px 1px 1px #000;
  border: 1px solid #CCC;*/
}
.task-cart p{
  margin: 2px;
}
.task-cart h4{
  margin:2px;
}

.pending{
  color : #D55
}
.in-progress{
  color: #aa3
}

.done{
  color: #D55
}

.close-button{
  position: absolute;
  top:4px;
  right:8px;
  cursor: pointer;
  color: #000;
  transition: color 0.3s ease;
}

.close-button:hover{
  text-shadow: 0px 0px 2px #500;
}

.alert{
  position: absolute;
  top:10px;
  right:10px;
  border-radius:4px
}

.error{
  background-color: #D88;
}

.warning{
  background-color: #AA1;
}

.info{
  background-color: #0A4;
}
</style>