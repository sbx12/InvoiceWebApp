<template>
    <div class="page-edit-team">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Edit Team - {{ team.name }}</h1>
            </div>

            <div class="column is-12">
                <div class="field">
                    <label>Name</label>

                    <div class="control">
                        <input type="text" name="name" class="input" v-model="team.name">
                    </div>
                </div>

                <div class="field">
                    <label>Organization Number</label>

                    <div class="control">
                        <input type="text" name="org_numer" class="input" v-model="team.org_numer">
                    </div>
                </div>

                <div class="field">
                    <label>First Invoice Number</label>

                    <div class="control">
                        <input type="number" name="first_invoice_number" class="input" v-model="team.first_invoice_number">
                    </div>
                </div>

                <div class="field">
                    <label>Bankaccount</label>

                    <div class="control">
                        <input type="text" name="bankaccount" class="input" v-model="team.bankaccount">
                    </div>
                </div>

                <div class="field">
                    <label>Email</label>

                    <div class="control">
                        <input type="email" class="input" v-model="team.email">
                    </div>
                </div>

                <div class="field">
                    <label>Address1</label>

                    <div class="control">
                        <input type="text" class="input" v-model="team.address1">
                    </div>
                </div>

                <div class="field">
                    <label>Address2</label>

                    <div class="control">
                        <input type="text" class="input" v-model="team.address2">
                    </div>
                </div>

                <div class="field">
                    <label>Zipcode</label>

                    <div class="control">
                        <input type="text" class="input" v-model="team.zipcode">
                    </div>
                </div>

                <div class="field">
                    <label>Place</label>

                    <div class="control">
                        <input type="text" class="input" v-model="team.place">
                    </div>
                </div>

                <div class="field">
                    <div class="control">
                        <button class="button is-success" @click="submitForm">Save Changes</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'EditTeam',
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
        submitForm() {
            axios
                .patch(`/api/v1/teams/${this.team.id}/`, this.team)
                .then(response => {
                    toast({
                        message: 'The changes was saved',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right',
                    })
                    this.$router.push('/dashboard/my-account')
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        }
    },
    async mounted() {
        await this.getOrCreateTeam()
    }

}
</script>