import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.baseURL = 'http://127.0.0.1:8000/api/'

const authToken = localStorage.getItem('authToken')
if (authToken) {
    axios.defaults.headers['Authorization'] = "Token " + authToken
}

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        loggedIn: false,
        user: '',
        busLines: [],
    },
    getters: {
        getAuth(state) {
            return state.loggedIn
        },
        getUserInfo(state) {
            return state.user
        },
        getBusLines(state) {
            return state.busLines
        }
    },
    mutations: {
        setLoggined(state) {
            state.loggedIn = true
        },
        setToken(state, token) {
            localStorage.setItem('authToken', token)
            state.loggedIn = true
            axios.defaults.headers['Authorization'] = "Token " + localStorage.getItem('authToken')
            router.push('/')
        },
        setLoggedOut(state) {
            state.loggedIn = false
        },
        setUserInfo(state, value) {
            state.user = value
        },
        setBusLines(state, value) {
            state.busLines = value
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
        updateBusLines(context) {
            return axios.get('buslines/')
                .then(response => {
                    context.commit('setBusLines', response.data)
                })
                .catch(e => {
                    console.log(e)
                })
        },
        bookTicket(context, pk) {
            return axios.get('/buslines/' + pk + '/book_ticket/')
                .then(response => {
                    console.log(response)
                })
                .catch(e => {
                    console.log(e)
                })
        },
    }
})