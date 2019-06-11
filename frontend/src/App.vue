<template>
    <div id="app">
        <div class="container">
            <div class="row justify-content-md-center">
                <div class="col-lg-3" id="nav" v-if="$store.state.loggedIn">
                    <h3 id="brand-name">FinManager</h3>
                    <div class="nav-menu">
                        <router-link to="/categories" class="nav-element">
                            Categories
                        </router-link>
                        <router-link to="/transactions" class="nav-element">
                            Transactions
                        </router-link>
                        <router-link to="/charts" class="nav-element">
                            Charts
                        </router-link>
                        <a href="#" @click.prevent="$store.dispatch('logout')" class="nav-element">
                            Sign Out
                        </a>
                    </div>
                </div>
                <div class="col-lg-9">
                    <router-view/>
                </div>
            </div>
        </div>
        <!-- set progressbar -->
        <vue-progress-bar></vue-progress-bar>
    </div>
</template>

<script>
    export default {
        name: 'App',
        created() {
            this.$Progress.start()
            //  hook the progress bar to start before we move router-view
            this.$router.beforeEach((to, from, next) => {
                this.$Progress.start()
                next()
            })
            if (localStorage.getItem('authToken')) {
                this.$store.commit('setLoggined')
            } else {
                this.$router.push('login')
            }
        },
    }
</script>

<style lang="less">
    @import (css) url('https://fonts.googleapis.com/css?family=Varela+Round');

    html, body {
        background: #eee;
    }

    #app {
        background: #eee;
        margin-bottom: 20px;
        margin-top: 20px;
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        color: #2c3e50;
    }

    #nav {
        #brand-name {
            font-family: 'Varela Round', sans-serif;
            font-weight: 700;
            line-height: 50px;
            padding-left: 25px;
        }

        .nav-element {
            padding-left: 15px;
            padding-right: 15px;
            line-height: 50px;
            font-weight: 700;
            font-family: 'Open Sans', sans-serif;
            display: block;
            letter-spacing: 0.5pt;
            color: #212529;
            border-radius: 5px;

            &:hover {
                background: #dddddd;
                text-decoration: none;
            }

            &.router-link-exact-active {
                background: #E3E3E3;
            }

            svg {
                margin-right: 5px;
            }
        }
    }
</style>