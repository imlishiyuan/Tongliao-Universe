<script setup lang="ts">

const cardInfo = defineProps<{
    avatar?:string,
    title?:string,
    sign?:string,
    qrcode?:string
}>()

</script>

<template>
    <div class="card">
        <a-space direction="vertical">
            <a-avatar v-if="cardInfo.avatar != undefined" :size="64" :src="cardInfo.avatar"></a-avatar>
            <a-typography-text strong v-if="cardInfo.title != undefined">{{ cardInfo.title }}</a-typography-text>
            <a-typography-text v-if="cardInfo.sign != undefined"><blockquote>{{cardInfo.sign}}</blockquote></a-typography-text>
            <a-qrcode error-level="H" v-if="cardInfo.qrcode" :value="cardInfo.qrcode" :icon="cardInfo.avatar" ></a-qrcode>
            <a-typography-link  v-if="cardInfo.qrcode" :href="cardInfo.qrcode" target="_blank">前往主页👉</a-typography-link> 
        </a-space>
    </div>
</template>

<style scoped>


</style>
