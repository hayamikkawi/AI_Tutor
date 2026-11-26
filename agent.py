# define the tools to the LLM 
tools = [
    {
        "type": "function", 
        "name": "add", 
        "description": "Add two numbers.", 
        "parameters": {
            "type": "object",
            "properties": {
                "a": {"type": "number"},
                "b": {"type": "number"}
            },
            "required": ["a", "b"],
            "additionalProperties": False
        },
        "strict": True
    }, 
    {
        "type": "function", 
        "name": "subtract", 
        "description": "Subtract the second parameter from the first one.", 
        "parameters": {
            "type": "object",
            "properties": {
                "a": {"type": "number"},
                "b": {"type": "number"}
            },
            "required": ["a", "b"],
            "additionalProperties": False
        },
        "strict": True
    }, 
    {
        "type": "function", 
        "name": "divide", 
        "description": "Divide the first parameter over the second one.", 
        "parameters": {
            "type": "object",
            "properties": {
                "a": {"type": "number"},
                "b": {"type": "number"}
            },
            "required": ["a", "b"],
            "additionalProperties": False
        },
        "strict": True
    }, 
    {
        "type": "function", 
        "name": "multiply", 
        "description": "Multiply two numbers.", 
        "parameters": {
            "type": "object",
            "properties": {
                "a": {"type": "number"},
                "b": {"type": "number"}
            },
            "required": ["a", "b"],
            "additionalProperties": False
        },
        "strict": True
    }
]