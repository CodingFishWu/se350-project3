<template>
  <div class="ui dimmer page" v-bind:class="{active:showModal}">
    <div class="ui active modal" transition="refresh" v-show="showModal">
      <i class="close icon" @click="close"></i>
      <div class="header">Header</div>
      <div class="content">
        <div class="ui form">
          <div class="disabled field">
            <label>Product Code:</label>
            <input type="text" placeholder="code product" v-model="code">
          </div>
          <div class="inline fields">
            <label>Sell or Buy</label>
            <div class="field">
              <div class="ui radio checkbox">
                <input type="radio" value="sell" v-model="s_b">
                <label>Sell</label>
              </div>
              <div class="ui radio checkbox">
                <input type="radio" value="buy" v-model="s_b">
                <label>Buy</label>
              </div>
            </div>
          </div>
          <div class="inline fields">
            <label for="fruit">Order Type:</label>
            <div class="field">
              <div class="ui radio checkbox">
                <input type="radio" value="market" v-model="type">
                <label>Market</label>
              </div>
            </div>
            <div class="field">
              <div class="ui radio checkbox">
                <input type="radio" value="limit" v-model="type">
                <label>Limit</label>
              </div>
            </div>
            <div class="field">
              <div class="ui radio checkbox">
                <input type="radio" value="stop" v-model="type">
                <label>Stop</label>
              </div>
            </div>
          </div>
          <div class="field">
            <label>Price</label>
            <input type="text" placeholder="price" v-model="price">
          </div>
          <div class="field">
            <label>Count</label>
            <input type="text" placeholder="count" v-model="count">
          </div>
          <div class="field">
            <div class="ui checkbox">
              <input type="checkbox" v-model="checkConfirm">
              <label>Confirm my action</label>
            </div>
          </div>
          <button class="ui button" @click="submit">Submit</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      showModal: false,
      code: this.$route.params.code,
      s_b: "sell",
      type: "market",
      price: 0,
      count: 0,
      checkConfirm: false
    }
  },
  transitions: {
    'refresh': {
      css: false,
      enter (el,done) {
        el.style.marginTop = -el.clientHeight/2 + 'px'
        done()
      },
      leave (el,done) {
        el.style.marginTop = -el.clientHeight/2 + 'px'
        done()
      }
    }
  },
  events: {
    showModal () {
      this.checkConfirm = false;
      this.showModal = true;
    }
  },
  methods: {
    close () {
      this.showModal = false;
    },
    submit () {
      if (this.checkConfirm) {
        this.$http.post('http://192.241.193.159/index.php/api/add_order',{
          s_b: this.s_b,
          type: this.type,
          product_code: this.code,
          amount: this.count,
          price: this.price
        }).then((response) => {
          this.showModal = false;
        },(response) => {console.log(response)})
      }
    }
  }
}
</script>
