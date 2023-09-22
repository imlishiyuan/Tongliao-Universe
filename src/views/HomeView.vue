<script setup lang="ts">
import MapView from './map/MapView.vue';
import {
  QuestionCircleOutlined,
  SyncOutlined,
  ShareAltOutlined,
  EyeOutlined,
  CopyOutlined
} from '@ant-design/icons-vue';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

import john from '@/assets/john.json'
import liganma from '@/assets/liganma.json'
import ClipboardJS from 'clipboard'
import { message } from 'ant-design-vue';


const [messageApi, contextHolder] = message.useMessage();

const map = ref()

const qrcodeVisible = ref<boolean>(false);

const shareVisible = ref<boolean>(false);

const aeraInfoVisible = ref<boolean>(false);

const href = window.location.href

const followInfo = {
  john:john,
  liganma: liganma,
}
const router = useRouter()

function toAbout() {
  router.push({name:"about"})
  
}

function resize(){
  map.value.mapResize()
}

function share() {
  console.log(href)
  // 打开弹窗展示二维码
  shareVisible.value = true
  new ClipboardJS("#copyShareLink")
  
}

function follow() {
  // 打开李干嘛与小约翰的弹窗
  qrcodeVisible.value = true

}

function clickArea(params:any){
  // 如果data有数据则打开弹窗
  console.log(params)
  aeraInfoVisible.value = true
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
        v-model:open="qrcodeVisible"
        title="感谢关注"
        centered
        @ok="qrcodeVisible = false"
      >
      <a-row :gutter="[16, 24]" justify="space-around" align="middle">
        <a-col :span="12" justify="space-around" align="middle">
          
          <a-qrcode
                error-level="H"
                :value="followInfo.john.space"
                :icon="'image/' + followInfo.john.avatar"
              />
        </a-col>
        <a-col :span="12" justify="space-around" align="middle">
          <a-qrcode
            error-level="H"
            :value="followInfo.liganma.space"
            :icon="'image/' + followInfo.liganma.avatar"
          />
        </a-col>
      </a-row>
        
        <template #footer>
        </template>
      </a-modal>

      <a-modal
        v-model:open="shareVisible"
        title="分享给朋友"
        centered
        @ok="qrcodeVisible = false"
      >
      <a-row :gutter="[16, 24]" justify="space-around" align="middle">
        <a-col :span="24" justify="space-around" align="middle" >
          
          <a-space direction="vertical" style="width: 100%;">
            <a-input-group compact>
            <a-button>
              链接
            </a-button>
            <a-input :value="href" style="width: calc(100% - 200px)" id="shareLink"/>
            <a-tooltip title="复制链接">
              <a-button id="copyShareLink" data-clipboard-action="copy" data-clipboard-target="#shareLink">
                <template #icon><CopyOutlined /></template>
              </a-button>
            </a-tooltip>
          </a-input-group>
          <a-qrcode
                error-level="H"
                :value="href"
                icon="favicon.ico"
              />
          </a-space>
          
        </a-col>
      </a-row>
        
        <template #footer></template>
      </a-modal>
    </div>
  </div>
</template>

<style scoped>
.content {
  position: relative;
}
</style>
