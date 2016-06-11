import Vue from 'vue'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'
import store from './vuex/store'
import 'semantic-ui/dist/semantic.min.css'
import App from './App'
import Item from './components/Item'
import Itemlist from './components/ItemList'
import Login from './components/Login'
import Order from './components/Order'

Vue.use(VueRouter)
Vue.use(VueResource)
Vue.http.options.emulateJSON = true;

var router = new VueRouter({
  history: true
})

router.map({
  '/': {
    component: Itemlist
  },
  '/item/:code': {
    component: Item
  },
  '/login': {
    component: Login
  },
  '/login/:target': {
    component: Login
  },
  '/order': {
    component: Order,
    auth: true
  }
})

router.beforeEach(function ({to,next}) {
  if (to.auth && !store.state.login) {
    router.go('/login'+to.path)
  } else {
    next()
  }
})

router.start(Vue.extend({
  components: { App },
  store
}), 'body')
