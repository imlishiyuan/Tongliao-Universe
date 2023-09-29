<script setup lang="ts">

import { EyeOutlined, CalendarOutlined,FieldTimeOutlined,UserOutlined,BankOutlined } from '@ant-design/icons-vue'

const cardInfo = defineProps<{
    title?: string,
    list: Array<{
        countryName?: Array<string>,
        personName?: Array<string>,
        organizationName?: Array<string>,
        name?: string,
        bvid?: string,
        aid?: number,
        cover?: string,
        view?: number,
        duration?: string,
        pub_date?: string,
        url?: string,
    }>
}>()

</script>

<template>
    <div class="card">
        <a-typography-text strong v-if="cardInfo.title != undefined">{{ cardInfo.title }}</a-typography-text>
        <a-divider></a-divider>
        <div v-for="(item,i) in list" :key="item.bvid">
            <a-row justify="start" :align="'top'">
                <a-col>
                    <a-row>
                        <a-col :span="14" :align="'start'">
                            <a-space direction="vertical">
                                <a-typography-link :href="item.url" target="_blank">{{ item.name }}</a-typography-link>
                                <a-typography-text type="secondary">
                                    <CalendarOutlined style="margin-right: 4px" /> {{ item.pub_date }}
                                </a-typography-text>
                            </a-space>
                        </a-col>
                        <a-col :span="9" justify="space-around" offset="1">
                            <a-image :width="100" :src="'image/' + item.cover"></a-image>
                        </a-col>
                    </a-row>
                    
                    <a-row v-if="item.personName instanceof Array && item.personName!=undefined && !item.personName.includes('#')">
                        <a-col>
                            <span>
                                <a-typography-text type="secondary">
                                    <UserOutlined  style="margin-right: 4px" /> {{ item.personName.join('、') }}
                                </a-typography-text>
                                
                            </span>
                        </a-col>
                    </a-row>
                    <a-row v-if="item.organizationName instanceof Array && item.organizationName!=undefined && !item.organizationName.includes('#')">
                        <a-col>
                            <span>
                                <a-typography-text type="secondary">
                                    <BankOutlined  style="margin-right: 4px" /> {{ item.organizationName.join('、') }}
                                </a-typography-text>
                                
                            </span>
                        </a-col>
                    </a-row>

                    <a-row>
                        <a-col>
                            <span>
                                <a-typography-text type="secondary">
                                    <EyeOutlined style="margin-right: 4px" /> {{ item.view }}
                                </a-typography-text>
                                <a-divider type="vertical"></a-divider>
                                <a-typography-text type="secondary">
                                    <FieldTimeOutlined style="margin-right: 4px" /> {{ item.duration }}
                                </a-typography-text>
                            </span>
                        </a-col>
                    </a-row>
                    
                </a-col>
            </a-row>
            <div v-if="i!= (list.length-1)" style="width: 100%; margin-bottom: 10px; border-bottom: 1px solid ; border-color: rgb(215, 212, 212);"></div>
        </div>
    </div>
</template>

<style scoped></style>
