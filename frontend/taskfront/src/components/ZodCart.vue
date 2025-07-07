<script setup lang="ts">

import {ref, reactive, defineProps} from 'vue';
import {ZodObject, type ZodRawShape} from 'zod';
import {getMeta} from "../schemas/ZodFieldMetaData"
import ZodForm from './ZodForm.vue';

const props = defineProps<{
    schemaRead: ZodObject<ZodRawShape>,
    schemaMod: ZodObject<ZodRawShape>,
    store:{
        save: (data:ZodRawShape) => Promise<boolean|undefined>
    }
    data:any,
}>();

const emit = defineEmits(['saved']);

const isEdit = ref(false);
const formData = reactive<Record<string,any>>({})

function initFormData(){
    const shape = props.schemaMod.shape;
    for(const key in shape){
        formData[key] = props.data?.[key];
    }
}

initFormData();

</script>

<template>
    <div v-if="!isEdit">
        <span @click="isEdit=!isEdit">modifier</span>
        <div v-for="(schemaField, key) in props.schemaRead.shape" :key="key" :style="getMeta(schemaField)?.hiden ? 'display: none;': ''">
            <component :is="getMeta(schemaField)?.widget">
                {{ data[key] }}
            </component>
        </div>
        <slot></slot>
    </div>
    <div v-else>
        <ZodForm :schema="schemaMod" :store="{save:props.store.save}" :initial-data="formData" @saved="emit('saved')" @canceled="isEdit=!isEdit"/>
    </div>
</template>