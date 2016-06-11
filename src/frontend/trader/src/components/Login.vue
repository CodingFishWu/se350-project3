<template>
  <div class="ui middle aligned center aligned grid sign-in">
      <div class="column sign-card">
          <h2 class="ui teal header login-header">
              请先登录
          </h2>
          <form id="form" class="ui large form">
              <div class="ui stacked segment">
                  <div class="field">
                      <div class="ui left icon input">
                          <i class="user icon"></i>
                          <input type="text" placeholder="用户名" v-model="user">
                      </div>
                  </div>
                  <div class="field">
                      <div class="ui left icon input">
                          <i class="lock icon"></i>
                          <input type="password" placeholder="密码" v-model="pass">
                      </div>
                  </div>
                  <div class="ui fluid large teal button" @click="submit">登录</div>
              </div>
              <div class="ui error message" v-show="err">{{err}}</div>
          </form>
      </div>
  </div>
</template>

<script>
import {getLogin} from '../vuex/getters'
import {checkLogin} from '../vuex/action'
export default {
  vuex: {
    getters: {
      getLogin
    },
    actions: {
      login: checkLogin
    }
  },
  data () {
    return {
      user: '',
      pass: '',
      err: ''
    }
  },
  methods: {
    submit () {
      console.log(this.$route.params)
      let result = this.login(this.user,this.pass)
      this.err = ''
      if (result.success) {
        if (this.$route.params.target) {
          this.$router.go('/'+this.$route.params.target)
        } else {
          this.$router.go('/')
        }
      } else {
        this.err = result.error
      }
    }
  }
}
</script>

<style scoped>
  div.sign-in {
      height: 100%;
      padding: 0 1rem;
  }
  .sign-card {
      margin: 0 1rem;
      max-width: 400px;
  }
  .ui.header.login-header {
      margin-top: 5em;
  }
</style>
