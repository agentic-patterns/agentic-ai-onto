# Agentic Ontology

This repository contains the **Agentic Ontology (AgentO)**, a formal semantic model for representing agents, their capabilities, interactions, and execution structures (e.g., Agents, tasks, goal  and workflow patterns). The ontology is designed to support research and applications in agentic AI.

## Ontology Overview

The ontology provides a structured vocabulary to represent:

- **Agents**: Entities capable of performing actions with autonomy.
- **Workflow**: Sequences or networks of actions or tasks, possibly with control flow (sequential, parallel, conditional).
- **Tasks & Tools**: Executable components that make up a plan, etc.

## 🔧 Class Definitions

| **Class**           | **Description**                                                                                                                   |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Agent**           | An entity capable of perceiving its environment, processing information, and acting to achieve goals.                             |
| **Capability**      | An ability that can be performed by an agent.                                                                                     |
| **Constraint**      | A rule or condition derived from the knowledge base that restricts or guides agent behavior or decision-making.                   |
| **Environment**     | The surroundings or context in which an agent operates.                                                                           |
| **WorkflowPattern** | A reusable and structured template that defines a sequence or logic of tasks and interactions within an agentic workflow.         |
| **WorkflowStep**    | An individual action or phase within a workflow pattern that contributes to task execution or goal achievement.                   |
| **Goal**            | An objective or desired state that an agent aims to achieve.                                                                      |
| **KnowledgeBase**   | A structured collection of information that an agent can reference.                                                               |
| **LanguageModel**   | Language Model that is used by an AI Agent.                                                                                       |
| **Memory**          | A knowledge structure that stores and retrieves past information, experiences, or states to support learning and decision-making. |
| **Objective**       | A collective objective that a team is assigned to accomplish.                                                                     |
| **Resource**        | Any asset that can be utilized by an agent to perform tasks.                                                                      |
| **Task**            | A specific activity that contributes to achieving a goal.                                                                         |
| **Team**            | A coordinated group of agents organized to pursue a common objective or set of tasks.                                             |
| **Tool**            | An instrument used by an agent to enhance its capabilities.                                                                       |



## Example Use

You can execute queries against the ontology via this public SPARQL endpoint:

SPARQL Endpoint: https://w3id.org/agentic-ai/sparql

The following SPARQL `CONSTRUCT` query demonstrates how to extract a structured view of an agentic team working toward a travel-planning related objective. This includes team members, their goals, tasks, workflow patterns, tools, and resources.

```sparql
PREFIX : <http://www.w3id.org/agentic-ai/onto#>

CONSTRUCT {
  ?team  :hasAgentMember ?agent ;
         :hasObjective ?objective ;
         :hasWorkflowPattern ?workflowPattern .
  ?workflowPattern :hasWorkflowStep ?workflowStep .
  ?workflowStep  :hasAssociatedTask ?task ;
                 :performedBy ?agent;
                 :nextStep ?nextWorkflowStep .
  ?agent :hasTask ?task ;
         :hasGoal ?goal ;
         :usesTool ?tool .
} 
WHERE {
  ?team :hasAgentMember ?agent ; 
        :hasObjective ?objective ;
        :hasWorkflowPattern ?workflowPattern .
  ?agent :hasTask ?task ; 
         :hasGoal ?goal .

  OPTIONAL {
    ?workflowPattern :hasWorkflowStep ?workflowStep .
    ?workflowStep :hasAssociatedTask ?task ;
                  :performedBy ?agent ; 
                  :nextStep ?nextWorkflowStep .
  }

  OPTIONAL { ?agent :usesTool ?tool . }
  OPTIONAL { ?agent :usesResource ?resource . }
  OPTIONAL { ?tool :accessesResource ?resource . }

  FILTER (regex(str(?objective), "Travel", "i"))
}
```
## License

The Ontology is developed by Kabul Kurniawan and team and released under the [MIT license](http://opensource.org/licenses/MIT). 

