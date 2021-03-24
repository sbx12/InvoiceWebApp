<template>
    <div class="page-invoices">
        <nav class="breadcrumb" aria-label="breadcrumbs">
            <ul>
                <li><router-link to="/dashboard">Dashboard</router-link></li>
                <li class="is-active"><router-link to="/dashboard/invoices" aria-current="true">Invoices</router-link></li>
            </ul>
        </nav>

        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Invoices</h1>
            </div>

            <div class="column is-12">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Client</th>
                            <th>Amount</th>
                            <th>Is Paid</th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr v-for="invoice in invoices" v-bind:key="invoice.id">
                            <td>{{ invoice.invoice_number }}</td>
                            <td>{{ invoice.client_name }}</td>
                            <td>{{ invoice.gross_amount }}</td>
                            <td>{{ invoice.is_paid }}</td>
                            <td>
                                <router-link :to="{ name: 'Invoice', params: { id: invoice.id }}" class="button is-light">Details</router-link>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'Invoices',
    data() {
        return {
            invoices: []
        }
    },
    methods: {
        getInvoices() {
            axios
                .get('/api/v1/invoices/')
                .then(response => {
                    this.invoices = response.data
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        }
    },
    mounted() {
        this.getInvoices()
    }
}
</script>