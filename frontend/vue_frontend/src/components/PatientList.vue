<template>
  <div>
    <h2>All Patients</h2>
    <div v-if="loading">Loading...</div>
    <div v-else>
      <div v-if="patients.length === 0">
        API läuft! Keine Patienten vorhanden.
      </div>
      <ul v-else>
        <li v-for="patient in patients" :key="patient.id">
          {{ patient.vorname }} {{ patient.nachname }} - {{ patient.email }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      patients: [],
      loading: true
    }
  },
  methods: {
    fetchPatients() {
      this.loading = true
      axios.get('http://127.0.0.1:8000/patients')
        .then(res => this.patients = res.data)
        .catch(err => console.error(err))
        .finally(() => this.loading = false)
    }
  },
  mounted() {
    this.fetchPatients()
  }
}
</script>
