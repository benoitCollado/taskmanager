import {defineStore} from 'pinia'
import axios from 'axios'
import {ref, reactive} from 'vue'
import {TaskReadSchema, TaskCreateSchema, type TaskCreate} from "../schemas/Task.schema"
import type {TaskRead} from "../schemas/Task.schema"
=======
import {z, type ZodRawShape} from "zod"

export const useTaskStore = defineStore('task',()=>{
  const tasks = reactive<TaskRead[]>([]);
  let lastFetched : number = 0
  const fetch = async (forced:boolean): Promise<void>=>{

    const now = Date.now();
    const threeMinutes = 3 * 60 * 1000;

    if(now - lastFetched < threeMinutes && !forced){
      return;
    }


>>>>>>> feature/vuetify
    try{
      const res = await axios.get<TaskRead[]>("http://localhost:8000/api/task/");
      const data: TaskRead[] = []
      res.data.forEach((object)=>{
        data.push(TaskReadSchema.parse(object))
      });
=======
      tasks.splice(0, tasks.length, ...data);
      lastFetched = now;
>>>>>>> feature/vuetify
    } catch {
        console.error("problème dans le fetch")
    }  
  }
=======
  const save = async (task:ZodRawShape): Promise<boolean | undefined>=>{
    try{
      const res = await axios.post<TaskCreate>("http://localhost:8000/api/task/", task);
      if(res.status === 201){
        return true;
      }else{
        return false;
      }
    }catch{
      console.error("problème dans le post");
    }
  }

  return {tasks, fetch, save};
>>>>>>> feature/vuetify
  
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
