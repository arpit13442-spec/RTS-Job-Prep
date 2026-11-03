"""
Extended Seed Data for Job Portal & Prep Website
Supplements seed_data.py with extra companies, technical topics, aptitude categories, and DSA sheets.
"""

EXTRA_COMPANIES = [
    {
        "id": "wipro",
        "name": "Wipro",
        "type": "IT & Services",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/a/a0/Wipro_Primary_Logo_Color_RGB.svg",
        "tier": "National Talent Hunt (NTH) / Elite & Turbo",
        "ctc": "Elite: ₹3.5 LPA | Turbo: ₹6.5 LPA",
        "eligibility": {
            "degree": "B.E. / B.Tech / M.E. / M.Tech / 5 year Integrated-M.Tech",
            "cgpa": "60% or 6.0 CGPA in 10th, 12th, and Graduation",
            "backlogs": "1 backlog allowed at assessment time; 0 at onboarding",
            "gap_years": "Maximum 3 years education gap allowed"
        },
        "exam_pattern": {
            "total_rounds": "2 Stages (Online Assessment + Interview)",
            "rounds": [
                {
                    "name": "Round 1: Online Assessment (AMCAT Platform)",
                    "duration": "128 Minutes",
                    "format": "Aptitude (48 mins) + Written Communication (20 mins) + Online Coding (60 mins, 2 problems)",
                    "details": "Sectional cutoffs. Quants (16 Q), Logical (14 Q), Verbal (22 Q). Coding allows C, C++, Java, Python."
                },
                {
                    "name": "Round 2: Technical & HR Discussion",
                    "duration": "20 - 30 Minutes",
                    "format": "One-on-one virtual interview",
                    "details": "College major projects, basic data structures, willingness to relocate to any Wipro campus, night shifts."
                }
            ]
        },
        "syllabus": [
            "Aptitude: Profit & Loss, Percentages, Coding-Decoding, Blood Relations, Reading Comprehension.",
            "Essay Writing: Coherence, grammar, sentence structure, spellings (graded by automated AI engine).",
            "Coding: Array frequency, string reversals, patterns, number manipulation."
        ],
        "past_questions": [
            "Find the frequency of each element in an array and print in sorted order.",
            "Write a program to remove vowels from a string and count consonants.",
            "Explain the difference between call by value and call by reference.",
            "What is primary key vs candidate key in SQL?"
        ],
        "tips": "In the essay writing test, avoid spelling mistakes and informal slang; the automated evaluator deducts heavy marks for punctuation errors."
    },
    {
        "id": "cognizant",
        "name": "Cognizant",
        "type": "IT & Services",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/9/95/Cognizant_logo_2022.svg",
        "tier": "GenC / GenC Elevate / GenC Next",
        "ctc": "GenC: ₹4.0 LPA | GenC Elevate: ₹5.5 LPA | GenC Next: ₹6.75 - ₹9 LPA",
        "eligibility": {
            "degree": "B.E. / B.Tech / M.E. / M.Tech / MCA / M.Sc (CS/IT)",
            "cgpa": "60% or 6.0 CGPA throughout 10th, 12th, and Degree",
            "backlogs": "Zero active backlogs at time of selection",
            "gap_years": "Max 12 months gap between academics"
        },
        "exam_pattern": {
            "total_rounds": "3 Stages",
            "rounds": [
                {
                    "name": "Round 1: GenC / Elevate Assessment",
                    "duration": "100 - 120 Minutes",
                    "format": "Numerical Ability, Verbal, Analytical Ability + Hands-on Coding",
                    "details": "Conducted on Superset / HirePro platform. Higher score elevates to GenC Next coding round."
                },
                {
                    "name": "Round 2: Technical Interview",
                    "duration": "30 - 45 Minutes",
                    "format": "Live problem-solving and resume deep-dive",
                    "details": "Questions on Java/Python, Object-Oriented principles, SQL queries, and DBMS keys."
                },
                {
                    "name": "Round 3: HR Round",
                    "duration": "15 - 20 Minutes",
                    "format": "Document verification and behavioral fit",
                    "details": "Location preferences, career goals, shift flexibility."
                }
            ]
        },
        "syllabus": [
            "Cognitive: Quantitative, Logical, Verbal, Automata Fix (debugging 7 code snippets).",
            "Technical: SQL Joins, HTML/CSS/JS basics, Java Collections / Python Dictionaries."
        ],
        "past_questions": [
            "Automata fix: Correct the logic error in bubble sort code snippet.",
            "Find the first non-repeating character in a stream of characters.",
            "SQL query to find employees with salaries higher than their managers.",
            "What is method overriding vs method overloading?"
        ],
        "tips": "Automata Fix requires debugging pre-written code with compiler errors or logical bugs under 20 minutes. Practice code tracing."
    },
    {
        "id": "atlassian",
        "name": "Atlassian",
        "type": "Product / Tier-1",
        "logo": "https://cdn.iconscout.com/icon/free/png-256/free-atlassian-logo-icon-download-in-svg-png-gif-file-formats--brand-social-media-pack-logos-icons-226522.png?f=webp&w=256",
        "tier": "Tier-1 Global",
        "ctc": "₹26 - ₹36 LPA (Fresher Graduate Software Engineer)",
        "eligibility": {
            "degree": "B.Tech / M.Tech / Dual Degree in Computer Science or related",
            "cgpa": "7.0+ CGPA preferred, strong coding profile",
            "backlogs": "Zero backlogs",
            "gap_years": "Standard university norms"
        },
        "exam_pattern": {
            "total_rounds": "4 Rounds",
            "rounds": [
                {
                    "name": "Round 1: Online Assessment (OA)",
                    "duration": "90 Minutes",
                    "format": "3-4 Algorithmic Coding Problems on HackerRank",
                    "details": "DP, Graphs, Strings, Greedy. Passing requires passing all test cases on at least 3 problems."
                },
                {
                    "name": "Round 2: Coding & Data Structures",
                    "duration": "60 Minutes",
                    "format": "1 Hard or 2 Medium DSA problems",
                    "details": "Strong focus on clean modular code, writing unit test cases, and edge handling."
                },
                {
                    "name": "Round 3: Craft / Low Level Design (LLD)",
                    "duration": "60 Minutes",
                    "format": "Object-Oriented Design & Code Implementation",
                    "details": "Design a File System, Rate Limiter, In-memory Tagged Content, or Snake Game."
                },
                {
                    "name": "Round 4: Values & Culture Interview",
                    "duration": "45 Minutes",
                    "format": "Atlassian Core Values Assessment",
                    "details": "Values: 'Open company, no bullshit', 'Build with heart and balance', 'Don't #@!% the customer', 'Play, as a team', 'Be the change you seek'."
                }
            ]
        },
        "syllabus": [
            "DSA: Graph Algorithms, Dynamic Programming, Heap, Trie, Sliding Window.",
            "LLD & OOP: SOLID principles, Design Patterns, Writing extensible object schemas.",
            "Concurrency: Multi-threading, Race Conditions, Thread-safe data structures."
        ],
        "past_questions": [
            "Design an in-memory File System with mkdir, addContentToFile, readContentFromFile.",
            "Implement a Rate Limiter with Token Bucket or Sliding Window Log algorithm.",
            "All O`one Data Structure with inc, dec, getMaxKey, getMinKey in O(1).",
            "Find the celebrity in a party of N people."
        ],
        "tips": "Atlassian puts massive weight on their Values Interview. Be authentic, transparent about mistakes, and demonstrate team-first collaboration."
    },
    {
        "id": "uber",
        "name": "Uber",
        "type": "Product / Tier-1",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/c/cc/Uber_logo_2018.png",
        "tier": "Tier-1 Global",
        "ctc": "₹32 - ₹50 LPA (Total compensation package)",
        "eligibility": {
            "degree": "B.Tech / M.Tech in CS / IT / EE",
            "cgpa": "7.5+ CGPA preferred",
            "backlogs": "No active backlogs",
            "gap_years": "University standard"
        },
        "exam_pattern": {
            "total_rounds": "4-5 Rounds",
            "rounds": [
                {
                    "name": "Round 1: Codesignal OA",
                    "duration": "70 Minutes",
                    "format": "4 Coding questions (Codesignal General Coding Assessment)",
                    "details": "Fast implementation + tricky edge-cases. Score > 800 usually needed."
                },
                {
                    "name": "Round 2: Data Structures & Algorithms",
                    "duration": "60 Minutes",
                    "format": "2 Hard Algorithmic Problems",
                    "details": "Graph BFS/DFS, Dijkstra, Segment Trees, Topological Sorting, Dynamic Programming."
                },
                {
                    "name": "Round 3: Advanced Coding & Concurrency",
                    "duration": "60 Minutes",
                    "format": "Complex system problem or concurrent data structure",
                    "details": "e.g., Thread-safe bounded queue, Rate limiter, Distributed ID generator."
                },
                {
                    "name": "Round 4: Engineering Manager / Cultural Fit",
                    "duration": "45 - 60 Minutes",
                    "format": "Past engineering challenges, trade-offs, architecture decisions",
                    "details": "Deep dive into real-world software failures, scale considerations, and bias for action."
                }
            ]
        },
        "syllabus": [
            "DSA: Advanced Graphs (Shortest Paths, MST, DSU), Dynamic Programming on Trees/Bitmask, Heaps.",
            "Concurrency & OS: Locks, Condition variables, Multi-threading, Race condition avoidance.",
            "System Concepts: Geospatial indexing (H3, Geohash, QuadTree), Distributed caching."
        ],
        "past_questions": [
            "Implement a Bus Route problem (BFS over bipartite graph of routes and stops).",
            "Evaluate Division (Graph DFS/BFS with weighted edges).",
            "Design an in-memory Rate Limiter supporting multiple users and custom quotas.",
            "Find median in a stream of running integers using two heaps."
        ],
        "tips": "Uber interviewers value extreme runtime optimization and rigorous boundary checks (empty inputs, integer overflow, memory leaks)."
    }
]

