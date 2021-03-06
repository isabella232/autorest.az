# Command Customizations

Autogenerated commands may be customized by adding appropriate directives into readme.az.md file.

## Renaming Commands 

Use following directive to rename command / command group: 

    directive: 
      - where: 
          command: vm create 
        set:
          command: vm create-modified

## Changing Command Group / Command Description 

Use following directive to change command / command group's description: 

    directive: 
      - where: 
          command: vm create 
        set:
          description: My updated command description


## Renaming Parameters

Use following directive format to rename parameter:
 

    directive: 
      - where: 
          command: vm create
          parameter-name: paremeter 
        set:
          name: modified-parameter-name

## Setting Parameter Alias

Use following directive format to rename parameter:
 

    directive: 
      - where: 
          command: vm create
          parameter-name: paremeter 
        set:
          alias: parameter-alias

## Setting Parameter Description

Use following directive format to set new parameter's decription:
 

    directive: 
      - where: 
          command: vm create
          parameter-name: paremeter 
        set:
          description: My parameter description

## Setting Parameter Implementation Hint

Use following directive format to rename parameter:
 

    directive: 
      - where: 
          command: vm create
          parameter-name: paremeter 
        set:
          hint: json

Values can be:
- json
- actions
- subgroup

NOTE: For json it may be needed to suppress Python SDK flattening. This will require additional directive applied before Python SDK is generated.

# Library Customizations

*azure.cli.core* is used as default library. Use following configuration in readme.az.md to replace it with your own cli core library:

    # Default value: azure.cli.core
    cli-core-lib: <your own cli core library>



