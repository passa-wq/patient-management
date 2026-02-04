import { createRouter, createWebHistory } from 'vue-router'
import PatientList from './components/PatientList.vue'
import AddPatient from './components/AddPatient.vue'

const routes = [
  { path: '/', component: PatientList },
  { path: '/add', component: AddPatient }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
