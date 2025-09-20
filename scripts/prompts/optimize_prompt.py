# WORKFLOW_OPTIMIZE_PROMPT = """You are building a Graph and corresponding Prompt to jointly solve {type} problems. 
# Referring to the given graph and prompt, which forms a basic example of a {type} solution approach, 
# please reconstruct and optimize them. You can add, modify, or delete nodes, parameters, or prompts. Include your 
# single modification in XML tags in your reply. Ensure they are complete and correct to avoid runtime failures. When 
# optimizing, you can incorporate critical thinking methods like review, revise, ensemble (generating multiple answers through different/similar prompts, then voting/integrating/checking the majority to obtain a final answer), selfAsk, etc. Consider 
# Python's loops (for, while, list comprehensions), conditional statements (if-elif-else, ternary operators), 
# or machine learning techniques (e.g., linear regression, decision trees, neural networks, clustering). The graph 
# complexity should not exceed 10. Use logical and control flow (IF-ELSE, loops) for a more enhanced graphical 
# representation.Ensure that all the prompts required by the current graph from prompt_custom are included.Exclude any other prompts.
# Output the modified graph and all the necessary Prompts in prompt_custom (if needed).
# The prompt you need to generate is only the one used in `prompt_custom.XXX` within Custom. Other methods already have built-in prompts and are prohibited from being generated. Only generate those needed for use in `prompt_custom`; please remove any unused prompts in prompt_custom.
# the generated prompt must not contain any placeholders.
# Considering information loss, complex graphs may yield better results, but insufficient information transmission can omit the solution. It's crucial to include necessary context during the process."""
WORKFLOW_OPTIMIZE_PROMPT = """You are building a flowchart and corresponding prompts to jointly solve problems of type {type}.
Meanwhile, you need to generate some runnable tools and insert them into your flowchart to facilitate easier execution of such tasks in the future. 
Refer to the provided flowchart and prompts (which together form a basic example of a solution approach for {type} problems) to reconstruct and optimize them.
You can add, modify, or delete nodes, parameters, or prompts. In your reply, wrap each of your modifications in XML tags.
Ensure the modified content is complete and correct to avoid runtime errors. When optimizing, you can incorporate critical thinking methods such as review, revise, ensemble (generating multiple answers through different/similar prompts and then obtaining a final answer via voting/integration/verification of the majority answers), selfAsk, etc.
You can also consider using Python's loops (for loops, while loops, list comprehensions), conditional statements (if-elif-else statements, ternary operators), or machine learning techniques (such as linear regression, decision trees, neural networks, clustering algorithms). The complexity of the flowchart must not exceed 10 nodes. Use logical flows and control flows (IF-ELSE branches, loops) to build a more sophisticated graphical representation.
Ensure all prompts required by the current flowchart are from and included in prompt_custom (custom prompt library). Do not include any other prompts.
Retain only the prompts in prompt_custom that need to be used and remove all unused prompts from it.
The generated prompts must not contain any placeholders. Considering the issue of information loss: flowcharts with higher complexity may yield better results, but insufficient information transmission may lead to the omission of solutions.
Therefore, it is crucial to incorporate necessary contextual information during the process.

Additionally, you should generate reusable tools (Python functions) for common tasks related to {type} problems. These tools should be saved in a separate tools.py file and imported into the workflow. The workflow should prioritize using these tools over direct LLM calls whenever possible. Only when no suitable tool exists for a specific task should the workflow fall back to using LLM capabilities.
I will give you a tools.py file with many examples of tools in it, and the tools you create also need to conform to this usage format.Here is the content of that file :{examples}.

For each tool you create:
1. Define a clear purpose and input/output specification
2. Include comprehensive error handling
3. Add detailed docstrings explaining usage
4. Ensure they are well-tested and robust

When designing the workflow, implement a tool selection mechanism that:
1. First attempts to match the task with available tools
2. Only uses LLM if no suitable tool is available
3. Provides clear feedback when falling back to LLM
"""

# WORKFLOW_INPUT = """
# Here is a graph and the corresponding prompt (prompt only related to the custom method) that performed excellently in a previous iteration (maximum score is 1). You must make further optimizations and improvements based on this graph. The modified graph must differ from the provided example, and the specific differences should be noted within the <modification>xxx</modification> section.\n
# <sample>
#     <experience>{experience}</experience>
#     <modification>(such as:add /delete /modify/ ...)</modification>
#     <score>{score}</score>
#     <graph>{graph}</graph>
#     <prompt>{prompt}</prompt>(only prompt_custom)
#     <operator_description>{operator_description}</operator_description>
# </sample>
# Below are the logs of some results with the aforementioned Graph that performed well but encountered errors, which can be used as references for optimization:
# {log}

# First, provide optimization ideas. **Only one detail point can be modified at a time**, and no more than 5 lines of code may be changed per modification—extensive modifications are strictly prohibited to maintain project focus!
# When introducing new functionalities in the graph, please make sure to import the necessary libraries or modules yourself, except for operator, prompt_custom, create_llm_instance, and CostManage, which have already been automatically imported.
# **Under no circumstances should Graph output None for any field.**
# Use custom methods to restrict your output format, rather than using code (outside of the code, the system will extract answers based on certain rules and score them).
# It is very important to format the Graph output answers, you can refer to the standard answer format in the log.
# You do not need to manually import prompt_custom or operator to use them; they are already included in the execution environment.
# """

