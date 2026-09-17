# Deep Research Agent

一个基于 DeepSeek API 从零实现的多阶段 Research Agent。

本项目没有一开始直接依赖 LangChain / LangGraph，
而是从底层 Agent Loop 和 Tool Calling 开始实现，
逐步加入 Planning、Tool Registry、Reflection 和 Web Research，
用于理解现代 AI Agent 的核心工作机制。

## Features

- DeepSeek Tool Calling
- Agent Loop
- Tool Registry
- Web Search
- Webpage Reading
- Planner
- Executor
- Reviewer / Reflection
- Retry Mechanism
- Research Report Generation

## Architecture

User
  ↓
Planner
  ↓
Executor
  ↓
Tools
  ↓
Reviewer
 ↙     ↘
Retry   Pass
         ↓
      Reporter
         ↓
    Final Report

## Tech Stack

Python
DeepSeek API
OpenAI SDK
DDGS
Requests
BeautifulSoup


