import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

// Bootstrap
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

// Load progressbar
import VueProgressBar from 'vue-progressbar'

const options = {
    color: 'rgb(79,105,194)',
    failedColor: 'red',
    height: '5px'
}

Vue.use(VueProgressBar, options)

Vue.use(BootstrapVue)

Vue.config.productionTip = false

new Vue({
    router,
    store,
    render: function (h) {
        return h(App)
    }
}).$mount('#app')
