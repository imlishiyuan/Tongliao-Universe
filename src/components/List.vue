<script setup lang="ts">
import { defineProps } from 'vue';

const cardInfo = defineProps<{
    title?:string,
    list?: Array<{
            cover?:string,
            title?:string,
            pubdate?:string,
            len?:string,
        }>
}>()

</script>

<template>
    <div class="card">
        <a-space  direction="vertical">
        <a-typography-text strong v-if="cardInfo.title != undefined">{{ cardInfo.title }}</a-typography-text>
        <a-list item-layout="vertical" size="large" :data-source="list">
            <template #renderItem="{ item }">
                <a-list-item key="item.title">
                    <template #actions>
                    观看数
                    </template>
                    <template #extra>
                    <img
                        width="100"
                        alt="封面"
                        :src="'image/'+ item.cover"
                    />
                    </template>
                    <a-list-item-meta :description="item.description">
                    <template #title>
                        <a :href="item.href">{{ item.title }}</a>
                    </template>
                    </a-list-item-meta>
                    {{ item.content }}
                </a-list-item>
            </template>
        </a-list>
        </a-space>
    </div>
</template>

<style scoped>


</style>
