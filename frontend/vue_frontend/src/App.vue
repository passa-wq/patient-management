<template>
  <div>
    <h1>Patient Management</h1>
    <nav>
      <router-link to="/">Patient List</router-link> |
      <router-link to="/add">Add Patient</router-link>
    </nav>
    <router-view :onAdded="fetchPatients"></router-view>
  </div>
</template>

<script>
import PatientList from './components/PatientList.vue'
import AddPatient from './components/AddPatient.vue'
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  { path: '/', component: PatientList, name: 'list' },
  { path: '/add', component: AddPatient, name: 'add' },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default {
  name: 'App',
  router,
  methods: {
    fetchPatients() {
      const listComp = this.$router.currentRoute.value.matched[0].instances.default
      if(listComp && listComp.fetchPatients) listComp.fetchPatients()
    }
  }
}
</script>
