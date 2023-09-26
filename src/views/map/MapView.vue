<script setup lang="ts">
// 地图主页
import * as echarts from 'echarts/core';

import {
    TitleComponent,
    VisualMapComponent,
    GeoComponent,
} from 'echarts/components';

import type {
    TitleComponentOption,
    VisualMapComponentOption,
    GeoComponentOption,

} from 'echarts/components'

import { MapChart, EffectScatterChart, CustomChart } from 'echarts/charts';
import type { MapSeriesOption, EffectScatterSeriesOption, CustomSeriesOption } from 'echarts/charts';
import { CanvasRenderer } from 'echarts/renderers';
import { inject, onMounted } from 'vue';
import type { Axios } from 'axios';
import usaJson from '@/assets/world.geo.json'
import country from '@/assets/country.json'

const clickArea = defineEmits(['clickArea'])

echarts.use([
    TitleComponent,
    VisualMapComponent,
    GeoComponent,
    MapChart,
    EffectScatterChart,
    CustomChart,
    CanvasRenderer
]);

type EChartsOption = echarts.ComposeOption<
    | TitleComponentOption
    | VisualMapComponentOption
    | GeoComponentOption
    | MapSeriesOption
    | EffectScatterSeriesOption
    | CustomSeriesOption
>;

let mapChart: any

let option: EChartsOption

let countrySet = new Set<string>(country.flatMap(item => item.countryName))

let countryList = Array.from(countrySet).map(item => {
    return {name:item,value:1}
})

onMounted(() => {

    const chartDom = document.getElementById('map')!

    resize()

    mapChart = echarts.init(chartDom, 'dark');

    mapChart.showLoading();

    const axios = inject<Axios>("axios")

    mapChart.hideLoading();

    echarts.registerMap('tongliao-world', usaJson as any, {
        // 此处需要将回龙观、天通苑与通辽标出
    });
    option = {
        title: {
            show: true,
            text: '通辽宇宙地图',
            borderColor: "#FFF",
            // 殷红
            textStyle: {
                color: "#82111f"
            },
            subtextStyle: {
                color: "#82111f"
            },
            subtext: 'the map of tongliao universe',
            top: 64,
            right: 64
        },
        // 藏花红、金黄、姜红
        visualMap: [
            {
                type: 'piecewise',
                show: true,
                hoverLink: false,
                itemWidth: 32,
                id: 'color',
                seriesIndex: 0,
                pieces: [
                    { gte: 1, lte: 1, label: "奇葩小国", color: "#ec2d7a" },
                    // { gte: 2, lte: 2, label: "硬核狠人", color: "#4d1018" },
                    // { gte: 3, lte: 3, label: "神奇组织", color: "#45b787" },
                    { gte: 4, lte: 4, label: "新大陆", color: "#eeb8c3" },
                    { gte: 5, lte: 5, label: "计量单位", color: "#f26b1f" },
                ],
                inverse: true,
                orient: 'vertical',
                left: 64,
                top: 64,
                selectedMode: false,
                textStyle: {
                    color: "#FFF"
                }
            },
        ],
        geo: [
            {
                name: '奇葩小国',
                type: 'map',
                roam: true,
                zoom: 1.1,
                selectedMode: false,
                map: 'tongliao-world',
                label: {
                    color: "#FFF",
                },
                itemStyle: {
                    areaColor: "#eeb8c3",
                    borderWidth: 0
                },
                emphasis: {
                    label: {
                        color: "#FFF",
                        show: true
                    },
                    itemStyle: {
                        areaColor: "#1661ab",
                        shadowColor: 'rgba(0, 0, 0, 0.7)',
                        shadowBlur: 10
                    }
                }
            }
        ],
        series: [
            {
                name: '奇葩小国',
                type: 'map',
                geoIndex: 0,
                selectedMode: false,
                map: 'tongliao-world',
                data: countryList
            },
            {
                name: '人口单位',
                type: 'effectScatter',
                geoIndex: 0,
                selectedMode: false,
                coordinateSystem: 'geo',
                data: [
                    {
                        name: "天通苑",
                        value: [116.420862, 40.061552],
                        itemStyle: {
                            color: "#f26b1f"
                        }
                    },
                    {
                        name: "回龙观",
                        value: [116.324618, 40.064687],
                        itemStyle: {
                            color: "#f26b1f"
                        },
                    }
                ],
                
                symbolSize: 4,
                label: {
                    formatter: '{b}',
                    color:'#fff',
                    textBorderColor: '#000',
                    textBorderWidth: 2,
                    position: 'right',
                    show: true
                },
            },
            {
                name: "面积单位",
                type: 'custom',
                geoIndex: 0,
                coordinateSystem: 'geo',
                selectedMode: false,
                data: [['通辽']],
                renderItem: (params: any, api: any)=> {
                    let coords = [
                        [123.087539, 44.522239],
                        [123.399602, 44.139572],
                        [123.577924, 43.646975],
                        [123.355022, 43.528576],
                        [123.741386, 43.301896],
                        [123.488763, 43.02007],
                        [123.280721, 42.802395],
                        [122.626874, 42.824197],
                        [122.374251, 42.682347],
                        [121.973026, 42.660495],
                        [121.586662, 42.474443],
                        [121.111137, 42.243849],
                        [120.858514, 42.232847],
                        [120.427569, 43.052654],
                        [120.769353, 43.366749],
                        [120.48701, 43.388351],
                        [120.992255, 43.603948],
                        [120.813933, 43.7866],
                        [120.769353, 44.075551],
                        [120.368128, 44.363098],
                        [119.253616, 45.269626],
                        [119.283336, 45.447136],
                        [119.550819, 45.634481],
                        [119.996624, 45.457561],
                        [120.011484, 45.634481],
                        [120.293827, 45.572102],
                        [120.947675, 45.196371],
                        [121.958166, 44.320587],
                        [122.463412, 44.235473],
                        [123.087539, 44.522239]
                    ]
                    let points = []
                    for (let i = 0; i < coords.length; i++) {
                        points.push(api.coord(coords[i]))
                    }
                    
                    return {
                        type: 'polygon',
                        shape: {
                            points: points
                        },
                        style: {
                            fill: '#f26b1f'
                        },
                        emphasis: {
                            style: {
                                shadowColor: 'rgba(0, 0, 0, 0.7)',
                                shadowBlur: 10
                            }
                        },
                        focus:'self',
                        textContent: {
                            type:'text',
                            style: {
                                textStroke: '#000',
                                lineWidth:2,
                                text: api.value(0)
                            }
                        },
                        textConfig: {
                            insideFill:'#FFF',
                            position: 'inside',
                        },
                    }
                }
            }
        ]
    };

    mapChart.setOption(option);

    mapChart.on("click", (params: any) => {
        clickArea('clickArea', params)
    })

    window.onresize = () => {
        resize()
        mapChart.resize()
    };

    function resize() {
        chartDom.style.width = window.innerWidth + 'px'
        chartDom.style.height = window.innerHeight + 'px'
    }

})



function mapResize() {
    console.log('mapResize')
    mapChart.setOption(option, true)
}

defineExpose({
    mapResize,
})

</script>

<template>
    <div id="map"></div>
</template>

<style scoped></style>
