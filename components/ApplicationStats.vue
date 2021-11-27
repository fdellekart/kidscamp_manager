<template>
  <div class="container">
    <div class="stats-header">
      <span>Aktuell {{ numberApplications }} Anmeldungen</span>
      <app-button id="download-button" @click="$emit('download-excel')"
        >Excel Herunterladen</app-button
      >
    </div>
    <div class="chart-container">
      <apex-chart
        :series="[{ name: 'Anmeldungen', data: Object.values(ageHistogram) }]"
        :options="{
          chart: { type: 'bar', toolbar: { show: false }, height: '100%' },
          xaxis: { categories: Object.keys(ageHistogram) },
          yaxis: { show: false },
          title: { text: 'Aufteilung über Alter' },
          colors: ['#fdcc2d'],
        }"
      ></apex-chart>
    </div>
  </div>
</template>

<script>
import AppButton from './UI/AppButton.vue'
export default {
  components: { AppButton },
  props: {
    numberApplications: {
      type: Number,
      required: true,
    },
  },
  computed: {
    ageHistogram() {
      const applications = this.$store.getters.applications
      const hist = {}
      Object.values(applications).forEach((application) => {
        if (!hist[application.child.age]) {
          hist[application.child.age] = 0
        }
        hist[application.child.age] += 1
      })
      return hist
    },
  },
}
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 300px;
}
.chart-container {
  height: 100%;
}
.stats-header {
  display: flex;
  flex-direction: row;
}
span {
  font-size: 30px;
  font-weight: bold;
}
#download-button {
  margin-left: 30px;
}
</style>
