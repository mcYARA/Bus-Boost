<template>
    <div id="home">
        <list-table>
            <template v-slot:tr>
                <th scope="col">Пункт відправлення</th>
                <th scope="col">Час відправлення</th>
                <th scope="col">Пункт прибуття</th>
                <th scope="col">Час прибуття</th>
                <th scope="col">Ціна</th>
                <th scope="col">Delete</th>
            </template>
            <template v-slot:tbody>
                <tr v-for="busLine in $store.getters.getBusLines">
                    <td>{{busLine.depart_settlement}}</td>
                    <td>{{busLine.depart_time_str}}</td>
                    <td>{{busLine.arrive_settlement}}</td>
                    <td>{{busLine.arrive_time_str}}</td>
                    <td>{{busLine.price}}</td>
                    <td class="min-width">
                        <button-component @click.native="$store.dispatch('bookTicket', busLine.pk)">Бронювати</button-component>
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
        name: "Home",
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