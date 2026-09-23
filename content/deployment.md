---
title: Self-hosting and data control.
description: Choose where SHADO runs, which models it uses and which services it can reach.
eyebrow: DEPLOYMENT & DATA CONTROL
---
## The local deployment path

For work that needs to stay within an organization, deploy the SHADO server and local models on infrastructure you control. Connect the dashboard, mobile companion and other supported clients to that server.

**Your client → your SHADO server → your local model and configured tools.**

This is a deployment choice, not an automatic guarantee that every feature runs offline. Search, external model providers and connected applications can create additional data paths.

## Choose the right setup

| Setup | How it works | What to evaluate |
|---|---|---|
| Local models | Inference runs on the compute available to your deployment. | Model capability, memory, GPU capacity and concurrency. |
| Optional cloud models | Requests go to an enabled external provider. | What data is sent, provider terms, credentials and API costs. |
| Connected tools and apps | SHADO calls services configured for the selected task. | Access permissions, information shared and action scope. |
| Desktop and device bridges | The agent interacts with an authorized target environment. | Device access, isolation, application permissions and supervision. |

## What you need

A deployment requires a suitable host, storage, network connectivity for the intended clients, and sufficient compute for the selected models. GPU memory and performance needs vary substantially with model size and workload; there is no single hardware specification for every deployment.

Prepare:

1. The first workflow you want to evaluate.
2. The models and languages it needs.
3. The number of people and simultaneous tasks it should support.
4. The files, applications and devices it may access.
5. The network boundary and external services it may use.
6. The people responsible for operation, updates and support.

## Follow the information

A local model can process a request on your infrastructure. An external AI provider receives the content included in requests sent to it. Search services receive search queries; connected file and communication services receive the information needed for their operations.

Voice processing can use different engines depending on configuration. Review speech input, transcription and read-aloud settings alongside your model settings.

The [Privacy Policy](/privacy/) explains the distinction between this public website, communication with the creator and a configured SHADO deployment.

## Government and enterprise evaluation

For an agency that restricts public cloud AI, the evaluation starts with local inference and a review of every connected service. Role presets select agent behavior and tools; they should not be treated as an enterprise employee-permission system.

Start with a bounded internal workflow, such as drafting from approved documents or preparing a research summary. Use representative information that is authorized for the evaluation.

Assess access controls, logging, retention, backup, human review and the behavior of enabled tools in the actual deployment. Self-hosting alone does not establish regulatory compliance or organizational approval.

SHADO is an independently developed platform. The use cases on this website describe opportunities for evaluation, not government endorsements or certified deployments.

## Operating costs and responsibilities

Local inference can avoid a cloud provider's per-request charge for that inference. Hardware, electricity, administration, networking and maintenance still have costs. Optional cloud APIs and other services may have separate fees.

Your organization supplies the accounts and credentials needed for its chosen integrations. Installation, access and ongoing operation should be agreed for the specific deployment.

## Start with a demonstration

Describe the workflow, expected users and deployment boundary. We can discuss what is available today, which components need configuration and what should be tested before adoption.

Contact {{< contact >}} to arrange a demonstration.
