import {defineStore} from 'pinia'
import axios from 'axios'
import { reactive} from 'vue'
import {TaskReadSchema,type TaskCreate} from "../schemas/Task.schema"
import type {TaskRead} from "../schemas/Task.schema"
import {type ZodRawShape} from "zod"

export const useTaskStore = defineStore('task',()=>{
  const tasks = reactive<TaskRead[]>([]);
  let lastFetched : number = 0
  const fetch = async (forced:boolean): Promise<void>=>{

    const now = Date.now();
    const threeMinutes = 3 * 60 * 1000;

    if(now - lastFetched < threeMinutes && !forced){
      return;
    }

    try{
      const res = await axios.get<TaskRead[]>("http://localhost:8000/api/task/");
      const data: TaskRead[] = []
      res.data.forEach((object)=>{
        data.push(TaskReadSchema.parse(object))
      });
      tasks.splice(0, tasks.length, ...data);
      lastFetched = now;
    } catch {
        console.error("problème dans le fetch")
    }  
  }
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

  const erase = async(id:number): Promise<boolean | undefined> => {
    try{
      const res = await axios.delete(`http://localhost:8000/api/task/${id}`);
      if(res.status === 204){
        return true;
      }else{
        return false;
      }
    }catch{
      console.log("une erreur est survenue dans la suppression de la donnée");
    }
  }

  return {tasks, fetch, save, erase};
  
})
