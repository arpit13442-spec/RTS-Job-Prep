"""
Seed data for Job Portal & Preparation Platform
Contains comprehensive data for:
1. Jobs & Internships
2. Aptitude (Quantitative, Logical, Verbal) notes, formulas, and practice MCQs
3. Technical (DBMS, OS, CN, OOP, System Design) notes and interview Q&As
4. HR Preparation (STAR framework, common questions, sample answers)
5. Companies Hiring Process (Exam Pattern, Syllabus, Eligibility, CTC, Questions)
6. Dedicated Topic-wise DSA Sheet (Arrays, Strings, Linked Lists, Trees, DP, Graphs, etc.)
"""

JOBS_DATA = [
    {
        "id": "job-1",
        "title": "Software Development Engineer - I (SDE-1)",
        "company": "Amazon",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Amazon_icon.svg",
        "location": "Bengaluru / Hyderabad (Hybrid)",
        "type": "Full-Time",
        "category": "Software Engineering",
        "experience": "0-2 Years",
        "salary": "₹18 - ₹24 LPA + Stocks",
        "work_mode": "Hybrid",
        "posted_date": "2 days ago",
        "deadline": "2026-11-30",
        "description": "Amazon is seeking ambitious Software Engineers to build scalable, high-throughput distributed systems that power global e-commerce and cloud infrastructure.",
        "responsibilities": [
            "Design and build robust, high-performance microservices using Java/C++ and AWS.",
            "Collaborate with product managers and principal engineers on architecture.",
            "Write clean, unit-tested, maintainable code following CI/CD practices.",
            "Participate in on-call rotations and monitor production latency metrics."
        ],
        "requirements": [
            "B.Tech/M.Tech in CS/IT or related STEM field (2024-2026 batches).",
            "Strong foundation in Data Structures, Algorithms, and Object-Oriented Design.",
            "Proficiency in at least one modern language (Java, C++, Python, Go).",
            "Understanding of distributed storage, relational databases (SQL), and REST APIs."
        ],
        "tags": ["Java", "AWS", "Distributed Systems", "DSA", "SQL"]
    },
    {
        "id": "job-2",
        "title": "Graduate Software Engineer (Campus 2026)",
        "company": "Google",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg",
        "location": "Bengaluru / Pune (Onsite)",
        "type": "Full-Time",
        "category": "Software Engineering",
        "experience": "Freshers (0 Years)",
        "salary": "₹22 - ₹32 LPA + Equity",
        "work_mode": "Onsite",
        "posted_date": "Just now",
        "deadline": "2026-11-25",
        "description": "Google software engineers develop next-generation technologies that change how billions of users connect, explore, and interact with information.",
        "responsibilities": [
            "Solve complex computational challenges in distributed search, cloud, and AI.",
            "Implement algorithms with optimal space and time guarantees.",
            "Conduct automated testing, peer code reviews, and performance profiling."
        ],
        "requirements": [
            "Bachelor's or Master's degree in Computer Science or equivalent.",
            "Superb problem-solving skills with competitive programming or deep DSA background.",
            "Fluency in C++, Java, or Python.",
            "Knowledge of OS internals, concurrency, and network protocols."
        ],
        "tags": ["C++", "Python", "Algorithms", "System Design", "Cloud"]
    },
    {
        "id": "job-3",
        "title": "Software Engineer - Frontend & Full Stack",
        "company": "Atlassian",
        "logo": "https://cdn.iconscout.com/icon/free/png-256/free-atlassian-logo-icon-download-in-svg-png-gif-file-formats--brand-social-media-pack-logos-icons-226522.png?f=webp&w=256",
        "location": "Remote (India)",
        "type": "Full-Time",
        "category": "Frontend / Full Stack",
        "experience": "1-3 Years",
        "salary": "₹24 - ₹30 LPA",
        "work_mode": "Remote",
        "posted_date": "1 day ago",
        "deadline": "2026-12-05",
        "description": "Join the Jira & Confluence teams to revolutionize developer and team collaboration tools using modern TypeScript, React, and GraphQL.",
        "responsibilities": [
            "Build reactive, accessible user interfaces with React, TypeScript, and state machines.",
            "Design GraphQL endpoints and micro-frontends with high test coverage.",
            "Optimize frontend bundle sizes, Core Web Vitals, and rendering pipelines."
        ],
        "requirements": [
            "Proficient with TypeScript, modern ECMAScript, React, and CSS architecture.",
            "Experience with state management, REST/GraphQL, and client caching.",
            "Good knowledge of browser DOM, event loop, and web security (CORS, XSS)."
        ],
        "tags": ["React", "TypeScript", "Node.js", "GraphQL", "Remote"]
    },
    {
        "id": "job-4",
        "title": "Digital Technology Specialist (Cadre Digital)",
        "company": "TCS (Tata Consultancy Services)",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/b/b1/Tata_Consultancy_Services_Logo.svg",
        "location": "Pan India (Mumbai / Pune / Chennai / Gurgaon / Kolkata)",
        "type": "Full-Time",
        "category": "IT & Services",
        "experience": "Freshers (0-1 Year)",
        "salary": "₹7.5 - ₹9 LPA",
        "work_mode": "Hybrid",
        "posted_date": "3 days ago",
        "deadline": "2026-12-15",
        "description": "TCS Digital offers roles for high-performing engineering freshers to work on cutting-edge digital transformation, Cloud, AI, and enterprise full-stack development.",
        "responsibilities": [
            "Develop enterprise applications for Fortune 500 financial and healthcare clients.",
            "Work with modern cloud platforms (Azure, AWS, GCP) and containerization.",
            "Participate in agile sprints and continuous integration pipelines."
        ],
        "requirements": [
            "BE/B.Tech/ME/M.Tech/MCA/M.Sc with 60% or 6.0 CGPA throughout academics.",
            "No active backlogs at the time of appearance.",
            "Foundational skills in Python, Java, SQL, and Web technologies.",
            "Strong cognitive aptitude and logical reasoning abilities."
        ],
        "tags": ["Java", "Python", "SQL", "Cloud", "Freshers"]
    },
    {
        "id": "job-5",
        "title": "Associate Software Engineer (ASE)",
        "company": "Accenture",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/c/cd/Accenture.svg",
        "location": "Bengaluru / Hyderabad / Pune / NCR",
        "type": "Full-Time",
        "category": "IT & Services",
        "experience": "Freshers (0 Years)",
        "salary": "₹4.5 - ₹6.5 LPA",
        "work_mode": "Hybrid",
        "posted_date": "4 days ago",
        "deadline": "2026-12-20",
        "description": "Kickstart your technology consulting career with Accenture's Advanced Technology Centers in India (ATCI).",
        "responsibilities": [
            "Develop, test, and maintain enterprise software components.",
            "Analyze business requirements and translate them into technical modules.",
            "Collaborate in cross-functional global teams."
        ],
        "requirements": [
            "B.E/B.Tech (All streams) or MCA/M.Sc (CS/IT).",
            "Minimum 65% aggregate or 6.5 CGPA with no pending backlogs.",
            "Basic knowledge of OOP, Relational Databases, and Scripting."
        ],
        "tags": ["C++", "Java", "Database", "Freshers", "Consulting"]
    },
    {
        "id": "job-6",
        "title": "Backend Engineering Intern (Summer 2027)",
        "company": "Razorpay",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/8/89/Razorpay_logo.svg",
        "location": "Bengaluru (Onsite)",
        "type": "Internship",
        "category": "Fintech / Backend",
        "experience": "Students / Pre-Final Year",
        "salary": "₹45,000 - ₹60,000 / month Stipend (PPO Eligible: ₹20 LPA)",
        "work_mode": "Onsite",
        "posted_date": "3 days ago",
        "deadline": "2026-12-10",
        "description": "Experience building India's premier payments gateway handling millions of real-time transactions per second.",
        "responsibilities": [
            "Build reliable payment processing pipelines with Go, PHP, or Python.",
            "Work with Redis caching, Kafka message queues, and MySQL sharding.",
            "Implement high-availability fault-tolerant APIs."
        ],
        "requirements": [
            "Penultimate year B.Tech/Dual degree students graduating in 2026 or 2027.",
            "Solid grasp of Data Structures, Concurrency, and Database Indexes.",
            "Prior open source contributions or hackathon projects are a big plus."
        ],
        "tags": ["Go", "Kafka", "Redis", "Fintech", "Internship"]
    },
    {
        "id": "job-7",
        "title": "Systems Engineer - Specialist Programmer (Power Programmer)",
        "company": "Infosys",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/9/95/Infosys_logo.svg",
        "location": "Bengaluru / Mysuru / Hyderabad",
        "type": "Full-Time",
        "category": "Software Engineering",
        "experience": "Freshers (0-1 Year)",
        "salary": "₹9.5 - ₹11.5 LPA",
        "work_mode": "Hybrid",
        "posted_date": "5 days ago",
        "deadline": "2026-12-18",
        "description": "Specialist Programmer (SP) is an elite coding role at Infosys aimed at top competitive programmers who tackle hardest algorithmic challenges.",
        "responsibilities": [
            "Develop core microservices, AI accelerators, and cloud-native solutions.",
            "Architect frameworks and lead sprint technical prototypes."
        ],
        "requirements": [
            "Strong competitive programming ranking (Codeforces, LeetCode, CodeChef).",
            "Advanced algorithmic knowledge: DP, Graph algorithms, Trees, Bit manipulation.",
            "Eligibility: B.E/B.Tech/M.E/M.Tech with 60%+ marks."
        ],
        "tags": ["DSA", "Competitive Programming", "Algorithms", "C++", "Java"]
    },
    {
        "id": "job-8",
        "title": "Software Development Engineer (Full Stack)",
        "company": "Microsoft",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/9/96/Microsoft_logo_%282012%29.svg",
        "location": "Hyderabad / Noida (Hybrid)",
        "type": "Full-Time",
        "category": "Software Engineering",
        "experience": "0-2 Years",
        "salary": "₹20 - ₹28 LPA + RSUs",
        "work_mode": "Hybrid",
        "posted_date": "1 day ago",
        "deadline": "2026-11-28",
        "description": "Build intelligent services and enterprise cloud tooling for Microsoft Azure, Office 365, and Developer tools.",
        "responsibilities": [
            "Design scalable backend services using C#/.NET Core and Azure microservices.",
            "Build modern web portals with TypeScript and React.",
            "Participate in design reviews and implement security/privacy compliance."
        ],
        "requirements": [
            "B.S./B.Tech or M.S. in Computer Science or related degree.",
            "Solid understanding of CS fundamentals, data structures, and multi-threading.",
            "Experience with C#, C++, Java, or Go."
        ],
        "tags": ["C#", ".NET", "Azure", "React", "Cloud"]
    }
]

