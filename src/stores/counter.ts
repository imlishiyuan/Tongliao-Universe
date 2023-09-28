import { ref, computed } from 'vue'
import { defineStore } from 'pinia'


// 也许我应该定义一个存储小国、狠人、组织的store，这样可以在本地获取数据
export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  const doubleCount = computed(() => count.value * 2)
  function increment() {
    count.value++
  }

  return { count, doubleCount, increment }
})
