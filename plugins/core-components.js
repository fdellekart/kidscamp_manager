import Vue from 'vue'
import { BootstrapVue } from 'bootstrap-vue'

import AppButton from '@/components/UI/AppButton'
import AppControlInput from '@/components/UI/AppControlInput'

import VueApexCharts from 'vue-apexcharts'

Vue.use(BootstrapVue)
Vue.component('AppButton', AppButton)
Vue.component('AppControlInput', AppControlInput)

Vue.use(VueApexCharts)
Vue.component('Apexchart', VueApexCharts)
