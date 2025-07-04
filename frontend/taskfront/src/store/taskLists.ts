import {defineStore} from 'pinia';
import {ref} from 'vue';
import axios from 'axios';
import {TaskListReadSchema} from "../schemas/TaskList.schema";
import type {TaskListRead} from "../schemas/TaskList.schema";


export const useTaskListStore = defineStore('tasklist', ()=>{
  const taskLists = ref<TaskListRead[]>([])
=======
  let lastFetched = 0;
  const fetch = async (forced:boolean)=>{
    const now = Date.now();
    const threeMinutes = 3 * 60 * 1000;

    if(now - lastFetched < threeMinutes && !forced){
      return;
    }

>>>>>>> feature/vuetify
    try{
      const res = await axios.get<TaskListRead[]>("http://localhost:8000/api/tasklist/")
      const data : TaskListRead[] = []
      res.data.forEach((object:TaskListRead) => {
        data.push(TaskListReadSchema.parse(object))
      });
      taskLists.value = data
      //console.log(data)
    }catch(err){
      console.error("erreur dans la récupération des données de listes de tâches", err);
    }
  }
  return{taskLists, fetch}
})
