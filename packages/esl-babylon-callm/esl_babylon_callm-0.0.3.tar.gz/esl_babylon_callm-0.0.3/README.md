# ESL-Babylon-CaLLM library

## Description

This Python library provides a class-based structures and tooling for developers to generate conversational models with
OpenAI GPT3, including the Legen Language Model (LLM). It uses OpenAI, Azure Chat, SQLalchemy, Pydantic, and Numpy
libraries. It provides a convenient, high-level interface for creating and managing conversation threads with AI models
in an organized, modular, and scalable manner.

Key features include conversation request structuring, conversation memory management, prompt templates management,
logging, error handling and the abstraction of many lower level tasks involved in generating and managing text-based AI
interactions with Azure Chat and OpenAI models.

**Note:** This library assumes you have a working knowledge of Python development and interaction with conversational AI
APIs.

## Prerequisites

Before you start, make sure you have the following software installed:

- Python 3.11.5: Download and install it from the official website (https://www.python.org/downloads/).

## Installation

1. pip
   ```bash
   pip install esl-babylon-callm
   ```

2. poetry
   ```bash
   poetry add esl-babylon-callm
   ```

## Usage

```python
from esl_babylon_callm.callm import ChatRequest, CaLLM
```

#### Disclaimer

This library is not officially affiliated with, endorsed by, or directly connected with OpenAI or any of the other
libraries used.


