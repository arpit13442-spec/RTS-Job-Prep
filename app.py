"""
Job Portal & Preparation Platform - Flask Application
Serves interactive web application and RESTful APIs for:
- Job portal & application tracking
- Aptitude preparation & interactive quizzes
- Technical CS subjects & interview flashcards
- HR preparation & STAR framework
- Companies hiring process & exam patterns
- Dedicated Topic-wise DSA Prep Sheet
"""

import os
import json
import sqlite3
from flask import Flask, render_template, request, jsonify, send_from_directory
from database import get_db, init_db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'job-prep-portal-secret-key-2026'

# Ensure database is initialized
init_db()

# ----------------- PAGE ROUTES -----------------
@app.route('/')
def index():
    return render_template('index.html')

# ----------------- JOBS API -----------------
@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    search = request.args.get('search', '').strip().lower()
    category = request.args.get('category', '').strip()
    work_mode = request.args.get('work_mode', '').strip()
    experience = request.args.get('experience', '').strip()
    job_type = request.args.get('type', '').strip()

    conn = get_db()
    cursor = conn.cursor()

    query = """
        SELECT j.*, 
               CASE WHEN b.job_id IS NOT NULL THEN 1 ELSE 0 END as is_bookmarked,
               CASE WHEN a.job_id IS NOT NULL THEN 1 ELSE 0 END as is_applied
        FROM jobs j
        LEFT JOIN bookmarks b ON j.id = b.job_id
        LEFT JOIN applications a ON j.id = a.job_id
        WHERE 1=1
    """
    params = []

    if search:
        query += " AND (LOWER(j.title) LIKE ? OR LOWER(j.company) LIKE ? OR LOWER(j.location) LIKE ? OR LOWER(j.tags) LIKE ?)"
        term = f"%{search}%"
        params.extend([term, term, term, term])

    if category and category != 'All':
        query += " AND j.category = ?"
        params.append(category)

    if work_mode and work_mode != 'All':
        query += " AND j.work_mode = ?"
        params.append(work_mode)

    if job_type and job_type != 'All':
        query += " AND j.type = ?"
        params.append(job_type)

    if experience and experience != 'All':
        if experience == 'Freshers':
            query += " AND (j.experience LIKE '%0%' OR j.experience LIKE '%Fresher%')"
        elif experience == 'Experienced':
            query += " AND (j.experience LIKE '%1%' OR j.experience LIKE '%2%' OR j.experience LIKE '%3%')"

    query += " ORDER BY j.created_at DESC"
    cursor.execute(query, params)
    rows = cursor.fetchall()

    jobs = []
    for r in rows:
        job = dict(r)
        job['responsibilities'] = json.loads(job['responsibilities']) if job['responsibilities'] else []
        job['requirements'] = json.loads(job['requirements']) if job['requirements'] else []
        job['tags'] = json.loads(job['tags']) if job['tags'] else []
        jobs.append(job)

    conn.close()
    return jsonify({"success": True, "count": len(jobs), "jobs": jobs})

