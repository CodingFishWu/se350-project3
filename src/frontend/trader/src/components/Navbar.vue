<template>
    <div class="ui compact left fixed vertical labeled icon teal inverted menu">
        <a class="item" v-link="{path: '/'}"><i class="home icon"></i> 首页 </a>
        <a class="item" v-link="{path: '/order'}"><i class="browser icon"></i> 订单 </a>
        <a class="item" v-show="!login" v-link="{path: '/login'}"><i class="user icon"></i> 登录 </a>
        <a class="item" v-show="login" @click="logout"><i class="user icon"></i> 登出 </a>
    </div>
</template>

<script>
import {getLogin} from '../vuex/getters'
import {logout} from '../vuex/action'

export default{
  vuex: {
    getters: {
      login: getLogin
    },
    actions: {
      logout
    }
  },
  data () {
    return {
      uid: 0,
      active: 0
    }
  }
}
</script>