EXTRA_DSA_TOPICS = [
    {
        "topic": "Strings",
        "description": "Character manipulation, palindromes, anagrams, substring patterns, and string matching.",
        "problems": [
            {
                "id": "dsa-17",
                "title": "Valid Anagram",
                "difficulty": "Easy",
                "leetcode_url": "https://leetcode.com/problems/valid-anagram/",
                "gfg_url": "https://www.geeksforgeeks.org/check-whether-two-strings-are-anagram-of-each-other/",
                "statement": "Given two strings s and t, return true if t is an anagram of s, and false otherwise.",
                "approach": "Frequency array of size 26. Count character frequencies in s (increment) and t (decrement). If all counts remain 0, they are anagrams.",
                "time_complexity": "O(N)",
                "space_complexity": "O(1) (26 characters)",
                "code": {
                    "cpp": """bool isAnagram(string s, string t) {
    if (s.length() != t.length()) return false;
    int counts[26] = {0};
    for (int i = 0; i < s.length(); ++i) {
        counts[s[i] - 'a']++;
        counts[t[i] - 'a']--;
    }
    for (int c : counts) if (c != 0) return false;
    return true;
}""",
                    "python": """def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t): return False
    count = {}
    for ch in s: count[ch] = count.get(ch, 0) + 1
    for ch in t:
        if ch not in count or count[ch] == 0: return False
        count[ch] -= 1
    return True""",
                    "java": """public boolean isAnagram(String s, String t) {
    if (s.length() != t.length()) return false;
    int[] count = new int[26];
    for (int i = 0; i < s.length(); i++) {
        count[s.charAt(i) - 'a']++;
        count[t.charAt(i) - 'a']--;
    }
    for (int c : count) if (c != 0) return false;
    return true;
}""",
                    "javascript": """function isAnagram(s, t) {
    if (s.length !== t.length) return false;
    const count = {};
    for (const c of s) count[c] = (count[c] || 0) + 1;
    for (const c of t) {
        if (!count[c]) return false;
        count[c]--;
    }
    return true;
}"""
                }
            },
            {
                "id": "dsa-18",
                "title": "Longest Palindromic Substring",
                "difficulty": "Medium",
                "leetcode_url": "https://leetcode.com/problems/longest-palindromic-substring/",
                "gfg_url": "https://www.geeksforgeeks.org/longest-palindromic-substring/",
                "statement": "Given a string s, return the longest palindromic substring in s.",
                "approach": "Expand Around Center: For each character (odd length centers) and pair of adjacent characters (even length centers), expand outwards while characters match. Track max palindrome length and start index.",
                "time_complexity": "O(N^2)",
                "space_complexity": "O(1)",
                "code": {
                    "cpp": """string longestPalindrome(string s) {
    int start = 0, maxLen = 0;
    auto expand = [&](int l, int r) {
        while (l >= 0 && r < s.length() && s[l] == s[r]) { --l; ++r; }
        if (r - l - 1 > maxLen) {
            start = l + 1;
            maxLen = r - l - 1;
        }
    };
    for (int i = 0; i < s.length(); ++i) {
        expand(i, i);
        expand(i, i + 1);
    }
    return s.substr(start, maxLen);
}""",
                    "python": """def longestPalindrome(s: str) -> str:
    start, max_len = 0, 0
    def expand(l, r):
        nonlocal start, max_len
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        if r - l - 1 > max_len:
            start, max_len = l + 1, r - l - 1
    for i in range(len(s)):
        expand(i, i)
        expand(i, i + 1)
    return s[start:start + max_len]""",
                    "java": """public String longestPalindrome(String s) {
    int start = 0, maxLen = 0;
    for (int i = 0; i < s.length(); i++) {
        int len1 = expand(s, i, i);
        int len2 = expand(s, i, i + 1);
        int len = Math.max(len1, len2);
        if (len > maxLen) {
            maxLen = len;
            start = i - (len - 1) / 2;
        }
    }
    return s.substring(start, start + maxLen);
}
private int expand(String s, int l, int r) {
    while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) { l--; r++; }
    return r - l - 1;
}""",
                    "javascript": """function longestPalindrome(s) {
    let start = 0, maxLen = 0;
    function expand(l, r) {
        while (l >= 0 && r < s.length && s[l] === s[r]) { l--; r++; }
        if (r - l - 1 > maxLen) {
            start = l + 1;
            maxLen = r - l - 1;
        }
    }
    for (let i = 0; i < s.length; i++) {
        expand(i, i);
        expand(i, i + 1);
    }
    return s.substring(start, start + maxLen);
}"""
                }
            }
        ]
    },
    {
        "topic": "Stacks & Queues",
        "description": "LIFO and FIFO operations, monotonic stacks, bracket validation, and cache structures.",
        "problems": [
            {
                "id": "dsa-19",
                "title": "Valid Parentheses",
                "difficulty": "Easy",
                "leetcode_url": "https://leetcode.com/problems/valid-parentheses/",
                "gfg_url": "https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/",
                "statement": "Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.",
                "approach": "Push opening brackets onto a stack. When a closing bracket arrives, verify that the stack is non-empty and the top matches the corresponding opening bracket. Pop the matched bracket.",
                "time_complexity": "O(N)",
                "space_complexity": "O(N)",
                "code": {
                    "cpp": """bool isValid(string s) {
    stack<char> st;
    for (char c : s) {
        if (c == '(' || c == '{' || c == '[') st.push(c);
        else {
            if (st.empty()) return false;
            char top = st.top(); st.pop();
            if ((c == ')' && top != '(') ||
                (c == '}' && top != '{') ||
                (c == ']' && top != '[')) return false;
        }
    }
    return st.empty();
}""",
                    "python": """def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for c in s:
        if c in mapping:
            if not stack or stack.pop() != mapping[c]:
                return False
        else:
            stack.append(c)
    return not stack""",
                    "java": """public boolean isValid(String s) {
    Stack<Character> stack = new Stack<>();
    for (char c : s.toCharArray()) {
        if (c == '(') stack.push(')');
        else if (c == '{') stack.push('}');
        else if (c == '[') stack.push(']');
        else if (stack.isEmpty() || stack.pop() != c) return false;
    }
    return stack.isEmpty();
}""",
                    "javascript": """function isValid(s) {
    const stack = [];
    const map = { ')': '(', '}': '{', ']': '[' };
    for (const c of s) {
        if (map[c]) {
            if (stack.pop() !== map[c]) return false;
        } else {
            stack.push(c);
        }
    }
    return stack.length === 0;
}"""
                }
            },
            {
                "id": "dsa-20",
                "title": "LRU Cache (Least Recently Used)",
                "difficulty": "Medium",
                "leetcode_url": "https://leetcode.com/problems/lru-cache/",
                "gfg_url": "https://www.geeksforgeeks.org/lru-cache-implementation/",
                "statement": "Design a data structure that follows the constraints of a Least Recently Used (LRU) cache with get(key) and put(key, value) operations running in O(1) average time complexity.",
                "approach": "Combine a Hash Map (for O(1) key-to-node lookup) and a Doubly Linked List (for O(1) removal and insertion at head). On get/put, move the accessed node to the head. When capacity is exceeded, evict the tail node.",
                "time_complexity": "O(1) for both get and put",
                "space_complexity": "O(Capacity)",
                "code": {
                    "cpp": """class LRUCache {
    int cap;
    list<pair<int, int>> lru;
    unordered_map<int, list<pair<int, int>>::iterator> mp;
public:
    LRUCache(int capacity) : cap(capacity) {}
    int get(int key) {
        if (!mp.count(key)) return -1;
        lru.splice(lru.begin(), lru, mp[key]);
        return mp[key]->second;
    }
    void put(int key, int value) {
        if (mp.count(key)) {
            lru.splice(lru.begin(), lru, mp[key]);
            mp[key]->second = value;
            return;
        }
        if (lru.size() == cap) {
            int k = lru.back().first;
            lru.pop_back();
            mp.erase(k);
        }
        lru.push_front({key, value});
        mp[key] = lru.begin();
    }
};""",
                    "python": """class Node:
    def __init__(self, k, v):
        self.k, self.v = k, v
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.v
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.k]""",
                    "java": """class LRUCache {
    private class Node { int k, v; Node prev, next; Node(int k, int v) { this.k = k; this.v = v; } }
    private int cap;
    private Map<Integer, Node> map = new HashMap<>();
    private Node head = new Node(0, 0), tail = new Node(0, 0);

    public LRUCache(int capacity) {
        this.cap = capacity;
        head.next = tail; tail.prev = head;
    }
    public int get(int key) {
        if (!map.containsKey(key)) return -1;
        Node node = map.get(key);
        remove(node); add(node);
        return node.v;
    }
    public void put(int key, int value) {
        if (map.containsKey(key)) remove(map.get(key));
        Node node = new Node(key, value);
        add(node); map.put(key, node);
        if (map.size() > cap) {
            Node lru = tail.prev;
            remove(lru); map.remove(lru.k);
        }
    }
    private void remove(Node n) { n.prev.next = n.next; n.next.prev = n.prev; }
    private void add(Node n) { n.next = head.next; n.prev = head; head.next.prev = n; head.next = n; }
}""",
                    "javascript": """class LRUCache {
    constructor(capacity) {
        this.cap = capacity;
        this.cache = new Map();
    }
    get(key) {
        if (!this.cache.has(key)) return -1;
        const v = this.cache.get(key);
        this.cache.delete(key);
        this.cache.set(key, v);
        return v;
    }
    put(key, value) {
        if (this.cache.has(key)) this.cache.delete(key);
        this.cache.set(key, value);
        if (this.cache.size > this.cap) {
            const firstKey = this.cache.keys().next().value;
            this.cache.delete(firstKey);
        }
    }
}"""
                }
            }
        ]
    },
    {
        "topic": "Binary Search",
        "description": "Logarithmic search on sorted arrays, search spaces, rotated arrays, and predicate monotonicity.",
        "problems": [
            {
                "id": "dsa-21",
                "title": "Search in Rotated Sorted Array",
                "difficulty": "Medium",
                "leetcode_url": "https://leetcode.com/problems/search-in-rotated-sorted-array/",
                "gfg_url": "https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/",
                "statement": "Given a sorted array of distinct values nums rotated at some unknown pivot, and a target, return the index of target if found, or -1 if not.",
                "approach": "At least one half of the array [low..mid] or [mid..high] is always strictly sorted. Determine which half is sorted, check if target lies within its bounds, and discard the other half.",
                "time_complexity": "O(log N)",
                "space_complexity": "O(1)",
                "code": {
                    "cpp": """int search(vector<int>& nums, int target) {
    int low = 0, high = nums.size() - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (nums[mid] == target) return mid;
        if (nums[low] <= nums[mid]) {
            if (nums[low] <= target && target < nums[mid]) high = mid - 1;
            else low = mid + 1;
        } else {
            if (nums[mid] < target && target <= nums[high]) low = mid + 1;
            else high = mid - 1;
        }
    }
    return -1;
}""",
                    "python": """def search(nums: list[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1""",
                    "java": """public int search(int[] nums, int target) {
    int low = 0, high = nums.length - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (nums[mid] == target) return mid;
        if (nums[low] <= nums[mid]) {
            if (nums[low] <= target && target < nums[mid]) high = mid - 1;
            else low = mid + 1;
        } else {
            if (nums[mid] < target && target <= nums[high]) low = mid + 1;
            else high = mid - 1;
        }
    }
    return -1;
}""",
                    "javascript": """function search(nums, target) {
    let low = 0, high = nums.length - 1;
    while (low <= high) {
        const mid = Math.floor((low + high) / 2);
        if (nums[mid] === target) return mid;
        if (nums[low] <= nums[mid]) {
            if (nums[low] <= target && target < nums[mid]) high = mid - 1;
            else low = mid + 1;
        } else {
            if (nums[mid] < target && target <= nums[high]) low = mid + 1;
            else high = mid - 1;
        }
    }
    return -1;
}"""
                }
            }
        ]
    },
    {
        "topic": "Bit Manipulation",
        "description": "Bitwise XOR, AND, OR, left/right shifts, masks, and low-level arithmetic.",
        "problems": [
            {
                "id": "dsa-22",
                "title": "Single Number",
                "difficulty": "Easy",
                "leetcode_url": "https://leetcode.com/problems/single-number/",
                "gfg_url": "https://www.geeksforgeeks.org/find-element-appears-once-array-every-element-appears-twice/",
                "statement": "Given a non-empty array of integers nums, every element appears twice except for one. Find that single one. You must implement a solution with a linear runtime complexity and use only constant extra space.",
                "approach": "XOR property: x ^ x = 0 and x ^ 0 = x. XORing all elements together causes all duplicate pairs to cancel each other out, leaving only the single unique number.",
                "time_complexity": "O(N)",
                "space_complexity": "O(1)",
                "code": {
                    "cpp": """int singleNumber(vector<int>& nums) {
    int res = 0;
    for (int n : nums) res ^= n;
    return res;
}""",
                    "python": """def singleNumber(nums: list[int]) -> int:
    res = 0
    for n in nums:
        res ^= n
    return res""",
                    "java": """public int singleNumber(int[] nums) {
    int res = 0;
    for (int n : nums) res ^= n;
    return res;
}""",
                    "javascript": """function singleNumber(nums) {
    return nums.reduce((acc, curr) => acc ^ curr, 0);
}"""
                }
            }
        ]
    }
]

