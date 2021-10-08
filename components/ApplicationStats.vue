<template>
  <div class="container">
    <span>Aktuell {{ numberApplications }} Anmeldungen</span>
    <div class="chart-container">
      <Apexchart
        :series="[{ name: 'Anmeldungen', data: Object.values(ageHistogram) }]"
        :options="{
          chart: { type: 'bar', toolbar: { show: false }, height: '100%' },
          xaxis: { categories: Object.keys(ageHistogram) },
          yaxis: { show: false },
        }"
      ></Apexchart>
    </div>
  </div>
</template>

<script>
export default {
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
  margin: 15px;
  width: 100%;
  height: 150px;
}
.chart-container {
  height: 100%;
}
span {
  font-size: 30px;
  font-weight: bold;
}
</style>
