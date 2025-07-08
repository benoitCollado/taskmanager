<script setup lang="ts">
  import {useTaskListStore} from "../store/taskLists";
  import { onMounted, ref} from 'vue';
  import ZodCart from "../components/ZodCart.vue";
  import ZodForm from "../components/ZodForm.vue";
  import { TaskListReadSchema, TaskListCreateSchema } from "../schemas/TaskList.schema";

  const isCreating = ref<boolean>(false);

  const store = useTaskListStore();

  onMounted(()=>{
    store.fetch(false);
  })

  async function handleSavedModifications(pyaload:any, id:number){
    try{ 
      const result = await store.modify(pyaload, id);
      if(result){
        await store.fetch(true);
        console.log("okay");
      }else{
        console.log("un problème est survenu dans le modification")
      }
    }catch(err){
      console.error("une erreur est survenue : ", err);
    }
  }

  async function handleCreate(payload:any){
    try{
      console.log("ici")
      const result = await store.save(payload);
      if(result){
        await store.fetch(true);
        openCloseForm();
        console.log("okay");
      }else{
        console.log("impossible de créer la nouvelle liste");
      }
    }catch(err){
      console.error("une erreur est survenue : " , err);
    }
  }

  async function eraseList(id:number){
    try{
      const result = await store.erase(id);
      if(result){
        await store.fetch(true);
        console.log("la supression est un succès");
      }else{
        console.log("la suppression est un echec");
      }
    }catch(err){
      console.error("erreur survenue dans la suppression :", err)
    }
  }

  function openCloseForm(){
     isCreating.value = !isCreating.value;
  }
</script>

<template>
  <div class="p-4">
    <h1>Listes de tâches </h1>


    <div v-for="list in store.taskLists" :key="list.id" class="task-cart">
      
        <ZodCart :data="list" :schema-mod="TaskListCreateSchema" :schema-read="TaskListReadSchema" @saved="(payload)=>handleSavedModifications(payload, list.id)">
          <template #link="props">
            <router-link :to="{name: 'TaskListDetail', params:{id:list.id}}">
              <component :is="props.widget">
                {{props.value}}
              </component>
            </router-link>
          </template>
          <span @click="eraseList(list.id)" class="close-button">X</span>
        </ZodCart>
    </div>
    <button v-if="!isCreating" @click="openCloseForm">Créer une Liste</button>
    <div v-if="isCreating" class="task-cart">
      <ZodForm :schema="TaskListCreateSchema" @saved="handleCreate" @canceled="openCloseForm" ></ZodForm>
    </div>
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