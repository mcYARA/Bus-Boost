import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'home',
            component: function () {
                return import('./views/Home.vue')
            }
        },
        {
            path: '/login',
            name: 'login',
            component: function () {
                return import('./views/Login.vue')
            }
        },
    ]
})
