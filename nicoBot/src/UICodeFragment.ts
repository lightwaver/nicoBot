export interface UICodeFragment {
    name?: string;
    function: CodeFunction;
    intent?: number;
    numVal?: number;
    direction?: Direction;
    strValue?: string;
    subFunctions?: UICodeFragment[];
    conditions?: UICondition[];
}

export enum Direction { left, right }
export enum CodeFunction {
    go,
    turn,
    while,
    if,
}

export interface UICondition {
    operator: Operator;
    left: any;
    right?: any;
    conditions?: UICondition[];
}

export enum Operator {
    equals = "=",
    greaterThan = ">",
    smallerThan = "<",
    greaterOrEqual = ">=",
    smallerOrEqual = "<=",
}