<template>
  <div class="ui large breadcrumb">
    <a class="section" v-link="{path: '/'}">商品列表</a>
    <i class="right angle icon divider"></i>
    <div class="active section">{{$route.params.code}}</div>
  </div>
  <select class="ui dropdown" v-model="broker">
    <option v-for="broker in brokerList" value="{{$index}}">{{broker.name}}</option>
  </select>
  <button class="ui green basic button" @click="showModal"><i class="icon add"></i> 新建订单 </button>
  <button class="ui green basic button" @click="testPost"><i class="icon add"></i> POST </button>
  <div class="ui grid">
    <h3 class="ui header">
      <i class="tasks icon"></i>
      <div class="content">Market Depth</div>
    </h3>
    <div class="row">
      <div class="eight wide column">
        <table class="ui orange single line table">
          <thead>
            <tr>
              <th>#</th>
              <th>Vol</th>
              <th>Buy Price</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="row in list | filterBy 'buy' in 's_b' | orderBy 'price' -1">
              <td>{{$index}}</td>
              <td>{{row.remain}}</td>
              <td>{{row.price}}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="eight wide column">
        <table class="ui blue single line table">
          <thead>
            <tr>
              <th>#</th>
              <th>Vol</th>
              <th>Sell Price</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="row in list | filterBy 'sell' in 's_b' | orderBy 'price'">
              <td>{{$index}}</td>
              <td>{{row.remain}}</td>
              <td>{{row.price}}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <h3 class="ui header">
      <i class="browser icon"></i>
      <div class="content">Transaction</div>
    </h3>
    <div class="row">
      <div class="column">
        <table class="ui teal single line table">
          <thead>
            <tr>
              <th>Type</th>
              <th>Price</th>
              <th>Amount</th>
              <th>Time</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="row in transaction">
              <td>{{row.s_b}}</td>
              <td>{{row.price}}</td>
              <td>{{row.amount}}</td>
              <td>{{row.create_time}}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
  <order-modal></order-modal>
</template>
<script>
import {getBrokerList,getBrokerSelected} from '../vuex/getters'
import {changeBroker} from '../vuex/action'
import OrderModal from './OrderModal'
export default {
  components: {
    OrderModal
  },
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
      list: [],
      transaction: []
    }
  },
  computed: {
    broker: {
      get () {
        return this.brokerSelected
      },
      set (val) {
        this.changeBroker(val)
        this.getMarketDepth()
      }
    }
  },
  methods: {
    testGet () {
      this.$http.get('http://192.241.193.159/index.php/api/test',{test:"test get"}).then((response) => {
        console.log(response)
      },(response) => {console.log(response)})
    },
    testPost () {
      this.$http.post('http://192.241.193.159/index.php/api/add_transaction',{
        type: 'trade',
        order_id: 2,
        number: 48,
        price: 100
      }).then((response) => {
        console.log(response)
      },(response) => {console.log(response)})
    },
    showModal () {
      this.$broadcast('showModal')
    },
    getMarketDepth () {
      this.$http.get(this.brokerList[this.brokerSelected].url+'/marketDepth/product/'+this.$route.params.code).then((response) => {
        this.$set('list',response.data)
      },(response) => {console.log(response)})
    },
    getTransaction () {
      this.$http.get("http://192.241.193.159/index.php/api/get_transaction/"+this.$route.params.code).then((response) => {
        this.$set('transaction',response.data)
      },(response) => {console.log(response)})
    }
  },
  ready () {
    this.broker = this.brokerSelected
    this.getMarketDepth()
    this.getTransaction()
  }
}
</script>

<style scoped>
 .ui.breadcrumb {
   margin-top: 2em;
   margin-bottom: 2em;
   margin-right: 2em;
 }
 .ui.dropdown {
   margin-right: 1em;
 }
</style>
