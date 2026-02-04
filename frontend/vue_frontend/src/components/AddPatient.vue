<template>
  <div>
    <h2>Add Patient</h2>
    <form @submit.prevent="addPatient">
      <input v-model="patient.vorname" placeholder="Vorname" required />
      <input v-model="patient.nachname" placeholder="Nachname" required />
      <input v-model="patient.email" placeholder="Email" required />
      <input v-model="patient.telefon" placeholder="Telefon" />
      <input v-model="patient.geburtsdatum" placeholder="YYYY-MM-DD" />
      <textarea v-model="patient.krankengeschichte" placeholder="Krankengeschichte"></textarea>
      <button type="submit">Add</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  props: ['onAdded'],
  data() {
    return {
      patient: {
        vorname: '',
        nachname: '',
        email: '',
        telefon: '',
        geburtsdatum: '',
        krankengeschichte: ''
      }
    }
  },
  methods: {
    addPatient() {
      axios.post('http://127.0.0.1:8000/patients', this.patient)
        .then(res => {
          alert('Patient added!')
          this.patient = { vorname:'', nachname:'', email:'', telefon:'', geburtsdatum:'', krankengeschichte:'' }
          if(this.onAdded) this.onAdded()
        })
        .catch(err => alert(err.response?.data?.detail || 'Fehler'))
    }
  }
}
</script>
