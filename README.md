# 🔥 Phoenix Sort

**Phoenix Sort** is a custom sorting algorithm inspired by Stalin Sort — but with a twist.  
Instead of deleting unsorted elements, it lets them **rise from the ashes** and reintegrate until the whole list is sorted.

> ✨ It's not just sorting — it's reincarnation.

---

## 🧠 Concept

Phoenix Sort works in cycles:

1. Build the longest non-decreasing sequence from left to right.
2. Reject any element that breaks the sequence.
3. Rebirth rejected elements by reinserting them into the sorted sequence using binary search.
4. Repeat until no rejected elements remain.

---

## 🚀 Features

- 🕊️ **Rebirth-based logic** — elements aren't deleted, they get another chance.
- ⚡ **Optimized reinsertion** using `bisect` for smart binary insert.
- 📚 Simple Python implementation, easy to hack on.
- 🧪 Ready for benchmarking and experimentation.

---

## 📦 Usage

```bash
git clone https://github.com/yourusername/phoenix-sort.git
cd phoenix-sort
python3 phoenix_sort.py
