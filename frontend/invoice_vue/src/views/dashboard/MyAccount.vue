<template>
    <div class="page-my-account">
        <h1 class="title">My account</h1>
        
        <strong>Team: </strong>{{ team.name }}<br>
        <strong>Username: </strong>{{ $store.state.user.username }}

        <hr>

        <div class="buttons">
            <router-link to="/dashboard/my-account/edit-team" class="button is-light">Edit Team</router-link>
            <button @click="logout()" class="button is-danger">Log out</button>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'MyAccount',
    data() {
        return {
            team: {}
        }
    },
    methods: {
        getOrCreateTeam() {
            axios
                .get('/api/v1/teams/')
                .then(response => {
                    this.team = response.data[0]
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        },
        logout() {
            axios
                .post("/api/v1/token/logout/")
                .then(response => {
                    axios.defaults.headers.common["Authorization"] = ""
                    localStorage.removeItem("token")
                    localStorage.removeItem("username")
                    localStorage.removeItem("userid")
                    this.$store.commit('removeToken')
                    this.$router.push('/')
                })
        }
    },
    async mounted() {
        await this.getOrCreateTeam()
    }
}
</script>