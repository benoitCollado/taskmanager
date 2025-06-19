import {defineStore} from 'pinia';
import {ref} from 'vue';
import axios from 'axios';
import Task from './task'

export interface TaskList{
  id: number,
  name: string,
  tasks:Task[]
}

export const useTaskListStore = defineStore('tasklist', ()=>{
  const taskLists = ref<TaskList[]>([])
  const fetchTaskList = async ()=>{
    try{
      const res = axios.get<TaskList>("https://08ca1522-3fb3-455c-9248-e538a904d79d-00-ijrqs1e7cp1.spock.replit.dev:3000/tasks/lists/")
      taskLists.value = res.data
    }catch{
      console.error("erreur dans la récupération des données de listes de tâches");
    }
  }
  return{tasllists, fetchTaskList}
})
