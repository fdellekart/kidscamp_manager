<template>
  <div>
    <header style="text-align: center">
      <h1>Bestrafungsra<b>T</b></h1>
    </header>

    <h5 style="display: inline">Angeklagter:</h5>
    <input v-show="show" v-model="angeklagter" type="text" />
    <p id="angeklagter" style="display: inline">{{ angeklagter }}</p>
    <br />
    <h5 style="display: inline">Ankläger:</h5>
    <input v-show="show" v-model="anklaeger" type="text" />
    <p id="anklaeger" style="display: inline">{{ anklaeger }}</p>
    <br />
    <button v-show="show" id="anklagen" @click="anklagen">anklagen</button
    ><br />

    <br />

    <h4 style="display: inline">Mitglied 1:</h4>
    <button
      v-show="showMitgliedBtn1 & !showMehrKandidaten"
      @click="chooseMitglied('mitglied1'), (showMitgliedBtn1 = false)"
    >
      ziehen
    </button>
    <p id="mitglied1" style="display: inline"></p>
    <br />
    <h4 style="display: inline">Mitglied 2:</h4>
    <button
      v-show="showMitgliedBtn2 & !showMehrKandidaten"
      @click="chooseMitglied('mitglied2'), (showMitgliedBtn2 = false)"
    >
      ziehen
    </button>
    <p id="mitglied2" style="display: inline"></p>
    <br />
    <h4 style="display: inline">Mitglied 3:</h4>
    <button
      v-show="showMitgliedBtn3 & !showMehrKandidaten"
      @click="chooseMitglied('mitglied3'), (showMitgliedBtn3 = false)"
    >
      ziehen
    </button>
    <p id="mitglied3" style="display: inline"></p>
    <br />
    <br />
    <h4><u>Kandidaten</u></h4>
    <p v-show="showMehrKandidaten">{{ mehrKandidaten }}</p>
    <p v-for="name in namen" :key="name">{{ name }}</p>
    <p>{{ kandidat }}</p>

    <input id="kandidat" v-model="kandidat" type="text" />
    <button id="save" @click="kandidatHinzufuegen">hinzufügen</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      angeklagter: '',
      anklaeger: '',
      kandidat: '',
      namen: ['flotschi', 'julia'],
      kandidatenAlreadyUsed: [],
      show: true,
      showMitgliedBtn1: true,
      showMitgliedBtn2: true,
      showMitgliedBtn3: true,
      mehrKandidaten: 'Bitte mehr Kandidaten hinzufügen!',
    }
  },
  computed: {
    showMehrKandidaten() {
      if (this.namen.length < 5) {
        return true
      } else {
        return false
      }
    },
  },
  methods: {
    anklagen() {
      console.log('angeklagter', this.angeklagter)
      this.kandidatenAlreadyUsed.push(this.angeklagter, this.anklaeger)
      this.show = false
    },
    kandidatHinzufuegen() {
      this.namen.push(this.kandidat)
      this.kandidat = ''
    },
    randomItem(namen) {
      let mitglied = namen[Math.floor(Math.random() * namen.length)]
      while (this.kandidatenAlreadyUsed.includes(mitglied)) {
        mitglied = namen[Math.floor(Math.random() * namen.length)]
      }
      return mitglied
    },
    chooseMitglied(mitgliedNr) {
      const mitglied = this.randomItem(this.namen)
      this.kandidatenAlreadyUsed.push(mitglied)
      document.getElementById(mitgliedNr).innerHTML = mitglied
    },
  },
}
</script>

<style scoped></style>
