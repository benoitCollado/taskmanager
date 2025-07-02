<script setup lang="ts">
import {ref, reactive, defineProps} from 'vue';
import {ZodObject, type ZodRawShape, type infer as InferZod, Schema} from 'zod';

interface Props<T extends ZodRawShape>{
    schema: ZodObject<T>
        store:{
            save:(data:InferZod<ZodObject<T>>) => Promise<void>
            fetch:()=>Promise<void>
        }
    initialData?: Partial<InferZod<ZodObject<T>>>
}

const props = defineProps<{
    schema: ZodObject<ZodRawShape>
    store:{
        save:(data:InferZod<ZodObject<ZodRawShape>>) => Promise<void>
        fetch:()=>Promise<void>
    }
    initialData?: Record<string, any>
}>();
console.log("props schema" , props.schema);
console.log("props store" , props.store);
console.log("props initialData" , props.initialData);


const isActive = ref(false);
const errors = reactive<Record<string, string | null >>({});
const formData = reactive<Record<string,any>>({});

function initFormData(){
    const shape = props.schema.shape;
    for(const key in shape){
        formData[key] = props.initialData?.[key] ?? getDefaultValue(shape[key]._def.typeName);
    }
}

function getDefaultValue(typeName: string){
    switch(typeName){
        case 'ZodString': return '';
        case 'ZodNumber': return 0;
        case 'ZodBoolean': return false;
        case 'ZodEnum': return '';
        default: return '';
    }
}

initFormData();

function openForm(){
    isActive.value = true;
    initFormData();
    Object.keys(errors).forEach(k=> errors[k] = null);
}

async function submit(){
    try{
        errorsClear();
        const parsed = props.schema.parse(formData);
        await props.store.save(parsed);
        await props.store.fetch();
        isActive.value = false;
    }catch (err : any){
        if(err.errors){
            err.errors.forEach((e:any)=>{
                errors[e.path[0]] = e.message;
            })
        }
    }
}

function errorsClear(){
    Object.keys(errors).forEach(k=>errors[k] = null);
}

</script>

<template>
    <button @click="openForm">Ajouter une Tâche</button>
    <form v-if="isActive" @submit.prevent="submit" style="margin-top:1rem; border:1px solid #CCC; padding:1rem; border-radius:6px;">
        <div v-for="(schemaField, key) in props.schema.shape" :key="key" style="margin-bottom:1rem;">
            <label :for="key.toString()" style="font-weight: bold; display:block; margin-bottom:0.3em;">{{ key }}</label>

            <input
                v-if="schemaField._def.typeName === 'ZodString'"
                type="text"
                :id="key.toString()"
                v-model="formData[key]"
                :placeholder="key.toString()"
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

        <button type="submit" style="margin-right: 0.5rem;">Enregistrer</button>
        <button type="button" @click="isActive = false">Annuler</button>
    </form>
</template>