# APTITUDE PREPARATION DATA
APTITUDE_DATA = {
    "topics": [
        {
            "id": "time-and-work",
            "name": "Time and Work",
            "category": "Quantitative",
            "icon": "fa-clock",
            "concept": "Time and Work problems examine the relationship between the number of workers, work done, and time taken. The fundamental principle is that Work = Rate × Time. If a person completes a task in 'n' days, their 1-day work is 1/n.",
            "formulas": [
                {"title": "1-Day Work", "formula": "If A can do a job in 'n' days, then A's 1-day work = 1/n"},
                {"title": "Combined Work Rate", "formula": "If A takes 'x' days and B takes 'y' days, combined 1-day work = (1/x) + (1/y) = (x + y)/(xy)"},
                {"title": "Total Time Taken Together", "formula": "Time = (x * y) / (x + y) days"},
                {"title": "Work & Wages Ratio", "formula": "Wages are distributed in the ratio of the work done by each individual per day: (1/x) : (1/y)"},
                {"title": "Men, Days, Hours, Work (MDH)", "formula": "(M1 * D1 * H1) / W1 = (M2 * D2 * H2) / W2"}
            ],
            "questions": [
                {
                    "id": "tw-1",
                    "question": "A can do a piece of work in 12 days, and B can do the same work in 18 days. If they work together, how many days will they take to complete the work?",
                    "options": ["7.2 days", "8.5 days", "6.0 days", "9.0 days"],
                    "correct": 0,
                    "explanation": "A's 1-day work = 1/12. B's 1-day work = 1/18.\nCombined 1-day work = 1/12 + 1/18 = (3 + 2)/36 = 5/36.\nTotal days required = 36 / 5 = 7.2 days."
                },
                {
                    "id": "tw-2",
                    "question": "12 men can complete a project in 8 days working 6 hours a day. How many days will 16 men take to complete the same work working 4 hours a day?",
                    "options": ["9 days", "8 days", "10 days", "12 days"],
                    "correct": 0,
                    "explanation": "Using MDH formula: (M1 * D1 * H1) = (M2 * D2 * H2)\n12 * 8 * 6 = 16 * D2 * 4\n576 = 64 * D2\nD2 = 576 / 64 = 9 days."
                },
                {
                    "id": "tw-3",
                    "question": "A and B can complete a work in 15 days and 10 days respectively. They started together, but B left after 2 days. How long will A take to finish the remaining work?",
                    "options": ["10 days", "12 days", "11 days", "8 days"],
                    "correct": 0,
                    "explanation": "Together 1-day work = (1/15) + (1/10) = 5/30 = 1/6.\nIn 2 days, work done = 2 * (1/6) = 1/3.\nRemaining work = 1 - 1/3 = 2/3.\nTime taken by A alone = (2/3) / (1/15) = (2/3) * 15 = 10 days."
                }
            ]
        },
        {
            "id": "speed-distance-time",
            "name": "Speed, Distance & Time",
            "category": "Quantitative",
            "icon": "fa-tachometer-alt",
            "concept": "Speed measures rate of travel: Speed = Distance / Time. Units conversion: 1 km/hr = 5/18 m/s, and 1 m/s = 18/5 km/hr. Average Speed = Total Distance / Total Time.",
            "formulas": [
                {"title": "Fundamental Relation", "formula": "Speed = Distance / Time ; Distance = Speed * Time"},
                {"title": "km/h to m/s conversion", "formula": "x km/hr = x * (5/18) m/s ; x m/s = x * (18/5) km/hr"},
                {"title": "Average Speed (Equal Distances)", "formula": "Avg Speed = (2 * S1 * S2) / (S1 + S2)"},
                {"title": "Relative Speed (Same Direction)", "formula": "Relative Speed = |S1 - S2|"},
                {"title": "Relative Speed (Opposite Direction)", "formula": "Relative Speed = S1 + S2"},
                {"title": "Train Crossing a Pole / Person", "formula": "Time = Length of Train / Speed of Train"},
                {"title": "Train Crossing a Platform / Bridge", "formula": "Time = (Length of Train + Length of Platform) / Speed of Train"}
            ],
            "questions": [
                {
                    "id": "sdt-1",
                    "question": "A car travels from City A to City B at 60 km/hr and returns from City B to City A at 40 km/hr. What is the average speed for the entire journey?",
                    "options": ["48 km/hr", "50 km/hr", "52 km/hr", "45 km/hr"],
                    "correct": 0,
                    "explanation": "Since distances are equal, Average Speed = (2 * S1 * S2) / (S1 + S2) = (2 * 60 * 40) / (60 + 40) = 4800 / 100 = 48 km/hr. Note: It is NOT the arithmetic mean (50)."
                },
                {
                    "id": "sdt-2",
                    "question": "A train 180 meters long is running at 72 km/hr. How much time does it take to cross a platform 220 meters long?",
                    "options": ["20 seconds", "18 seconds", "25 seconds", "15 seconds"],
                    "correct": 0,
                    "explanation": "Speed = 72 * (5/18) = 20 m/s.\nTotal Distance = Length of Train + Length of Platform = 180 + 220 = 400 m.\nTime = Distance / Speed = 400 / 20 = 20 seconds."
                }
            ]
        },
        {
            "id": "percentages-profit-loss",
            "name": "Percentages, Profit & Loss",
            "category": "Quantitative",
            "icon": "fa-percent",
            "concept": "Percentage means per hundred. Profit occurs when Selling Price (SP) > Cost Price (CP). Loss occurs when CP > SP. Profit% and Loss% are always calculated on the Cost Price (CP) unless stated otherwise.",
            "formulas": [
                {"title": "Profit and Loss", "formula": "Profit = SP - CP ; Loss = CP - SP"},
                {"title": "Profit % & Loss %", "formula": "Profit % = (Profit / CP) * 100 ; Loss % = (Loss / CP) * 100"},
                {"title": "SP with Profit %", "formula": "SP = CP * (100 + Profit%) / 100"},
                {"title": "SP with Loss %", "formula": "SP = CP * (100 - Loss%) / 100"},
                {"title": "Discount and Marked Price", "formula": "Discount = Marked Price (MP) - SP ; Discount % = (Discount / MP) * 100"}
            ],
            "questions": [
                {
                    "id": "pl-1",
                    "question": "An article is sold for ₹840 at a profit of 20%. What was the cost price of the article?",
                    "options": ["₹700", "₹680", "₹720", "₹750"],
                    "correct": 0,
                    "explanation": "SP = CP * 1.20 => 840 = CP * 1.20 => CP = 840 / 1.20 = ₹700."
                },
                {
                    "id": "pl-2",
                    "question": "If the price of petrol increases by 25%, by what percentage must a driver reduce their consumption so that the total expenditure remains unchanged?",
                    "options": ["20%", "25%", "16.66%", "30%"],
                    "correct": 0,
                    "explanation": "Formula: Reduction % = [r / (100 + r)] * 100 = [25 / (100 + 25)] * 100 = (25 / 125) * 100 = 20%."
                }
            ]
        },
        {
            "id": "logical-syllogisms",
            "name": "Syllogisms & Deductive Logic",
            "category": "Logical",
            "icon": "fa-brain",
            "concept": "Syllogism questions present premises assumed to be true, followed by conclusions. Use Venn diagrams to test whether conclusions definitely follow in all possible representations.",
            "formulas": [
                {"title": "All A are B", "formula": "Circle A is completely inside circle B"},
                {"title": "Some A are B", "formula": "Circle A and Circle B overlap at least partially"},
                {"title": "No A is B", "formula": "Circle A and Circle B are completely disjoint with zero intersection"},
                {"title": "Either-Or Condition", "formula": "Both conclusions are independently uncertain + one is positive ('Some') and one is negative ('No') + same subject and predicate"}
            ],
            "questions": [
                {
                    "id": "syl-1",
                    "question": "Statements:\n1. All cars are vehicles.\n2. All vehicles are machines.\nConclusions:\nI. All cars are machines.\nII. Some machines are cars.",
                    "options": ["Both I and II follow", "Only I follows", "Only II follows", "Neither follows"],
                    "correct": 0,
                    "explanation": "Cars ⊂ Vehicles ⊂ Machines. Therefore all cars are machines (I follows). Since cars exist inside machines, some machines are cars (II follows). Both conclusions follow."
                },
                {
                    "id": "syl-2",
                    "question": "Statements:\n1. Some pens are pencils.\n2. All pencils are erasers.\nConclusions:\nI. Some pens are erasers.\nII. No eraser is a pen.",
                    "options": ["Only I follows", "Only II follows", "Either I or II follows", "Neither follows"],
                    "correct": 0,
                    "explanation": "Some pens overlap with pencils, and all pencils are inside erasers. The overlapping portion of pens with pencils is definitively inside erasers. Therefore 'Some pens are erasers' is certainly TRUE. Conclusion II is false."
                }
            ]
        },
        {
            "id": "blood-relations",
            "name": "Blood Relations & Family Tree",
            "category": "Logical",
            "icon": "fa-users",
            "concept": "Blood relation problems test logical deduction of family connections. Draw a generational tree: Horizontal lines for siblings/spouses (+/- for gender), vertical lines for generation changes (parent-child).",
            "formulas": [
                {"title": "Generations Notation", "formula": "+: Male, -: Female, =: Married couple, ---: Siblings, |: Parent to child"},
                {"title": "Maternal vs Paternal", "formula": "Maternal = Mother's side (Maternal Uncle, etc.), Paternal = Father's side"}
            ],
            "questions": [
                {
                    "id": "br-1",
                    "question": "Pointing to a photograph of a boy, Suresh said, 'He is the son of the only son of my mother.' How is Suresh related to that boy?",
                    "options": ["Father", "Uncle", "Brother", "Grandfather"],
                    "correct": 0,
                    "explanation": "'The only son of my mother' means Suresh himself (assuming Suresh is male). So the boy is the son of Suresh. Hence, Suresh is the father."
                },
                {
                    "id": "br-2",
                    "question": "A is B's brother. C is A's mother. D is C's father. E is B's son. How is D related to A?",
                    "options": ["Maternal Grandfather", "Grandfather", "Father", "Uncle"],
                    "correct": 0,
                    "explanation": "A's mother is C. D is C's father. The father of one's mother is Maternal Grandfather."
                }
            ]
        },
        {
            "id": "verbal-ability",
            "name": "Verbal Ability & Grammar",
            "category": "Verbal",
            "icon": "fa-book-open",
            "concept": "Verbal tests evaluate grammar rules (Subject-Verb Agreement, Tenses, Modifiers, Parallelism), vocabulary, and reading comprehension logic.",
            "formulas": [
                {"title": "Subject-Verb Agreement", "formula": "Singular subject requires singular verb; plural subject requires plural verb. Neither/Nor takes verb of nearest subject."},
                {"title": "Modifier Placement", "formula": "A modifying phrase must be placed directly adjacent to the noun it modifies."}
            ],
            "questions": [
                {
                    "id": "va-1",
                    "question": "Identify the grammatically correct sentence:",
                    "options": [
                        "Neither the manager nor the employees were informed about the schedule change.",
                        "Neither the manager nor the employees was informed about the schedule change.",
                        "Neither the manager or the employees were informed about the schedule change.",
                        "Neither the manager nor the employee were informed about the schedule change."
                    ],
                    "correct": 0,
                    "explanation": "In 'Neither...nor' constructions, the verb agrees with the closer subject. 'Employees' is plural, so 'were informed' is correct."
                },
                {
                    "id": "va-2",
                    "question": "Choose the word that is most nearly OPPOSITE in meaning to 'METICULOUS':",
                    "options": ["Careless", "Thorough", "Painstaking", "Punctual"],
                    "correct": 0,
                    "explanation": "'Meticulous' means showing great attention to detail; very careful and precise. Its direct opposite (antonym) is 'Careless' or 'Sloppy'."
                }
            ]
        }
    ]
}

