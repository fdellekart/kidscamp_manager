<template>
  <div>
    <header style="text-align: center">
      <h1>Bestrafungsra<b>T</b></h1>
    </header>

    <h4 style="display: inline">Angeklagter:</h4>
    <input id="angeklagter" v-model="angeklagter" type="text" />
    <p id="angeklagter" style="display: inline">{{ angeklagter }}</p>
    <br />
    <h4 style="display: inline">Ankläger:</h4>
    <input id="ankläger" type="text" />
    <p id="ankläger" style="display: inline"></p>
    <br />
    <button id="anklagen" @click="anklagen">anklagen</button><br />

    <br />

    <h4 style="display: inline">Mitglied 1:</h4>
    <button id="mitglied1Ziehen">ziehen</button>
    <p id="mitglied1" style="display: inline"></p>
    <br />
    <h4 style="display: inline">Mitglied 2:</h4>
    <button id="mitglied2Ziehen">ziehen</button>
    <p id="mitglied2" style="display: inline"></p>
    <br />
    <h4 style="display: inline">Mitglied 3:</h4>
    <button id="mitglied3Ziehen">ziehen</button>
    <p id="mitglied3" style="display: inline"></p>
    <br />
    <br />
    <h4><u>Kandidaten</u></h4>
    <p v-for="name in namen" :key="name">{{ name }}</p>

    <input id="kandidat" v-model="kandidat" type="text" />
    <button id="save" @click="kandidatHinzufuegen">hinzufügen</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      angeklagter: '',
      namen: ['flotschi', 'julia'],
    }
  },
  methods: {
    anklagen() {
      console.log('angeklagter', this.angeklagter)
    },
    kandidatHinzufuegen() {
      this.namen.push(this.kandidat)
    },
  },
}
</script>

<style scoped></style>
