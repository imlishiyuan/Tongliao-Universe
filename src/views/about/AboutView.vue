<script setup lang="ts">
// 关于
import {ArrowLeftOutlined} from '@ant-design/icons-vue'
import About from '@/components/About.md'
import { useRouter } from 'vue-router';
import john from '@/assets/john.json'

const router = useRouter()


</script>

<template>
    <header class="header">
        <a-button type="primary" ghost @click="() => router.go(-1)"><ArrowLeftOutlined /> 回到地图</a-button> 
    </header>
    <main class="article">
        <About></About>
    </main>
    <footer class="footer">&COPY; Copyright <a-typography-link href="https://www.lishiyuan.cn/" target="_blank">lishiyuan</a-typography-link> {{new Date().getFullYear()}}. </footer>

    <a-float-button-group shape="circle">
        <a-back-top :visibility-height="0" />
    </a-float-button-group>
</template>

<style scoped>
.header {
    height: 56px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}
.header button {
    padding: 10px;
    height: 56px;
    border: 0px;
}

.article {
    padding: 24px;
    background-color: #fff;
    min-height: 280px;
    margin: 24px;
    border-radius: 2px;
    box-shadow: 0 1px 3px rgba(103, 101, 101, 0.1);
    overflow: hidden;
    transition: all 0.3s;
    font-size: 16px;
    line-height: 1.8;
    color: #606266;
    font-variant-ligatures: normal;
    font-variant-caps: normal;
    font-variant-numeric: normal;
    font-variant-east-asian: normal;
    font-weight: 400;
    font-stretch: normal;
    font-size-adjust: none;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC',
        'Hiragino Sans GB', 'Microsoft YaHei', 'Helvetica Neue', Helvetica,
        Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji',
        'Segoe UI Symbol';
}

.footer{
    text-align: center;
    padding: 12px;
    background-color: #fff;
}
</style>
