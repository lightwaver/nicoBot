<template>
    <div>
        <h1>{{ hello }}</h1>
        <div>
            Hier das Programm:
            <button @click="onPlay"> > Run</button>
        </div>
        <div class="codeFrame">
        <Sortable :list="elements" item-key="id" tag="div" :options="options" >
            <template #item="{ element, index }">
                <CodeFragment :fragment="element" :id="index * 100" />
            </template>
        </Sortable>
        </div>
    </div>
</template>
<script lang="ts">
 function onPlay() {

 }
</script>
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
    { function: CodeFunction.if, conditions: [{ left: "x", operator: Operator.equals, right: "2"}, 
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
.codeFrame {
    padding: 5px;
    margin: 5px;
    border-left: 3px solid #888;
    border-top: 3px solid #888;
    border-right: 3px solid #ccc;
    border-bottom: 3px solid #ccc;
    border-radius: .5em;
    background-color: #efefef;
    height: 100%;
    min-height: 500px;
    overflow: scroll;
}

button {
    border-left: 1px solid #888;
    border-top: 1px solid #888;
    border-right: 1px solid #ccc;
    border-bottom: 1px solid #ccc;
    border-radius: 0.3em;
    background-color: #efefef;
    padding: 0 5px;
}
</style>