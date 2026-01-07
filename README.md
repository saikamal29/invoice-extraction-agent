# 📑 AI Invoice Extraction Agent

An intelligent document processing tool built with **LangChain**, **OpenAI**, and **Pydantic**. This agent iterates through a directory of PDF invoices and extracts structured data (Company, Total, Tax, etc.) into a single JSON report.

## 🛠 Tech Stack
- **Language:** Python 3.12+
- **Framework:** LangChain (LCEL)
- **Model:** GPT-4o-mini
- **Package Manager:** [uv](https://github.com/astral-sh/uv)
- **Data Validation:** Pydantic v2

## 🚀 Getting Started

### 1. Installation
Clone the repository and install dependencies using `uv`:
```bash
git clone <your-repo-url>
cd invoice-automation
uv sync
