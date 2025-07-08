import {defineStore} from 'pinia';
import {ref} from 'vue';
import axios from 'axios';
import {TaskListReadSchema} from "../schemas/TaskList.schema";
import type {TaskListRead} from "../schemas/TaskList.schema";
import { type ZodRawShape } from 'zod';


export const useTaskListStore = defineStore('tasklist', ()=>{
  const taskLists = ref<TaskListRead[]>([])
  let lastFetched = 0;
  const fetch = async (forced:boolean)=>{
    const now = Date.now();
    const threeMinutes = 3 * 60 * 1000;

    if(now - lastFetched < threeMinutes && !forced){
      return;
    }
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

  const save = async (taskList:ZodRawShape): Promise<boolean | undefined>=>{
    try{
      const result = await axios.post("http://localhost:8000/api/tasklist/", taskList);
      if(result.status === 201){
        return true;
      }else{
        return false;
      }
    }catch(err){
      console.error("une erreur est survenue", err);
    }
  }

  const modify = async (taskList:ZodRawShape, id:number): Promise<boolean|undefined>=>{
    try{
      const result = await axios.put(`http://localhost:8000/api/tasklist/${id}`,taskList);
      if(result.status === 201){
        return true;
      }else{
        return false;
      }
    }catch(err){
      console.error("une erreur est survenue", err);
    }
  }

  const erase = async (id:number): Promise<boolean|undefined> =>{
    try{
      const result = await axios.delete(`http://localhost:8000/api/tasklist/${id}`);
      if(result.status === 204){
        return true;
      }else{
        return false;
      }
    }catch(err){
      console.log("une erreur est survenue :", err);
    }
  }
  return{taskLists, fetch, save, modify, erase}
})
