# Document QA RAG Assistant

## Overview

The Document QA RAG Assistant is a retrieval-augmented generation application that allows users to upload operational documents and ask questions against their contents.

The system retrieves relevant document evidence before generating an answer, helping reduce unsupported or hallucinated responses.

## V1 Objective

A user must be able to upload one or more operational documents, ask a question, and receive an answer grounded exclusively in retrieved document evidence.

The response should include:

- Answer
- Supporting source
- Document or section citation
- Grounding indicator
- Insufficient-evidence response when the documents do not support an answer

## Initial Supported File Types

- PDF
- DOCX
- TXT

## Planned Stack

- Python
- Streamlit
- OpenAI API
- OpenAI Embeddings
- ChromaDB
- PyMuPDF
- python-docx

## V1 Success Criteria

- Documents can be uploaded and processed
- Text can be chunked and indexed
- Relevant evidence can be retrieved
- Questions generate grounded answers
- Sources are displayed with answers
- Unsupported questions return an insufficient-evidence response
- Controlled test cases validate retrieval and answer quality