EXTRA_TECHNICAL_SUBJECTS = [
    {
        "id": "system-design",
        "name": "System Design Fundamentals",
        "icon": "fa-server",
        "summary": "High-Level Architecture, Scalability, Caching, Load Balancing, CDN, Microservices, and Message Queues.",
        "key_notes": [
            "Horizontal vs Vertical Scaling: Vertical scaling (scaling up) means adding more RAM/CPU to an existing machine (has hardware limit). Horizontal scaling (scaling out) means adding more commodity machines (stateless servers behind a load balancer).",
            "Load Balancers: Distribute traffic across server pool. Algorithms: Round Robin, Weighted Round Robin, Least Connections, IP Hash. Layer 4 (Transport, TCP/UDP) vs Layer 7 (Application, HTTP/URL paths).",
            "Caching Strategies: Cache-Aside (Lazy loading), Write-Through, Write-Behind, Write-Around. Cache eviction policies: LRU (Least Recently Used), LFU (Least Frequently Used), FIFO.",
            "Database Sharding & Replication: Master-Replica for read scaling. Sharding (Horizontal partitioning) by Shard Key (Hash-based, Range-based) for write scaling.",
            "Message Queues (Kafka, RabbitMQ): Decouples producers from consumers, provides backpressure, buffer bursts, and asynchronous background job execution."
        ],
        "qa_list": [
            {
                "q": "Design a URL Shortener service (like TinyURL / bit.ly). What are the key architectural components?",
                "a": "1. Functional Requirements: Given long URL, generate unique short URL (e.g., domain/abc123). Given short URL, redirect with HTTP 301/302 to original destination.\n2. Hash Algorithm: Base62 encoding (a-z, A-Z, 0-9). With 7 characters, 62^7 = ~3.5 trillion unique combinations.\n3. Counter/Token Service: A distributed Snowflake ID generator or Range-based ZooKeeper token distributor generates unique sequential 64-bit IDs converted to Base62.\n4. Caching: 80-20 rule. Cache top 20% most accessed URLs in Redis to serve 80% of reads with sub-millisecond latency.\n5. Database: Relational (PostgreSQL) or NoSQL (Cassandra/DynamoDB) with schema: id (PK), hash_key (Indexed), original_url, created_at, expires_at."
            },
            {
                "q": "What is the difference between Cache-Aside and Write-Through caching?",
                "a": "Cache-Aside: The application first checks the cache. If cache miss, it reads from the database, stores the result in the cache, and returns it. Good for read-heavy workloads where data doesn't change frequently.\nWrite-Through: The application writes to the cache, and the cache synchronously writes to the database before returning success. Guarantees consistency between cache and DB, but introduces write latency."
            }
        ]
    }
]
