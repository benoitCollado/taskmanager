<script setup lang="ts">
import {reactive, defineProps} from 'vue';
import {ZodObject, type ZodRawShape} from 'zod';
import {getMeta} from "../schemas/ZodFieldMetaData"


const props = defineProps<{
    schema: ZodObject<ZodRawShape>,
    initialData?: Record<string, any>
}>();

const emit = defineEmits<{
    (e:'saved', payload:any):void
    (e:'canceled'):void
}>();

const errors = reactive<Record<string, string | null >>({});
const formData = reactive<Record<string,any>>({});

function initFormData(){
    const shape = props.schema.shape;
    for(const key in shape){
        const meta = getMeta(shape[key]);
        formData[key] = props.initialData?.[key] ?? getDefaultValue(shape[key]._def.typeName, meta);
    }
}

function getDefaultValue(typeName: string, meta?: Record<string, any>){
    if(meta?.default !== undefined) return meta.default;
    switch(typeName){
        case 'ZodString': return '';
        case 'ZodNumber': return 0;
        case 'ZodBoolean': return false;
        case 'ZodEnum': return '';
        default: return '';
    }
}

initFormData();
Object.keys(errors).forEach(k=> errors[k] = null);

    


async function submit(){
    try{
        errorsClear();
        const parsed = props.schema.parse(formData);
        //const result = await props.store.save(parsed);
        if (parsed){
            emit('saved', parsed);
            console.log("là");
        }else{
            errors['erreur post'] = "impossible d'enregitrer la tâche veuillez recommencr plus tard"
        }

    }catch (err : any){
        if(err.errors){
            err.errors.forEach((e:any)=>{
                errors[e.path[0]] = e.message;
            })
        }else{
            console.log("une erreur est survenue : "  ,err);
        }
    }
}

function errorsClear(){
    Object.keys(errors).forEach(k=>errors[k] = null);
}

</script>

<template>
        <div v-for="(schemaField, key) in props.schema.shape" :key="key" style="margin-bottom:1rem;" :style="getMeta(schemaField)?.hiden ? 'display: none;':''">
            <label :for="key.toString()" style="font-weight: bold; display:block; margin-bottom:0.3em;">{{ getMeta(schemaField)?.label ?? key }}</label>

            <input
                v-if="getMeta(schemaField)?.widget  === 'input'"
                :type="getMeta(schemaField)?.inputType ?? 'text'"
                :id="key.toString()"
                v-model="formData[key]"
                :placeholder="getMeta(schemaField)?.placeholder ?? key.toString()"
                style="width:90%; padding:0.5rem; border-radius:4px; border:1px solid #aaa;"
            />

            <input
                v-else-if="schemaField._def.typeName === 'ZodNumber'"
                type="number"
                :id="key.toString()"
                v-model="formData[key]"
                style="width:90%; padding:0.5rem; border-radius:4px; border:1px solid #aaa;"
            />

            <input
                v-else-if="schemaField._def.typeName === 'ZodBoolean'"
                type="checkbox"
                :id="key.toString()"
                v-model="formData[key]"

            />
            <select
                v-else-if="schemaField._def.typeName === 'ZodEnum'"
                :id="key.toString()"
                v-model="formData[key]"
                style="width:90%; padding:0.5rem; border-radius: 4px; border:1px solid #aaa;"
            >
                <option     
                    v-for="option in schemaField._def.values" 
                    :key="option" 
                    :value="option"
                >
                {{ option }}
                </option>
            </select>

            <div v-if="errors[key]" style="color: red; font-size:0.85rem; margin-top: 0.2rem;">{{ errors[key] }}</div>
        </div>

        <button type="button" @click="submit" style="margin-right: 0.5rem;">Enregistrer</button>
        <button type="button" @click="emit('canceled')">Annuler</button>
</template>