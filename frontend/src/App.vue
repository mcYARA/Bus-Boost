<template>
    <div id="app">
        <b-navbar fixed="top" type="light" v-if="$store.state.loggedIn">
            <div class="container text-uppercase">
                <b-navbar-nav>
                    <b-nav-item to="/">Розклад руху</b-nav-item>
                    <b-nav-item to="/tickets">Мої квитки</b-nav-item>
                </b-navbar-nav>
                <b-navbar-nav class="ml-auto">
                    <b-nav-item @click.prevent="$store.dispatch('logout')">Вихід</b-nav-item>
                </b-navbar-nav>
            </div>
        </b-navbar>
        <div class="container" id="content">
            <div class="justify-content-md-center">
                <router-view/>
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

    #content {
        margin-top: 80px;
    }

    .navbar-light {
        box-shadow: 0 1px 5px -2px gray;
        background-color: #fff !important;

        a:not(.dropdown-item) {
            text-shadow: none;
        }

        .active a {
            color: #536AB3 !important;
        }

        .navbar-brand {
            color: #586994 !important;
        }
    }

    .navbar-nav .nav-link {
        line-height: 30px;
        font-size: 10.5pt;
        font-weight: 500;
    }
</style>