<template>
  <div class="ui large secondary pointing menu">
    <a class="active item">商品列表</a>
    <div class="right menu">
      <div class="item">
        <div class="ui transparent icon input">
          <input type="text" v-model='code' placeholder="Search for code...">
          <i class="search icon"></i>
        </div>
      </div>
    </div>
  </div>
  <select class="ui dropdown" v-model="broker">
    <option v-for="broker in brokerList" value="{{$index}}">{{broker.name}}</option>
  </select>
  <br>
  <br>
  <div class="ui four column grid">
    <div class="column" v-for="item in list | filterBy code in 'code' 'name'">
      <div class="ui fluid card">
        <div class="content">
          <div class="header">{{item.code}} {{item.name}}</div>
          <div class="description">
            <p>种类: {{item.type}}</p>
            <p>单位: {{item.unit}}</p>
          </div>
        </div>
        <a class="ui bottom attached button" v-link="{path: '/item/'+item.code}"><i class="search icon"></i> 查看行情 </a>
      </div>
    </div>
  </div>
</template>

<script>
import {getBrokerList,getBrokerSelected} from '../vuex/getters'
import {changeBroker} from '../vuex/action'
export default{
  vuex: {
    getters: {
      brokerList: getBrokerList,
      brokerSelected: getBrokerSelected
    },
    actions: {
      changeBroker
    }
  },
  data () {
    return {
      code: '',
      list: []
    }
  },
  computed: {
    broker: {
      get () {
        return this.brokerSelected
      },
      set (val) {
        this.changeBroker(val)
      }
    }
  },
  ready () {
    this.broker = this.brokerSelected
    this.$http.get('http://192.241.193.159/index.php/api/item').then((response) => {
      this.$set('list',response.data)
    },(response) => {console.log(response)})
  }
}
</script>

<style scoped>
  .ui.menu {
    margin-top: 1em;
    margin-bottom: 2em;
  }
</style>
