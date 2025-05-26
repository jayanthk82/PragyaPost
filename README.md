# 🧠 PragyaPost: AI-Powered LinkedIn Post Generator


---

## 📐 Architecture Design

PragyaPost is a modular NLP pipeline designed to turn unstructured drafts into high-quality, emotionally intelligent LinkedIn posts. Its architecture includes:

1. **📝 Streamlit UI (Input Layer)**  
   - Users input a rough LinkedIn post draft.
   - Optionally, users can upload previous LinkedIn posts to personalize the tone and persona.

2. **🧠 Large Language Model (LLM: LLaMA GPT-based)**  
   - Analyzes the draft + persona context to generate a **refined, high-level version** of the post.
   - Emphasizes tone, emotional impact, and narrative coherence.

3. **🧹 Small Language Model (SLM: BERT2BERT)**  
   - Serves as a **postprocessing clarity filter**.
   - Compresses the LLM output into a **concise, structured summary**.
   - Removes verbose or redundant sections.

4. **📤 Output Display (Streamlit UI)**  
   - Displays the final, share-ready post.
   - (Optional future feature: highlights emotional tone shifts and style improvements.)

> This layered architecture ensures **clarity, quality, and scalability** without sacrificing control or user personalization.

---

## 🧠 SLM’s Logic and Role (BERT2BERT)

The SLM is fine-tuned to act as a **final summarizer and post-cleaning filter**:

- Distills the LLM output into its **core message**.
- Reduces noise (e.g., excessive punctuation, repetitive phrases).
- Ensures final output is **concise, structured, and emotionally aligned**.

> 🔍 Think of it as a **post-production editor**: the LLM creates the story, the SLM polishes it into something crisp and professional.

---

## 📊 Training Dataset (Synthetic)

Since no labeled dataset existed for this task, a synthetic dataset was created using prompt-engineered pairs:

| Source | Description |
|--------|-------------|
| GPT-4 | Draft-to-summary pairs were auto-generated to simulate noisy → clean transformation |
| Manual Curation | Over 500 examples crafted by hand using real post styles (celebratory, humble, job transitions, etc.) |

> These pairs were used to fine-tune the BERT2BERT model for task-specific summarization.

---

## 💡 Why This Matters

This project demonstrates the following key capabilities:

- ✅ **System design**: combining multiple models for clarity + emotional intelligence.
- ✅ **Model selection**: choosing lightweight summarizers (SLM) and powerful generators (LLM).
- ✅ **Synthetic training**: working around data scarcity with creative dataset generation.
- ✅ **Deployment thinking**: intuitive UI, modular design, and cloud-ready structure.

---

## 🚀 Future Enhancements

- Deploy on the cloud for real-time generation at scale.
- Add tone presets (humble, confident, story-driven).
- Improve SLM using real user data and feedback loops.
