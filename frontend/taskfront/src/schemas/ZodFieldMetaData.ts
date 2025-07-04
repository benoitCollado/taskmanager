import {z, type ZodTypeAny} from "zod";

export function withMeta<T extends ZodTypeAny>(schema : T, meta: Record<string,any>): T {
    (schema as any )._def.meta = meta;
    return schema;
}

export function getMeta<T extends ZodTypeAny>(schema:T): Record<string, any> | undefined {
    return (schema as any)._def.meta;
}