# TECHNICAL PREPARATION DATA (Core CS)
TECHNICAL_DATA = {
    "subjects": [
        {
            "id": "dbms",
            "name": "Database Management Systems (DBMS)",
            "icon": "fa-database",
            "summary": "Core concepts in Relational Databases, ACID transactions, Normalization, SQL, Indexing, and NoSQL architecture.",
            "key_notes": [
                "ACID Properties: Atomicity (all or nothing), Consistency (preserves invariants), Isolation (concurrent transactions execute as if sequential), Durability (committed data survives crashes).",
                "Normalization: 1NF (atomic values, no repeating groups), 2NF (in 1NF and no partial dependencies on composite primary key), 3NF (in 2NF and no transitive functional dependencies), BCNF (for every functional dependency X -> Y, X must be a super key).",
                "Indexing: B+ Trees are preferred over Hash Indexes for range queries. Clustered index determines physical sorting order (only 1 per table); Non-clustered index stores pointers to rows.",
                "Joins: INNER JOIN, LEFT OUTER JOIN, RIGHT OUTER JOIN, FULL OUTER JOIN, CROSS JOIN.",
                "Deadlocks: Occur when two transactions hold locks that each other requires. Prevented via 2-Phase Locking (2PL), wait-die or wound-wait schemes."
            ],
            "qa_list": [
                {
                    "q": "What is the difference between TRUNCATE, DROP, and DELETE?",
                    "a": "DELETE is a DML (Data Manipulation Language) command that removes rows one by one, logs each row deletion (allowing ROLLBACK), and activates database triggers.\nTRUNCATE is a DDL command that deallocates entire data pages, is faster, cannot be rolled back in many DBMS, and resets auto-increment counters.\nDROP is a DDL command that removes both data and the table schema definition completely from the database catalog."
                },
                {
                    "q": "What are Clustered vs Non-Clustered Indexes?",
                    "a": "A Clustered Index physically reorders the rows of the table on disk to match the index key order. Because data can only be sorted in one way physically, there can be only ONE clustered index per table (typically the Primary Key).\nA Non-Clustered Index is an auxiliary structure containing sorted key values paired with row pointers (RID or clustered key) pointing to the actual data location. A table can have multiple non-clustered indexes."
                },
                {
                    "q": "Explain the CAP Theorem in distributed databases.",
                    "a": "CAP Theorem states that a distributed data store can simultaneously guarantee at most two out of three properties:\n1. Consistency: Every read receives the most recent write or an error.\n2. Availability: Every non-failing node returns a non-error response.\n3. Partition Tolerance: The system continues to operate despite network packet loss or network partitions.\nIn distributed networks where network partitions are inevitable (P is mandatory), systems must trade off between Consistency (CP, e.g. HBase, MongoDB) or Availability (AP, e.g. Cassandra, DynamoDB)."
                }
            ]
        },
        {
            "id": "os",
            "name": "Operating Systems (OS)",
            "icon": "fa-microchip",
            "summary": "Processes, Threads, Concurrency, Synchronization, Deadlocks, Memory Management, and Virtual Memory.",
            "key_notes": [
                "Process vs Thread: A process is an independent program in execution with its own isolated address space (code, data, heap, stack). A thread is a lightweight unit of execution within a process that shares code, data, and heap, but has its own stack and registers.",
                "Deadlock Coffman Conditions: 1. Mutual Exclusion, 2. Hold and Wait, 3. No Preemption, 4. Circular Wait. Breaking any one condition prevents deadlocks.",
                "CPU Scheduling: First-Come First-Served (FCFS), Shortest Job First (SJF), Round Robin (RR), Priority Scheduling, Multi-Level Feedback Queue.",
                "Virtual Memory & Paging: Paging divides logical memory into fixed pages and physical memory into page frames. Page faults happen when a referenced page is not in RAM, causing OS to load it from secondary storage (LRU, FIFO replacement)."
            ],
            "qa_list": [
                {
                    "q": "What is the difference between Mutex and Semaphore?",
                    "a": "A Mutex (Mutual Exclusion) is a locking mechanism used to synchronize access to a single shared resource. It has ownership: only the thread that locked the mutex can unlock it (binary lock).\nA Semaphore is a signaling mechanism (using integer counter). It allows multiple threads (up to count N) to access a resource pool simultaneously. Wait (P) decrements counter, Signal (V) increments. Any thread can signal a semaphore; there is no concept of ownership."
                },
                {
                    "q": "What is Thrashing in Operating Systems?",
                    "a": "Thrashing occurs when the system spends more time swapping pages in and out of secondary storage (page faults) than executing actual instructions. It happens when the total working set size of all active processes exceeds available physical RAM. Solved by the Working Set Model or decreasing degree of multiprogramming."
                },
                {
                    "q": "How does context switching work?",
                    "a": "Context switching is the mechanism of saving the state of the currently running process/thread (PCB: Program Counter, CPU registers, stack pointers) into memory and restoring the state of the next ready process so it can resume execution on the CPU."
                }
            ]
        },
        {
            "id": "cn",
            "name": "Computer Networks (CN)",
            "icon": "fa-network-wired",
            "summary": "OSI and TCP/IP models, Transport layer protocols (TCP/UDP), Routing, DNS, HTTP/HTTPS, and Socket programming.",
            "key_notes": [
                "TCP vs UDP: TCP is connection-oriented, reliable (guaranteed delivery via ACKs and retransmissions), flow-controlled (sliding window), and ordered. UDP is connectionless, unreliable, lightweight, and suitable for low-latency streaming and gaming.",
                "TCP 3-Way Handshake: SYN -> SYN-ACK -> ACK establishes reliable full-duplex sequence numbers.",
                "DNS Lookup: Browser Cache -> OS Cache -> Local Resolver -> Root Nameserver (.) -> TLD Nameserver (.com) -> Authoritative Nameserver -> IP returned.",
                "HTTPS/TLS Handshake: Uses asymmetric encryption (RSA/ECC) to authenticate and securely negotiate a symmetric session key (AES) for encrypted communication."
            ],
            "qa_list": [
                {
                    "q": "What happens when you type https://www.google.com in your browser and press Enter?",
                    "a": "1. DNS Resolution: Browser resolves domain to IP address via local cache or recursive DNS hierarchy.\n2. TCP Handshake: Client initiates 3-way handshake (SYN, SYN-ACK, ACK) with server IP on port 443.\n3. TLS/SSL Handshake: Client and server exchange certificates, verify identity, and agree on symmetric encryption key.\n4. HTTP Request: Client sends HTTP GET request encrypted with session key.\n5. Server Processing: Web server/load balancer processes request and returns HTTP 200 response with HTML/CSS/JS payload.\n6. Browser Rendering: DOM tree and CSSOM are constructed, layout calculated, and pixels painted on screen."
                },
                {
                    "q": "What is the difference between HTTP/1.1, HTTP/2, and HTTP/3?",
                    "a": "HTTP/1.1 introduced persistent connections, but suffered from Head-of-Line (HoL) blocking at application level.\nHTTP/2 introduced binary framing, multiplexing multiple streams over a single TCP connection, and header compression (HPACK).\nHTTP/3 replaces TCP with QUIC protocol (built over UDP), eliminating TCP-level Head-of-Line blocking and enabling zero-RTT handshakes."
                }
            ]
        },
        {
            "id": "oops",
            "name": "Object-Oriented Programming (OOP) & SOLID",
            "icon": "fa-cubes",
            "summary": "The 4 Pillars of OOP, SOLID Principles, and Core Software Design Patterns.",
            "key_notes": [
                "4 Pillars: Encapsulation (data hiding via access modifiers), Abstraction (hiding implementation details via interfaces/abstract classes), Inheritance (code reuse and hierarchical taxonomy), Polymorphism (compile-time overloading and runtime method overriding).",
                "SOLID Principles: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion.",
                "Design Patterns: Creational (Singleton, Factory, Builder), Structural (Adapter, Decorator, Facade), Behavioral (Observer, Strategy, Command)."
            ],
            "qa_list": [
                {
                    "q": "Explain the SOLID principles with quick examples.",
                    "a": "S - Single Responsibility: A class should have only one reason to change (e.g., separate InvoiceCalculator from InvoicePrinter).\nO - Open/Closed: Software entities should be open for extension but closed for modification (use interfaces/abstract strategies).\nL - Liskov Substitution: Subclasses must be substitutable for their base classes without breaking correctness (e.g. Square inheriting Rectangle can violate area calculations).\nI - Interface Segregation: Clients should not be forced to depend on methods they do not use (prefer small, role-specific interfaces).\nD - Dependency Inversion: High-level modules should not depend on low-level modules; both should depend on abstractions (Dependency Injection)."
                },
                {
                    "q": "What is the difference between Abstract Class and Interface?",
                    "a": "An Interface defines a pure contract (behavioral blueprint) that unrelated classes can implement; supports multiple inheritance.\nAn Abstract Class represents an 'is-a' core identity and can hold state (instance variables) and default concrete method implementations; languages like Java allow a class to inherit only one abstract class."
                }
            ]
        }
    ]
}

