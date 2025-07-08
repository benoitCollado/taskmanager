<script setup lang="ts">

import {ref, reactive, defineProps} from 'vue';
import {ZodObject, type ZodRawShape} from 'zod';
import {getMeta} from "../schemas/ZodFieldMetaData"
import ZodForm from './ZodForm.vue';

const props = defineProps<{
    schemaRead: ZodObject<ZodRawShape>,
    schemaMod: ZodObject<ZodRawShape>,
    data:any,
}>();

const emit = defineEmits<{
    (e:'saved', payload:any):void
}>();

const isEdit = ref(false);
const formData = reactive<Record<string,any>>({})

function initFormData(){
    const shape = props.schemaMod.shape;
    for(const key in shape){
        formData[key] = props.data?.[key];
    }
}

initFormData();
function handleEmitSave(payload:any){
    try{
        const result = props.schemaMod.parse(payload)
        isEdit.value= !isEdit.value;
        if(result){
            emit('saved', payload)
        }else{
            console.log("erreur les données ne sont cohérentes");
        }
    }catch(err){
        console.error("une erreur est survenue : ", err);
    }
}
</script>

<template>
    <div v-if="!isEdit">
        <span @click="isEdit=!isEdit">modifier</span>
        <div v-for="(schemaField, key) in props.schemaRead.shape" :key="key" :style="getMeta(schemaField)?.hiden ? 'display: none;': ''">
            
                <!-- Si le champ a une meta link, on passe par le slot link -->
                <slot
                    name="link"
                    :field="key"
                    :value="data[key]"
                    :widget="getMeta(schemaField)?.widget"
                >
                <component :is="getMeta(schemaField)?.widget">
                    {{ data[key] }}
                </component>
                </slot>

                <!-- Sinon rendu normal -->
                <!--<component v-else :is="getMeta(schemaField)?.widget">
                {{ data[key] }}
                </component>-->
        </div>
        <slot></slot>
    </div>
    <div v-else>
        <ZodForm :schema="schemaMod" :initial-data="formData" @saved="handleEmitSave" @canceled="isEdit=!isEdit"/>
    </div>
</template>