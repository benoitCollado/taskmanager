import {z} from "zod";
import {TASK_STATUS} from "../constants/constants"

export const TaskReadSchema = z.object({
  name:z.string(),
  id:z.number(),
  list_id:z.number(),
  status: z.enum(TASK_STATUS)
});

export type TaskRead = z.infer<typeof TaskReadSchema>;