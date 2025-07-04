<template>
 <nav>
  <button><router-link :to="{name:'TaskLists'}">Acceuil</router-link></button>
 </nav>
  <main>
    <router-view/>
  </main>
</template>

<script setup lang="ts">
</script>
