# LibreOne

**One unified AI workspace. One conversation. Every artifact, model, tool, and workflow.**

LibreOne is a unified, multimodal AI workspace concept designed to bring chat, knowledge, office files, software tools, business applications, and autonomous workflows into one conversational environment.

Instead of treating chat, documents, spreadsheets, presentations, code, and enterprise systems as separate destinations, LibreOne aims to let people work across them from a single place: ask, analyze, create, edit, execute, collaborate, and follow through.

> **A single conversation can become an end-to-end piece of work:** understand source files, analyze data, generate an Excel model, prepare a PowerPoint, write a DOCX report, update a knowledge workspace, create engineering tasks, and prepare communications—with permissions, approvals, and evidence at each step.

---

## Product vision

LibreOne brings together six connected experiences:

1. **One chat** — a persistent conversational workspace for people, teams, projects, and agents.
2. **Every modality** — text, documents, images, audio, video, and structured data.
3. **Every model** — a gateway to hosted and locally operated AI models.
4. **Every capability** — tools, MCP servers, APIs, connectors, code execution, and agents.
5. **Every artifact** — create, read, analyze, transform, and edit common work formats.
6. **One governed execution layer** — identity, policy, privacy, approvals, observability, and audit.

## Universal chat and workspace

LibreOne is intended to make the conversation the common entry point for work.

- Conversations, threads, projects, and workspaces
- File upload and contextual file understanding
- Multimodal prompts and responses
- Search across connected and uploaded content
- Artifact previews and editing workflows
- Tool and agent activity visible in the conversation
- Human review, approval, and continuation of work
- Results linked to their source material and execution evidence

## Multimodal understanding

The product scope includes working with:

- **Text:** questions, instructions, long-form content, and structured prompts
- **Documents:** PDF, DOCX, Markdown, TXT, and other common text formats
- **Spreadsheets:** XLSX, CSV, tabular data, and formulas
- **Presentations:** PPTX, slides, diagrams, and speaker notes
- **Images:** image understanding, visual analysis, and image generation workflows
- **Audio:** speech input, transcription, and audio understanding
- **Video:** video input, transcription, summaries, and visual understanding
- **Structured data:** JSON, XML, YAML, and database records
- **Engineering content:** source code, repositories, diffs, logs, and notebooks

Actual support depends on the selected model, enabled tools, and available file-processing components.

## Local and cloud AI gateway

LibreOne is designed around a common gateway for model access, rather than binding the workspace to a single provider.

The intended gateway responsibilities include:

- A consistent interface for hosted and local models
- Provider and model configuration
- Routing by task, capability, privacy requirement, latency, and cost
- Local, on-premises, edge, and cloud inference targets
- Model-specific capability awareness, including vision, audio, and code
- Authentication, quotas, usage accounting, and request controls
- Fallback and provider error handling where configured

The objective is to let a user work through one interface while model selection and execution are governed centrally.

## AI data washing and privacy gateway

**AI data washing** is the privacy and data-preparation layer between user content and model execution.

Its intended pipeline is:

`Source data → inspect → classify → transform → apply policy → route → process → restore permitted output → record evidence`

Potential controls include:

- Detection and classification of personal, confidential, regulated, and secret information
- Redaction, masking, tokenization, and pseudonymization
- Policy-based decisions about local versus external processing
- Data minimization and selective context sharing
- Credential and secret detection
- Controlled reconstruction of tokenized values where authorized
- Audit records describing what was transformed and where data was sent

Data washing must be policy-driven and reversible only where explicitly authorized. It is not a substitute for access control, legal review, or data-loss-prevention controls.

## Agents and orchestration

LibreOne's intended agent platform encompasses:

- Agent identity, registry, configuration, and lifecycle
- Goals, context, sessions, planning, and execution
- Tools, skills, and capability discovery
- Delegation and multi-agent coordination
- Foreground and background execution
- Durable workflows, checkpoints, retries, and recovery
- Human-in-the-loop review, approval, and escalation
- Cancellation, timeouts, and execution limits
- Verification of results and auditable execution history

Agent autonomy is bounded by the identity, permissions, policies, and approvals applicable to each task.

## Universal artifact workspace

LibreOne aims to work directly with the formats people use every day.

| Work area | Formats and content |
|---|---|
| Documents | DOCX, PDF, Markdown, TXT, RTF |
| Spreadsheets | XLSX, CSV, tabular data |
| Presentations | PPTX, slide content |
| Knowledge | Notion-style pages, wikis, knowledge bases |
| Structured data | JSON, XML, YAML |
| Software | Git repositories, source code, issues, pull requests, notebooks |
| Visuals | Images, diagrams, screenshots, whiteboards |
| Audio and video | Audio files, video files, transcripts, subtitles |
| Communications | Email, chat, collaboration messages |
| Enterprise data | CRM, ERP, SAP, databases, and business APIs |

The goal is more than file upload: users should be able to ask LibreOne to interpret, create, transform, compare, and update artifacts through authorized operations.