@app.route('/api/jobs/<job_id>', methods=['GET'])
def get_job_detail(job_id):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT j.*, 
               CASE WHEN b.job_id IS NOT NULL THEN 1 ELSE 0 END as is_bookmarked,
               CASE WHEN a.job_id IS NOT NULL THEN 1 ELSE 0 END as is_applied
        FROM jobs j
        LEFT JOIN bookmarks b ON j.id = b.job_id
        LEFT JOIN applications a ON j.id = a.job_id
        WHERE j.id = ?
    """, (job_id,))
    row = cursor.fetchone()

    if not row:
        conn.close()
        return jsonify({"success": False, "message": "Job not found"}), 404

    job = dict(row)
    job['responsibilities'] = json.loads(job['responsibilities']) if job['responsibilities'] else []
    job['requirements'] = json.loads(job['requirements']) if job['requirements'] else []
    job['tags'] = json.loads(job['tags']) if job['tags'] else []

    # Get similar jobs
    cursor.execute("""
        SELECT id, title, company, salary, location, type 
        FROM jobs 
        WHERE category = ? AND id != ? 
        LIMIT 3
    """, (job['category'], job_id))
    similar = [dict(r) for r in cursor.fetchall()]

    conn.close()
    return jsonify({"success": True, "job": job, "similar_jobs": similar})

@app.route('/api/jobs', methods=['POST'])
def create_job():
    data = request.json or {}
    title = data.get('title', '').strip()
    company = data.get('company', '').strip()

    if not title or not company:
        return jsonify({"success": False, "message": "Title and Company are required"}), 400

    job_id = f"custom-job-{os.urandom(4).hex()}"
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO jobs 
        (id, title, company, logo, location, type, category, experience, salary, work_mode, posted_date, deadline, description, responsibilities, requirements, tags, is_custom)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'Just now', ?, ?, ?, ?, ?, 1)
    """, (
        job_id,
        title,
        company,
        data.get('logo', 'https://cdn-icons-png.flaticon.com/512/3281/3281289.png'),
        data.get('location', 'Remote / Hybrid'),
        data.get('type', 'Full-Time'),
        data.get('category', 'Software Engineering'),
        data.get('experience', '0-2 Years'),
        data.get('salary', 'Competitive CTC'),
        data.get('work_mode', 'Hybrid'),
        data.get('deadline', 'Open until filled'),
        data.get('description', 'Exciting software engineering opportunity.'),
        json.dumps(data.get('responsibilities', ["Collaborate with engineering team", "Build scalable features"])),
        json.dumps(data.get('requirements', ["Bachelor's in CS or equivalent", "Good DSA knowledge"])),
        json.dumps(data.get('tags', ["Engineering", "Tech"]))
    ))

    conn.commit()
    conn.close()
    return jsonify({"success": True, "job_id": job_id, "message": "Job posted successfully!"})

@app.route('/api/jobs/<job_id>/bookmark', methods=['POST'])
def toggle_bookmark(job_id):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT 1 FROM bookmarks WHERE job_id = ?", (job_id,))
    exists = cursor.fetchone()

    if exists:
        cursor.execute("DELETE FROM bookmarks WHERE job_id = ?", (job_id,))
        is_bookmarked = False
        msg = "Removed from saved jobs"
    else:
        cursor.execute("INSERT INTO bookmarks (job_id) VALUES (?)", (job_id,))
        is_bookmarked = True
        msg = "Saved to bookmarks"

    conn.commit()
    conn.close()
    return jsonify({"success": True, "is_bookmarked": is_bookmarked, "message": msg})

@app.route('/api/bookmarks', methods=['GET'])
def get_bookmarked_jobs():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT j.*, 1 as is_bookmarked,
               CASE WHEN a.job_id IS NOT NULL THEN 1 ELSE 0 END as is_applied
        FROM jobs j
        JOIN bookmarks b ON j.id = b.job_id
        LEFT JOIN applications a ON j.id = a.job_id
        ORDER BY b.created_at DESC
    """)
    rows = cursor.fetchall()
    jobs = []
    for r in rows:
        job = dict(r)
        job['tags'] = json.loads(job['tags']) if job['tags'] else []
        jobs.append(job)

    conn.close()
    return jsonify({"success": True, "count": len(jobs), "jobs": jobs})

@app.route('/api/jobs/<job_id>/apply', methods=['POST'])
def apply_job(job_id):
    data = request.json or {}
    full_name = data.get('full_name', '').strip()
    email = data.get('email', '').strip()

    if not full_name or not email:
        return jsonify({"success": False, "message": "Full Name and Email are required"}), 400

    conn = get_db()
    cursor = conn.cursor()

    # Check if already applied
    cursor.execute("SELECT id FROM applications WHERE job_id = ? AND email = ?", (job_id, email))
    if cursor.fetchone():
        conn.close()
        return jsonify({"success": False, "message": "You have already applied for this role with this email!"}), 400

    cursor.execute("""
        INSERT INTO applications 
        (job_id, full_name, email, phone, college, degree, graduation_year, cgpa, resume_name, cover_note, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'Applied')
    """, (
        job_id,
        full_name,
        email,
        data.get('phone', ''),
        data.get('college', ''),
        data.get('degree', ''),
        data.get('graduation_year', ''),
        data.get('cgpa', ''),
        data.get('resume_name', 'Resume_Uploaded.pdf'),
        data.get('cover_note', '')
    ))

    conn.commit()
    app_id = cursor.lastrowid
    conn.close()

    return jsonify({"success": True, "application_id": app_id, "message": "Application submitted successfully! Track status in My Applications."})

@app.route('/api/applications', methods=['GET'])
def get_applications():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT a.*, j.title as job_title, j.company as job_company, j.location as job_location, j.logo as job_logo, j.salary as job_salary
        FROM applications a
        JOIN jobs j ON a.job_id = j.id
        ORDER BY a.applied_at DESC
    """)
    rows = cursor.fetchall()
    apps = [dict(r) for r in rows]
    conn.close()

    return jsonify({"success": True, "count": len(apps), "applications": apps})

