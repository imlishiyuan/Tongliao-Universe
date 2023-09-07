<script setup lang="ts">
import FloatButton from '@/components/FloatButton.vue';
import MapView from './map/MapView.vue';
import Card from '@/components/Card.vue';
</script>

<template>
  <div class="content">
    <MapView></MapView>
    <!-- <Card></Card> -->
    <FloatButton></FloatButton>
  </div>
</template>

<style scoped>
.content {
  position: relative;
}
</style>
