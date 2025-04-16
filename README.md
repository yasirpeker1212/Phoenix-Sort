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

## ⏱ Time Complexity

| Case        | Time Complexity      |
|-------------|----------------------|
| Best Case   | O(n log n)           |
| Average     | O(n log n × k)       |
| Worst Case  | O(n² log n)          |

Where `k` is the number of passes needed to completely rebirth all elements.

Phoenix Sort performs efficiently on nearly sorted lists, but may slow down on highly shuffled input.

---

## 📦 Usage

```bash
git clone https://github.com/yasirpeker1212/phoenix-sort.git
cd phoenix-sort
python3 phoenix_sort.py
```

You’ll see the original and sorted list printed with time taken.

---

## 📈 Example

```python
data = [5, 1, 4, 2, 6, 0, 7]
sorted_data, history = phoenix_sort_optimized(data)
print(sorted_data)  # [0, 1, 2, 4, 5, 6, 7]
```

---

## 🛠️ Future Plans

- [ ] Add unit tests
- [ ] Compare performance with Quick Sort, Merge Sort, and Timsort
- [ ] Interactive visualizer (optional)
- [ ] C / Rust version for fun
- [ ] Jupyter Notebook demo
- [ ] WebAssembly playground

---

## 🐣 Why the name?

Like the mythical Phoenix, this algorithm revives elements that fall out of order and gives them new life — again and again — until balance is achieved.

---

## 🤝 Contributing

Feel free to fork, star, and submit PRs if you have ideas to improve the algorithm or explore new optimization strategies.

---

## 📄 License

MIT License

---

🪶 *Let your data rise from the ashes.*  
— *The Phoenix*
