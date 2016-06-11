<template>
    <div id="app">
        <navbar></navbar>
        <main style="margin-left: 85px;">
          <div class="ui container">
            <router-view></router-view>
          </div>
        </main>
    </div>
</template>

<script>
import Navbar from './components/Navbar'

export default {
  components: {
    Navbar
  }
}
</script>

<style rel="stylesheet/scss" scoped>
</style>
