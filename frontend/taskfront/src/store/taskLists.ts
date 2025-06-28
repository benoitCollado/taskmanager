import {defineStore} from 'pinia';
import {ref} from 'vue';
import axios from 'axios';
import {TaskListReadSchema} from "../schemas/TaskList.schema";
import type {TaskListRead} from "../schemas/TaskList.schema";


export const useTaskListStore = defineStore('tasklist', ()=>{
  const taskLists = ref<TaskListRead[]>([])
  const fetchTaskList = async ()=>{
    try{
      const res = await axios.get<TaskListRead[]>("https://08ca1522-3fb3-455c-9248-e538a904d79d-00-ijrqs1e7cp1.spock.replit.dev:3000/api/tasklist/")
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
  return{taskLists, fetchTaskList}
})
