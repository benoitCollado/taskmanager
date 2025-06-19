import {defineStore} from 'pinia'
import axios from 'axios'
import {ref} from 'vue'

export interface Task{
  id: number
  name: string
  status: string
  list_id: number
}

export const useTaskStore = defineStore('task',()=>{
  const tasks = ref<Task[]>([]);
  const fetchTasks = async ()=>{
    try{
      const res = await axios.get<Task[]>("https://08ca1522-3fb3-455c-9248-e538a904d79d-00-ijrqs1e7cp1.spock.replit.dev:3000/tasks/");
      tasks.value = res.data;
      console.log(tasks.value);
    } catch {
        console.error("problème dans le fetch")
    }  
  }

  return {tasks, fetchTasks};
  
}/*{
  state: () => ({
    tasks: [] as Task,
  }),
  actions:{
    async fetchTasks(){
      const res = await axios.get<Task[]>("https://08ca1522-3fb3-455c-9248-e538a904d79d-00-ijrqs1e7cp1.spock.replit.dev:3000/tasks/");
      this.tasks = res.data;
      console.log(res.data);
    }
  }
}*/)
