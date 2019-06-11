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
                <tr v-for="busLine in $store.getters.getBusLines">
                    <td>{{busLine.depart_settlement}}</td>
                    <td>{{busLine.depart_time}}</td>
                    <td>{{busLine.arrive_settlement}}</td>
                    <td>{{busLine.arrive_settlement}}</td>
                    <td class="min-width">Тут буде кнопка</td>
                </tr>
            </template>
        </list-table>
    </div>
</template>

<script>
    import InputBox from '@/components/InputBox.vue'
    import ListTable from '@/components/ListTable.vue'

    export default {
        name: "Categories",
        components: {InputBox, ListTable},
        data() {
            return {
                newCategory: {
                    title: '',
                    type: 'e'
                },
                updatingCategory: {
                    pk: 0,
                    title: '',
                    type: ''
                },
                categories: [],
                updateModalShow: false,
            }
        },
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