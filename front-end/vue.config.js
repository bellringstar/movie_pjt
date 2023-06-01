const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: [
    'vuetify'
  ],
  // errorHandler: function(err, vm, info) {
  //   console.log(err)
  //   console.log(vm)
  //   console.log(info)
  //   return true;
  // }
})
