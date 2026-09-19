# TechRadar V1 — Product Requirements

## Goal

Build the first usable version of TechRadar: a personal daily technology edition that collects, selects and explains the most relevant things worth knowing each day.

The goal of V1 is not to provide an endless news feed.

Instead, TechRadar should create one finite Daily Edition that can be consumed in approximately 10–15 minutes.

## Target User

V1 has a single user: me.
Authentication, user accounts and multi-user personalization are intentionally excluded from V1.

## Daily Edition

Each Daily Edition contains:

### Top Story
One technology story selected as the most interesting or important story of the day.

### Tech News
Four additional technology stories relevant to software engineering, AI/ML, infrastructure and the broader technology industry.

### Startup Radar
Three interesting startup-related stories or companies worth discovering.

### Today I Learned
One software engineering or Computer Science concept to learn.

Examples:

- CI/CD
- Kubernetes
- Redis
- Kafka
- Observability
- Distributed Systems
- RAG
- Vector Databases

### Daily Coding
One coding interview problem with:

- Title
- Difficulty
- Topic
- Link
- Completion status

## Daily Feedback

The user can provide feedback on each Daily Edition and its individual items.

Feedback may include:

- Like / dislike an item
- Save an item
- Mark a concept as too easy or too difficult
- Add free-text feedback about the edition

Example feedback:

> "Too much business news today. I want more technical stories."

> "I already understand Docker basics. Show me more advanced infrastructure concepts."

> "More startups like this one."

The system should store this feedback and use it to gradually improve future Daily Editions.

In V1, feedback will primarily be collected and stored.

Future versions may use an LLM to extract preferences from free-text feedback and update a user preference profile that influences ranking and content selection.

## Content Pipeline

The system should transform raw information into a curated Daily Edition.

High-level pipeline:
Collect → Normalize → Deduplicate → Classify → Rank → Enrich → Store → Display

## Article Enrichment

Selected articles should include:
- Original title
- Original source
- Link to original content
- Short summary
- Why it matters
- Technical context
- Category

## Product Principles

### Finite by design

TechRadar should not use infinite scrolling.

The product should answer:

"What is worth knowing today?"

### Original sources first

TechRadar should always preserve and link to the original source.

### AI enhances the system

LLMs may help summarize, classify and explain content, but they should not be the source of the news itself.

### Store processed results

Opening TechRadar should not require regenerating content with an LLM.

The Daily Edition should be generated beforehand and stored in the database.

## Out of Scope for V1

The following are intentionally excluded from V1:

- User accounts
- Social features
- Mobile application
- Infinite feed
- Complex recommendation models
- Kubernetes deployment
- Native notifications
- Multiple personalized users