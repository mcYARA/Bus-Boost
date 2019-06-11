<template>
    <table class="table table-responsive mb-4 table-borderless">
        <thead>
        <tr>
            <slot name="tr"></slot>
        </tr>
        </thead>
        <tbody>
        <slot name="tbody"></slot>
        </tbody>
    </table>
</template>

<script>
    export default {
        name: "ListTable",
    }
</script>

<style scoped lang="less">
    .table {
        background: #fff;
        border-radius: 5px;
        padding: 5px 15px;
        box-shadow: 0 0 30px 0 rgba(2, 0, 0, 0.10);

        th {
            color: #717171;
            text-transform: uppercase;
            font-size: 9pt;
            font-weight: 700;
        }

        tr {
            border-bottom: 1px solid #f2f2f2;
        }

        td {
            vertical-align: middle !important;
            font-size: 11pt;

            &.min-width {
                white-space: nowrap;
                width: 1%;
            }
        }

        tbody tr:last-child {
            border-bottom: none;
        }
    }
</style>