# HR INTERVIEW PREPARATION DATA
HR_DATA = {
    "star_framework": {
        "title": "The STAR Method for Behavioral Interviews",
        "description": "The STAR framework is the industry gold standard for answering behavioral questions ('Tell me about a time when...'). It provides clear, structured storytelling.",
        "steps": [
            {"letter": "S", "word": "Situation", "description": "Set the context: Where were you working/studying? What was the project or challenge? Keep it brief (15-20% of answer)."},
            {"letter": "T", "word": "Task", "description": "Define the specific goal or responsibility assigned to you. What needed to be achieved?"},
            {"letter": "A", "word": "Action", "description": "The core part (50-60% of answer): What specific actions did YOU take? Tools used, strategies applied, how you collaborated, and how you overcame obstacles."},
            {"letter": "R", "word": "Result", "description": "Quantifiable outcome: Did performance improve by 30%? Did you meet the deadline? What did you learn?"}
        ]
    },
    "questions": [
        {
            "id": "hr-1",
            "question": "Tell me about yourself.",
            "category": "Introduction",
            "tip": "Structure using Past, Present, Future. Keep it within 90-120 seconds. Focus on skills, engineering achievements, and why you are excited about this specific role.",
            "sample_answer": "I am a final-year Computer Science student passionate about scalable web applications and distributed systems. Recently, I built an end-to-end real-time collaboration tool using React and Node.js that handled concurrent socket updates, and I completed a software internship where I optimized SQL queries by 35%.\nI have solved over 300 DSA problems across competitive platforms, strengthening my algorithmic thinking. I'm eager to bring my problem-solving skills to your engineering team and contribute to mission-critical products."
        },
        {
            "id": "hr-2",
            "question": "Why do you want to join our company?",
            "category": "Motivation",
            "tip": "Never give generic praise. Research specific products, engineering blogs, company culture values, or recent tech migrations.",
            "sample_answer": "I have been following your engineering work on high-availability distributed systems, specifically how your team handles peak traffic during sale events. Your culture of high ownership and developer autonomy resonates with how I like to work. Joining this company gives me the chance to solve scale challenges that impact millions of users while learning from seasoned senior engineers."
        },
        {
            "id": "hr-3",
            "question": "What is your greatest weakness, and how are you addressing it?",
            "category": "Self-Awareness",
            "tip": "Pick a genuine professional weakness (not a cliché like 'I am too perfectionist'), and immediately focus on the active steps you take to manage it.",
            "sample_answer": "Earlier, I had a tendency to dive directly into code implementation before fully refining edge-case documentation and architectural diagrams. During a hackathon, this led to time wasted rewriting an API schema. Since then, I adopted a discipline of drafting mini design docs and edge-case checklists before writing code, which has significantly improved my sprint velocity."
        },
        {
            "id": "hr-4",
            "question": "Describe a conflict you had with a team member and how you resolved it.",
            "category": "Behavioral",
            "tip": "Use STAR. Focus on professional discussion over personal ego, finding data-driven compromises, and delivering the project.",
            "sample_answer": "Situation: In our final year capstone project, my teammate and I disagreed on database selection—he favored MongoDB for flexible schemas while I proposed PostgreSQL because of relational transaction consistency.\nTask: We had to finalize the tech stack within 2 days to meet the project milestone.\nAction: Instead of debating opinions, I benchmarked our 5 primary user workflows and demonstrated that 80% of our queries required strict ACID relations and complex joins. I scheduled a quick whiteboard discussion where we reviewed the query patterns together.\nResult: We agreed on PostgreSQL, met our delivery deadline without bugs, and maintained strong mutual respect throughout the project."
        },
        {
            "id": "hr-5",
            "question": "Do you have any questions for us?",
            "category": "Closing",
            "tip": "ALWAYS ask thoughtful questions! Asking nothing signals lack of curiosity.",
            "sample_answer": "1. What does a typical onboarding sprint look like for an engineer in this team?\n2. What is the biggest technical challenge your team is tackling over the next two quarters?\n3. What qualities differentiate a good engineer from an exceptional one in your organization?"
        }
    ]
}