## Tools, connectors, and MCP

LibreOne is intended to connect the conversation to external systems through governed capabilities:

- MCP servers and tools
- REST APIs and application functions
- File stores and cloud drives
- GitHub and GitLab
- Knowledge and collaboration platforms
- Databases and data warehouses
- CRM, ERP, and enterprise systems
- Email and messaging platforms
- Web research and browser-based sources
- Local applications and execution environments

Connector access should be explicit, scoped, and auditable. Availability depends on configured integrations and granted credentials.

## Secure execution environment

For code and operational tasks, the intended execution layer includes:

- Language runtimes and notebooks
- File and data processing
- Isolated processes or containers
- CPU, memory, disk, and time limits
- Network access controls
- Secret isolation
- Execution cancellation and failure handling
- Persistent state only where deliberately enabled
- Logs and traceable execution results

Execution environments must not be treated as trusted merely because an agent requested the operation.

## Knowledge, memory, and evidence

LibreOne's product scope includes contextual knowledge across conversations and work:

- Conversation and session context
- Task and project memory
- Long-term user or workspace knowledge, where enabled
- Document indexing and retrieval
- Lexical and semantic search
- Vector and graph-based retrieval where configured
- Metadata, access filtering, and source provenance
- Citations and evidence attached to generated results
- Retention, deletion, and synchronization controls

Retrieved information should respect the permissions of the user and the connected source.

## Enterprise governance

The intended enterprise foundation includes:

- User authentication and enterprise identity integration
- Role- and policy-based authorization
- Workspace and tenant separation
- Permission-aware retrieval and connector access
- Secrets and credential management
- Data handling and residency policies
- Approval and escalation workflows
- Usage limits and resource controls
- Audit trails and administrative controls

Tenant isolation and security boundaries must be enforced in the backend and data layer, not just represented in the user interface.

## Observability and evaluation

A production deployment should be able to inspect the behavior and performance of models, agents, tools, and workflows.

The scope includes:

- Model, agent, and tool traces
- Request latency, errors, and throughput
- Token and cost accounting
- Workflow and agent execution history
- Evaluation datasets and quality checks
- User feedback and outcome measurement
- Operational dashboards and alerting
- Privacy-aware analytics and retention

ClickHouse and Langfuse are possible components in this area; their use is deployment-dependent and should not be inferred from this product description.

## Example: one conversation, an entire workflow

A user provides several project documents and asks:

1. Read and compare the source PDFs and spreadsheets.
2. Identify discrepancies and explain the evidence.
3. Build an Excel analysis with formulas and charts.
4. Create a PowerPoint for stakeholders.
5. Write a detailed DOCX report.
6. Update the project knowledge space.
7. Create GitHub or project-management tasks for unresolved items.
8. Prepare an email or Teams summary for review.

LibreOne's goal is to coordinate that work through one conversation, while applying the user's access rights, data policies, approvals, and execution controls at each stage.

## Architecture at a glance

`User / Team`
→ `Unified Chat & Workspace`
→ `Multimodal Ingestion`
→ `Context, Knowledge & Memory`
→ `Privacy / AI Data Washing Gateway`
→ `Local + Cloud Model Gateway`
→ `Agent & Capability Orchestration`
→ `Policy / Approval Controls`
→ `Tools, MCP, Connectors & Sandboxed Execution`
→ `Artifacts, Results & Evidence`

Cross-cutting services include identity, tenant isolation, secrets, audit, observability, evaluation, and deployment operations.

## Project status and implementation accuracy

This README describes **LibreOne's product direction and intended scope**. It is not a declaration that every listed capability is already implemented, production-ready, or enabled in this repository.

Implementation status must be established from source code, tests, configuration, deployment manifests, and runtime verification. In particular, terms such as *durable execution*, *self-healing*, *stateful code execution*, *tenant isolation*, *AI data washing*, and *MCP security* require demonstrable enforcement and behavior—not just configuration names, diagrams, or documentation.

## Design principles

- **One workspace, not another collection of disconnected applications.**
- **Model-independent:** route work to the model that fits the task and policy.
- **Local-first when required:** preserve on-premises and local inference options.
- **Privacy before inference:** inspect and govern data before external processing.
- **Capabilities over ad hoc integrations:** expose tools through consistent, permissioned interfaces.
- **Human control:** approvals and escalation for consequential operations.
- **Evidence by default:** retain source references and execution history.
- **Open and extensible:** support models, tools, connectors, runtimes, and deployment environments.
- **Honest implementation claims:** distinguish product vision from verified functionality.

## Contributing

Contributions, issue reports, and technical discussions are welcome. Please include reproducible steps, relevant logs, expected behavior, and environment details when reporting defects.

Before contributing, review the repository's contribution and security guidance if present.

## License

The repository license governs use, modification, and distribution. If no license file is present, all rights remain with the copyright holder; do not assume the code is open source.

---

**LibreOne — one chat for work across models, files, tools, agents, and enterprise systems.**
