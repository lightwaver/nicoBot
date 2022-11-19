<template>
    <div>
        {{ hello }}

        <Sortable :list="elements" item-key="id" tag="div" :options="options" >
            <template #item="{ element, index }">
                <CodeFragment :fragment="element" :id="index * 100" />
            </template>
        </Sortable>
    </div>
</template>

<script setup lang="ts">
//
import { UICodeFragment, CodeFunction, Direction, Operator } from "@/UICodeFragment";
import { Sortable } from "sortablejs-vue3";
import CodeFragment from "./CodeFragment.vue";


let hello = "Hallo Nico!";
let options: Sortable.SortableOptions = {
 
};
let elements: UICodeFragment[] = [
    { function: CodeFunction.go, numVal: 30 },
    { function: CodeFunction.turn, direction: Direction.left },
    { function: CodeFunction.go, numVal: 30 },
    { function: CodeFunction.go, numVal: -60, conditions: [{ left: "x", operator: Operator.equals, right: "2"}, 
    { left: "y", operator: Operator.smallerThan, right: "1", conditions: [
    { left: "z", operator: Operator.equals, right: "2"},
    ]}],
    subFunctions: [
        { function: CodeFunction.turn, direction: Direction.left },
        { function: CodeFunction.go, numVal: 30 },
    ]
},
    
];


</script>

<style scoped>
</style>