# COMPANIES HIRING PROCESS DATA
COMPANIES_DATA = [
    {
        "id": "google",
        "name": "Google",
        "type": "Product / FAANG",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg",
        "tier": "Tier-1 Tech",
        "ctc": "₹22 - ₹35 LPA (Fresher SDE-1)",
        "eligibility": {
            "degree": "B.Tech / M.Tech / Dual Degree (CS, IT, ECE, EE, Math)",
            "cgpa": "6.5+ CGPA or 65% aggregate (often no strict CGPA filter for off-campus)",
            "backlogs": "No active backlogs at the time of joining",
            "gap_years": "Up to 1-2 years allowed with valid justification"
        },
        "exam_pattern": {
            "total_rounds": "5-6 Rounds",
            "rounds": [
                {
                    "name": "Round 1: Online Assessment / Google Online Challenge (GOC)",
                    "duration": "60 - 90 Minutes",
                    "format": "2 Algorithmic Coding Problems (Medium-Hard)",
                    "details": "Conducted on HackerEarth or Google testing platform. Topics: Dynamic Programming, Graph algorithms, Advanced Tree traversals, Fenwick/Segment Trees."
                },
                {
                    "name": "Round 2: Technical Interview 1 (Live Coding)",
                    "duration": "45 Minutes",
                    "format": "1-2 DSA Problems on Google Docs / Interview Portal",
                    "details": "Interviewer evaluates thinking out loud, time/space complexity analysis, clean code, handling edge cases, and code correctness without auto-complete."
                },
                {
                    "name": "Round 3: Technical Interview 2 (Advanced DSA)",
                    "duration": "45 Minutes",
                    "format": "Data Structures & Complex Logic",
                    "details": "Deep questions on Graphs (Dijkstra, BFS/DFS, TopoSort), DP, and custom data structure design."
                },
                {
                    "name": "Round 4: Technical Interview 3 (DSA & Problem Solving)",
                    "duration": "45 Minutes",
                    "format": "Algorithmic Design & Optimization",
                    "details": "Focus on scalability, tradeoffs between memory and runtime."
                },
                {
                    "name": "Round 5: Googlyness & Leadership (Behavioral)",
                    "duration": "45 Minutes",
                    "format": "Situational & Cultural Assessment",
                    "details": "Assesses navigating ambiguity, teamwork, intellectual humility, doing the right thing, and pushing boundaries."
                }
            ]
        },
        "syllabus": [
            "Data Structures: Graphs, Segment Trees, Trie, Heaps, Balanced Trees, Disjoint Set Union (DSU).",
            "Algorithms: Dynamic Programming (1D, 2D, bitmask, trees), Binary Search variants, Dijkstra, Sliding Window.",
            "Core CS: Operating Systems (Virtual memory, Concurrency, Threads), Computer Networks (TCP/IP), System Design basics."
        ],
        "past_questions": [
            "Find the Median of Two Sorted Arrays in O(log(min(n, m))) time.",
            "Alien Dictionary: Determine the order of characters in an unknown language using topological sort.",
            "Shortest Path in a Grid with Obstacles Elimination (BFS with 3D state).",
            "Design an in-memory Key-Value store with transactional rollback (BEGIN, COMMIT, ROLLBACK)."
        ],
        "tips": "Practice speaking your thoughts aloud while coding. Never start writing code until you and the interviewer agree on the optimal algorithmic approach and constraints."
    },
    {
        "id": "amazon",
        "name": "Amazon",
        "type": "Product / FAANG",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Amazon_icon.svg",
        "tier": "Tier-1 Tech",
        "ctc": "₹28 - ₹45 LPA (Full CTC including base + stocks)",
        "eligibility": {
            "degree": "B.E. / B.Tech / M.Tech in CS/IT/ECE or related branches",
            "cgpa": "6.5+ CGPA or 65% in 10th, 12th, and Degree",
            "backlogs": "Zero active backlogs",
            "gap_years": "Maximum 1 year gap allowed"
        },
        "exam_pattern": {
            "total_rounds": "4-5 Rounds",
            "rounds": [
                {
                    "name": "Round 1: Online Assessment (OA)",
                    "duration": "90 Minutes",
                    "format": "2 Coding Questions + Work Style Simulation (Amazon Leadership Principles)",
                    "details": "Conducted on HackerRank. Topics: Arrays, Strings, Trees, Greedy. Followed by a 15-minute behavioral survey."
                },
                {
                    "name": "Round 2: Technical Interview 1 (DSA & LP)",
                    "duration": "60 Minutes",
                    "format": "1-2 Coding Questions + 15 mins Leadership Principles",
                    "details": "Questions on Trees, Graphs, Hash Maps, Priority Queues + Customer Obsession/Bias for Action questions."
                },
                {
                    "name": "Round 3: Technical Interview 2 (DSA & Low-Level Design)",
                    "duration": "60 Minutes",
                    "format": "Problem Solving & OOP Design",
                    "details": "Coding question + Object-Oriented Design (e.g., Design a Parking Lot or Amazon Locker) + Ownership LP questions."
                },
                {
                    "name": "Round 4: Bar Raiser Round",
                    "duration": "60 Minutes",
                    "format": "Independent Senior Interviewer Assessment",
                    "details": "Evaluates candidate against Amazon's global hiring bar. Deep dive into projects, complex behavioral scenarios, and algorithmic rigor."
                }
            ]
        },
        "syllabus": [
            "Data Structures: Binary Trees, BST, Heaps/Priority Queue, Graph Traversals, Hash Maps, Linked Lists.",
            "Algorithms: BFS, DFS, Topological Sort, Two Pointers, Dynamic Programming, Greedy.",
            "Amazon 16 Leadership Principles: Customer Obsession, Ownership, Bias for Action, Dive Deep, Deliver Results, Earn Trust."
        ],
        "past_questions": [
            "LRU Cache implementation with O(1) get and put operations.",
            "Number of Islands (Matrix BFS/DFS).",
            "Word Ladder (Shortest transformation sequence).",
            "Course Schedule (Cycle detection in Directed Graph)."
        ],
        "tips": "Every round has 15-20 minutes dedicated to Leadership Principles! Prepare 2 distinct STAR stories for every major Leadership Principle."
    },
    {
        "id": "microsoft",
        "name": "Microsoft",
        "type": "Product / FAANG",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/9/96/Microsoft_logo_%282012%29.svg",
        "tier": "Tier-1 Tech",
        "ctc": "₹20 - ₹28 LPA (Fresher SDE)",
        "eligibility": {
            "degree": "B.Tech / M.Tech in CS / IT / Electronics",
            "cgpa": "7.0+ CGPA with no standing backlogs",
            "backlogs": "0 active backlogs",
            "gap_years": "Up to 2 years education gap permissible"
        },
        "exam_pattern": {
            "total_rounds": "4 Rounds",
            "rounds": [
                {
                    "name": "Round 1: Online Assessment",
                    "duration": "70 - 90 Minutes",
                    "format": "3 Coding Questions on Codility / Mettle",
                    "details": "Focus on String manipulation, Array algorithms, Tree traversals, and dynamic programming."
                },
                {
                    "name": "Round 2: Technical Interview 1",
                    "duration": "45 - 60 Minutes",
                    "format": "Live Coding & Core CS",
                    "details": "DSA problems + Questions on Memory management, Pointers, OS threads, and Garbage Collection."
                },
                {
                    "name": "Round 3: Technical Interview 2",
                    "duration": "45 - 60 Minutes",
                    "format": "Problem Solving & System Concepts",
                    "details": "Trees/Graphs + Low-Level Design (OOD) + Project discussions."
                },
                {
                    "name": "Round 4: AA (As Appropriate) / Partner Director Round",
                    "duration": "45 Minutes",
                    "format": "Engineering mindset & Cultural alignment",
                    "details": "Growth Mindset questions, past projects, dealing with failure, and problem solving."
                }
            ]
        },
        "syllabus": [
            "Data Structures: Linked Lists, Binary Trees, Stacks, Queues, Graphs, Tries.",
            "Core CS: Operating Systems (Synchronization, Deadlocks, Memory Paging), DBMS, Object-Oriented Principles.",
            "Design: Low-Level Class Diagrams, Design Patterns (Singleton, Factory, Observer)."
        ],
        "past_questions": [
            "Reverse Nodes in k-Group.",
            "Serialize and Deserialize a Binary Tree.",
            "Find Lowest Common Ancestor in a Binary Tree.",
            "Implement a Thread-Safe Singleton class."
        ],
        "tips": "Microsoft loves production-ready, readable code. Name variables descriptively and handle null/empty inputs proactively."
    },
    {
        "id": "tcs",
        "name": "TCS (Tata Consultancy Services)",
        "type": "IT & Services",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/b/b1/Tata_Consultancy_Services_Logo.svg",
        "tier": "National Qualifier Test (NQT)",
        "ctc": "Ninja: ₹3.6 LPA | Digital: ₹7.5 LPA | Prime: ₹9 - ₹11 LPA",
        "eligibility": {
            "degree": "B.E. / B.Tech / M.E. / M.Tech / MCA / M.Sc",
            "cgpa": "Minimum 60% or 6.0 CGPA throughout 10th, 12th, Diploma, and Graduation",
            "backlogs": "At most 1 active backlog allowed at the time of appearing (must be cleared before joining)",
            "gap_years": "Overall academic gap not to exceed 24 months"
        },
        "exam_pattern": {
            "total_rounds": "2 Stages (Online NQT + In-person / Virtual Interview)",
            "rounds": [
                {
                    "name": "Round 1: Foundation Section (Cognitive)",
                    "duration": "75 Minutes",
                    "format": "Numerical Ability (20 Q), Reasoning Ability (20 Q), Verbal Ability (25 Q)",
                    "details": "Mandatory for all profiles (Ninja/Digital/Prime). Adaptive sectional timers on TCS iON platform."
                },
                {
                    "name": "Round 2: Advanced Section (Digital / Prime Qualifier)",
                    "duration": "90 Minutes",
                    "format": "Advanced Quantitative (15 Q) + Advanced Reasoning (10 Q) + 2 Advanced Hands-on Coding",
                    "details": "Coding 1 (Easy-Medium, 30 mins) + Coding 2 (Medium-Hard, 45 mins). Compilers for C, C++, Java, Python."
                },
                {
                    "name": "Round 3: Technical + Managerial + HR Interview",
                    "duration": "30 - 45 Minutes",
                    "format": "Combined Panel Interview",
                    "details": "Questions on Final Year project, SQL queries, OOPs concepts, willingness to relocate, and shift flexibility."
                }
            ]
        },
        "syllabus": [
            "Aptitude: Time & Work, Speed Distance Time, Mixtures, Permutations, Syllogisms, Series.",
            "Coding: Arrays, Strings, Matrices, Recursion, Number Theory (Primes, GCD, Palindromes).",
            "Technical: Basic SQL (Joins, Group By, Primary Keys), SDLC methodologies, OOPs concepts."
        ],
        "past_questions": [
            "Rotate Matrix by 90 degrees in-place.",
            "Find the smallest missing positive integer in an unsorted array.",
            "Write a SQL query to find the second highest salary from Employee table.",
            "Check if two strings are anagrams of each other without library sort."
        ],
        "tips": "Sectional timers are strictly enforced in TCS NQT. You cannot jump between sections once a timer begins! Manage your pacing strictly."
    },
    {
        "id": "infosys",
        "name": "Infosys",
        "type": "IT & Services",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/9/95/Infosys_logo.svg",
        "tier": "InfyTQ / HackWithInfy / Off-Campus",
        "ctc": "SE: ₹3.6 LPA | DSE: ₹6.5 LPA | Specialist Programmer (SP): ₹9.5 LPA",
        "eligibility": {
            "degree": "B.E / B.Tech / M.E / M.Tech / MCA",
            "cgpa": "60% or 6.0 CGPA throughout 10th, 12th, and College",
            "backlogs": "Zero active backlogs at time of assessment",
            "gap_years": "Up to 2 years gap permissible"
        },
        "exam_pattern": {
            "total_rounds": "2 Stages",
            "rounds": [
                {
                    "name": "Round 1: Online Assessment",
                    "duration": "100 Minutes",
                    "format": "Reasoning Ability (15 Q) + Mathematical Ability (10 Q) + Verbal Ability (20 Q) + Pseudocode (5 Q) + Puzzle Solving (4 Q)",
                    "details": "Conducted on Infosys testing platform with AI proctoring."
                },
                {
                    "name": "HackWithInfy / SP Qualifier (For High Package Roles)",
                    "duration": "180 Minutes",
                    "format": "3 Complex Algorithmic Coding Questions",
                    "details": "Scoring 1.5+ problems qualifies for Specialist Programmer (SP) ₹9.5 LPA interview."
                },
                {
                    "name": "Round 2: Technical & HR Interview",
                    "duration": "25 - 40 Minutes",
                    "format": "Technical Discussion & Resume Verification",
                    "details": "Explain college projects, basic Java/Python code execution, DBMS questions, and behavioral questions."
                }
            ]
        },
        "syllabus": [
            "Mathematical & Logical: Data Interpretation, Cryptarithmetic, Seating arrangement, Time-speed-work.",
            "Pseudocode: Bitwise operators, looping constructs, recursion output tracing.",
            "Coding (SP/DSE): Dynamic Programming, Graph algorithms, Trees."
        ],
        "past_questions": [
            "Cryptarithmetic puzzle solving: SEND + MORE = MONEY.",
            "Longest Increasing Subsequence with custom constraints.",
            "Explain normal forms with real banking example.",
            "Write code to implement a stack using two queues."
        ],
        "tips": "Infosys pseudocode questions often have tricky nested loops and bitwise operators. Trace through tables on paper carefully."
    },
    {
        "id": "accenture",
        "name": "Accenture",
        "type": "IT & Services",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/c/cd/Accenture.svg",
        "tier": "Campus Drive",
        "ctc": "ASE: ₹4.5 LPA | FSE: ₹6.5 LPA",
        "eligibility": {
            "degree": "All branches of B.E. / B.Tech / MCA / M.Sc (CS/IT)",
            "cgpa": "65% or 6.5 CGPA throughout academics",
            "backlogs": "No active backlogs at time of joining",
            "gap_years": "Maximum 1 year gap allowed during education"
        },
        "exam_pattern": {
            "total_rounds": "3 Stages (Cognitive & Technical Assessment -> Coding -> Communication Assessment -> Interview)",
            "rounds": [
                {
                    "name": "Stage 1: Cognitive & Technical Assessment",
                    "duration": "90 Minutes",
                    "format": "90 Questions (English, Critical Thinking, Abstract Reasoning, Common Application & MS Office, Pseudocode, Networking & Cloud)",
                    "details": "Elimination stage. Must clear sectional cutoffs to unlock coding test immediately."
                },
                {
                    "name": "Stage 2: Coding Assessment",
                    "duration": "45 Minutes",
                    "format": "2 Hands-on Coding Questions",
                    "details": "Conducted immediately after Stage 1. Usually Arrays, Strings, Matrix transformations."
                },
                {
                    "name": "Stage 3: Communication Assessment",
                    "duration": "20 Minutes",
                    "format": "Automated Audio Test (Reading, Listening, Sentence repetition, Story retelling)",
                    "details": "Evaluates fluency, pronunciation, and vocabulary via automated speech recognition."
                },
                {
                    "name": "Stage 4: Technical & HR Interview",
                    "duration": "25 - 30 Minutes",
                    "format": "Virtual Interview",
                    "details": "Review of technical projects, certifications, strengths, and adaptability."
                }
            ]
        },
        "syllabus": [
            "Technical: MS Office, Cloud Fundamentals (SaaS, IaaS, PaaS), Network Security, Pseudocode tracing.",
            "Coding: Basic to Intermediate level logic (Palindromes, Array rotations, String transformations).",
            "Communication: Pronunciation, active listening, voice clarity."
        ],
        "past_questions": [
            "Count number of carries when adding two numbers.",
            "Find the maximum product of a contiguous subarray.",
            "Explain the difference between Cloud Computing and traditional on-prem servers.",
            "Pseudocode output evaluation with bitwise XOR and shift operators."
        ],
        "tips": "For the automated communication assessment, use a quiet room and a clear wired headset with good microphone clarity."
    }
]