WORKFLOW_INPUT = """
Here is a graph and the corresponding prompt (prompt only related to the custom method) that performed excellently in a previous iteration (maximum score is 1). You must make further optimizations and improvements based on this graph. The modified graph must differ from the provided example, and the specific differences should be noted within the <modification>xxx</modification> section.\n
<sample>
    <experience>{experience}</experience>
    <modification>(such as:add /delete /modify/ ...)</modification>
    <score>{score}</score>
    <graph>{graph}</graph>
    <prompt>{prompt}</prompt>(only prompt_custom)
    <operator_description>{operator_description}</operator_description>
    <tools>{tools}</tools>(previously generated tools for reference)
</sample>
Below are the logs of some results with the aforementioned Graph that performed well but encountered errors, which can be used as references for optimization:
{log}

First, provide optimization ideas. **Only one detail point can be modified at a time**, and no more than 5 lines of code may be changed per modification—extensive modifications are strictly prohibited to maintain project focus!
When introducing new functionalities in the graph, please make sure to import the necessary libraries or modules yourself, except for operator, prompt_custom, create_llm_instance, and CostManage, which have already been automatically imported.
**Under no circumstances should Graph output None for any field.**
Use custom methods to restrict your output format, rather than using code (outside of the code, the system will extract answers based on certain rules and score them).
It is very important to format the Graph output answers, you can refer to the standard answer format in the log.
You do not need to manually import prompt_custom or operator to use them; they are already included in the execution environment.

Additionally, you should generate reusable tools (Python functions) for common tasks related to {type} problems. These tools should be saved in a separate tools.py file and imported into the workflow. The workflow should prioritize using these tools over direct LLM calls whenever possible. Only when no suitable tool exists for a specific task should the workflow fall back to using LLM capabilities.
I will give you a tools.py file with many examples of tools in it, and the tools you create also need to conform to this usage format.Here is the content of that file :{examples}.

When optimizing, consider creating specialized tools for common tasks in {type} problems. These tools should be designed to:
1. Handle specific sub-tasks efficiently
2. Reduce reliance on LLM calls
3. Be reusable across similar problems
4. Include proper error handling and validation

For the workflow, implement a tool selection strategy that:
1. First attempts to solve the problem using available tools
2. Falls back to LLM only when no suitable tool exists
3. Documents which tools were used and why
"""



WORKFLOW_CUSTOM_USE = """\nHere's an example of using the `custom` method in graph:
```
# You can write your own prompt in <prompt>prompt_custom</prompt> and then use it in the Custom method in the graph
response = await self.custom(input=problem, instruction=prompt_custom.XXX_PROMPT)
# You can also concatenate previously generated string results in the input to provide more comprehensive contextual information.
# response = await self.custom(input=problem+f"xxx:{xxx}, xxx:{xxx}", instruction=prompt_custom.XXX_PROMPT)
# The output from the Custom method can be placed anywhere you need it, as shown in the example below
solution = await self.generate(problem=f"question:{problem}, xxx:{response['response']}")
```
Note: In custom, the input and instruction are directly concatenated(instruction+input), and placeholders are not supported. Please ensure to add comments and handle the concatenation externally.\n

**Introducing multiple operators at appropriate points can enhance performance. If you find that some provided operators are not yet used in the graph, try incorporating them.**
**Additionally, consider creating and using specialized tools for common tasks. Tools should be preferred over LLM calls when available:**
Example of using a tool instead of LLM
try:
result = await self.tool_execute(tool_name="specific_tool", input_data=problem_data)
if result['success']:
solution = result['output']
else:
# Fall back to LLM if tool fails
solution = await self.custom(input=problem, instruction=prompt_custom.XXX_PROMPT)
except Exception as e:
# Fall back to LLM if tool is not available
solution = await self.custom(input=problem, instruction=prompt_custom.XXX_PROMPT)
"""



WORKFLOW_TEMPLATE = """from typing import Literal
import workspace.{dataset}.workflows.template.operator as operator
import workspace.{dataset}.workflows.round_{round}.prompt as prompt_custom
import workspace.{dataset}.workflows.round_{round}.tools as tools_module
from scripts.async_llm import create_llm_instance


from scripts.evaluator import DatasetType

{graph}
"""

# TOOL_GENERATION_PROMPT = """
# Based on the problem type '{problem_type}', analyze the common tasks and sub-problems that frequently appear.
# Create specialized Python tools (functions) that can handle these tasks efficiently without requiring LLM assistance.

# For each tool you create:
# 1. Provide a clear, descriptive name that reflects its purpose
# 2. Define precise input parameters with type hints
# 3. Specify the expected output format
# 4. Include comprehensive error handling
# 5. Add detailed docstrings explaining usage and examples
# 6. Ensure the tool is focused on a single, specific task

# The tools should be designed to:
# - Reduce reliance on LLM calls
# - Be reusable across similar problems
# - Handle edge cases gracefully
# - Provide clear error messages when unable to process input

# Organize the tools in a logical structure within the tools.py file, grouping related functions together.
# """

# TOOL_SELECTION_PROMPT = """
# Given the current task: {task}
# And the available tools: {available_tools}

# Analyze whether any of the available tools can solve this task or a significant portion of it.
# Consider each tool's purpose, input requirements, and capabilities.

# If a suitable tool exists:
# - Identify which tool is most appropriate
# - Explain why it's suitable
# - Describe how to apply it to the task

# If no suitable tool exists:
# - Explain why existing tools are inadequate
# - Consider whether the task could be broken down into sub-tasks that existing tools could handle
# - Suggest what new tool might be created to handle this type of task in the future

# Your response should include:
# 1. A boolean indicating whether a suitable tool exists (true/false)
# 2. The name of the most appropriate tool (if applicable)
# 3. A detailed explanation of your reasoning
# """

# TOOL_FALLBACK_PROMPT = """
# The available tools were unable to handle the task: {task}
# Reason: {reason}

# Now falling back to LLM-based solution. Please solve the task using reasoning and knowledge.

# Task: {task}
# Additional context: {context}

# Please provide a step-by-step solution to the task.
# """