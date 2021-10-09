import Vue from 'vue'
import { BootstrapVue } from 'bootstrap-vue'

import VueApexCharts from 'vue-apexcharts'
import AppButton from '@/components/UI/AppButton'
import AppControlInput from '@/components/UI/AppControlInput'

export default () => {
  Vue.component('AppButton', AppButton)
  Vue.component('AppControlInput', AppControlInput)
  Vue.component('Apexchart', VueApexCharts)

  Vue.use(VueApexCharts)
  Vue.use(BootstrapVue)
}