# ----------------- APTITUDE API -----------------
@app.route('/api/prep/aptitude', methods=['GET'])
def get_aptitude_topics():
    category = request.args.get('category', '').strip()
    conn = get_db()
    cursor = conn.cursor()

    query = "SELECT * FROM aptitude_topics WHERE 1=1"
    params = []
    if category and category != 'All':
        query += " AND category = ?"
        params.append(category)

    cursor.execute(query, params)
    topics = []
    for r in cursor.fetchall():
        top = dict(r)
        top['formulas'] = json.loads(top['formulas']) if top['formulas'] else []
        # get question count
        cursor.execute("SELECT COUNT(*) FROM aptitude_questions WHERE topic_id = ?", (top['id'],))
        top['question_count'] = cursor.fetchone()[0]
        topics.append(top)

    conn.close()
    return jsonify({"success": True, "topics": topics})

@app.route('/api/prep/aptitude/<topic_id>', methods=['GET'])
def get_aptitude_topic_detail(topic_id):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM aptitude_topics WHERE id = ?", (topic_id,))
    row = cursor.fetchone()
    if not row:
        conn.close()
        return jsonify({"success": False, "message": "Topic not found"}), 404

    topic = dict(row)
    topic['formulas'] = json.loads(topic['formulas']) if topic['formulas'] else []

    cursor.execute("SELECT id, question, options, correct, explanation FROM aptitude_questions WHERE topic_id = ?", (topic_id,))
    questions = []
    for q in cursor.fetchall():
        q_item = dict(q)
        q_item['options'] = json.loads(q_item['options']) if q_item['options'] else []
        questions.append(q_item)

    topic['questions'] = questions
    conn.close()
    return jsonify({"success": True, "topic": topic})

@app.route('/api/prep/aptitude/quiz/submit', methods=['POST'])
def submit_quiz():
    data = request.json or {}
    topic_id = data.get('topic_id')
    user_answers = data.get('answers', {})  # { question_id: selected_index }

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id, correct, explanation FROM aptitude_questions WHERE topic_id = ?", (topic_id,))
    rows = cursor.fetchall()

    correct_count = 0
    total = len(rows)
    details = []

    for r in rows:
        q_id = r['id']
        correct_idx = r['correct']
        selected_idx = user_answers.get(q_id)
        is_correct = (selected_idx is not None and int(selected_idx) == correct_idx)
        if is_correct:
            correct_count += 1
        details.append({
            "id": q_id,
            "correct_index": correct_idx,
            "user_index": selected_idx,
            "is_correct": is_correct,
            "explanation": r['explanation']
        })

    # Save to quiz_results
    cursor.execute("""
        INSERT INTO quiz_results (topic_id, score, total_questions)
        VALUES (?, ?, ?)
    """, (topic_id, correct_count, total))
    conn.commit()
    conn.close()

    percentage = round((correct_count / total * 100), 1) if total > 0 else 0
    return jsonify({
        "success": True,
        "score": correct_count,
        "total": total,
        "percentage": percentage,
        "details": details
    })

# ----------------- TECHNICAL CS API -----------------
@app.route('/api/prep/technical', methods=['GET'])
def get_technical_subjects():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, icon, summary FROM technical_subjects")
    subjects = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return jsonify({"success": True, "subjects": subjects})

@app.route('/api/prep/technical/<subject_id>', methods=['GET'])
def get_technical_subject_detail(subject_id):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM technical_subjects WHERE id = ?", (subject_id,))
    row = cursor.fetchone()
    if not row:
        conn.close()
        return jsonify({"success": False, "message": "Subject not found"}), 404

    sub = dict(row)
    sub['key_notes'] = json.loads(sub['key_notes']) if sub['key_notes'] else []
    sub['qa_list'] = json.loads(sub['qa_list']) if sub['qa_list'] else []
    conn.close()
    return jsonify({"success": True, "subject": sub})

# ----------------- HR API -----------------
@app.route('/api/prep/hr', methods=['GET'])
def get_hr_prep():
    from seed_data import HR_DATA
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM hr_questions")
    questions = [dict(r) for r in cursor.fetchall()]
    conn.close()

    return jsonify({
        "success": True,
        "star_framework": HR_DATA["star_framework"],
        "questions": questions
    })

