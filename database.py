"""
Database module for Job Portal & Preparation Platform
Handles SQLite initialization, seeding, query helpers, and state persistence.
"""

import sqlite3
import json
import os
import sys

# Add current folder to path for seed imports
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

DB_PATH = os.path.join(BASE_DIR, "portal.db")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Create tables and seed initial data if database is fresh."""
    conn = get_db()
    cursor = conn.cursor()

    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS jobs (
        id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        company TEXT NOT NULL,
        logo TEXT,
        location TEXT,
        type TEXT,
        category TEXT,
        experience TEXT,
        salary TEXT,
        work_mode TEXT,
        posted_date TEXT,
        deadline TEXT,
        description TEXT,
        responsibilities TEXT,
        requirements TEXT,
        tags TEXT,
        is_custom INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS applications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        job_id TEXT NOT NULL,
        full_name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT,
        college TEXT,
        degree TEXT,
        graduation_year TEXT,
        cgpa TEXT,
        resume_name TEXT,
        cover_note TEXT,
        status TEXT DEFAULT 'Applied',
        applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (job_id) REFERENCES jobs(id)
    );

    CREATE TABLE IF NOT EXISTS bookmarks (
        job_id TEXT PRIMARY KEY,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (job_id) REFERENCES jobs(id)
    );

    CREATE TABLE IF NOT EXISTS aptitude_topics (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        icon TEXT,
        concept TEXT,
        formulas TEXT
    );

    CREATE TABLE IF NOT EXISTS aptitude_questions (
        id TEXT PRIMARY KEY,
        topic_id TEXT NOT NULL,
        question TEXT NOT NULL,
        options TEXT NOT NULL,
        correct INTEGER NOT NULL,
        explanation TEXT,
        FOREIGN KEY (topic_id) REFERENCES aptitude_topics(id)
    );

    CREATE TABLE IF NOT EXISTS technical_subjects (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        icon TEXT,
        summary TEXT,
        key_notes TEXT,
        qa_list TEXT
    );

    CREATE TABLE IF NOT EXISTS hr_questions (
        id TEXT PRIMARY KEY,
        question TEXT NOT NULL,
        category TEXT,
        tip TEXT,
        sample_answer TEXT
    );

    CREATE TABLE IF NOT EXISTS companies (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        type TEXT,
        logo TEXT,
        tier TEXT,
        ctc TEXT,
        eligibility TEXT,
        exam_pattern TEXT,
        syllabus TEXT,
        past_questions TEXT,
        tips TEXT
    );

    CREATE TABLE IF NOT EXISTS dsa_topics (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT,
        order_idx INTEGER DEFAULT 0
    );

    CREATE TABLE IF NOT EXISTS dsa_problems (
        id TEXT PRIMARY KEY,
        topic_id TEXT NOT NULL,
        title TEXT NOT NULL,
        difficulty TEXT NOT NULL,
        leetcode_url TEXT,
        gfg_url TEXT,
        statement TEXT,
        approach TEXT,
        time_complexity TEXT,
        space_complexity TEXT,
        code TEXT,
        FOREIGN KEY (topic_id) REFERENCES dsa_topics(id)
    );

    CREATE TABLE IF NOT EXISTS dsa_user_progress (
        problem_id TEXT PRIMARY KEY,
        is_solved INTEGER DEFAULT 0,
        needs_revision INTEGER DEFAULT 0,
        notes TEXT,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (problem_id) REFERENCES dsa_problems(id)
    );

    CREATE TABLE IF NOT EXISTS quiz_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic_id TEXT,
        score INTEGER,
        total_questions INTEGER,
        completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    conn.commit()

    # Check if seeding is needed
    cursor.execute("SELECT COUNT(*) FROM jobs")
    job_count = cursor.fetchone()[0]
    if job_count == 0:
        seed_all(conn)

    conn.close()

def seed_all(conn):
    """Seed comprehensive initial data from seed_data and seed_extra."""
    from seed_data import JOBS_DATA, APTITUDE_DATA, TECHNICAL_DATA, HR_DATA, COMPANIES_DATA, DSA_SHEET_DATA
    from seed_extra import EXTRA_COMPANIES, EXTRA_DSA_TOPICS, EXTRA_TECHNICAL_SUBJECTS

    cursor = conn.cursor()

    # 1. Jobs
    for j in JOBS_DATA:
        cursor.execute("""
            INSERT OR IGNORE INTO jobs 
            (id, title, company, logo, location, type, category, experience, salary, work_mode, posted_date, deadline, description, responsibilities, requirements, tags)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            j["id"], j["title"], j["company"], j.get("logo", ""), j["location"], j["type"],
            j["category"], j["experience"], j["salary"], j["work_mode"], j["posted_date"],
            j["deadline"], j["description"], json.dumps(j.get("responsibilities", [])),
            json.dumps(j.get("requirements", [])), json.dumps(j.get("tags", []))
        ))

    # 2. Aptitude
    for t in APTITUDE_DATA["topics"]:
        cursor.execute("""
            INSERT OR IGNORE INTO aptitude_topics (id, name, category, icon, concept, formulas)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (t["id"], t["name"], t["category"], t.get("icon", ""), t["concept"], json.dumps(t.get("formulas", []))))

        for q in t.get("questions", []):
            cursor.execute("""
                INSERT OR IGNORE INTO aptitude_questions (id, topic_id, question, options, correct, explanation)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (q["id"], t["id"], q["question"], json.dumps(q["options"]), q["correct"], q.get("explanation", "")))

    # 3. Technical Core CS
    all_tech = TECHNICAL_DATA["subjects"] + EXTRA_TECHNICAL_SUBJECTS
    for sub in all_tech:
        cursor.execute("""
            INSERT OR IGNORE INTO technical_subjects (id, name, icon, summary, key_notes, qa_list)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (sub["id"], sub["name"], sub.get("icon", ""), sub["summary"], json.dumps(sub.get("key_notes", [])), json.dumps(sub.get("qa_list", []))))

    # 4. HR Questions
    for hr in HR_DATA["questions"]:
        cursor.execute("""
            INSERT OR IGNORE INTO hr_questions (id, question, category, tip, sample_answer)
            VALUES (?, ?, ?, ?, ?)
        """, (hr["id"], hr["question"], hr.get("category", ""), hr.get("tip", ""), hr.get("sample_answer", "")))

    # 5. Companies
    all_companies = COMPANIES_DATA + EXTRA_COMPANIES
    for c in all_companies:
        cursor.execute("""
            INSERT OR IGNORE INTO companies (id, name, type, logo, tier, ctc, eligibility, exam_pattern, syllabus, past_questions, tips)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            c["id"], c["name"], c.get("type", ""), c.get("logo", ""), c.get("tier", ""), c.get("ctc", ""),
            json.dumps(c.get("eligibility", {})), json.dumps(c.get("exam_pattern", {})),
            json.dumps(c.get("syllabus", [])), json.dumps(c.get("past_questions", [])), c.get("tips", "")
        ))

    # 6. DSA Sheet Topics & Problems
    all_dsa = DSA_SHEET_DATA + EXTRA_DSA_TOPICS
    for idx, dsa_topic in enumerate(all_dsa):
        topic_id = dsa_topic["topic"].lower().replace(" ", "-").replace("&", "and").replace("(", "").replace(")", "")
        cursor.execute("""
            INSERT OR IGNORE INTO dsa_topics (id, name, description, order_idx)
            VALUES (?, ?, ?, ?)
        """, (topic_id, dsa_topic["topic"], dsa_topic.get("description", ""), idx))

        for prob in dsa_topic.get("problems", []):
            cursor.execute("""
                INSERT OR IGNORE INTO dsa_problems 
                (id, topic_id, title, difficulty, leetcode_url, gfg_url, statement, approach, time_complexity, space_complexity, code)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                prob["id"], topic_id, prob["title"], prob["difficulty"],
                prob.get("leetcode_url", ""), prob.get("gfg_url", ""),
                prob.get("statement", ""), prob.get("approach", ""),
                prob.get("time_complexity", ""), prob.get("space_complexity", ""),
                json.dumps(prob.get("code", {}))
            ))

    conn.commit()
    print("Database successfully initialized and seeded.")

if __name__ == "__main__":
    init_db()
