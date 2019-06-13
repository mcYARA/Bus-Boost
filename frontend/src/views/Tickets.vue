<template>
    <div id="home">
        <list-table>
            <template v-slot:tr>
                <th scope="col">Пункт відправлення</th>
                <th scope="col">Час відправлення</th>
                <th scope="col">Пункт прибуття</th>
                <th scope="col">Edit</th>
                <th scope="col">Delete</th>
            </template>
            <template v-slot:tbody>
                <tr v-for="ticket in $store.getters.getTickets">
                    <td>{{ticket.bus_line_info}}</td>
                    <td>{{ticket.bus_line_info.depart_time_str}}</td>
                    <td>{{ticket.arrive_settlement}}</td>
                    <td>{{ticket.arrive_settlement}}</td>
                    <td class="min-width">
                        <button-component @click.native="$store.dispatch('bookTicket', ticket.pk)">Бронювати</button-component>
                    </td>
                </tr>
            </template>
        </list-table>
    </div>
</template>

<script>
    import InputBox from '@/components/InputBox.vue'
    import ListTable from '@/components/ListTable.vue'
    import ButtonComponent from '@/components/ButtonComponent.vue'

    export default {
        name: "Tickets",
        components: {InputBox, ListTable, ButtonComponent},
        methods: {
            beforeUpdate() {
                this.$Progress.start()
            },
            updated() {
                this.$Progress.finish()
            }
        },
        created() {
            this.$store.dispatch('updateBusLines')
            this.$store.dispatch('updateTickets')
            this.$Progress.finish()
        },
        beforeUpdate() {
            this.$Progress.start()
        },
        updated() {
            this.$Progress.finish()
        }
    }
</script>

<style scoped lang="less">
</style>