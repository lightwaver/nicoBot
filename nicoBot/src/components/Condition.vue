<template>
<div class="inline">
    <div v-for="(c, ix) in conditions" class="inline condition">
        <div class="inline" v-if="ix > 0">or</div>
        <div class="inline" v-if="c.conditions">(</div>
        <div class="inline" v-if="(depth ?? 0) == 0 && !(c.conditions)">if</div>
        <div class="inline fieldLeft">{{ c.left }}</div>
        <div class="inline operator">{{ c.operator }}</div>
        <div class="inline fieldRight">{{ c.right }}</div>
        <div class="inline" v-if="c.conditions">
            and <Condition :conditions="c.conditions" :depth="(depth ?? 0) + 1"/>)
        </div>
    </div>
</div>
</template>
<script setup lang="ts">
import { UICondition } from '@/UICodeFragment';
interface ConditionProps {
    conditions: UICondition[];
    depth?: number;
};

const props = defineProps<ConditionProps>()
</script>
<style scoped>
.inline {
    display: inline-flex;
}
.condition {
    padding: 0 5px;
    background-color: #afa;
    outline: 0 1px 0 0 solid silver;
    border-radius: 1em;
}
.condition > div {
    padding: 0 5px;
}

</style>