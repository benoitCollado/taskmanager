import {z} from "zod"
import {TaskReadSchema} from "./Task.schema"
import {withMeta} from "./ZodFieldMetaData"

export const TaskListReadSchema = z.object({
  id: withMeta(z.number(),{
    label:"id",
    placeholder:"id",
    readonly:true,
    widget:"p",
    hiden:true,
  }),
  name: withMeta(z.string(),{
    label:"name",
    placeholder:"list",
    readonly:true,
    widget:"h4",
    hiden:false,
    link:true
  }),
  tasks_list:withMeta(z.array(TaskReadSchema),{
    label:"tasks list",
    placeholder:"",
    readonly:true,
    widget:"ZodCart",
    hiden:true
  })
});

export type TaskListRead = z.infer<typeof TaskListReadSchema>;

export const TaskListCreateSchema = z.object({
  name: withMeta(z.string(),{
    label:"name",
    placeholder:"list",
    readonly:false,
    widget:"input",
    inputType:"text",
    hiden:false,
    default:"nom de liste"
  }),
});

export type TaskListcreate = z.infer<typeof TaskListCreateSchema>;