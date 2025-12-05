You are an expert in agent systems and ontology population.

You will be given:
1) An existing ontology file in Turtle format (http://www.w3id.org/agentic-ai/onto)
{{ontology}}
2) The source code and configuration of an agent-based solution (with agents, tasks, tools, workflows, prompts, etc.)
{{source_code}}

Your task:

1. Study the ontology file.
   - Treat it as a fixed schema with all classes and properties already defined.
   - Do NOT add, modify, or remove any classes or properties in the schema!

2. Study the source code and configuration.
   - Extract all instance-level information needed to fully describe the solution (agents, tasks, tools, workflows, prompts, parameters, data/artifacts, etc.).

3. Populate the ontology with individuals based on the extracted information. The goal is that another LLM can reconstruct the agent solution from the ontology instances you create. Do not add source code because we do not know the target framework to recreate the agent solution, so keep the semantic meaning and logic instead.
   - Use ONLY the existing classes and properties from the ontology!
   - Create individuals for all relevant entities and connect them with the appropriate properties.
   - Preserve all information from the source code (including prompts, parameters, and important logic) as literals or links between individuals. Fidelity is important, do not change or condense information.

4. If some aspects of the solution cannot be modeled with the current ontology:
   - Do NOT invent new classes or properties!
   - Do NOT model programming information (e.g., specific code structures, language-specific constructs, or implementation details), we are interested in the semantic meaning. Do NOT model framework specific functions and SDKs! Do NOT model UI components!
   - Model them as closely as possible with the existing schema but do not abuse the schema (e.g., do not press different classes and info in literals and descriptions).
   - If concepts are missing: list any missing concepts, limitations, or necessary extensions in an “Issues / Assumptions” comment block at the top of the Turtle output. Do not put it into the ontology in descriptions, etc.

Output format:

- Respond with the instance information in .ttl format.
- At the very top of the Turtle content, write a comment block:

  Issues / Assumptions:
  - <issue 1 or "No issues detected">
  - <issue 2>
  ...

  Do not ask for confirmation or clarifications, just produce the output as specified.