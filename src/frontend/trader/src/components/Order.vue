<template>
  <div class="ui large secondary pointing menu">
    <a class="active item">订单列表</a>
    <div class="right menu">
      <div class="item">
        <div class="ui transparent icon input">
          <input type="text" v-model='code' placeholder="Search for code...">
          <i class="search icon"></i>
        </div>
      </div>
    </div>
  </div>
  <div class='order-card' v-for="row in orderList">
    <div class="ui top attached segment">
      <table class='ui very basic signle line table'>
          <tr>
            <th>{{row.order.product_code}}</th>
            <th>type: {{row.order.type}}</th>
            <th>status: {{row.order.status}}</th>
            <th>remain: {{row.order.remain}}</th>
            <th>time: {{row.order.created_time}}</th>
            <th><button class="ui tiny red basic button" v-show="row.order.status !== 'finished' && row.order.status !== 'canceled'" @click="cancelOrder($index)"><i class="icon remove"></i> cancel </button></th>
          </tr>
      </table>
    </div>
    <div class="ui bottom attached segment">
      <table class="ui very basic single line table">
        <thead>
          <tr>
            <th>id</th>
            <th>broker</th>
            <th>status</th>
            <th>amount</th>
            <th>price</th>
            <th>remain</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in row.item">
            <td>{{item.id}}</td>
            <td>{{item.broker}}</td>
            <td>{{item.status}}</td>
            <td>{{item.amount}}</td>
            <td>{{item.price}}</td>
            <td>{{item.remain}}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>

export default {
  data () {
    return {
      orderList: []
    }
  },
  methods: {
    getOrder () {
      this.$http.get('http://192.241.193.159/index.php/api/get_order').then((response) => {
        this.$set('orderList',response.data)
      },(response) => {console.log(response)})
    },
    cancelOrder (index) {
      this.$http.post('http://192.241.193.159/index.php/api/cancel_order',{
        oid: this.orderList[index].order.id
      }).then((response) => {
        this.getOrder()
      },(response) => {console.log(response)})
    }
  },
  ready () {
    this.getOrder()
  }
}
</script>

<style scoped>
  .ui.menu {
    margin-top: 1em;
    margin-bottom: 2em;
  }
  .order-card {
    margin-top: 1em;
    margin-bottom: 1em;
  }
</style>
