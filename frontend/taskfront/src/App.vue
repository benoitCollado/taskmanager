<template>
 <v-app>
  <v-app-bar app>
    <v-toolbar-title>Gestionaire des tâches</v-toolbar-title>
    <v-spacer />
    <v-btn text :to="{name:'TaskLists'}">Acceuil</v-btn>
  </v-app-bar>
  <v-main class="pa-4">
    <router-view/>
  </v-main>
 </v-app>
</template>

<script setup lang="ts">
</script>
