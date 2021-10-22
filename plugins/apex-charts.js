import Vue from 'vue'

import VueApexCharts from 'vue-apexcharts'

export default () => {
  Vue.component('ApexChart', VueApexCharts)
  Vue.use(VueApexCharts)
}
