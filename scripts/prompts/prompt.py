
ANSWER_GENERATION_PROMPT = """
Think step by step and solve the problem.
1. In the "thought" field, explain your thinking process in detail.
2. In the "answer" field, provide the final answer concisely and clearly. The answer should be a direct response to the question, without including explanations or reasoning.
Your task: {input}
"""

FORMAT_PROMPT = """
For the question described as {problem_description},
please extract a short and concise answer contains only one word/few words from the following solution: {solution}.
Make sure there are no additional comments or explanations in your response.
"""

SC_ENSEMBLE_PROMPT = """
Given the question described as follows: {question}
Several solutions have been generated to address the given question. They are as follows:
{solutions}

Carefully evaluate these solutions and identify the answer that appears most frequently across them. This consistency in answers is crucial for determining the most reliable solution.

In the "thought" field, provide a detailed explanation of your thought process. In the "solution_letter" field, output only the single letter ID (A, B, C, etc.) corresponding to the most consistent solution. Do not include any additional text or explanation in the "solution_letter" field.
"""

PYTHON_CODE_VERIFIER_PROMPT = """
You are a professional Python programmer. Your task is to write complete, self-contained code based on a given mathematical problem and output the answer. The code should include all necessary imports and dependencies, and be ready to run without additional setup or environment configuration.

Problem description: {problem}
Other analysis: {analysis}
{feedback}

Your code should:
1. Implement the calculation steps described in the problem.
2. Define a function named `solve` that performs the calculation and returns the result. The `solve` function should not require any input parameters; instead, it should obtain all necessary inputs from within the function or from globally defined variables.
3. `solve` function return the final calculation result.

Please ensure your code is efficient, well-commented, and follows Python best practices. The output should be limited to basic data types such as strings, integers, and floats. It is prohibited to transmit images or other file formats. The code output is intended for a text-based language model.
"""


REFLECTION_ON_PUBLIC_TEST_PROMPT = """
Given a code problem and a python code solution which failed to pass test or execute, you need to analyze the reason for the failure and propose a better code solution.: 
### problem
{problem}

### Code Solution
{solution}

### Execution Result
{exec_pass}

#### Failed Test Case
{test_fail}

Please provide a reflection on the failed test cases and code solution, followed by a better code solution without any additional text or test cases.
"""

MD_ENSEMBLE_PROMPT = """
Given the question described as follows: {question}
Several solutions have been generated to address the given question. They are as follows:
{solutions}

Carefully evaluate these solutions and identify the solution that is more capable of solving the problem compared to other solutions, as this is crucial for problem-solving.

In the "thought" field, provide a detailed explanation of your thought process. In the "solution_letter" field, output only the single letter ID (A, B, C, etc.) corresponding to the solution. Do not include any additional text or explanation in the "solution_letter" field.
"""

REVIEW_PROMPT = """
Given a problem and a thoughtful solution, your task is to using critical thinking (questioning) to review the solution's correctness and provide a review result in boolean format.

problem: {problem}
solution: {solution}

If you are more than 95 percent confident that the final answer is incorrect, please return False and give a feedback for the error. Otherwise, please return True and give a explanation for the correctness.
"""

REVISE_PROMPT = """
Given a problem and a thoughtful solution which is just reviewed as incorrect, your task is to revise the solution to solve the question and ensure the final code solution is wrapped with ```python```.

problem: {problem}
solution: {solution}
feedback: {feedback}

Ensure the output code is self-contained, and without any additional text or test cases.
"""

# 新增的工具相关提示词
TOOL_GENERATION_PROMPT = """
Based on the problem type '{problem_type}', analyze the common tasks and sub-problems that frequently appear.
Create specialized Python tools (functions) that can handle these tasks efficiently without requiring LLM assistance.

For each tool you create:
1. Provide a clear, descriptive name that reflects its purpose
2. Define precise input parameters with type hints
3. Specify the expected output format
4. Include comprehensive error handling
5. Add detailed docstrings explaining usage and examples
6. Ensure the tool is focused on a single, specific task

The tools should be designed to:
- Reduce reliance on LLM calls
- Be reusable across similar problems
- Handle edge cases gracefully
- Provide clear error messages when unable to process input

Organize the tools in a logical structure within the tools.py file, grouping related functions together.
"""

TOOL_SELECTION_PROMPT = """
Given the current task: {task}
And the available tools: {available_tools}

Analyze whether any of the available tools can solve this task or a significant portion of it.
Consider each tool's purpose, input requirements, and capabilities.

If a suitable tool exists:
- Identify which tool is most appropriate
- Explain why it's suitable
- Describe how to apply it to the task

If no suitable tool exists:
- Explain why existing tools are inadequate
- Consider whether the task could be broken down into sub-tasks that existing tools could handle
- Suggest what new tool might be created to handle this type of task in the future

Your response should include:
1. A boolean indicating whether a suitable tool exists (true/false)
2. The name of the most appropriate tool (if applicable)
3. A detailed explanation of your reasoning
"""

TOOL_FALLBACK_PROMPT = """
The available tools were unable to handle the task: {task}
Reason: {reason}

Now falling back to LLM-based solution. Please solve the task using reasoning and knowledge.

Task: {task}
Additional context: {context}

Please provide a step-by-step solution to the task.
"""

TOOL_EXECUTION_PROMPT = """
Execute the following tool with the provided input data:
Tool: {tool_name}
Input: {input_data}

Please follow these steps:
1. Validate the input data against the tool's requirements
2. Execute the tool's logic
3. Handle any errors or exceptions gracefully
4. Return the result in the standardized format

Standardized response format:
{{
    "success": true/false,
    "output": "result data if successful",
    "error": "error message if not successful"
}}
"""

TOOL_EVALUATION_PROMPT = """
Evaluate the performance of a tool execution:
Tool: {tool_name}
Input: {input_data}
Output: {output_data}
Success: {success_status}

Analyze:
1. Whether the tool successfully completed the task
2. The quality and accuracy of the output
3. Any limitations or edge cases encountered
4. Suggestions for improving the tool

Based on this evaluation, determine if:
- The tool is suitable for this type of task and should be used again
- The tool needs modifications to handle similar tasks better
- A different approach (e.g., LLM fallback) would be more appropriate
"""