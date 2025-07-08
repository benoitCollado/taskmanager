import {defineStore} from 'pinia'
import axios from 'axios'
import {ref} from 'vue'
import {TaskReadSchema,type TaskCreate} from "../schemas/Task.schema"
import type {TaskRead} from "../schemas/Task.schema"
import {type ZodRawShape} from "zod"

export const useTaskStore = defineStore('task',()=>{
  const tasks = ref<TaskRead[]>([]);
  let lastFetched = ref(0);
  const fetch = async (forced:boolean): Promise<void>=>{

    const now = Date.now();
    const threeMinutes = 3 * 60 * 1000;

    if(now - lastFetched.value < threeMinutes && !forced){
      return;
    }

    try{
      const res = await axios.get<TaskRead[]>("http://localhost:8000/api/task/");
      const data: TaskRead[] = []
      res.data.forEach((object)=>{
        data.push(TaskReadSchema.parse(object))
      });
      tasks.value.splice(0, tasks.value.length, ...data);
      lastFetched.value = now;
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

  const erase = async (id:number): Promise<boolean | undefined> => {
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

  const modify = async (id:number, task:ZodRawShape): Promise<boolean|undefined> => {
    try{
      const res = await axios.put(`http://localhost:8000/api/task/${id}`, task);
      if(res.status === 201){
        return true;
      }else{
        return false;
      }
    }catch{
      console.error("problème survenue dans mla modification coté server");
    }
  }

  return {tasks, fetch, save, erase, modify};
  
})
