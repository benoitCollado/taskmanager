import {z} from "zod"
import {TaskReadSchema} from "./Task.schema"

export const TaskListReadSchema = z.object({
  id: z.number(),
  name: z.string(),
  tasks_list:z.array(TaskReadSchema)
});

export type TaskListRead = z.infer<typeof TaskListReadSchema>;