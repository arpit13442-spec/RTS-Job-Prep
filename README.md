# RTS Job Prep - All-in-One Job Portal & Placement Preparation Platform

A full-stack, production-ready web application designed for engineering students and job seekers preparing for campus placements and off-campus tech recruitment drives.

---

## 🌟 Key Features

### 1. 💼 Job Portal & Application Tracker
- **Browse & Filter Opportunities:** Search by role, company, skills, or location. Filter by:
  - Category (Software Engineering, Frontend/Full Stack, Fintech/Backend, IT & Services)
  - Work Mode (Remote, Hybrid, Onsite)
  - Experience (Freshers/Interns, 1-3 Years)
  - Job Type (Full-Time, Internship)
- **Interactive Job Details Modal:** Complete role descriptions, day-to-day responsibilities, requirements, CTC packages, application deadlines, and similar recommended jobs.
- **Mock Application Tracking System (ATS):**
  - Instant 1-click application submission with personal info, college, graduation year, CGPA, and resume upload simulation.
  - Track application status pipeline: `Applied` ➔ `Under Review` ➔ `Interview Scheduled` ➔ `Selected`.
- **Bookmarks & Saved Jobs:** Save interesting openings to apply later with persistence in SQLite.
- **Post a Job Opening:** Community & recruiter form to post new job listings that are immediately available on the portal.

---

### 2. 🎯 Preparation Hub

#### A. Aptitude Preparation (Quantitative, Logical, Verbal)
- **Topics Covered:** Time & Work, Speed Distance & Time, Percentages, Profit & Loss, Syllogisms & Deductive Logic, Blood Relations, Verbal Ability & Grammar.
- **Formula Cheatsheets:** Clear mathematical rules, shortcut formulas, unit conversion matrices, and standard assumptions for campus exams.
- **Interactive Practice Quizzes:**
  - Real-time quiz interface with timer.
  - Automated grading with percentage scores.
  - Step-by-step mathematical solutions and explanations for every question.

#### B. Technical Preparation (Core Computer Science)
- **Subjects Covered:**
  - **Database Management Systems (DBMS):** ACID properties, Normalization (1NF, 2NF, 3NF, BCNF), Indexing (B+ Trees vs Hash), Joins, SQL Commands (TRUNCATE vs DROP vs DELETE), and CAP Theorem.
  - **Operating Systems (OS):** Process vs Thread address spaces, CPU Scheduling algorithms, Coffman's Deadlock conditions, Mutex vs Semaphore, Thrashing, and Context Switching.
  - **Computer Networks (CN):** OSI & TCP/IP models, TCP 3-way handshake, DNS lookup cycle, HTTP/1.1 vs HTTP/2 vs HTTP/3, and HTTPS/TLS handshakes.
  - **OOP & SOLID Principles:** 4 Pillars (Encapsulation, Abstraction, Inheritance, Polymorphism), SOLID breakdown with code design patterns (Singleton, Factory, Observer).
  - **System Design Fundamentals:** Horizontal vs Vertical scaling, Layer 4/7 Load balancers, Caching policies (Cache-Aside vs Write-Through), Database Sharding, and URL Shortener architecture.
- **Interactive Accordion & Flashcards:** Direct answers to the most frequently asked technical interview questions with syntax-highlighted code.

#### C. HR Interview & STAR Method Preparation
- **STAR Framework Guide:** Structured breakdown of Situation, Task, Action, and Result for behavioral interview questions.
- **High-Frequency Question Bank:** Detailed interviewer intent, common pitfalls, and verified model answers for freshers and experienced candidates:
  - "Tell me about yourself." (Past, Present, Future structure)
  - "Why do you want to join our company?"
  - "What is your greatest weakness, and how are you addressing it?"
  - "Describe a conflict you had with a team member and how you resolved it."
  - "Do you have any questions for us?"
- **Interactive HR Practice Simulator:** Type your response to any prompt and run an automated evaluation against the STAR rubric.

---

### 3. 🏢 Companies Hiring Process & Exam Guide
Comprehensive profiles for top tech giants and IT service companies:
- **Product & FAANG:** Google, Amazon, Microsoft, Atlassian, Uber, Razorpay.
- **IT & Service Giants:** TCS (Ninja, Digital, Prime), Infosys (SE, DSE, Specialist Programmer), Accenture (ASE, FSE), Wipro (Elite & Turbo), Cognizant (GenC, Elevate, GenC Next).

