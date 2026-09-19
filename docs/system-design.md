# TechRadar — System Design

## Overview

TechRadar generates a curated Daily Edition from multiple external technology sources.

The system collects raw content, converts it into a common internal format, removes duplicates, ranks relevant items, enriches selected content using an LLM, and stores the finished edition for later consumption.

## High-Level Architecture

External Sources
→ Collectors
→ Normalization
→ Deduplication
→ Ranking
→ LLM Enrichment
→ PostgreSQL
→ FastAPI
→ React

User feedback is stored and can later influence the ranking process.

## Main Components

### Collectors

Responsible for retrieving content from external sources.

Each source may expose data differently, so every source will have its own collector.

### Normalization

Transforms content from different sources into a common internal data model.

### Deduplication

Prevents the same story from appearing multiple times when it is discovered through different sources.

V1 should begin with simple deterministic approaches before introducing semantic or embedding-based deduplication.

### Ranking

Scores candidate content and selects the items that will appear in the Daily Edition.

Possible ranking signals include:

- Freshness
- Relevance
- Importance
- Technical learning value
- User preferences

### LLM Enrichment

The LLM operates on selected content rather than acting as the original information source.

Possible tasks:

- Summarization
- Categorization
- "Why it matters"
- Technical context

### Database

PostgreSQL stores both raw and processed application data.

Possible entities include:

- Articles
- Startups
- Daily Editions
- Edition Items
- Concepts
- Coding Problems
- Feedback

### Backend API

FastAPI exposes the application data to the frontend and handles user actions.

Example endpoints:

GET /api/editions/today

POST /api/feedback

### Frontend

React provides the Daily Edition interface and allows the user to interact with content and provide feedback.

### Daily Generation

A background process generates the Daily Edition.

During early development this process may be triggered manually.

A scheduler can later generate the edition automatically every morning.

## V1 Engineering Principle

Prefer the simplest implementation that allows the complete system to work end-to-end.

Infrastructure should be introduced when the system has a concrete need for it, rather than only to increase the number of technologies used by the project.