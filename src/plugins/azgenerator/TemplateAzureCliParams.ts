﻿/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

import { CodeModelAz } from "./CodeModelAz"
import { EscapeString, ToCamelCase, Capitalize } from "../../utils/helper";
import { SchemaType } from "@azure-tools/codemodel";


let hasActions: boolean = false;
let hasBoolean: boolean = false;
let hasEnum: boolean = false;
let actions: string[] = [];

export function GenerateAzureCliParams(model: CodeModelAz): string[] {
    let output: string[] = [];
    let hasActions: boolean = false;
    let hasBoolean: boolean = false;
    let hasTags: boolean = false;
    let hasResourceGroup: boolean = false;
    let hasLocationType: boolean = false;
    let hasEnum: boolean = false;
    let actions: string[] = [];
        
    var output_args: string[] = [];

    output_args.push("");
    output_args.push("");
    output_args.push("def load_arguments(self, _):");
    //output.push("    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')");

    if (model.SelectFirstCommandGroup()) {
        do {
            //let methods: string[] = model.CommandGroup_Commands;

            if (model.SelectFirstCommand()) {
                do {
                    output_args = output_args.concat(getCommandBody(model));
                    if(model.Command_CanSplit) {
                        output_args = output_args.concat(getCommandBody(model, true));
                    }
                }
                while (model.SelectNextCommand());
            }
        } while (model.SelectNextCommandGroup());
    }
    output.push("# --------------------------------------------------------------------------------------------");
    output.push("# Copyright (c) Microsoft Corporation. All rights reserved.");
    output.push("# Licensed under the MIT License. See License.txt in the project root for license information.");
    output.push("# --------------------------------------------------------------------------------------------");
    output.push("# pylint: disable=line-too-long");
    output.push("# pylint: disable=too-many-lines");
    output.push("# pylint: disable=too-many-statements");
    output.push("");
    //output.push("from knack.arguments import CLIArgumentType");

    if (hasTags || hasBoolean || hasEnum || hasResourceGroup || hasLocationType)
    {
        output.push("from azure.cli.core.commands.parameters import (");
        if (hasTags) output.push("    tags_type,");
        if (hasBoolean) output.push("    get_three_state_flag,");
        if (hasEnum) output.push("    get_enum_type,");
        if (hasResourceGroup) output.push("    resource_group_name_type,");
        if (hasLocationType )output.push("    get_location_type,");
        output[output.length - 1] = output[output.length - 1].split(",")[0];
        output.push(")");
    }

    if (hasActions) {
        output.push("from azext_" + model.Extension_NameUnderscored + ".action import (")

        for (let idx: number = 0; idx < actions.length; idx++) {
            let action = actions[idx];
            output.push("    " + action + (idx < actions.length - 1 ? "," : ""));
        }
        output.push(")")
    }

    output = output.concat(output_args);

    output.push("");
    return output;
}

function getCommandBody(model: CodeModelAz, needUpdate: boolean = false) {
    //let method: string = methods[mi];

    //let ctx = model.SelectCommand(method);
    //if (ctx == null)
    //    continue;
    let output_args: string [] = [];
    output_args.push("");
    if(needUpdate) {
        output_args.push("    with self.argument_context('" + model.Command_Name.replace(/ create/g, " update") + "') as c:");
    } else {
        output_args.push("    with self.argument_context('" + model.Command_Name + "') as c:");
    }
    
    if (!model.SelectFirstOption()) {
        output_args.push("        pass");
    }
    else {
        let hasParam = false;
        do {
            if(model.Option_IsFlattened) {
                continue;
            }
            hasParam = true;
            let parameterName = model.Option_NamePython;

            let argument = "        c.argument('" + parameterName + "'";

            // this is to handle names like "format", "type", etc
            if (parameterName == "type" || parameterName == "format") {
                argument = "        c.argument('_" + parameterName + "'";
                argument += ", options_list=['--" + parameterName + "']";
            }

            if (model.Option_Type == SchemaType.Boolean) {
                hasBoolean = true;
                argument += ", arg_type=get_three_state_flag()";
            }
            else if (model.Option_Type == SchemaType.Choice || model.Option_Type == SchemaType.SealedChoice) {
                hasEnum = true;
                argument += ", arg_type=get_enum_type([";

                model.Option_EnumValues.forEach(element => {
                    if (!argument.endsWith("[")) argument += ", ";
                    argument += "'" + element + "'";
                });
                argument += "])";
            }

            if (parameterName == "resource_group_name") {
                argument += ", resource_group_name_type";
            }
            else if (parameterName == "tags") {
                argument += ", tags_type";
            }
            else if (parameterName == "location") {
                argument += ", arg_type=get_location_type(self.cli_ctx)";
            }
            else {
                argument += ", id_part=None, help='" + EscapeString(model.Option_Description) + "'";
            }

            if (model.Option_IsList) {
                if (model.Option_Type == SchemaType.Object || model.Option_Type == SchemaType.Array) {
                    let actionName: string = "Add" + Capitalize(ToCamelCase(model.Option_Name));
                    argument += ", action=" + actionName;
                    hasActions = true;

                    if (actions.indexOf(actionName) < 0) {
                        actions.push(actionName);
                    }
                }
                argument += ", nargs='+'";
            }

            argument += ")";

            output_args.push(argument);
        } while (model.SelectNextOption());
        if (!hasParam) {
            output_args.push("        pass");
        }
    }
    return output_args;
}