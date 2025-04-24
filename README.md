# ActionPoint GPT-3 Few-Shot Summarizer

This repository contains an early **prompt engine** developed by [ActionPoint](https://actionpoint.ai) in 2021–2022 to enable few-shot summarization of meetings using GPT-3.

At the time, GPT-3 required **explicit examples** to understand how to summarize structured meeting conversations. This engine simulated dialogue, constructed prompts, and appended highlights as training context for each request.

⚠️ **Note**: This engine was used briefly in production before being deprecated with the release of GPT-3.5, which allowed direct instruction without few-shot examples.

---

## ✨ Why It Matters

- Demonstrates a practical workaround from the early GPT era
- Shows how prompt scaffolding helped overcome LLM limitations
- Precursor to today's agentic prompting and chain-of-thought formatting

---

## 🧠 What It Does

- Randomly generates fake meeting utterances based on attendees and keywords
- Formats them in timestamped structure:  
  `Speaker // Time\nSpeech\n\n`
- Appends a structured `Highlight: <<...>>` block with synthesized summaries
- Used to "teach" GPT-3 what a summary looks like before the real meeting content

---

## Example Usage

```python
from promptEngine import generateFakeShots

meeting = {
  "keywords": ["Project X", "Migration Plan", "Risk Review"],
  "attendees": ["Alex", "Jordan", "Morgan"]
}

prompt = generateFakeShots(meeting, 3)
print(prompt)
```
📝 **Style note**:  
Yeah, the function names are in camelCase — back in 2021 I didn’t know Python didn’t like that.  
I kept them this way because that’s how it was back then. It's part of the story.
