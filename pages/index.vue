<template>
  <div class="container">
    <h1 id="main-heading" class="heading">
      Anmeldung KidsCamp {{ currentYear }}
    </h1>
    <div class="separator"></div>
    <div v-if="!applicationFinished" class="parent-container">
      <h2>Erziehungsberechtigter</h2>
      <InputForm
        v-if="!isParentSaved"
        :person="parentData"
        @save="onSaveParent($event)"
      />
      <AppPersonInfo
        v-else
        :first-name="parentData.firstName"
        :last-name="parentData.lastName"
        :mail="parentData.mail"
        :show-delete-icon="false"
        @toggle-edit="isParentSaved = false"
      />
    </div>
    <div v-if="!applicationFinished" class="separator"></div>
    <div v-if="!applicationFinished" class="children-container">
      <h2>Kinder</h2>
      <child-input-and-display
        v-for="idx in Object.keys(children)"
        :key="idx"
        :idx="idx"
        style="width: 100%"
        @delete="onDeleteChild($event)"
        @save="onSaveChild($event)"
      />
      <AppButton class="add-button" @click="onAddChild"
        >Kind Hinzufügen</AppButton
      >
    </div>
    <p v-if="showParentWarning" class="warning">
      Bitte Erziehungsberechtigten angeben und speichern.
    </p>
    <p v-if="showChildrenEmptyWarning" class="warning">
      Bitte Kinder angeben und speichern.
    </p>
    <p v-if="!applicationFinished" class="agreetext" :style="agreeTextStyle">
      Mit dem Absenden der Anmeldung erkläre ich mich einverstanden, dass die
      angegebenen Daten vom "Verein zur Durchführung von Kinderferienlagern -
      KIDSCAMP" gespeichert werden und dass ich per Mail Informationen zum Lager
      erhalte.
    </p>
    <p v-if="!applicationFinished" class="datainfo">
      Bei Unklarheiten bezüglich Speicherung und Löschung der angegebenen Daten
      kontaktiere uns bitte über unsere Website oder per Mail. Die Informationen
      dienen der Planung und Erreichbarkeit und werden keinesfalls an Dritte
      weitergegeben.
    </p>
    <p v-if="showCaptchaWarning & !applicationFinished" class="warning">
      Bitte verifiziere, dass du kein Roboter bist.
    </p>
    <recaptcha v-if="!applicationFinished" />
    <div v-if="!applicationFinished" class="submit-button-container">
      <AppButton @click="onSend">Anmeldung absenden</AppButton>
    </div>
    <h2 v-if="applicationFinished" class="thank-text">
      Vielen Dank für deine Anmeldung!
    </h2>
    <p v-if="applicationFinished">
      Ein E-Mail wurde als Bestätigung an <b>{{ parentData.mail }}</b> versandt.
      <br />
      <br />
      Solltest du keine Mail erhalten haben, setze dich bitte über
      <a href="https://www.kidscamp.at/contact"> unsere Website </a> mit uns in
      Kontakt.
      <br />
      <br />
      Für den Fall, dass das Mail nicht in deinem Posteingang landet,
      <b>kontrolliere bitte auch den Spam Ordner</b>.
      <br />
      <br />
      Um die Zeit bis zum Camp zu überbrücken und um dann auf jeden Fall Top
      vorbereitet zu sein, könnt ihr euch in der Zwischenzeit die
      <a href="https://www.kidscamp.at/camp-tipps">Packliste und Tipps</a>
      ansehen.
      <br />
      <br />
      Liebe Grüße und bis dann,<br />
      <br />
      <i class="fas fa-campground"></i>
      <b>Das gesamte KidsCamp Team</b>
      <i class="fas fa-campground"></i>
    </p>
  </div>
</template>

<script>
import Vue from 'vue'
import InputForm from '@/components/input/InputForm'
import AppPersonInfo from '@/components/UI/AppPersonInfo'
import ChildInputAndDisplay from '@/components/input/ChildInputAndDisplay'

