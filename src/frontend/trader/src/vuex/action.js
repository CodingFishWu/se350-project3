export const checkLogin = function ({dispatch, state},user,pass) {
  dispatch('LOGIN')
  return {
    success: true
  }
}

export const logout = function ({dispatch, state}) {
  dispatch('LOGOUT')
  this.$router.go('/')
}

export const changeBroker = function ({dispatch, state},broker) {
  dispatch('CHANGEBROKER',broker)
}
