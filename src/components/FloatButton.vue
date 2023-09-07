<script lang="ts" setup>
import {
  QuestionCircleOutlined,
  SyncOutlined,
  ShareAltOutlined,
  HeartOutlined
} from '@ant-design/icons-vue';

</script>

<template>
  <a-float-button-group shape="square" :style="{ right: '94px' }">
    <!-- 关于  -->
    <a-float-button>
      <template #icon>
        <QuestionCircleOutlined />
      </template>
    </a-float-button>
    <!-- 同步  -->
    <a-float-button>
      <template #icon>
        <SyncOutlined />
      </template>
    </a-float-button>
    <!-- 分享  -->
    <a-float-button>
      <template #icon>
        <ShareAltOutlined />
      </template>
    </a-float-button>
    <!-- 关注  -->
    <a-float-button>
      <template #icon>
        <HeartOutlined />
      </template>
    </a-float-button>
  </a-float-button-group>
</template>