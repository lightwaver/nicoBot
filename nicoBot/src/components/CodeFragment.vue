<template>
    <div>
        <div class="draggable command" :key="id">
            <div class="name">{{ fragment.name }}</div>
            <div v-if="fragment.conditions">
                <Condition class="condition" :conditions="fragment.conditions" :depth="0" />:
            </div>
            <div v-if="fragment.function != CodeFunction.if" class="function inline">{{ CodeFunction[fragment.function] }}&nbsp;</div>
            <div v-if="fragment.function != CodeFunction.if" class="value inline" >{{ fragment.numVal }}{{ fragment.strValue }} {{ fragment.direction ? Direction[fragment.direction] : "" }}</div>

            <div class="intent">
            <Sortable :list="fragment.subFunctions" item-key="id" tag="div" >
                <template #item="{ element, index }">
                    <CodeFragment :fragment="fr" :id="id * 100 + ix" v-if="fragment.subFunctions" v-for="(fr, ix) in fragment.subFunctions"/>
                </template>
            </Sortable>
            </div>
        </div>
    </div>
</template>
<script setup lang="ts">
import { Sortable } from "sortablejs-vue3";
import { UICodeFragment, CodeFunction, Direction } from '@/UICodeFragment';
import Condition from "./Condition.vue";

export interface CodeFragmentProps {
    fragment: UICodeFragment;
    id: number;
};


const props = defineProps<CodeFragmentProps>()
</script>
<style scoped>
.command {
    padding: 0 5px;
    display:block;
    width: 100%;
}
.command > .condition {
    padding: 0 5px;
    display: inline-block;
}
.command > .command {
    display: block;
}

.intent {
    padding-left: 15px;
}
.inline {
    display: inline-flex;
}
</style>    