export default {
  components: {
    InputForm,
    AppPersonInfo,
    ChildInputAndDisplay,
  },
  layout: 'application',
  data() {
    return {
      parentData: { firstName: null, lastName: null, mail: null },
      isParentSaved: false,
      children: { child_0: { firstName: null, lastName: null, age: null } },
      isAddingChild: false,
      isEditingChild: false,
      childToEditIndex: null,
      childToEdit: undefined,
      applicationFinished: false,
      showParentWarning: false,
      showChildrenEmptyWarning: false,
      showCaptchaWarning: false,
    }
  },
  head() {
    return {
      title: 'Anmeldung KidsCamp 2022',
    }
  },
  computed: {
    currentYear() {
      return new Date().getFullYear()
    },
    showChildInputForm() {
      return (
        this.children.length === 0 || this.isAddingChild || this.isEditingChild
      )
    },
    agreeTextStyle() {
      if (this.highlightAgreement) {
        return { color: 'red', 'font-weight': 'bold' }
      } else {
        return {}
      }
    },
  },
  methods: {
    onSaveParent(parentData) {
      this.parentData = parentData
      this.isParentSaved = true
    },
    onSaveChild({ idx, child }) {
      Vue.set(this.children, idx, child)
    },
    getChildIndex(childData) {
      return this.children.findIndex(
        (e) =>
          e.firstName + e.lastName === childData.firstName + childData.lastName
      )
    },
    onEditChild(childData) {
      this.isEditingChild = true
      this.childToEditIndex = this.getChildIndex(childData)
      this.childToEdit = childData
    },
    onCancelChild() {
      this.isEditingChild = false
      this.isAddingChild = false
      this.childToEditIndex = null
      this.childToEdit = undefined
    },
    onDeleteChild(childIdx) {
      Vue.delete(this.children, childIdx)
    },
    async onSend() {
      const children = Object.values(this.children).filter(
        (x) => (x.firstName !== null) & (x.lastName !== null) & (x.age !== null)
      )

      if (!this.verifyInputs(children)) {
        return
      }

      const token = await this.getRecaptchaToken()

      if (!token) {
        this.showCaptchaWarning = true
        return
      }

      children.forEach((child) => {
        this.$axios
          .post('api/application/add', {
            child,
            parent: this.parentData,
            token,
          })
          .catch(this.handleApplicationError)
      })

      this.$axios
        .post('api/application/confirm', {
          mail: this.parentData.mail,
          firstName: this.parentData.firstName,
          children,
          token,
        })
        .then(() => {
          this.applicationFinished = true
        })
        .catch(this.handleApplicationError)

      await this.$recaptcha.reset()
    },
    async getRecaptchaToken() {
      try {
        const token = await this.$recaptcha.getResponse()
        return token
      } catch (error) {
        return false
      }
    },
    verifyInputs(children) {
      if (!this.isParentSaved) {
        this.showParentWarning = true
        return false
      }
      this.showParentWarning = false

      if (children.length === 0) {
        this.showChildrenEmptyWarning = true
        return false
      }
      this.showChildrenEmptyWarning = false

      return true
    },
    handleApplicationError(e) {
      console.log('Error:', e)
    },
    onAddChild() {
      let newKey
      if (Object.keys(this.children).length === 0) {
        newKey = 'child_0'
      } else {
        const indexes = Object.keys(this.children).map((x) => +x.split('_')[1])
        const maxIdx = indexes.reduce((x, y) => (x > y ? x : y))
        const newIdx = maxIdx + 1
        newKey = 'child_' + newIdx
      }
      Vue.set(this.children, newKey, {
        firstName: null,
        lastName: null,
        age: null,
      })
    },
  },
}
</script>

<style scoped>
.parent-container {
  margin-top: 5%;
}
.heading {
  margin-top: 5%;
}
.children-container {
  margin-top: 5%;
}
.separator {
  height: 2px;
  background-color: darkgray;
  margin-top: 5%;
}
.add-button {
  margin-top: 3%;
}
.container {
  margin-bottom: 5%;
}
.submit-button-container {
  margin-top: 5%;
}
.warning {
  margin-top: 10px;
  color: red;
  font-weight: bold;
}
#main-heading {
  text-align: center;
}
.thank-text {
  margin-top: 25px;
  margin-bottom: 25px;
  text-align: center;
}
p {
  text-align: center;
}
.agreecheckboxwithtext {
  display: flex;
  flex-direction: row;
  margin-top: 30px;
}
.agreecheckbox {
  margin: 20px;
}
.agreetext {
  margin-top: 15px;
  text-align: left;
}
.datainfo {
  text-align: left;
}
</style>
