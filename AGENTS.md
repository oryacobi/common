🧠 Agent Operating Instructions

This repository supports autonomous development by AI agents (Codex, Opcode, Cursor-Agents, etc.).
This file defines how agents must behave, the architecture rules, task execution protocol, and constraints required to keep development stable, predictable, and maintainable.

Agents must treat this file as a strict contract.


---

1. 📌 Project Purpose

This repository (oryacobi/common) contains foundational building blocks for a larger system, including:

statistical models

time-series forecasting

portfolio optimization

data ingestion pipelines

shared utilities and infrastructure

CI/CD workflows

shared backend logic used across multiple services


It does not contain the final “application product.”
It is a common library used by multiple future agents and services.


---

2. 🏛️ Architecture Principles (Clean Architecture)

Agents must always follow Clean Architecture.

2.1 Layers

Domain

Pure business rules

Entities, Value Objects

No external imports beyond Python stdlib


Use Cases / Application

Orchestrates domain operations

Stateless

Only depends on Domain


Interfaces (Ports)

Abstract repositories

External service interfaces

No external implementations


Adapters (Infrastructure)

Implement repository interfaces

Handle I/O, DB access, external APIs

No business logic


Entry Points

CLI / REST / workers

Only import Use Cases



2.2 Rules

No circular dependencies

Domain must not depend on infrastructure

Everything must be testable

Prefer small modules (≈ ≤ 200 lines when reasonable)

Clear separation between “pure logic” and “side effects”



---

3. 📦 Repository Rules for Agents

3.1 Creating New Modules

Agents must:

create the smallest possible unit of functionality

keep code atomic and well-contained

include tests for new logic

add docstrings where appropriate

update documentation if behavior or public APIs change

avoid introducing new dependencies without clear justification


3.2 Modifying Existing Modules

Agents must:

preserve backwards compatibility unless explicitly instructed otherwise

avoid modifying architecture boundaries

avoid refactoring unrelated areas in the same change

keep changes localized to the relevant feature

leave clear, descriptive commit messages


3.3 Commit & PR Rules

Small, incremental, reviewable changes

Each commit should correspond to one atomic task

Avoid large cross-cutting refactors in a single PR

PRs must include:

a short summary

a description of what changed and why

migration notes if interfaces or behavior changed




---

4. 🔧 CI/CD & Local Quality Requirements

4.1 CI/CD Expectations

Agents must ensure:

GitHub Actions workflows remain green

All tests pass in CI

No secrets are committed

Linting remains clean

CI configuration is changed carefully and intentionally


At this stage, CI should at minimum:

verify Python version

install dependencies

run tests

run formatting/lint checks


4.2 Mandatory Local Checks Before Finalising a Task

Before an agent marks a task as complete, opens a PR, or considers work “done”, it must run all of the following in the environment:

1. Code formatting with Black

Always check your formatting with Black before finalising your task.

Example (conventional, not mandatory command name):

black .



2. Import ordering with isort

Check isort on the environment before finalising your task.

Example:

isort .



3. Unit tests

Always run the unit tests in the environment before finalising your task.

Example:

pytest




Agents must not consider their work complete, nor open a PR, if:

Black fails or changes files

isort fails or changes files

any unit test fails


In such cases, the agent must fix the issues and re-run these checks until they pass.


---

5. 📐 Coding Standards

5.1 Style

Follow PEP8

Use type hints everywhere (functions, methods, public attributes)

Use dataclasses or Pydantic models where appropriate

Prefer explicit, readable code over “clever” constructs

Keep functions cohesive and focused


5.2 Testing

Every new module should have a corresponding test module

Use pytest

Tests must not depend directly on external services (DBs, APIs, networks)

Use mocks, fakes, or fixtures for I/O and external dependencies


5.3 Error Handling

Prefer custom error types in the domain/use-case layers

Avoid raising bare Exception or overly generic errors

Do not silently swallow errors



---

6. 🧩 Task Execution Rules for Agents

Agents must follow a strict task loop.

6.1 Planning

Break high-level tasks into small, granular subtasks

For non-trivial work, formulate a brief internal plan before editing code

When ambiguity is high and cannot be resolved from the repo, request clarification


6.2 Execution

Implement the minimum necessary changes to satisfy the task

Keep logic deterministic and testable

Respect architecture boundaries at all times

Reuse existing patterns and abstractions when possible


6.3 Validation

Before considering a task complete, agents must:

Run Black, isort, and unit tests as described in §4.2

Ensure no unused imports or obvious dead code

Ensure type hints are consistent and pass basic static checks (e.g. mypy, if configured)

Ensure public interfaces remain documented


6.4 Output

When finishing a task, agents should produce a short summary including:

What was implemented or changed

Which files were modified

Which tests were added or updated

Any follow-up or TODOs that should be considered next



---

7. 🚫 Prohibited Actions

Agents must not:

introduce broad refactors unrelated to the current task

bypass architecture layers to “shortcut” access (e.g. domain calling infra)

commit or open PRs without running Black, isort, and tests

add new external libraries casually or redundantly

delete public APIs or modules unless explicitly instructed

weaken tests or comment them out to “make CI green”

generate large, monolithic files that mix multiple concerns

merge changes that break CI/CD



---

8. 🔍 Decision Guidance

When uncertain, agents should prefer:

Simplicity over complexity

Predictability over cleverness

Separation of concerns over convenience

Pure logic + tests over implicit behavior

Explicit boundaries over hidden couplings


If a choice risks architecture integrity or testability → stop and seek clarification.


---

9. 🧭 Long-Term Roadmap (Guiding Direction)

Development should gradually move toward:

1. A strong shared utilities and common tools layer


2. Reusable domain models for forecasting and portfolio operations


3. Robust ingestion & ETL primitives for time-series and metadata


4. Simulation and backtesting modules


5. Messaging/event abstractions for later integration


6. Infrastructure adapters to external DBs/APIs (added incrementally)


7. Clean interfaces for the main application(s) to consume


8. A comprehensive test suite and reliable CI/CD



Each step should be small, testable, and valuable on its own.


---

10. 🤖 Multi-Agent Protocol

If multiple agents are involved:

Planner Agent: breaks work into subtasks, prioritizes them

Executor Agent: implements code according to this file

Reviewer Agent: checks architecture, tests, and formatting (Black + isort)

Coordinator Agent: only merges when CI/CD passes and checks are satisfied


All agents must treat this document as the source of truth for behavior in this repo.


---

11. 🏁 Final Note

This repository is a precision foundation for a broader system.
Agents must operate deliberately, safely, and with strict adherence to:

Clean Architecture

Black formatting

isort import ordering

Comprehensive unit testing

Small, incremental, well-tested changes


This file overrides any default or generic agent behavior when working in oryacobi/common.
