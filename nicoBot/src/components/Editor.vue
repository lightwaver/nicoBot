<template>
    <div>
        {{ hello }}

        <Sortable :list="elements" item-key="id" tag="div" :options="options">
            <template #item="{ element, index }">
                <div class="draggable command" :key="element.id">
                    <div class="name">{{ element.name }}</div>
                    <Condition :conditions="element.conditions" />
                    <div class="function">{{ CodeFunction[element.function] }}</div>
                    <div class="value">{{ element.numVal }}{{ element.strVal }} {{ Direction[element.direction] }}</div>
                </div>
            </template>
        </Sortable>
    </div>
</template>

<script setup lang="ts">
//
import { UICodeFragment, CodeFunction, Direction, Operator } from "@/UICodeFragment";
import { Sortable } from "sortablejs-vue3";
import Condition from "./Condition.vue";

let hello = "Hallo Nico!";
let options = {

};
let elements: UICodeFragment[] = [
    { function: CodeFunction.go, numVal: 30 },
    { function: CodeFunction.turn, direction: Direction.left },
    { function: CodeFunction.go, numVal: 30 },
    { function: CodeFunction.go, numVal: -60, conditions: [{ left: "x", operator: Operator.equals, right: "2"}] },
    
];


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