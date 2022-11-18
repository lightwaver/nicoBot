<template>
    <div>
        <div class="draggable command" :key="id">
                    <div class="name">{{ fragment.name }}</div>
                    <Condition :conditions="fragment.conditions" />
                    <div class="function">{{ CodeFunction[fragment.function] }}</div>
                    <div class="value">{{ fragment.numVal }}{{ fragment.strValue }} {{ fragment.direction ? Direction[fragment.direction] : "" }}</div>
                    <div v-if="fragment.subFunctions" v-for="(fr, ix) in fragment.subFunctions">
                        <CodeFragment :fragment="fr" :id="ix * 100" />
                    </div>
        </div>
    </div>
</template>
<script setup lang="ts">
import { UICodeFragment, CodeFunction, Direction } from '@/UICodeFragment';
import Condition from "./Condition.vue";

interface CodeFragmentProps {
    fragment: UICodeFragment;
    id: number;
};

const props = defineProps<CodeFragmentProps>()
</script>
<style scoped>
.command {
    padding: 5px;
    border: 1px solid silver;
    display:block;
    width: 100%;
}
.command > div {
    padding: 5px;
    display: inline-block;
}
</style>    