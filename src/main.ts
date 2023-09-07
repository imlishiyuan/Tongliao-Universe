import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import Antd from 'ant-design-vue';
import axios from 'axios'
import VueAxios from 'vue-axios'


import App from './App.vue'
import router from './router'


const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(VueAxios, axios)
app.use(Antd)

app.provide('axios', app.config.globalProperties.axios)
app.provide('$http', app.config.globalProperties.axios)

app.mount('#app')