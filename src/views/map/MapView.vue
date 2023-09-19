<script setup lang="ts">
// 地图主页
import * as echarts from 'echarts/core';
import {
    TitleComponent,
    LegendComponent,
    VisualMapComponent,
    GeoComponent,
} from 'echarts/components';

import type {
    TitleComponentOption,
    VisualMapComponentOption,
    LegendComponentOption,
    GeoComponentOption,

} from 'echarts/components'

import type {} from 'echarts/types/dist/shared'
import { MapChart } from 'echarts/charts';
import type { MapSeriesOption } from 'echarts/charts';
import { CanvasRenderer } from 'echarts/renderers';
import { inject, onMounted } from 'vue';
import type { Axios } from 'axios';
import usaJson from '@surbowl/world-geo-json-zh'

echarts.use([
    TitleComponent,
    VisualMapComponent,
    LegendComponent,
    GeoComponent,
    MapChart,
    CanvasRenderer
]);

type EChartsOption = echarts.ComposeOption<
    | TitleComponentOption
    | LegendComponentOption
    | VisualMapComponentOption
    | GeoComponentOption
    | MapSeriesOption
>;

let mapChart:any

let option: EChartsOption


onMounted(() => {

    const chartDom = document.getElementById('map')!

    resize()

    mapChart = echarts.init(chartDom,'dark');

    mapChart.showLoading();

    const axios = inject<Axios>("axios")

    mapChart.hideLoading();
    
    echarts.registerMap('tongliao-world', usaJson as any, {
        // 此处需要将回龙观、天通苑与通辽标出
    });
    option = {
        title: {
            show:true,
            text: '通辽宇宙地图',
            borderColor: "#FFF",
            // 殷红
            textStyle:{
                color: "#82111f"
            },
            subtextStyle:{
                color: "#82111f"
            },
            subtext: 'the map of tongliao universe',
            top: 64,
            right: 64
        },
        // 藏花红、姜红
        visualMap:{
            type: 'piecewise',
            show:true,
            categories:['奇葩小国','未探索区域'],
            orient: 'vertical',
            left: 64,
            top: 64,
            selectedMode:false,
            dimension:0,
            inRange:{
                color:['#ec2d7a','#eeb8c3']
            },
            outOfRange: {
                color:"#eeb8c3"
            }
        },
        series: [
            {
                name: '奇葩小国',
                type: 'map',
                roam: true,
                zoom: 1.1,
                selectedMode: false,
                map: 'tongliao-world',
                label:{
                    color:"#FFF",
                },
                itemStyle:{
                    areaColor:'#ec2d7a',
                    borderWidth:0
                },
                emphasis: {
                    label: {
                        color:"#FFF",
                        show: true
                    },
                    itemStyle:{
                        areaColor:"#1661ab",
                        shadowColor: 'rgba(0, 0, 0, 0.7)',
                        shadowBlur: 10
                    }
                },
                data: [
                    {
                        name:"乍得",
                        groupId:'奇葩小国'
                    }
                ]
            }
        ]
    };

    mapChart.setOption(option);
    
    window.onresize = () => {
        resize()
        mapChart.resize()
    };

    function resize(){
        chartDom.style.width = window.innerWidth+'px'
        chartDom.style.height = window.innerHeight+'px'
    }

})



function mapResize(){
    console.log('mapResize')
    mapChart.setOption(option,true)
}

defineExpose({
    mapResize,
})




</script>

<template>
    <div id="map"></div>
</template>

<style scoped>
</style>