# ----------------- COMPANIES HIRING PROCESS API -----------------
@app.route('/api/companies', methods=['GET'])
def get_companies():
    search = request.args.get('search', '').strip().lower()
    company_type = request.args.get('type', '').strip()

    conn = get_db()
    cursor = conn.cursor()

    query = "SELECT id, name, type, logo, tier, ctc FROM companies WHERE 1=1"
    params = []

    if search:
        query += " AND (LOWER(name) LIKE ? OR LOWER(type) LIKE ? OR LOWER(tier) LIKE ?)"
        term = f"%{search}%"
        params.extend([term, term, term])

    if company_type and company_type != 'All':
        query += " AND type LIKE ?"
        params.append(f"%{company_type}%")

    cursor.execute(query, params)
    companies = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return jsonify({"success": True, "count": len(companies), "companies": companies})

@app.route('/api/companies/<company_id>', methods=['GET'])
def get_company_detail(company_id):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM companies WHERE id = ?", (company_id,))
    row = cursor.fetchone()
    if not row:
        conn.close()
        return jsonify({"success": False, "message": "Company not found"}), 404

    comp = dict(row)
    comp['eligibility'] = json.loads(comp['eligibility']) if comp['eligibility'] else {}
    comp['exam_pattern'] = json.loads(comp['exam_pattern']) if comp['exam_pattern'] else {}
    comp['syllabus'] = json.loads(comp['syllabus']) if comp['syllabus'] else []
    comp['past_questions'] = json.loads(comp['past_questions']) if comp['past_questions'] else []
    conn.close()

    return jsonify({"success": True, "company": comp})

# ----------------- DEDICATED TOPIC-WISE DSA SHEET API -----------------
@app.route('/api/dsa/topics', methods=['GET'])
def get_dsa_topics():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT t.id, t.name, t.description, t.order_idx,
               COUNT(p.id) as total_problems,
               SUM(CASE WHEN up.is_solved = 1 THEN 1 ELSE 0 END) as solved_problems
        FROM dsa_topics t
        LEFT JOIN dsa_problems p ON t.id = p.topic_id
        LEFT JOIN dsa_user_progress up ON p.id = up.problem_id
        GROUP BY t.id
        ORDER BY t.order_idx ASC
    """)
    topics = []
    for r in cursor.fetchall():
        top = dict(r)
        top['solved_problems'] = top['solved_problems'] or 0
        top['progress_pct'] = round((top['solved_problems'] / top['total_problems'] * 100), 1) if top['total_problems'] > 0 else 0
        topics.append(top)

    conn.close()
    return jsonify({"success": True, "topics": topics})

@app.route('/api/dsa/problems', methods=['GET'])
def get_dsa_problems():
    topic_id = request.args.get('topic', '').strip()
    difficulty = request.args.get('difficulty', '').strip()
    status = request.args.get('status', '').strip()  # all, solved, unsolved, revision
    search = request.args.get('search', '').strip().lower()

    conn = get_db()
    cursor = conn.cursor()

    query = """
        SELECT p.id, p.topic_id, p.title, p.difficulty, p.leetcode_url, p.gfg_url,
               p.time_complexity, p.space_complexity, t.name as topic_name,
               COALESCE(up.is_solved, 0) as is_solved,
               COALESCE(up.needs_revision, 0) as needs_revision,
               COALESCE(up.notes, '') as notes
        FROM dsa_problems p
        JOIN dsa_topics t ON p.topic_id = t.id
        LEFT JOIN dsa_user_progress up ON p.id = up.problem_id
        WHERE 1=1
    """
    params = []

    if topic_id and topic_id != 'all':
        query += " AND p.topic_id = ?"
        params.append(topic_id)

    if difficulty and difficulty != 'all':
        query += " AND p.difficulty = ?"
        params.append(difficulty)

    if search:
        query += " AND (LOWER(p.title) LIKE ? OR LOWER(t.name) LIKE ?)"
        term = f"%{search}%"
        params.extend([term, term])

    if status == 'solved':
        query += " AND up.is_solved = 1"
    elif status == 'unsolved':
        query += " AND (up.is_solved IS NULL OR up.is_solved = 0)"
    elif status == 'revision':
        query += " AND up.needs_revision = 1"

    query += " ORDER BY t.order_idx ASC, p.id ASC"
    cursor.execute(query, params)
    problems = [dict(r) for r in cursor.fetchall()]
    conn.close()

    return jsonify({"success": True, "count": len(problems), "problems": problems})

@app.route('/api/dsa/problems/<problem_id>', methods=['GET'])
def get_dsa_problem_detail(problem_id):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT p.*, t.name as topic_name,
               COALESCE(up.is_solved, 0) as is_solved,
               COALESCE(up.needs_revision, 0) as needs_revision,
               COALESCE(up.notes, '') as notes
        FROM dsa_problems p
        JOIN dsa_topics t ON p.topic_id = t.id
        LEFT JOIN dsa_user_progress up ON p.id = up.problem_id
        WHERE p.id = ?
    """, (problem_id,))
    row = cursor.fetchone()

    if not row:
        conn.close()
        return jsonify({"success": False, "message": "Problem not found"}), 404

    prob = dict(row)
    prob['code'] = json.loads(prob['code']) if prob['code'] else {}
    conn.close()
    return jsonify({"success": True, "problem": prob})

