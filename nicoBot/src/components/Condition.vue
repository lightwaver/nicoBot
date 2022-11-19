<template>
<div>
    <div v-for="(c, ix) in conditions" class="condition">
        <span v-if="ix > 0">or</span> if
        <div class="fieldLeft">{{ c.left }}</div>
        <div class="operator">{{ c.operator }}</div>
        <div class="fieldRight">{{ c.right }}</div>
        <div v-if="c.conditions">
            and <Condition :conditions="c.conditions" />
        </div>
    </div>
</div>
</template>
<script setup lang="ts">
import { UICondition, Operator } from '@/UICodeFragment';
interface ConditionProps {
    conditions?: UICondition[];
};

const props = defineProps<ConditionProps>()
</script>
<style scoped>
.condition {
    padding: 0 5px;
    border: 1px solid silver;
    display:block;
    width: 100%;
    background-color: #FFaaaa;
}
.condition > div {
    padding: 5px;
    display: inline-block;
}

</style>