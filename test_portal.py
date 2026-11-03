import sys
import json
sys.path.append(r'C:\Users\Win11\.gemini\antigravity\scratch\job-prep-portal')
from app import app

client = app.test_client()

# 1. Main Page
res = client.get('/')
assert res.status_code == 200, f'Index failed: {res.status_code}'
print('✓ 1. Index HTML loaded successfully (200 OK)')

# 2. Jobs API
res = client.get('/api/jobs')
data = res.get_json()
assert data['success'] and len(data['jobs']) >= 8
print(f'✓ 2. Jobs API: {len(data["jobs"])} jobs retrieved')

# 3. Bookmark toggle
res = client.post('/api/jobs/job-1/bookmark')
data = res.get_json()
assert data['success'] and 'is_bookmarked' in data
print(f'✓ 3. Bookmark toggle succeeded (state: {data["is_bookmarked"]})')

# 4. Apply
import time
res = client.post('/api/jobs/job-1/apply', json={
    'full_name': 'Aarav Sharma',
    'email': f'aarav_{int(time.time())}@example.com',
    'phone': '+91 9876543210',
    'college': 'IIT Delhi',
    'graduation_year': '2026',
    'cgpa': '9.1',
    'cover_note': 'Strong background in algorithms and distributed systems.'
})
data = res.get_json()
assert data['success']
print('✓ 4. Job application submitted')

# 5. Applications list
res = client.get('/api/applications')
data = res.get_json()
assert data['success'] and len(data['applications']) >= 1
print(f'✓ 5. Applications retrieved: {len(data["applications"])}')

# 6. Aptitude
res = client.get('/api/prep/aptitude')
data = res.get_json()
assert data['success'] and len(data['topics']) >= 6
print(f'✓ 6. Aptitude topics: {len(data["topics"])}')

# 7. Aptitude Quiz submission
res = client.post('/api/prep/aptitude/quiz/submit', json={
    'topic_id': 'time-and-work',
    'answers': {'tw-1': 0, 'tw-2': 0}
})
data = res.get_json()
assert data['success'] and data['score'] >= 1
print(f'✓ 7. Quiz evaluated: {data["score"]}/{data["total"]} ({data["percentage"]}%)')

# 8. Technical
res = client.get('/api/prep/technical/dbms')
data = res.get_json()
assert data['success'] and len(data['subject']['key_notes']) >= 4
print('✓ 8. Technical CS notes and Q&A retrieved')

# 9. HR
res = client.get('/api/prep/hr')
data = res.get_json()
assert data['success'] and len(data['questions']) >= 5
print(f'✓ 9. HR questions & STAR framework: {len(data["questions"])} questions')

# 10. Companies
res = client.get('/api/companies/google')
data = res.get_json()
assert data['success'] and data['company']['name'] == 'Google'
assert len(data['company']['exam_pattern']['rounds']) >= 4
print('✓ 10. Company hiring guide retrieved (Google)')

# 11. DSA Progress
res = client.post('/api/dsa/problems/dsa-1/progress', json={
    'is_solved': 1,
    'needs_revision': 1,
    'notes': 'Optimal hashmap complement lookup in O(N) time and O(N) space.'
})
data = res.get_json()
assert data['success'] and data['is_solved'] == True
print('✓ 11. DSA Progress & Notes saved')

# 12. Stats
res = client.get('/api/stats')
data = res.get_json()
assert data['success']
print(f'✓ 12. Stats Dashboard verified: Jobs Applied={data["jobs"]["applied"]}, DSA Solved={data["dsa"]["solved"]}')

print('\n========================================')
print('🎉 ALL 12 INTEGRATION TESTS PASSED!')
print('========================================')