@app.route('/api/dsa/problems/<problem_id>/progress', methods=['POST'])
def update_dsa_progress(problem_id):
    data = request.json or {}
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT is_solved, needs_revision, notes FROM dsa_user_progress WHERE problem_id = ?", (problem_id,))
    existing = cursor.fetchone()

    if existing:
        is_solved = data.get('is_solved', existing['is_solved'])
        needs_revision = data.get('needs_revision', existing['needs_revision'])
        notes = data.get('notes', existing['notes'])

        cursor.execute("""
            UPDATE dsa_user_progress 
            SET is_solved = ?, needs_revision = ?, notes = ?, updated_at = CURRENT_TIMESTAMP
            WHERE problem_id = ?
        """, (1 if is_solved else 0, 1 if needs_revision else 0, notes, problem_id))
    else:
        is_solved = data.get('is_solved', 0)
        needs_revision = data.get('needs_revision', 0)
        notes = data.get('notes', '')

        cursor.execute("""
            INSERT INTO dsa_user_progress (problem_id, is_solved, needs_revision, notes)
            VALUES (?, ?, ?, ?)
        """, (problem_id, 1 if is_solved else 0, 1 if needs_revision else 0, notes))

    conn.commit()
    conn.close()

    return jsonify({
        "success": True,
        "problem_id": problem_id,
        "is_solved": bool(is_solved),
        "needs_revision": bool(needs_revision),
        "message": "Progress updated successfully!"
    })

# ----------------- OVERVIEW STATS API -----------------
@app.route('/api/stats', methods=['GET'])
def get_stats():
    conn = get_db()
    cursor = conn.cursor()

    # Total jobs
    cursor.execute("SELECT COUNT(*) FROM jobs")
    total_jobs = cursor.fetchone()[0]

    # Applications submitted
    cursor.execute("SELECT COUNT(*) FROM applications")
    total_applications = cursor.fetchone()[0]

    # Saved jobs
    cursor.execute("SELECT COUNT(*) FROM bookmarks")
    total_bookmarks = cursor.fetchone()[0]

    # DSA Stats
    cursor.execute("SELECT COUNT(*) FROM dsa_problems")
    total_dsa = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM dsa_user_progress WHERE is_solved = 1")
    solved_dsa = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM dsa_user_progress WHERE needs_revision = 1")
    revision_dsa = cursor.fetchone()[0]

    # Aptitude Quizzes
    cursor.execute("SELECT COUNT(*), AVG(score * 100.0 / total_questions) FROM quiz_results")
    quiz_row = cursor.fetchone()
    quizzes_taken = quiz_row[0] or 0
    avg_quiz_score = round(quiz_row[1], 1) if quiz_row[1] is not None else 0

    # Total companies
    cursor.execute("SELECT COUNT(*) FROM companies")
    total_companies = cursor.fetchone()[0]

    conn.close()

    return jsonify({
        "success": True,
        "jobs": {
            "total": total_jobs,
            "applied": total_applications,
            "bookmarked": total_bookmarks
        },
        "dsa": {
            "total": total_dsa,
            "solved": solved_dsa,
            "revision": revision_dsa,
            "percentage": round((solved_dsa / total_dsa * 100), 1) if total_dsa > 0 else 0
        },
        "aptitude": {
            "quizzes_taken": quizzes_taken,
            "avg_score": avg_quiz_score
        },
        "companies_count": total_companies
    })

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
