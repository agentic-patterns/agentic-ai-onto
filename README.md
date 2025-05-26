# Agentic Ontology

This repository contains the **Agentic Ontology (AgentO)**, a formal semantic model for representing agents, their capabilities, interactions, and execution structures (e.g., Agents, tasks, goal  and workflow patterns). The ontology is designed to support research and applications in agentic AI.

## 🌐 Ontology Overview

The ontology provides a structured vocabulary to represent:

- **Agents**: Entities capable of performing actions with autonomy.
- **Workflow**: Sequences or networks of actions or tasks, possibly with control flow (sequential, parallel, conditional).
- **Tasks & Tools**: Executable components that make up a plan, etc.

The model is suitable for integration with knowledge graphs, semantic reasoning engines, and agent-based modeling tools.

## 🧪 Example Use

You can execute queries against the ontology via this public SPARQL endpoint:

👉 SPARQL Endpoint: https://w3id.org/agentic-ai/sparql

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

