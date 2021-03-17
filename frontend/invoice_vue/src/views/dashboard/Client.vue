<template>
    <div class="page-client">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">{{ client.name }}</h1>

                <router-link :to="{ name: 'EditClient', params: { id: client.id }}" class="button is-light mt-4">Edit</router-link>
            </div>

            <div class="column is-12">
                <h2 class="subtitle">Contact Details</h2>

                <p>NAME: <strong>{{ client.name }}</strong></p>

                <p>ADDRESS1: {{ client.address1 }}</p>
                <p>ADDRESS2: {{ client.address2 }}</p>
                <p>ZIPCODE: {{ client.zipcode }}</p>
                <p>PLACE: {{ client.place }}</p>
                <p>COUNTRY: {{ client.country }}</p>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Client',
    data() {
        return {
            client: {}
        }
    },
    methods: {
        getClient() {
            const clientID = this.$route.params.id

            axios
                .get(`api/v1/clients/${clientID}`)
                .then(response => {
                    this.client = response.data
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        }
    },
    mounted() {
        this.getClient()
    },

}
</script>