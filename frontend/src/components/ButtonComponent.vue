<template>
    <button>
        <slot></slot>
    </button>
</template>

<script>
    export default {
        name: "ButtonComponent"
    }
</script>

<style scoped lang="less">
    button {
        width: 100%;
        font-weight: 700;
        text-transform: uppercase;
        border-radius: 5px;
        font-size: 0.9em;
        background: #4f69c2;
        padding: 8px 20px;
        color: #eeeeee;
        //box-shadow: 0 3px 15px 0 rgba(2, 0, 0, 0.25);
        transition: 0.2s;
        border: none;

        &:hover {
            //box-shadow: 0 7px 20px 0 rgba(2, 0, 0, 0.4);
            background: #4463af;
            transition: 0.2s;
        }
    }
</style>