Each company guide includes:
- **Eligibility Criteria:** Minimum CGPA/percentage (10th, 12th, Degree), backlog allowance, eligible branches, and gap year rules.
- **Round-by-Round Breakdown:** Online Assessment pattern, duration, marking scheme, sectional cutoffs, and platform used (HackerRank, Superset, TCS iON, Mettle, Codility).
- **Detailed Syllabus:** Sectional breakdowns for Cognitive Aptitude, Hands-on Coding, Technical MCQs, and Domain knowledge.
- **Salary / Compensation:** Full breakdown of base salary, CTC, bonuses, and stocks.
- **Real Past Interview Questions:** Algorithmic and technical questions asked in recent placement drives.
- **Insider Preparation Tips:** Proven strategies for cracking each specific company.

---

### 4. ⚡ Dedicated Topic-Wise DSA Sheet
- **Curated Categorized Roadmap (10 Topics):**
  1. Arrays & Hashing
  2. Strings
  3. Two Pointers & Sliding Window
  4. Linked Lists
  5. Stacks & Queues
  6. Binary Search
  7. Trees & Binary Search Trees (BST)
  8. Graphs & Topological Sort
  9. Dynamic Programming
  10. Bit Manipulation
- **Real-Time Progress Tracker:** Visual animated progress bar displaying overall and per-topic completion percentages.
- **Filters:** Search problem by name, filter by topic, difficulty (Easy, Medium, Hard), or status (Unsolved, Solved, Needs Revision ★).
- **Practice Links:** Direct links to LeetCode and GeeksforGeeks for each problem.
- **Multi-Language Solution Code Viewer:**
  - Complete algorithmic approach and optimal Time & Space complexity analysis.
  - Tabbed syntax-highlighted code in **C++**, **Python**, **Java**, and **JavaScript** with 1-click copy to clipboard.
- **Personal Notes Tracker:** Write and persist personal intuition, edge case caveats, or custom code variations for any problem.

---

### 5. 📊 Dashboard & Analytics
- Overview cards for total applications submitted, DSA problems solved, revision queue, and aptitude quiz accuracy.
- Application status pipeline table with direct access to applied role details.

---

## 🛠️ Architecture & Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python 3.15, Flask 3.1.3 |
| **Database** | SQLite 3 with atomic transactions & JSON attributes |
| **Frontend UI** | Modern Responsive HTML5, Tailwind CSS (via CDN) |
| **Icons & Fonts** | FontAwesome 6, Google Inter & Fira Code |
| **Code Highlighting** | Prism.js (supports C++, Python, Java, JS) |
| **State & Storage** | Real-time REST API sync + localStorage caching |

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.8+ (Python 3.10+ recommended)
- `flask` package:
  ```bash
  pip install Flask
  ```

### 2. Run the Application
Navigate to the project directory:
```bash
cd "C:\Users\Win11\.gemini\antigravity\scratch\job-prep-portal"
python app.py
```

Open your browser and navigate to:
```
http://127.0.0.1:5000
```

### 3. Run the Automated Test Suite
To verify all REST endpoints, database queries, and quiz scoring logic:
```bash
python test_portal.py
```
Expected output:
```
✓ 1. Index HTML loaded successfully (200 OK)
✓ 2. Jobs API: 8 jobs retrieved
✓ 3. Bookmark toggle succeeded
✓ 4. Job application submitted
✓ 5. Applications retrieved: 1
✓ 6. Aptitude topics: 6
✓ 7. Quiz evaluated: 2/3 (66.7%)
✓ 8. Technical CS notes and Q&A retrieved
✓ 9. HR questions & STAR framework: 5 questions
✓ 10. Company hiring guide retrieved (Google)
✓ 11. DSA Progress & Notes saved
✓ 12. Stats Dashboard verified: Jobs Applied=1, DSA Solved=1
🎉 ALL 12 INTEGRATION TESTS PASSED!
```

---

## 📁 Project Structure

```
job-prep-portal/
├── app.py                  # Flask routes, REST APIs, and application server
├── database.py             # SQLite database initialization, schema, and seeding
├── seed_data.py            # Primary dataset: Jobs, Aptitude, Core CS, HR, Companies, DSA Sheet
├── seed_extra.py           # Extended dataset: Additional companies, technical topics, DSA problems
├── test_portal.py          # Automated integration test suite
├── portal.db               # SQLite database file (created on startup)
├── templates/
│   └── index.html          # Responsive single-page application UI
├── static/
│   ├── css/
│   │   └── custom.css      # Custom styling, dark mode, glassmorphism, scrollbars
│   └── js/
│       └── app.js          # SPA state management, reactive filters, quiz engine, modal controller
└── README.md               # Documentation and usage guide
```
