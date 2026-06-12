# appendix/prototype/prototype_llm_agent.py

```python
"""
prototype_llm_agent.py

Optional prototype demonstrating how an LLM API might generate structured
journal-entry candidates.

This file is intentionally minimal.

It is not required for the whitepaper workflow.
The same structure may be produced manually through ChatGPT, a local LLM,
another API, or any other receipt-processing workflow.

Important:
- Do not upload unmasked sensitive information.
- Do not treat LLM output as a final tax decision.
- Always preserve original evidence separately.
"""

from __future__ import annotations

import os

from dotenv import load_dotenv
from openai import OpenAI

from prototype_schema import JournalEntryCandidate


SYSTEM_PROMPT = """
You are an LLM assistant supporting small business accounting preparation.

You are not a tax accountant.
You do not make final tax decisions.
You generate journal-entry candidates, descriptions, audit_logs, and review flags.

Rules:
1. Do not invent information that is not provided.
2. If information is unclear, mark it as needs_review.
3. If a value is estimated, explicitly state that it is estimated.
4. Separate tax-included amount, tax-excluded amount, and tax amount where possible.
5. Generate an audit_log explaining business purpose, account reasoning, payment route, and unresolved issues.
6. The output is a candidate for review, not a final accounting or tax conclusion.
"""


class PrototypeLLMAgent:
    """
    Minimal LLM agent for generating structured journal-entry candidates.

    This class is optional and only demonstrates one possible implementation.
    """

    def __init__(self, model: str = "gpt-4o-mini"):
        load_dotenv()
        api_key = os.environ.get("OPENAI_API_KEY")

        if not api_key:
            raise RuntimeError(
                "OPENAI_API_KEY is not set. "
                "Create a .env file or set the environment variable."
            )

        self.client = OpenAI(api_key=api_key)
        self.model = model

    def process_transaction_memo(self, memo: str) -> JournalEntryCandidate:
        """
        Generate a structured journal-entry candidate from a transaction memo.

        Parameters
        ----------
        memo:
            Text memo describing the transaction.
            In the full workflow, this may be produced from OCR + user purpose description.

        Returns
        -------
        JournalEntryCandidate
            Structured journal-entry candidate.
        """
        if not memo or not memo.strip():
            raise ValueError("memo must not be empty.")

        response = self.client.beta.chat.completions.parse(
            model=self.model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": (
                        "Generate a journal-entry candidate from the following transaction memo. "
                        "Return structured data only.\n\n"
                        f"{memo}"
                    ),
                },
            ],
            response_format=JournalEntryCandidate,
        )

        parsed = response.choices[0].message.parsed

        if parsed is None:
            raise RuntimeError("The LLM response could not be parsed.")

        return parsed


if __name__ == "__main__":
    agent = PrototypeLLMAgent()

    sample_memo = """
    Date: 2026-04-15
    Vendor: Example Electronics
    Amount: 55,000 JPY including tax
    Purpose: Business-use PC monitor for development work
    Payment: Paid by representative's personal credit card as a temporary advance
    Evidence: Paper receipt saved in 2026_FiscalYear/04/01_original/
    """

    entry = agent.process_transaction_memo(sample_memo)

    print(entry.model_dump_json(indent=2, ensure_ascii=False))
```
