<script setup lang="ts">
import MapView from './map/MapView.vue';
import {
  QuestionCircleOutlined,
  SyncOutlined,
  ShareAltOutlined,
  EyeOutlined
} from '@ant-design/icons-vue';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const map = ref()

const modal2Visible = ref<boolean>(false);

const followInfo = [
  {
    name:"小约翰可汗",
    href:"https://space.bilibili.com/23947287"
  },
  {
    name:"李干嘛",
    href:"https://space.bilibili.com/1156068103"
  },
]
const router = useRouter()

function toAbout() {
  router.push({name:"about"})
  
}
function resize(){
  map.value.mapResize()
}

function share() {
  let href= window.location.href
  console.log(href)
  // 打开弹窗展示二维码
  modal2Visible.value = true
}

function follow() {
  // 打开李干嘛与小约翰的弹窗
  modal2Visible.value = true
}

function clickArea(params:any){
  // 如果data有数据则打开弹窗
  console.log(params)
  modal2Visible.value = true
}

</script>

<template>
  <div class="content">
    <MapView ref="map" @click-area="clickArea"></MapView>
    <!-- <Card></Card> -->
    <a-float-button-group shape="square" :style="{ right: '64px' }">
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

    <div class="models">
      <a-modal
        v-model:open="modal2Visible"
        title="Vertically centered modal dialog"
        centered
        @ok="modal2Visible = false"
      >
        <p>some contents...</p>
        <p>some contents...</p>
        <p>some contents...</p>
      </a-modal>
    </div>
  </div>
</template>

<style scoped>
.content {
  position: relative;
}
</style>
