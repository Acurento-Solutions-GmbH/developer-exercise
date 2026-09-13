<p align="center"><img src="docs/banner.svg" alt="Acurento · Developer Exercise · Small change. Clear decisions." width="960"></p>

<p align="center"><strong>English</strong> · <a href="README.de.md">Deutsch</a></p>

<p align="center"><strong>60-minute exercise · 45-minute conversation · AI explicitly welcome</strong><br>Python with no extra packages · No legal knowledge required</p>

---

## Welcome to Acurento

We build software that makes complex work easier to understand. Our legal registry platform helps companies and consultants identify and manage relevant regulatory changes.

This small exercise gives you a glimpse of that work. We want to understand how you read existing code, make decisions, and verify results. An incomplete solution with clear reasoning is welcome. Extra features or elaborate documentation do not earn extra points.

## The task

> “One customer's installation capacity is missing. Yet the system says **not affected**. Can we trust that assessment?”

Take over the small existing program in this repository. Investigate this report, improve the assessment, and add meaningful tests.

For each customer, the output should give one of these assessments:

| Status | Meaning |
|---|---|
| `affected` | The available data establishes that the rule applies. |
| `not_affected` | The available data establishes that the rule does not apply. |
| `needs_review` | The available data is insufficient to decide. |

Each assessment needs a short **explanation grounded in the available data**, understandable to a consultant. If review is needed, make clear which information is missing.

### The complete domain rule

The fictional rule **DEMO-001** applies to installations of type **F-01** with a capacity of **at least 5 tonnes per hour**. All other installation types are outside the scope of this rule.

- Each customer in this exercise has exactly one installation with a known type.
- Capacity is a nonnegative number in tonnes per hour. `0` is a valid, known value.
- `null` or an absent `capacity_t_h` field means **unknown**.
- All other fields are present and correct. Inputs are valid JSON.
- All information refers to the same point in time. There are no other laws or exceptions in this exercise.

**The rule, companies, and data are entirely fictional.** Use only the rule above; no external legal research is needed. The assessment supports a review and is not an overall compliance verdict about a customer.

### Scope

Improve the existing function and its explanations. Keep the documented status values, customer IDs, and rule IDs in the output. You may restructure the code as needed.

A web interface, database, API, deployment, or runtime LLM is outside the scope. A general rules engine and comprehensive input validation are not required either.

## Get started in two minutes

Requires **Python 3.10 or later**, with no extra packages or credentials.

```bash
git clone https://github.com/Acurento-Solutions-GmbH/developer-exercise.git
cd developer-exercise
python3 -m relevance
python3 -m unittest discover -s tests -v
```

On Windows, replace `python3` with `py -3`. Alternatively, select **Code → Download ZIP** above, extract it, and run the commands from the extracted folder.

The program writes JSON to standard output. You can also supply your own inputs or save the output:

```bash
python3 -m relevance --customers data/customers.json --rule data/rule.json
python3 -m relevance > result.json
```

The existing tests cover only two known cases and the executable interface. **Passing tests do not mean that the reported problem has been fixed.**

| File | Purpose |
|---|---|
| [`relevance/assessment.py`](relevance/assessment.py) | Existing assessment logic — start here |
| [`data/rule.json`](data/rule.json) | The fictional rule as data |
| [`data/customers.json`](data/customers.json) | Three synthetic customer profiles |
| [`tests/test_assessment.py`](tests/test_assessment.py) | Initial tests for you to extend |
| [`HANDOVER.md`](HANDOVER.md) | Short handover template |

Python is our suggestion. If you can express yourself much better in another language, you may use the same interface and data in that language. Document simple run and test commands; framework choice is not assessed.

## Time and tools

**Please stop after 60 minutes in total**, even if something is unfinished. Reading, implementation, tests, and the handover all count. A suggested split: 10 minutes to understand, 30 to change, 10 to verify, and 10 to hand over. If local setup blocks you, contact your hiring contact; installation problems should not determine your result.

AI assistants, coding agents, autocomplete, and documentation are explicitly allowed — including generating the entire implementation. What matters is that you can understand and verify the result. Working without AI is equally welcome. If you want to use AI but do not have access, tell your hiring contact before starting so we can arrange comparable access.

Briefly note which tools you used and how you checked important results. A full chat transcript or screen recording is not required. You do not need to find an AI mistake or manufacture a story about rejecting suggestions.

## Submission

Send your existing Acurento hiring contact **a ZIP file** containing your solution or a link to a **separate private repository**. Arrange the necessary GitHub access with that person. For a private repository, use an independent copy; a fork of this public repository cannot be made private.

Please do not submit a solution through a public pull request, issue, or public fork, so the exercise remains useful for other candidates.

Include:

1. Your code and tests, with working run and test commands.
2. One completed handover template: [`HANDOVER.md`](HANDOVER.md), **at most 300 words** in total.

You may include the JSON output, but it is not a required deliverable. German and English are equally welcome. Please do not include credentials or real customer data. Your submission is for recruitment and is not commissioned production work.

## The follow-up conversation

If we move forward together after reviewing your submission, we will schedule **45 minutes**:

| Duration | Activity |
|---|---|
| 10 minutes | Demonstrate your solution and trace one case through the code |
| 10 minutes | Discuss one decision and how you verified it |
| 20 minutes | Work through a small new requirement together |
| 5 minutes | What would you release, and what would you improve next? |

---

<p align="center">Acurento · Software for decisions you can explain</p>
