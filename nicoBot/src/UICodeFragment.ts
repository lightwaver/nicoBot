export interface UICodeFragment {
    name?: string;
    function: CodeFunction;
    intent?: number;
    numVal?: number;
    direction?: Direction;
    strValue?: string;
    subFunctions?: UICodeFragment[];
    conditions?: Condition[];
}

export enum Direction { left, right }
export enum CodeFunction {
    go,
    turn,
    while,
}

export interface Condition {
    operator: Operator;
    left: any;
    right?: any;
    conditions?: Condition[];
}

export enum Operator {
    equals = "=",
    greaterThan = ">",
    smallerThan = "<",
    greaterOrEqual = ">=",
    smallerOrEqual = "<=",
}