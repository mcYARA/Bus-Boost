<template>
    <div class="card input-card mb-3">
        <span class="card-header card-title"><b>{{title}}</b></span>
        <div class="card-body">
            <slot></slot>
        </div>
    </div>
</template>

<script>
    export default {
        name: "InputBox",
        props: ['title',]
    }
</script>

<style scoped lang="less">
    .card {
        border: none;
    }

    .input-card {
        background: #fbfbfb;
        box-shadow: 0 3px 15px 0 rgba(2, 0, 0, 0.15);

        .card-title {
            font-size: 75%;
            font-weight: 600;
            text-transform: uppercase;
        }

        input[type=file] {
            border: none;
            background: inherit;
            width: inherit;

            &:focus {
                border: none;
            }
        }

        input:not([type=submit]):not([type=file]) {
            font-weight: 700;
            width: 100%;
            border: 2px solid #e9eaef;
            border-radius: 5px;
            margin-bottom: 15px;
            line-height: 30px;
            transition: .1s;
        }
    }
</style>