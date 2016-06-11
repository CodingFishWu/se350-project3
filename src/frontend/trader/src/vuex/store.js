import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {
  login: false,
  brokerList: [{name:'broker 1',url:'http://104.199.165.224:8000'},
  {name:'broker 2',url:'http://104.199.161.112:8000'}],
  brokerSelected: 0
}

const mutations = {
  LOGIN (state) {
    state.login = true
  },
  LOGOUT (state) {
    state.login = false
  },
  CHANGEBROKER (state,broker) {
    state.brokerSelected = broker
  }
}

export default new Vuex.Store({
  state,
  mutations
})