# DEDICATED TOPIC-WISE DSA SHEET DATA
DSA_SHEET_DATA = [
    {
        "topic": "Arrays & Hashing",
        "description": "Fundamental array manipulation, prefix sums, hash table lookups, and frequency maps.",
        "problems": [
            {
                "id": "dsa-1",
                "title": "Two Sum",
                "difficulty": "Easy",
                "leetcode_url": "https://leetcode.com/problems/two-sum/",
                "gfg_url": "https://www.geeksforgeeks.org/check-if-pair-with-given-sum-exists-in-array/",
                "statement": "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume each input would have exactly one solution.",
                "approach": "Use a Hash Map to store each number's value along with its index. For each element x, check if (target - x) already exists in the hash map. If found, return [map[target - x], current_index]. This achieves single-pass O(N) time.",
                "time_complexity": "O(N)",
                "space_complexity": "O(N)",
                "code": {
                    "cpp": """vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> mp;
    for (int i = 0; i < nums.size(); ++i) {
        int complement = target - nums[i];
        if (mp.find(complement) != mp.end()) {
            return {mp[complement], i};
        }
        mp[nums[i]] = i;
    }
    return {};
}""",
                    "python": """def twoSum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []""",
                    "java": """public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        int complement = target - nums[i];
        if (map.containsKey(complement)) {
            return new int[] { map.get(complement), i };
        }
        map.put(nums[i], i);
    }
    return new int[]{};
}""",
                    "javascript": """function twoSum(nums, target) {
    const map = new Map();
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        if (map.has(complement)) {
            return [map.get(complement), i];
        }
        map.set(nums[i], i);
    }
    return [];
}"""
                }
            },
            {
                "id": "dsa-2",
                "title": "Maximum Subarray (Kadane's Algorithm)",
                "difficulty": "Medium",
                "leetcode_url": "https://leetcode.com/problems/maximum-subarray/",
                "gfg_url": "https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/",
                "statement": "Given an integer array nums, find the subarray with the largest sum, and return its sum.",
                "approach": "Kadane's Algorithm: Maintain current_sum and max_sum. For each element, either add it to current_sum or start a new subarray with the current element (i.e., current_sum = max(num, current_sum + num)). Update max_sum at each step.",
                "time_complexity": "O(N)",
                "space_complexity": "O(1)",
                "code": {
                    "cpp": """int maxSubArray(vector<int>& nums) {
    int max_so_far = nums[0];
    int curr_max = nums[0];
    for (size_t i = 1; i < nums.size(); ++i) {
        curr_max = max(nums[i], curr_max + nums[i]);
        max_so_far = max(max_so_far, curr_max);
    }
    return max_so_far;
}""",
                    "python": """def maxSubArray(nums: list[int]) -> int:
    curr_sum = max_sum = nums[0]
    for x in nums[1:]:
        curr_sum = max(x, curr_sum + x)
        max_sum = max(max_sum, curr_sum)
    return max_sum""",
                    "java": """public int maxSubArray(int[] nums) {
    int maxSoFar = nums[0], currMax = nums[0];
    for (int i = 1; i < nums.length; i++) {
        currMax = Math.max(nums[i], currMax + nums[i]);
        maxSoFar = Math.max(maxSoFar, currMax);
    }
    return maxSoFar;
}""",
                    "javascript": """function maxSubArray(nums) {
    let curr = nums[0], maxVal = nums[0];
    for (let i = 1; i < nums.length; i++) {
        curr = Math.max(nums[i], curr + nums[i]);
        maxVal = Math.max(maxVal, curr);
    }
    return maxVal;
}"""
                }
            },
            {
                "id": "dsa-3",
                "title": "Contains Duplicate",
                "difficulty": "Easy",
                "leetcode_url": "https://leetcode.com/problems/contains-duplicate/",
                "gfg_url": "https://www.geeksforgeeks.org/check-given-array-contains-duplicate-elements-within-k-distance/",
                "statement": "Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.",
                "approach": "Store visited elements in a hash set. If the set already contains the current number, return true immediately. If loop finishes, return false.",
                "time_complexity": "O(N)",
                "space_complexity": "O(N)",
                "code": {
                    "cpp": """bool containsDuplicate(vector<int>& nums) {
    unordered_set<int> seen;
    for (int n : nums) {
        if (seen.count(n)) return true;
        seen.insert(n);
    }
    return false;
}""",
                    "python": """def containsDuplicate(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))""",
                    "java": """public boolean containsDuplicate(int[] nums) {
    Set<Integer> set = new HashSet<>();
    for (int n : nums) {
        if (!set.add(n)) return true;
    }
    return false;
}""",
                    "javascript": """function containsDuplicate(nums) {
    return new Set(nums).size !== nums.length;
}"""
                }
            },
            {
                "id": "dsa-4",
                "title": "Product of Array Except Self",
                "difficulty": "Medium",
                "leetcode_url": "https://leetcode.com/problems/product-of-array-except-self/",
                "gfg_url": "https://www.geeksforgeeks.org/a-product-array-puzzle/",
                "statement": "Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i], without using the division operation.",
                "approach": "Compute prefix products in a first forward pass. Then, use a running suffix product variable in a reverse pass to multiply with the prefix product already stored.",
                "time_complexity": "O(N)",
                "space_complexity": "O(1) extra space",
                "code": {
                    "cpp": """vector<int> productExceptSelf(vector<int>& nums) {
    int n = nums.size();
    vector<int> res(n, 1);
    for (int i = 1; i < n; ++i) res[i] = res[i - 1] * nums[i - 1];
    int right = 1;
    for (int i = n - 1; i >= 0; --i) {
        res[i] *= right;
        right *= nums[i];
    }
    return res;
}""",
                    "python": """def productExceptSelf(nums: list[int]) -> list[int]:
    n = len(nums)
    res = [1] * n
    for i in range(1, n):
        res[i] = res[i - 1] * nums[i - 1]
    right = 1
    for i in range(n - 1, -1, -1):
        res[i] *= right
        right *= nums[i]
    return res""",
                    "java": """public int[] productExceptSelf(int[] nums) {
    int n = nums.length;
    int[] res = new int[n];
    res[0] = 1;
    for (int i = 1; i < n; i++) res[i] = res[i - 1] * nums[i - 1];
    int right = 1;
    for (int i = n - 1; i >= 0; i--) {
        res[i] *= right;
        right *= nums[i];
    }
    return res;
}""",
                    "javascript": """function productExceptSelf(nums) {
    const n = nums.length;
    const res = new Array(n).fill(1);
    for (let i = 1; i < n; i++) res[i] = res[i - 1] * nums[i - 1];
    let right = 1;
    for (let i = n - 1; i >= 0; i--) {
        res[i] *= right;
        right *= nums[i];
    }
    return res;
}"""
                }
            }
        ]
    },
    {
        "topic": "Two Pointers & Sliding Window",
        "description": "Techniques for linear scans, searching sorted arrays, and tracking variable/fixed length contiguous subarrays.",
        "problems": [
            {
                "id": "dsa-5",
                "title": "3Sum",
                "difficulty": "Medium",
                "leetcode_url": "https://leetcode.com/problems/3sum/",
                "gfg_url": "https://www.geeksforgeeks.org/find-triplets-array-whose-sum-equal-zero/",
                "statement": "Given an integer array nums, return all the unique triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.",
                "approach": "Sort the array. Loop through the array with index i. If nums[i] > 0, break early. Skip duplicates for i. Use two pointers (left = i + 1, right = n - 1) to find pairs where nums[left] + nums[right] == -nums[i]. Adjust pointers and skip duplicates.",
                "time_complexity": "O(N^2)",
                "space_complexity": "O(1) extra space",
                "code": {
                    "cpp": """vector<vector<int>> threeSum(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> res;
    int n = nums.size();
    for (int i = 0; i < n - 2; ++i) {
        if (i > 0 && nums[i] == nums[i - 1]) continue;
        int l = i + 1, r = n - 1;
        while (l < r) {
            int sum = nums[i] + nums[l] + nums[r];
            if (sum == 0) {
                res.push_back({nums[i], nums[l], nums[r]});
                while (l < r && nums[l] == nums[l + 1]) ++l;
                while (l < r && nums[r] == nums[r - 1]) --r;
                ++l; --r;
            } else if (sum < 0) ++l;
            else --r;
        }
    }
    return res;
}""",
                    "python": """def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]: l += 1
                while l < r and nums[r] == nums[r - 1]: r -= 1
                l += 1; r -= 1
            elif s < 0: l += 1
            else: r -= 1
    return res""",
                    "java": """public List<List<Integer>> threeSum(int[] nums) {
    Arrays.sort(nums);
    List<List<Integer>> res = new ArrayList<>();
    for (int i = 0; i < nums.length - 2; i++) {
        if (i > 0 && nums[i] == nums[i - 1]) continue;
        int l = i + 1, r = nums.length - 1;
        while (l < r) {
            int sum = nums[i] + nums[l] + nums[r];
            if (sum == 0) {
                res.add(Arrays.asList(nums[i], nums[l], nums[r]));
                while (l < r && nums[l] == nums[l + 1]) l++;
                while (l < r && nums[r] == nums[r - 1]) r--;
                l++; r--;
            } else if (sum < 0) l++;
            else r--;
        }
    }
    return res;
}""",
                    "javascript": """function threeSum(nums) {
    nums.sort((a, b) => a - b);
    const res = [];
    for (let i = 0; i < nums.length - 2; i++) {
        if (i > 0 && nums[i] === nums[i - 1]) continue;
        let l = i + 1, r = nums.length - 1;
        while (l < r) {
            const sum = nums[i] + nums[l] + nums[r];
            if (sum === 0) {
                res.push([nums[i], nums[l], nums[r]]);
                while (l < r && nums[l] === nums[l + 1]) l++;
                while (l < r && nums[r] === nums[r - 1]) r--;
                l++; r--;
            } else if (sum < 0) l++;
            else r--;
        }
    }
    return res;
}"""
                }
            },
            {
                "id": "dsa-6",
                "title": "Trapping Rain Water",
                "difficulty": "Hard",
                "leetcode_url": "https://leetcode.com/problems/trapping-rain-water/",
                "gfg_url": "https://www.geeksforgeeks.org/trapping-rain-water/",
                "statement": "Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.",
                "approach": "Two-pointer approach: Maintain left and right pointers, and variables left_max and right_max. Move the pointer pointing to the smaller maximum because the trapped water at that position is strictly limited by that smaller boundary.",
                "time_complexity": "O(N)",
                "space_complexity": "O(1)",
                "code": {
                    "cpp": """int trap(vector<int>& height) {
    int l = 0, r = height.size() - 1;
    int left_max = 0, right_max = 0, water = 0;
    while (l < r) {
        if (height[l] < height[r]) {
            if (height[l] >= left_max) left_max = height[l];
            else water += left_max - height[l];
            ++l;
        } else {
            if (height[r] >= right_max) right_max = height[r];
            else water += right_max - height[r];
            --r;
        }
    }
    return water;
}""",
                    "python": """def trap(height: list[int]) -> int:
    l, r = 0, len(height) - 1
    left_max = right_max = water = 0
    while l < r:
        if height[l] < height[r]:
            if height[l] >= left_max: left_max = height[l]
            else: water += left_max - height[l]
            l += 1
        else:
            if height[r] >= right_max: right_max = height[r]
            else: water += right_max - height[r]
            r -= 1
    return water""",
                    "java": """public int trap(int[] height) {
    int l = 0, r = height.length - 1;
    int leftMax = 0, rightMax = 0, water = 0;
    while (l < r) {
        if (height[l] < height[r]) {
            if (height[l] >= leftMax) leftMax = height[l];
            else water += leftMax - height[l];
            l++;
        } else {
            if (height[r] >= rightMax) rightMax = height[r];
            else water += rightMax - height[r];
            r--;
        }
    }
    return water;
}""",
                    "javascript": """function trap(height) {
    let l = 0, r = height.length - 1;
    let leftMax = 0, rightMax = 0, water = 0;
    while (l < r) {
        if (height[l] < height[r]) {
            if (height[l] >= leftMax) leftMax = height[l];
            else water += leftMax - height[l];
            l++;
        } else {
            if (height[r] >= rightMax) rightMax = height[r];
            else water += rightMax - height[r];
            r--;
        }
    }
    return water;
}"""
                }
            },
            {
                "id": "dsa-7",
                "title": "Longest Substring Without Repeating Characters",
                "difficulty": "Medium",
                "leetcode_url": "https://leetcode.com/problems/longest-substring-without-repeating-characters/",
                "gfg_url": "https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/",
                "statement": "Given a string s, find the length of the longest substring without repeating characters.",
                "approach": "Sliding window with hash map. Keep track of the most recent index of each character. When a character repeats within the current window [start, end], advance the start pointer to last_seen[char] + 1.",
                "time_complexity": "O(N)",
                "space_complexity": "O(min(N, charset))",
                "code": {
                    "cpp": """int lengthOfLongestSubstring(string s) {
    unordered_map<char, int> mp;
    int max_len = 0, start = 0;
    for (int end = 0; end < s.length(); ++end) {
        if (mp.count(s[end])) {
            start = max(start, mp[s[end]] + 1);
        }
        mp[s[end]] = end;
        max_len = max(max_len, end - start + 1);
    }
    return max_len;
}""",
                    "python": """def lengthOfLongestSubstring(s: str) -> int:
    char_map = {}
    max_len = start = 0
    for end, ch in enumerate(s):
        if ch in char_map and char_map[ch] >= start:
            start = char_map[ch] + 1
        char_map[ch] = end
        max_len = max(max_len, end - start + 1)
    return max_len""",
                    "java": """public int lengthOfLongestSubstring(String s) {
    Map<Character, Integer> map = new HashMap<>();
    int maxLen = 0, start = 0;
    for (int end = 0; end < s.length(); end++) {
        char ch = s.charAt(end);
        if (map.containsKey(ch)) {
            start = Math.max(start, map.get(ch) + 1);
        }
        map.put(ch, end);
        maxLen = Math.max(maxLen, end - start + 1);
    }
    return maxLen;
}""",
                    "javascript": """function lengthOfLongestSubstring(s) {
    const map = new Map();
    let maxLen = 0, start = 0;
    for (let end = 0; end < s.length; end++) {
        if (map.has(s[end])) {
            start = Math.max(start, map.get(s[end]) + 1);
        }
        map.set(s[end], end);
        maxLen = Math.max(maxLen, end - start + 1);
    }
    return maxLen;
}"""
                }
            }
        ]
    },
    {
        "topic": "Linked Lists",
        "description": "Pointer manipulation, cycle detection, reordering, and dummy head patterns.",
        "problems": [
            {
                "id": "dsa-8",
                "title": "Reverse Linked List",
                "difficulty": "Easy",
                "leetcode_url": "https://leetcode.com/problems/reverse-linked-list/",
                "gfg_url": "https://www.geeksforgeeks.org/reverse-a-linked-list/",
                "statement": "Given the head of a singly linked list, reverse the list, and return the reversed list.",
                "approach": "Iterative 3-pointer method: Maintain prev (initialized to NULL), curr (head), and next_node. At each step, store curr->next, reverse pointer curr->next = prev, and advance prev = curr, curr = next_node.",
                "time_complexity": "O(N)",
                "space_complexity": "O(1)",
                "code": {
                    "cpp": """ListNode* reverseList(ListNode* head) {
    ListNode* prev = nullptr;
    ListNode* curr = head;
    while (curr) {
        ListNode* nextNode = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nextNode;
    }
    return prev;
}""",
                    "python": """def reverseList(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev""",
                    "java": """public ListNode reverseList(ListNode head) {
    ListNode prev = null, curr = head;
    while (curr != null) {
        ListNode next = curr.next;
        curr.next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}""",
                    "javascript": """function reverseList(head) {
    let prev = null, curr = head;
    while (curr) {
        const next = curr.next;
        curr.next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}"""
                }
            },
            {
                "id": "dsa-9",
                "title": "Linked List Cycle (Floyd's Tortoise and Hare)",
                "difficulty": "Easy",
                "leetcode_url": "https://leetcode.com/problems/linked-list-cycle/",
                "gfg_url": "https://www.geeksforgeeks.org/detect-loop-in-a-linked-list/",
                "statement": "Given head, the head of a linked list, determine if the linked list has a cycle in it.",
                "approach": "Floyd's Cycle-Finding Algorithm: Use two pointers moving at different speeds (slow by 1 step, fast by 2 steps). If there is a loop, fast will inevitably catch up and equal slow.",
                "time_complexity": "O(N)",
                "space_complexity": "O(1)",
                "code": {
                    "cpp": """bool hasCycle(ListNode *head) {
    ListNode *slow = head, *fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) return true;
    }
    return false;
}""",
                    "python": """def hasCycle(head) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False""",
                    "java": """public boolean hasCycle(ListNode head) {
    ListNode slow = head, fast = head;
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow == fast) return true;
    }
    return false;
}""",
                    "javascript": """function hasCycle(head) {
    let slow = head, fast = head;
    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow === fast) return true;
    }
    return false;
}"""
                }
            },
            {
                "id": "dsa-10",
                "title": "Merge k Sorted Lists",
                "difficulty": "Hard",
                "leetcode_url": "https://leetcode.com/problems/merge-k-sorted-lists/",
                "gfg_url": "https://www.geeksforgeeks.org/merge-k-sorted-linked-lists/",
                "statement": "You are given an array of k linked-lists lists, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.",
                "approach": "Min-Heap (Priority Queue) approach: Push the head node of each list into the min-heap. Pop the minimum node, append it to the result list, and push the next node from that specific list into the heap.",
                "time_complexity": "O(N log k) where N is total nodes",
                "space_complexity": "O(k)",
                "code": {
                    "cpp": """struct Compare {
    bool operator()(ListNode* a, ListNode* b) { return a->val > b->val; }
};
ListNode* mergeKLists(vector<ListNode*>& lists) {
    priority_queue<ListNode*, vector<ListNode*>, Compare> pq;
    for (auto l : lists) if (l) pq.push(l);
    ListNode dummy(0);
    ListNode* tail = &dummy;
    while (!pq.empty()) {
        ListNode* top = pq.top(); pq.pop();
        tail->next = top;
        tail = tail->next;
        if (top->next) pq.push(top->next);
    }
    return dummy.next;
}""",
                    "python": """import heapq
def mergeKLists(lists):
    h = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(h, (node.val, i, node))
    dummy = curr = ListNode(0)
    while h:
        val, i, node = heapq.heappop(h)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(h, (node.next.val, i, node.next))
    return dummy.next""",
                    "java": """public ListNode mergeKLists(ListNode[] lists) {
    PriorityQueue<ListNode> pq = new PriorityQueue<>((a, b) -> a.val - b.val);
    for (ListNode l : lists) if (l != null) pq.add(l);
    ListNode dummy = new ListNode(0), tail = dummy;
    while (!pq.isEmpty()) {
        ListNode top = pq.poll();
        tail.next = top;
        tail = tail.next;
        if (top.next != null) pq.add(top.next);
    }
    return dummy.next;
}""",
                    "javascript": """// Priority Queue or Divide & Conquer merge pairs of lists"""
                }
            }
        ]
    },
    {
        "topic": "Trees & Binary Search Trees (BST)",
        "description": "Tree traversals (Inorder, Preorder, Postorder, Level-order), LCA, Height, and BST search properties.",
        "problems": [
            {
                "id": "dsa-11",
                "title": "Lowest Common Ancestor of a Binary Tree",
                "difficulty": "Medium",
                "leetcode_url": "https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/",
                "gfg_url": "https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/",
                "statement": "Given a binary tree, find the lowest common ancestor (LCA) of two given nodes p and q.",
                "approach": "Recursive post-order traversal: If root is null or root equals p or q, return root. Recursively search left and right subtrees. If both return non-null, root is the LCA. If only one is non-null, return that non-null child.",
                "time_complexity": "O(N)",
                "space_complexity": "O(H) recursion stack",
                "code": {
                    "cpp": """TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    if (!root || root == p || root == q) return root;
    TreeNode* left = lowestCommonAncestor(root->left, p, q);
    TreeNode* right = lowestCommonAncestor(root->right, p, q);
    if (left && right) return root;
    return left ? left : right;
}""",
                    "python": """def lowestCommonAncestor(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if left and right:
        return root
    return left or right""",
                    "java": """public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
    if (root == null || root == p || root == q) return root;
    TreeNode left = lowestCommonAncestor(root.left, p, q);
    TreeNode right = lowestCommonAncestor(root.right, p, q);
    if (left != null && right != null) return root;
    return left != null ? left : right;
}""",
                    "javascript": """function lowestCommonAncestor(root, p, q) {
    if (!root || root === p || root === q) return root;
    const left = lowestCommonAncestor(root.left, p, q);
    const right = lowestCommonAncestor(root.right, p, q);
    if (left && right) return root;
    return left || right;
}"""
                }
            },
            {
                "id": "dsa-12",
                "title": "Binary Tree Level Order Traversal",
                "difficulty": "Medium",
                "leetcode_url": "https://leetcode.com/problems/binary-tree-level-order-traversal/",
                "gfg_url": "https://www.geeksforgeeks.org/level-order-tree-traversal/",
                "statement": "Given the root of a binary tree, return the level order traversal of its nodes' values (i.e., from left to right, level by level).",
                "approach": "Queue-based BFS: Initialize queue with root. In a loop while queue is not empty, get current level size = queue.size(). Pop that many nodes, append values to current level array, and enqueue their left and right children.",
                "time_complexity": "O(N)",
                "space_complexity": "O(N)",
                "code": {
                    "cpp": """vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>> res;
    if (!root) return res;
    queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        int sz = q.size();
        vector<int> level;
        for (int i = 0; i < sz; ++i) {
            TreeNode* node = q.front(); q.pop();
            level.push_back(node->val);
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        res.push_back(level);
    }
    return res;
}""",
                    "python": """from collections import deque
def levelOrder(root):
    if not root: return []
    res, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(level)
    return res""",
                    "java": """public List<List<Integer>> levelOrder(TreeNode root) {
    List<List<Integer>> res = new ArrayList<>();
    if (root == null) return res;
    Queue<TreeNode> q = new LinkedList<>();
    q.add(root);
    while (!q.isEmpty()) {
        int size = q.size();
        List<Integer> level = new ArrayList<>();
        for (int i = 0; i < size; i++) {
            TreeNode curr = q.poll();
            level.add(curr.val);
            if (curr.left != null) q.add(curr.left);
            if (curr.right != null) q.add(curr.right);
        }
        res.add(level);
    }
    return res;
}""",
                    "javascript": """function levelOrder(root) {
    if (!root) return [];
    const res = [], q = [root];
    while (q.length) {
        const sz = q.length, level = [];
        for (let i = 0; i < sz; i++) {
            const node = q.shift();
            level.push(node.val);
            if (node.left) q.push(node.left);
            if (node.right) q.push(node.right);
        }
        res.push(level);
    }
    return res;
}"""
                }
            }
        ]
    },
    {
        "topic": "Graphs",
        "description": "Breadth-First Search, Depth-First Search, Topological Sort, Cycle Detection, and Shortest Paths.",
        "problems": [
            {
                "id": "dsa-13",
                "title": "Number of Islands",
                "difficulty": "Medium",
                "leetcode_url": "https://leetcode.com/problems/number-of-islands/",
                "gfg_url": "https://www.geeksforgeeks.org/find-the-number-of-islands-using-dfs/",
                "statement": "Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.",
                "approach": "Iterate through every cell. Whenever an unvisited '1' is found, increment island counter and initiate DFS/BFS to sink the connected component (mark all connected '1's as '0').",
                "time_complexity": "O(M * N)",
                "space_complexity": "O(M * N) recursion/queue",
                "code": {
                    "cpp": """void dfs(vector<vector<char>>& grid, int r, int c) {
    if (r < 0 || c < 0 || r >= grid.size() || c >= grid[0].size() || grid[r][c] != '1') return;
    grid[r][c] = '0';
    dfs(grid, r + 1, c); dfs(grid, r - 1, c);
    dfs(grid, r, c + 1); dfs(grid, r, c - 1);
}
int numIslands(vector<vector<char>>& grid) {
    int count = 0;
    for (int i = 0; i < grid.size(); ++i) {
        for (int j = 0; j < grid[0].size(); ++j) {
            if (grid[i][j] == '1') {
                ++count;
                dfs(grid, i, j);
            }
        }
    }
    return count;
}""",
                    "python": """def numIslands(grid: list[list[str]]) -> int:
    if not grid: return 0
    rows, cols, count = len(grid), len(grid[0]), 0
    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            dfs(r + dr, c + dc)
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)
    return count""",
                    "java": """public int numIslands(char[][] grid) {
    int count = 0;
    for (int i = 0; i < grid.length; i++) {
        for (int j = 0; j < grid[0].length; j++) {
            if (grid[i][j] == '1') {
                count++;
                dfs(grid, i, j);
            }
        }
    }
    return count;
}
void dfs(char[][] grid, int r, int c) {
    if (r < 0 || c < 0 || r >= grid.length || c >= grid[0].length || grid[r][c] != '1') return;
    grid[r][c] = '0';
    dfs(grid, r + 1, c); dfs(grid, r - 1, c);
    dfs(grid, r, c + 1); dfs(grid, r, c - 1);
}""",
                    "javascript": """function numIslands(grid) {
    let count = 0;
    function dfs(r, c) {
        if (r < 0 || c < 0 || r >= grid.length || c >= grid[0].length || grid[r][c] !== '1') return;
        grid[r][c] = '0';
        dfs(r + 1, c); dfs(r - 1, c);
        dfs(r, c + 1); dfs(r, c - 1);
    }
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {
            if (grid[i][j] === '1') {
                count++;
                dfs(i, j);
            }
        }
    }
    return count;
}"""
                }
            },
            {
                "id": "dsa-14",
                "title": "Course Schedule (Topological Sort)",
                "difficulty": "Medium",
                "leetcode_url": "https://leetcode.com/problems/course-schedule/",
                "gfg_url": "https://www.geeksforgeeks.org/find-whether-it-is-possible-to-finish-all-tasks-or-not-from-given-dependencies/",
                "statement": "There are numCourses courses labeled 0 to numCourses - 1. You are given an array prerequisites. Return true if you can finish all courses; otherwise false.",
                "approach": "Kahn's Algorithm (BFS with In-degrees): Build adjacency list and in-degree array. Push all nodes with in-degree 0 into a queue. While queue is not empty, pop a node, decrement in-degrees of neighbors. If a neighbor reaches 0, push to queue. If processed nodes == numCourses, there is no cycle.",
                "time_complexity": "O(V + E)",
                "space_complexity": "O(V + E)",
                "code": {
                    "cpp": """bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
    vector<vector<int>> adj(numCourses);
    vector<int> indegree(numCourses, 0);
    for (auto& p : prerequisites) {
        adj[p[1]].push_back(p[0]);
        ++indegree[p[0]];
    }
    queue<int> q;
    for (int i = 0; i < numCourses; ++i) if (indegree[i] == 0) q.push(i);
    int count = 0;
    while (!q.empty()) {
        int u = q.front(); q.pop();
        ++count;
        for (int v : adj[u]) {
            if (--indegree[v] == 0) q.push(v);
        }
    }
    return count == numCourses;
}""",
                    "python": """from collections import deque
def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    adj = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses
    for dest, src in prerequisites:
        adj[src].append(dest)
        indegree[dest] += 1
    q = deque([i for i in range(numCourses) if indegree[i] == 0])
    count = 0
    while q:
        u = q.popleft()
        count += 1
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    return count == numCourses""",
                    "java": """public boolean canFinish(int numCourses, int[][] prerequisites) {
    List<List<Integer>> adj = new ArrayList<>();
    for (int i = 0; i < numCourses; i++) adj.add(new ArrayList<>());
    int[] indegree = new int[numCourses];
    for (int[] p : prerequisites) {
        adj.get(p[1]).add(p[0]);
        indegree[p[0]]++;
    }
    Queue<Integer> q = new LinkedList<>();
    for (int i = 0; i < numCourses; i++) if (indegree[i] == 0) q.add(i);
    int count = 0;
    while (!q.isEmpty()) {
        int u = q.poll();
        count++;
        for (int v : adj.get(u)) {
            if (--indegree[v] == 0) q.add(v);
        }
    }
    return count == numCourses;
}""",
                    "javascript": """function canFinish(numCourses, prerequisites) {
    const adj = Array.from({length: numCourses}, () => []);
    const inDeg = new Array(numCourses).fill(0);
    for (const [dest, src] of prerequisites) {
        adj[src].push(dest);
        inDeg[dest]++;
    }
    const q = [];
    for (let i = 0; i < numCourses; i++) if (inDeg[i] === 0) q.push(i);
    let count = 0;
    while (q.length) {
        const u = q.shift();
        count++;
        for (const v of adj[u]) {
            if (--inDeg[v] === 0) q.push(v);
        }
    }
    return count === numCourses;
}"""
                }
            }
        ]
    },
    {
        "topic": "Dynamic Programming",
        "description": "Optimal substructure, overlapping subproblems, memoization, and tabular bottom-up solutions.",
        "problems": [
            {
                "id": "dsa-15",
                "title": "Coin Change",
                "difficulty": "Medium",
                "leetcode_url": "https://leetcode.com/problems/coin-change/",
                "gfg_url": "https://www.geeksforgeeks.org/coin-change-dp-7/",
                "statement": "Given an integer array coins representing coins of different denominations and an integer amount, return the fewest number of coins that you need to make up that amount. If cannot be made, return -1.",
                "approach": "Bottom-up 1D DP: Let dp[i] be the minimum coins needed for amount i. Initialize dp[0] = 0, and all other dp entries to infinity (or amount + 1). For each i from 1 to amount, and each coin c, dp[i] = min(dp[i], 1 + dp[i - c]) if i >= c.",
                "time_complexity": "O(amount * coins.length)",
                "space_complexity": "O(amount)",
                "code": {
                    "cpp": """int coinChange(vector<int>& coins, int amount) {
    vector<int> dp(amount + 1, amount + 1);
    dp[0] = 0;
    for (int i = 1; i <= amount; ++i) {
        for (int c : coins) {
            if (i >= c) dp[i] = min(dp[i], 1 + dp[i - c]);
        }
    }
    return dp[amount] > amount ? -1 : dp[amount];
}""",
                    "python": """def coinChange(coins: list[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for c in coins:
            if i >= c:
                dp[i] = min(dp[i], 1 + dp[i - c])
    return dp[amount] if dp[amount] != float('inf') else -1""",
                    "java": """public int coinChange(int[] coins, int amount) {
    int[] dp = new int[amount + 1];
    Arrays.fill(dp, amount + 1);
    dp[0] = 0;
    for (int i = 1; i <= amount; i++) {
        for (int c : coins) {
            if (i >= c) dp[i] = Math.min(dp[i], 1 + dp[i - c]);
        }
    }
    return dp[amount] > amount ? -1 : dp[amount];
}""",
                    "javascript": """function coinChange(coins, amount) {
    const dp = new Array(amount + 1).fill(amount + 1);
    dp[0] = 0;
    for (let i = 1; i <= amount; i++) {
        for (const c of coins) {
            if (i >= c) dp[i] = Math.min(dp[i], 1 + dp[i - c]);
        }
    }
    return dp[amount] > amount ? -1 : dp[amount];
}"""
                }
            },
            {
                "id": "dsa-16",
                "title": "Longest Common Subsequence (LCS)",
                "difficulty": "Medium",
                "leetcode_url": "https://leetcode.com/problems/longest-common-subsequence/",
                "gfg_url": "https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/",
                "statement": "Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.",
                "approach": "2D DP Table: dp[i][j] stores the LCS length of text1[0..i-1] and text2[0..j-1]. If characters match: dp[i][j] = 1 + dp[i-1][j-1]. Otherwise, take the maximum of excluding one character from either text: max(dp[i-1][j], dp[i][j-1]).",
                "time_complexity": "O(M * N)",
                "space_complexity": "O(M * N) (or O(min(M, N)) with space optimization)",
                "code": {
                    "cpp": """int longestCommonSubsequence(string text1, string text2) {
    int m = text1.size(), n = text2.size();
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
    for (int i = 1; i <= m; ++i) {
        for (int j = 1; j <= n; ++j) {
            if (text1[i - 1] == text2[j - 1]) dp[i][j] = 1 + dp[i - 1][j - 1];
            else dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
        }
    }
    return dp[m][n];
}""",
                    "python": """def longestCommonSubsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]""",
                    "java": """public int longestCommonSubsequence(String text1, String text2) {
    int m = text1.length(), n = text2.length();
    int[][] dp = new int[m + 1][n + 1];
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (text1.charAt(i - 1) == text2.charAt(j - 1)) dp[i][j] = 1 + dp[i - 1][j - 1];
            else dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
        }
    }
    return dp[m][n];
}""",
                    "javascript": """function longestCommonSubsequence(text1, text2) {
    const m = text1.length, n = text2.length;
    const dp = Array.from({length: m + 1}, () => new Array(n + 1).fill(0));
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (text1[i - 1] === text2[j - 1]) dp[i][j] = 1 + dp[i - 1][j - 1];
            else dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
        }
    }
    return dp[m][n];
}"""
                }
            }
        ]
    }
]
