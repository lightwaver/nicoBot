<template>
    <div>
        <div class="draggable command" :key="id">
            <div class="name">{{ fragment.name }}</div>
            <Condition v-if="fragment.conditions" class="condition" :conditions="fragment.conditions" />
            <div class="function">{{ CodeFunction[fragment.function] }}</div>
            <div class="value">{{ fragment.numVal }}{{ fragment.strValue }} {{ fragment.direction ? Direction[fragment.direction] : "" }}</div>

            <Sortable :list="fragment.subFunctions" item-key="id" tag="div" :options="options" >
                <template #item="{ element, index }">
                    <CodeFragment :fragment="fr" :id="id * 100 + ix" v-if="fragment.subFunctions" v-for="(fr, ix) in fragment.subFunctions"/>
                </template>
            </Sortable>

        </div>
    </div>
</template>
<script setup lang="ts">
import { Sortable } from "sortablejs-vue3";
import { UICodeFragment, CodeFunction, Direction } from '@/UICodeFragment';
import Condition from "./Condition.vue";

interface CodeFragmentProps {
    fragment: UICodeFragment;
    id: number;
    options?: Sortable.SortableOptions;
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
.command > .condition {
    padding: 5px;
    display: inline-block;
}
.command > .command {
    display: block;
}
</style>    