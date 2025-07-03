import {z} from "zod";
import {TASK_STATUS} from "../constants/constants"
import * as metaZod from "./ZodFieldMetaData"
import { readonly } from "zod/v4";
import { fa } from "vuetify/locale";

export const TaskReadSchema = z.object({
  name: metaZod.withMeta(z.string(),{
    label:"Nom",
    placeholder:"entrer une tâche",
    readonly:true,
    widget:"h2",
    hiden:false,
  }),
  id: metaZod.withMeta(z.number(),{
    label:"N° id",
    placeholder: null,
    readonly:true,
    widget:"p",
    hiden:true,
  }),
  list_id: metaZod.withMeta(z.number(),{
    label:"N° de liste id",
    placeholder: null,
    readonly:true,
    widget:"p",
    hiden:true,
  }),
  status: metaZod.withMeta(z.enum(TASK_STATUS),{
    label:"status de la tâche",
    placeholder:"pending",
    readonly:true,
    widget:"p",
    hiden:false,
  }),
});

export type TaskRead = z.infer<typeof TaskReadSchema>;

export const TaskCreateSchema = z.object({
  name: metaZod.withMeta(z.string(),{
    label:"Nom",
    placeholder:"entrer une tâche",
    readonly:false,
    widget:"input",
    inputType:"text",
    hiden:false,
    default:"tâche"
  }),
  list_id: metaZod.withMeta(z.number(),{
    label:"N° de liste id",
    placeholder: null,
    readonly:true,
    widget:"input",
    inputType:"number",
    hiden:true,
  }),
  status: metaZod.withMeta(z.enum(TASK_STATUS),{
    label:"status de la tâche",
    placeholder:"pending",
    readonly:false,
    widget:"select",
    hiden:false,
    default:TASK_STATUS[0],
  }),
});

export type TaskCreate = z.infer<typeof TaskCreateSchema>;