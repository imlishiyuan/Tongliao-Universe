<script setup lang="ts">
import MapView from './map/MapView.vue';
import Card from '@/components/Card.vue';
import {
  QuestionCircleOutlined,
  SyncOutlined,
  ShareAltOutlined,
  EyeOutlined
} from '@ant-design/icons-vue';
import { ref } from 'vue';

const map = ref()

function toAbout() {
  
}
function resize(){
  map.value.mapResize()
}

function share() {

}

function follow() {

}

</script>

<template>
  <div class="content">
    <MapView ref="map"></MapView>
    <!-- <Card></Card> -->
    <a-float-button-group shape="square" :style="{ right: '32px' }">
      <!-- 关于  -->
      <a-float-button @click="toAbout" tooltip="关于">
        <template #icon>
          <QuestionCircleOutlined />
        </template>
      </a-float-button>
      <!-- 同步  -->
      <a-float-button @click="resize" tooltip="重置地图">
        <template #icon>
          <SyncOutlined />
        </template>
      </a-float-button>
      <!-- 分享  -->
      <a-float-button @click="share" tooltip="分享">
        <template #icon>
          <ShareAltOutlined />
        </template>
      </a-float-button>
      <!-- 关注  -->
      <a-float-button @click="follow" tooltip="关注">
        <template #icon>
          <EyeOutlined />
        </template>
      </a-float-button>
    </a-float-button-group>
  </div>
</template>

<style scoped>
.content {
  position: relative;
}
</style>
