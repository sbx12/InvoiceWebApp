<template>
    <div class="page-invoice">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Invoice - {{ invoice.invoice_number }}</h1>
            </div>

            <div class="column is-12">
                <h2 class="subtitle">Client</h2>

                <p>NAME: <strong>{{ invoice.client_name }}</strong></p>

                <p>ADDRESS1: {{ invoice.client_address1 }}</p>
                <p>ADDRESS2: {{ invoice.client_address2 }}</p>
                <p>ZIPCODE: {{ invoice.client_zipcode }}</p>
                <p>PLACE: {{ invoice.client_place }}</p>
                <p>COUNTRY: {{ invoice.client_country }}</p>
            </div>

            <div class="column is-12">
                <h3 class="is-size-4">Items</h3>
                
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <td>ID</td>
                            <td>Title</td>
                            <td>Quantity</td>
                            <td>Amount</td>
                        </tr>
                    </thead>

                    <tbody>
                        <tr v-for="item in invoice.items" v-bind:key="item.id">
                            <td>{{ item.id }}</td>
                            <td>{{ item.title }}</td>
                            <td>{{ item.quantity }}</td>
                            <td>{{ item.net_amount }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Invoice',
    data() {
        return {
            invoice: {},
            items: {}
        }
    },
    methods: {
        getInvoice() {
            const invoiceID = this.$route.params.id

            axios
                .get(`api/v1/invoices/${invoiceID}`)
                .then(response => {
                    this.invoice = response.data
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        },
    },
    async mounted() {
        await this.getInvoice()
    },

}
</script>