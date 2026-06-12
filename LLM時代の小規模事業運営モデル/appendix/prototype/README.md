# appendix/prototype/README.md

## Prototype Code

This directory contains prototype code related to the whitepaper:

**LLM時代の小規模事業運営モデル**

The main purpose of this repository is not to provide accounting software.

The main purpose is to present:

* a whitepaper on small business operation in the LLM era;
* a practical case study of completing a first corporate tax return without accounting software or a tax accountant;
* an operational model for receipt processing, accounting preparation, audit-log generation, and monthly journal creation using an LLM.

The code in this directory is only a **Proof of Concept**.

It demonstrates how the ideas described in the whitepaper may be translated into a minimal data-processing structure.

---

## 1. Positioning

The prototype code is subordinate to the whitepaper.

```text
Main:
whitepaper / case-study / operational notes

Subordinate:
prototype code
```

This code is not intended to be:

* production accounting software;
* tax filing software;
* tax advice software;
* a replacement for tax accountants or professionals;
* a guaranteed compliance system.

It is a minimal demonstration of the following concept:

```text
Receipt / invoice / payment memo
↓
LLM output in structured schema
↓
Monthly journal data
↓
Excel / CSV export
↓
Year-end aggregation
```

---

## 2. Directory Structure

```text
appendix/
└── prototype/
    ├── README.md
    ├── requirements.txt
    ├── prototype_schema.py
    ├── prototype_excel_exporter.py
    └── prototype_llm_agent.py
```

---

## 3. Files

### `prototype_schema.py`

Defines the standard data structure expected from the LLM.

The schema reflects the operating model described in:

* `appendix/account_setup_template.md`
* `appendix/accounting_data_preparation.md`
* `appendix/monthly_workflow.md`

It includes fields such as:

* transaction date;
* vendor;
* tax-included amount;
* tax-excluded amount;
* tax type;
* tax amount;
* debit account;
* credit account;
* payment method;
* payer;
* description;
* audit_log;
* evidence location;
* confirmation status.

### `prototype_excel_exporter.py`

Converts structured LLM output into an Excel-compatible monthly journal.

This file demonstrates how monthly LLM logs can be transformed into spreadsheet data.

### `prototype_llm_agent.py`

Optional demonstration of how an LLM API call may generate structured journal-entry candidates.

This file is included only as a conceptual example.

Users may replace this part with:

* ChatGPT manual workflow;
* local LLM;
* another LLM API;
* OCR pipeline;
* spreadsheet import/export tools.

---

## 4. Important Notes

This prototype assumes that the user separately preserves original evidence.

Chat history is not treated as official evidence storage.

The user should separately preserve:

```text
Original receipts
Original PDFs
Electronic invoices
Card statements
Bank statements
Masked processing copies
LLM outputs
Excel / CSV journals
Monthly summaries
```

The prototype does not guarantee legal, tax, or accounting correctness.

The user remains responsible for:

* final accounting confirmation;
* tax classification confirmation;
* evidence preservation;
* professional consultation where necessary;
* official filing procedures;
* compliance with applicable laws and regulations.

---

## 5. Conceptual Workflow

```text
1. User provides receipt image or payment memo.
2. LLM generates structured accounting data.
3. User reviews uncertain items.
4. Structured entries are exported to Excel.
5. Monthly journals are preserved.
6. At year-end, maintained monthly journals are integrated.
```

This approach avoids processing hundreds or thousands of raw receipts at year-end.

Instead, the workload is distributed monthly.

---

## 6. No Support / No Maintenance Policy

This prototype is provided as-is.

This repository does not provide:

* operational support;
* accounting support;
* tax support;
* bug-fix guarantees;
* compatibility guarantees;
* long-term maintenance.

Developers may freely fork, modify, reimplement, or extend the prototype according to their own needs.

---

## 7. Suggested Use

This code is best understood as a reference implementation for the following idea:

```text
LLM logs are not the final journal.

LLM logs are source memos.

Monthly journals are intermediate accounting data.

Year-end journals are created by integrating maintained monthly journals.
```

The most important point is not the code itself.

The most important point is the operating structure:

```text
Evidence
↓
LLM-assisted explanation
↓
Structured accounting candidate
↓
Monthly journal
↓
Year-end aggregation
↓
Tax return preparation
```
