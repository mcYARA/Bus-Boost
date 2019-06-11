import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.baseURL = '/api/'

const authToken = localStorage.getItem('authToken')
if (authToken) {
    axios.defaults.headers['Authorization'] = "Token " + authToken
}

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        loggedIn: false,
        user: '',
    },
    getters: {
        getAuth(state) {
            return state.loggedIn
        },
        getUserInfo(state) {
            return state.user
        },
    },
    mutations: {
        setLoggined(state) {
            state.loggedIn = true
        },
        setToken(state, token) {
            localStorage.setItem('authToken', token)
            state.loggedIn = true
            axios.defaults.headers['Authorization'] = "Token " + localStorage.getItem('authToken')
            router.push('/categories')
        },
        setLoggedOut(state) {
            state.loggedIn = false
        },
        setUserInfo(state, value) {
            state.user = value
        },
    },
    actions: {
        // Auth
        login(context, payload) {
            return axios.post('auth/token/login/', payload)
                .then(response => {
                    context.commit('setToken', response.data.auth_token)
                })
                .catch(e => {
                    console.log(e)
                })
        },
        logout(context) {
            return axios.post('auth/token/logout/')
                .then(response => {
                    context.commit('setLoggedOut')
                    delete axios.defaults.headers['Authorization']
                    localStorage.removeItem('authToken')
                    router.push('login')
                })
                .catch(e => {
                    console.log(e)
                })
        },
    }
})