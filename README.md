# Inverkids_RAG_System

This service allows a Large Language Model (LLM) to **safely retrieve structured and unstructured data** without ever generating SQL or accessing the database directly.
The LLM selects from a **whitelisted set of tools**, while all execution logic remains under backend control.

## Core Concepts

- **Agentic RAG**:
  The LLM decides _what to do_, not _how to do it_.
- **Tool / Function Calling**:
  The LLM can only invoke pre-approved backend functions.
- **SQL Safety**:
  All queries are predefined, parameterized, and version-controlled.
- **Lambda-Oriented Design**:
  Stateless execution, fast cold starts, and least-privilege IAM.

## Architecture Overview

<pre class="overflow-visible! px-0!" data-start="1252" data-end="1466"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>User</span><span> Request
     ↓
API Gateway
     ↓
Lambda </span><span>Handler</span><span>
     ↓
LLM (tool calling)
     ↓
Tool Router
     ↓
Query / RAG Layer
     ↓
PostgreSQL (pgvector)
     ↓
LLM (response formatting)
     ↓
</span><span>User</span><span> Response
</span></span></code></div></div></pre>

**Important**:
The LLM never generates SQL and never connects to the database.

## Project Structure

<pre class="overflow-visible! px-0!" data-start="1580" data-end="3125"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>rag-agent/
│
├── src/
│   ├── app/
│   │   ├── handler.py            </span><span># Lambda entrypoint</span><span>
│   │   ├── router.py             </span><span># Tool-call routing</span><span>
│   │   ├── validator.py          </span><span># Input & permission validation</span><span>
│   │   └── context_builder.py    </span><span># Builds RAG context</span><span>
│   │
│   ├── llm/
│   │   ├── client.py             </span><span># LLM client abstraction</span><span>
│   │   ├── tools.py              </span><span># Tool definitions (schemas)</span><span>
│   │   └── prompts/
│   │       ├── system.txt
│   │       ├── intent.txt
│   │       └── formatter.txt
│   │
│   ├── db/
│   │   ├── connection.py         </span><span># PostgreSQL connection</span><span>
│   │   ├── embeddings.py         </span><span># pgvector helpers</span><span>
│   │   └── queries/
│   │       ├── activities.py
│   │       ├── texts.py
│   │       └── analytics.py
│   │
│   ├── rag/
│   │   ├── retriever.py          </span><span># Vector + metadata retrieval</span><span>
│   │   ├── ranker.py             </span><span># Optional re-ranking</span><span>
│   │   └── filters.py            </span><span># Level / topic constraints</span><span>
│   │
│   ├── security/
│   │   ├── auth.py               </span><span># Authorization logic</span><span>
│   │   └── policies.py           </span><span># Tool access rules</span><span>
│   │
│   ├── utils/
│   │   ├── logger.py
│   │   ├── errors.py
│   │   └── timing.py
│   │
│   └── config/
│       ├── settings.py           </span><span># Environment config</span><span>
│       └── constants.py
│
├── tests/
│   ├── test_router.py
│   ├── test_queries.py
│   ├── test_rag.py
│   └── test_handler.py
│
├── requirements.txt
├── README.md
└── infrastructure/
    ├── sam.yaml                  </span><span># AWS SAM template</span><span>
    └── iam.json                  </span><span># Least-privilege IAM</span><span>
</span></span></code></div></div></pre>

## Design Principles Applied

### Clean Architecture

- **LLM logic ≠ business logic**
- **Routing ≠ execution**
- **Retrieval ≠ formatting**

### SOLID

- **S**ingle responsibility per module
- **O**pen for extension (new tools)
- **L**iskov-safe function contracts
- **I**nterface segregation (LLM client abstraction)
- **D**ependency inversion (no hard LLM dependency)

## Security Model

| Risk                 | Mitigation              |
| -------------------- | ----------------------- |
| SQL injection        | No SQL from LLM         |
| Prompt injection     | Tool allowlisting       |
| Over-fetching        | Parameter validation    |
| Privilege escalation | IAM + policy checks     |
| Data leakage         | Explicit tool contracts |

## Dependencies

### Python Version

<pre class="overflow-visible! px-0!" data-start="3820" data-end="3864"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>Python </span><span>3.11</span><span> (recommended </span><span>for</span><span> </span><span>Lambda</span><span>)
</span></span></code></div></div></pre>

### Runtime Dependencies

`requirements.txt`:

<pre class="overflow-visible! px-0!" data-start="3912" data-end="3990"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-txt"><span><span>openai>=1.0.0
psycopg2-binary>=2.9
python-dotenv>=1.0
pydantic>=2.0
</span></span></code></div></div></pre>

Optional (recommended for production):

<pre class="overflow-visible! px-0!" data-start="4031" data-end="4057"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-txt"><span><span>boto3
structlog
</span></span></code></div></div></pre>

## Environment Variables

All configuration is **environment-based**, compatible with Lambda:

<pre class="overflow-visible! px-0!" data-start="4162" data-end="4257"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>OPENAI_API_KEY=...
DB_HOST=...
DB_NAME=...
DB_USER=...
DB_PASSWORD=...
DB_PORT=5432
</span></span></code></div></div></pre>

> Use **AWS Secrets Manager** in production.

## Running Locally (Simulation)

<pre class="overflow-visible! px-0!" data-start="4346" data-end="4434"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python -m venv venv
</span><span>source</span><span> venv/bin/activate
pip install -r requirements.txt
</span></span></code></div></div></pre>

<pre class="overflow-visible! px-0!" data-start="4436" data-end="4565"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>from</span><span> src.app.handler </span><span>import</span><span> handler

</span><span>print</span><span>(handler({
    </span><span>"prompt"</span><span>: </span><span>"Get texts for level 3 math fractions"</span><span>
}, </span><span>None</span><span>))
</span></span></code></div></div></pre>

## Deploying to AWS Lambda

### 1. Package

<pre class="overflow-visible! px-0!" data-start="4618" data-end="4659"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>sam build
sam deploy --guided
</span></span></code></div></div></pre>

### 2. Recommended AWS Services

- API Gateway (HTTP API)
- Lambda (Python 3.11)
- RDS Postgres + pgvector
- RDS Proxy
- Secrets Manager
- CloudWatch Logs

## Testing Strategy

- **Unit tests**: tools, queries, routing
- **Integration tests**: Postgres + pgvector
- **Contract tests**: LLM tool schemas
- **Security tests**: invalid tool calls

## Extending the System

To add a new capability:

1. Define a new tool in `llm/tools.py`
2. Implement logic in `db/queries/`
3. Register tool → function mapping in `router.py`
4. Add tests

No changes to the LLM prompt logic required.

## Summary

This project is:

- **LLM-driven but backend-controlled**
- **Safe by design**
- **Cloud-native**
- **Extensible**
- **Production-ready**

It follows patterns used in **real-world agentic systems** deployed at scale.
