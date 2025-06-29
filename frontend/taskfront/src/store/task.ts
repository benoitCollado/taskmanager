import {defineStore} from 'pinia'
import axios from 'axios'
import {ref} from 'vue'
import {TaskReadSchema} from "../schemas/Task.schema"
import type {TaskRead} from "../schemas/Task.schema"

export const useTaskStore = defineStore('task',()=>{
  const tasks = ref<TaskRead[]>([]);
  const fetchTasks = async ()=>{
    try{
      const res = await axios.get<TaskRead[]>("https://08ca1522-3fb3-455c-9248-e538a904d79d-00-ijrqs1e7cp1.spock.replit.dev:3000/api/task/");
      const data: TaskRead[] = []
      res.data.foreach((object)=>{
        data.push(TaskReadSchema.parse(object))
      });
      tasks.value = data;
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
