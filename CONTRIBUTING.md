# Contributing to the Subprime Code Crisis Report

> **"We are the architects of logic, not consumers of syntax."**

This repository is not just a report; it is a living document of the software industry's struggle against unmanaged complexity. We welcome contributions from engineers, researchers, and leaders who value **Engineering Velocity** over **Typing Speed**.

However, to maintain the integrity of this data, we enforce strict standards.

---

## 🚫 The "No Vibe Coding" Standard

We are fighting against the flood of unverified, AI-generated noise. Therefore, we cannot become what we fight.

**1. No Raw AI Output**
Do not copy-paste output from ChatGPT, Claude, or Gemini directly into this repository.
*   If you use AI to draft a section, you must **rewrite it** to ensure factual accuracy and human tone.
*   PRs that smell like "LLM Slop" (repetitive phrasing, hallucinations, lack of specific insight) will be closed without debate.

**2. Data > Vibes**
We prioritize empirical evidence over subjective feelings.
*   ❌ **Bad:** "Copilot makes my team lazy."
*   ✅ **Good:** "After adopting Copilot, our PR rejection rate increased by 15% (Source: Internal Jira Data)."

**3. Anonymity is Key**
When submitting case studies or "Horror Stories," **sanitize everything**.
*   Remove company names.
*   Remove proprietary code.
*   Focus on the *pattern of failure*, not the specific IP.

---

## 📋 How You Can Help

### 1. Submit a "Horror Story" (Case Study)
We are collecting anonymized examples of **"Plausible Lies"**—code that looked correct, passed tests, but caused architectural rot or production failures.
*   **Action:** Open an Issue with the tag `case-study`.
*   **Format:**
    *   *The Context:* (e.g., React Frontend, Fintech)
    *   *The AI Mistake:* (e.g., Hallucinated a secure library that didn't exist)
    *   *The Cost:* (e.g., 3 days of debugging by a Senior Dev)

### 2. Refine the Protocols
Our [Defense Protocols](protocols/README.md) are battle-tested, but they can be improved.
*   Do you have a better metric than "Code Churn"?
*   Do you have a script that detects "AI Slop" in PRs?
*   **Action:** Submit a Pull Request (PR) to the `protocols/` directory.

### 3. Fix the Report
If you find factual errors or have newer data (e.g., updated METR/DORA reports):
*   **Action:** Submit a PR to the relevant chapter in `report/`.
*   **Requirement:** Cite your sources.

---

## ⚖️ License & Attribution

By contributing to this repository, you agree that your contributions will be licensed under the **CC-BY-SA 4.0** license.

You also agree to the **Code of Conduct**:
*   Critique the *tool* and the *process*, not the *person*.
*   Many developers are forced to use these tools by management. They are victims of the crisis, not the villains.

---

**Read. Verify. Push Back.**