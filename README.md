# DSA Roadmap — Python First

A structured, hands-on journey to build strong **Data Structures and Algorithms (DSA)** fundamentals using Python, practise technical-interview problems on **LeetCode**, and develop competitive-programming skills on **Codeforces**.

The goal is not to collect Accepted submissions. The goal is to understand why an approach works, analyse its time and space complexity, implement it independently, and remember it well enough to use on unfamiliar problems.

> **Learning strategy:** Learn DSA in Python first. After building a solid foundation, translate selected solutions into JavaScript when useful for web-development interviews. Consider C++ later if competitive programming becomes a bigger priority.

---

## Table of Contents

- [Goals](#goals)
- [Learning Approach](#learning-approach)
- [Repository Structure](#repository-structure)
- [Roadmap](#roadmap)
- [Weekly Routine](#weekly-routine)
- [Problem-Solving Workflow](#problem-solving-workflow)
- [Problem Log](#problem-log)
- [How to Write Notes](#how-to-write-notes)
- [Progress Checklist](#progress-checklist)
- [Resources](#resources)
- [Languages](#languages)

## Goals

- [ ] Understand time and space complexity and use Big-O analysis confidently.
- [ ] Learn core data structures and common algorithmic patterns.
- [ ] Implement important algorithms from memory in Python.
- [ ] Solve problems on LeetCode and Codeforces consistently.
- [ ] Practise explaining the reasoning, correctness, and complexity of each solution.
- [ ] Review old problems using spaced practice instead of repeatedly starting from scratch.
- [ ] Build a searchable personal reference of notes, implementations, and lessons learned.
- [ ] Translate selected solutions into JavaScript after the Python foundation is established.

## Learning Approach

For each topic, follow this cycle:

1. **Understand:** Learn the concept and identify when it is useful.
2. **Implement:** Write a small implementation without copying a complete solution.
3. **Practise:** Solve a few problems that use the concept.
4. **Explain:** Record the approach, correctness reasoning, and complexity in your own words.
5. **Review:** Re-solve the problem later without looking at the original code.
6. **Apply:** Solve mixed problems where the relevant pattern is not stated in advance.

Use hints when necessary, but avoid immediately reading the full editorial. First write down what you tried, where you got stuck, and what information would help you move forward.

### Suggested review intervals

Revisit challenging problems after approximately **1, 3, 7, and 14 days**. These are practical starting intervals, not fixed rules. Review sooner when you have forgotten the approach; extend the interval when you can solve it easily.

## Repository Structure

```text
dsa-roadmap/
├── README.md
├── notes/
│   ├── big-o-complexity.md
│   ├── arrays-and-hashing.md
│   └── ...
├── implementations/
│   ├── searching/
│   ├── sorting/
│   ├── linked-list/
│   ├── trees/
│   ├── graphs/
│   └── dynamic-programming/
├── solutions/
│   ├── leetcode/
│   │   ├── arrays-hashing/
│   │   ├── two-pointers/
│   │   ├── sliding-window/
│   │   ├── binary-search/
│   │   ├── linked-list/
│   │   ├── trees/
│   │   ├── graphs/
│   │   └── dynamic-programming/
│   └── codeforces/
│       ├── 800/
│       ├── 900/
│       └── ...
├── notebooks/
│   └── ...
└── progress/
    ├── problem-log.csv
    └── mistakes.md
```

Adjust the folders as the repository grows. Use **`.py` files** for normal solutions and reusable implementations. Use **Jupyter notebooks (`.ipynb`) selectively** for experiments, visualisations, recursion traces, graph traversal, or DP tables—not as the default format for every online-judge submission.

## Roadmap

This is a flexible 24-week plan. Move forward when you understand the concepts and can solve representative problems—not just because a week has ended. The initial target is around **6–8 hours per week**.

| Phase | Topics | Practice focus | Target outcome |
|---|---|---|---|
| **Weeks 1–4: Foundations** | Big-O, Python collections, arrays, strings, hashing, sorting, prefix sums, two pointers, sliding windows, binary search | LeetCode Easy and selected Medium; beginner Codeforces implementation problems | Explain complexity and recognize common array patterns. |
| **Weeks 5–8: Core structures** | Linked lists, stacks, queues, deques, recursion, backtracking, trees, BSTs, heaps | LeetCode linked-list, stack, recursion, and tree problems; beginner Codeforces | Implement and use common data structures confidently. |
| **Weeks 9–12: Core algorithms** | Greedy, intervals, graph representation, BFS, DFS, connected components, basic 1D/2D DP | LeetCode Easy/Medium and topic-based Codeforces practice | Identify common approaches and begin solving mixed problems. |
| **Weeks 13–16: Deeper graphs and DP** | Topological sort, disjoint-set union (DSU), shortest paths, knapsack patterns, subsequences, LIS | LeetCode Medium and selected CSES problems | Derive state transitions and choose appropriate graph algorithms. |
| **Weeks 17–20: Competitive-programming foundations** | GCD, primes and sieves, modular arithmetic, bit manipulation, stronger greedy reasoning, graph and DP variations | Regular Codeforces contests and upsolving | Improve implementation speed and reasoning under time pressure. |
| **Weeks 21–24: Consolidation** | Mixed revision; optional tries, Fenwick trees, segment trees, monotonic queues, advanced graph algorithms | Timed LeetCode sessions, mock interviews, Codeforces contests | Identify weaknesses and build a focused plan for continued practice. |

### Topic checklist

- [ ] Complexity analysis and Python built-in data structures
- [ ] Arrays and strings
- [ ] Hash maps and sets
- [ ] Sorting and prefix sums
- [ ] Two pointers and sliding window
- [ ] Binary search
- [ ] Linked lists
- [ ] Stacks, queues, and deques
- [ ] Recursion and backtracking
- [ ] Trees and binary search trees
- [ ] Heaps and priority queues
- [ ] Greedy algorithms and intervals
- [ ] Graph representation, BFS, and DFS
- [ ] Topological sorting and DSU
- [ ] Shortest paths
- [ ] Dynamic programming
- [ ] Number theory and modular arithmetic
- [ ] Bit manipulation
- [ ] Mixed and timed practice
- [ ] Optional advanced data structures

## Weekly Routine

Aim for five focused sessions per week. Adjust the duration around university deadlines and exams.

| Session | Activity |
|---|---|
| 1 | Learn one concept and implement it from memory. |
| 2 | Solve 1–2 LeetCode problems related to the concept. |
| 3 | Attempt another problem independently; explain correctness and complexity. |
| 4 | Solve 1–2 Codeforces problems at an appropriate difficulty. |
| 5 | Re-solve older problems, review mistakes, and update notes. |

A reasonable starting target is **3 new LeetCode problems and 2 Codeforces problems each week**, in addition to review. Spend as much time as needed to understand a hard problem; problem counts are not the main measure of progress.

## Problem-Solving Workflow

Use this checklist when attempting a problem:

1. [ ] Restate the problem in my own words.
2. [ ] Identify constraints, inputs, outputs, and edge cases.
3. [ ] Work through at least one example by hand.
4. [ ] Develop a brute-force approach first.
5. [ ] Look for a better algorithm or data structure.
6. [ ] State the time and space complexity before coding.
7. [ ] Implement the solution without copying a complete answer.
8. [ ] Test normal cases, edge cases, and boundary conditions.
9. [ ] Explain why the algorithm is correct.
10. [ ] Record the key insight and any mistake made.
11. [ ] Re-solve later without looking at the original code.

If stuck for around 25–35 minutes on a typical interview-style problem, take a hint or consult an explanation. The purpose is to learn the missing idea, then close the explanation and implement the solution independently.

## Problem Log

Track progress in `progress/problem-log.csv`. Suggested columns:

```csv
Date,Platform,Problem,URL,Topic,Difficulty,Result,Hint Used,Time Spent,Review Date,Key Lesson
```

Suggested result labels:

- `Independent` — solved without hints or editorial.
- `Hint` — needed a small hint.
- `Editorial` — needed to study the full explanation.
- `Re-solved` — solved again during review without help.

Track mistakes in `progress/mistakes.md`. Useful categories include misunderstanding the problem, choosing the wrong pattern, missing an edge case, incorrect complexity analysis, implementation errors, and forgetting a known technique.

## How to Write Notes

Create one Markdown note per major topic. Keep notes concise enough to review quickly, but detailed enough to reconstruct the idea.

Use this template:

```markdown
# Topic Name

## Core idea
Explain it in my own words.

## When should I use it?
What clues suggest this technique?

## How it works
Explain the steps using a small example.

## Why it is correct
State the invariant or reasoning that makes it work.

## Complexity
- Time:
- Space:
- Explanation:

## Python pattern
Write the reusable implementation from memory.

## Common mistakes
Record edge cases and debugging lessons.

## Problems to revisit
- Problem — key lesson — next review date
```

For each solution, use a short comment header:

```python
"""Platform: LeetCode
Problem: Two Sum
URL: https://leetcode.com/problems/two-sum/
Pattern: Hash map
Time: O(n)
Space: O(n)
Key idea: Store previously seen values and look for the complement.
"""
```

Write explanations in your own words rather than copying tutorials. The notes should help you rebuild the reasoning after a gap in practice.

## Progress Checklist

Review progress every four weeks.

- [ ] I can implement the topics studied without following a tutorial.
- [ ] I can explain why my solution is correct.
- [ ] I can analyse time and space complexity.
- [ ] I can handle edge cases and test my code systematically.
- [ ] I can re-solve previously studied problems without looking at the solution.
- [ ] I can recognize familiar patterns in differently worded problems.
- [ ] I review and upsolve problems I could not solve during practice or contests.
- [ ] I know which topics need more work in the next study cycle.

Measure progress by independent problem solving, retention, and reasoning—not by the total number of submissions alone.

## Resources

### Interview-style practice
- [LeetCode](https://leetcode.com/)
- [LeetCode 75 Study Plan](https://leetcode.com/studyplan/leetcode-75/)

### Competitive programming
- [Codeforces Problemset](https://codeforces.com/problemset)
- [Codeforces contests](https://codeforces.com/contests)
- [CSES Problem Set](https://cses.fi/problemset/)
- [CP-Algorithms](https://cp-algorithms.com/)
- [USACO Guide](https://usaco.guide/)

### Python and notebooks
- [Python documentation](https://docs.python.org/3/)
- [Jupyter documentation](https://docs.jupyter.org/)

Use these resources selectively. Learn a concept, practise it, and return to a reference when you need clarification rather than trying to consume every resource from beginning to end.

## Languages

### Python — primary language
Use Python for learning concepts, implementing algorithms, and the majority of early LeetCode and Codeforces practice.

### JavaScript — later application
After the first 10–12 weeks, translate selected solutions into JavaScript to connect DSA knowledge with web-development work and interview requirements. Focus on language differences and built-in data structures rather than relearning the algorithm.

### C++ — optional
Consider C++ if competitive programming becomes a major priority or if your target contests, courses, or interviews require it. There is no need to study Python, JavaScript, and C++ in parallel at the beginning.

---

## Guiding Principle

**Learn a concept, implement it, solve unfamiliar problems, explain your reasoning, and revisit it after time has passed.** Consistent deliberate practice beats collecting solutions that you cannot reproduce independently.
