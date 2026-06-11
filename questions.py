CATEGORIES = [
    {
        "id": "programming",
        "name": "Programming Fundamentals",
        "color": "#2563eb",
        "description": "Core CS concepts: algorithms, data structures, complexity.",
        "question_count": 10,
    },
    {
        "id": "java",
        "name": "Java",
        "color": "#0891b2",
        "description": "Java language, OOP principles, and JVM internals.",
        "question_count": 10,
    },
    {
        "id": "python",
        "name": "Python",
        "color": "#059669",
        "description": "Python syntax, standard library, and common patterns.",
        "question_count": 10,
    },
    {
        "id": "webdev",
        "name": "Web Development",
        "color": "#7c3aed",
        "description": "HTML, CSS, JavaScript, and web protocols.",
        "question_count": 10,
    },
    {
        "id": "gk",
        "name": "General Knowledge",
        "color": "#b45309",
        "description": "Science, history, geography, and current affairs.",
        "question_count": 10,
    },
]

QUESTIONS = {
    "programming": [
        {
            "question": "What does CPU stand for?",
            "options": ["Central Processing Unit", "Computer Personal Unit", "Central Program Utility", "Core Processing Unit"],
            "correct": 0,
        },
        {
            "question": "Which data structure follows LIFO order?",
            "options": ["Queue", "Stack", "Linked List", "Binary Tree"],
            "correct": 1,
        },
        {
            "question": "What is the time complexity of binary search?",
            "options": ["O(n)", "O(n²)", "O(log n)", "O(1)"],
            "correct": 2,
        },
        {
            "question": "Which is NOT one of the four pillars of OOP?",
            "options": ["Encapsulation", "Polymorphism", "Compilation", "Inheritance"],
            "correct": 2,
        },
        {
            "question": "A function that calls itself is called:",
            "options": ["Lambda function", "Recursive function", "Callback function", "Anonymous function"],
            "correct": 1,
        },
        {
            "question": "What does RAM stand for?",
            "options": ["Random Access Memory", "Read Access Module", "Rapid Application Memory", "Runtime Allocation Memory"],
            "correct": 0,
        },
        {
            "question": "Which sorting algorithm has O(n log n) average-case complexity?",
            "options": ["Bubble Sort", "Selection Sort", "Quick Sort", "Insertion Sort"],
            "correct": 2,
        },
        {
            "question": "An API is best described as:",
            "options": ["A type of database", "A contract for software components to communicate", "A programming language", "A network protocol"],
            "correct": 1,
        },
        {
            "question": "Which of the following is a statically compiled language?",
            "options": ["JavaScript", "Python", "Ruby", "C++"],
            "correct": 3,
        },
        {
            "question": "A deadlock occurs when:",
            "options": ["A program runs out of memory", "Two or more processes wait indefinitely for each other", "A network request times out", "A function recurses too deeply"],
            "correct": 1,
        },
    ],
    "java": [
        {
            "question": "Which keyword creates a subclass in Java?",
            "options": ["implements", "inherits", "extends", "super"],
            "correct": 2,
        },
        {
            "question": "Default value of an uninitialized int field in Java?",
            "options": ["null", "-1", "0", "undefined"],
            "correct": 2,
        },
        {
            "question": "Which of the following is a reference type in Java?",
            "options": ["int", "String", "boolean", "char"],
            "correct": 1,
        },
        {
            "question": "JVM stands for:",
            "options": ["Java Virtual Machine", "Java Variable Method", "Java Verified Module", "Java Version Manager"],
            "correct": 0,
        },
        {
            "question": "Every Java application requires which method signature?",
            "options": ["public void start()", "public static void main(String[] args)", "public void run()", "static void init()"],
            "correct": 1,
        },
        {
            "question": "To create a thread by implementing an interface, you use:",
            "options": ["Threadable", "Runnable", "Executable", "Worker"],
            "correct": 1,
        },
        {
            "question": "Multiple methods with the same name but different parameters is called:",
            "options": ["Method overriding", "Method overloading", "Polymorphism", "Abstraction"],
            "correct": 1,
        },
        {
            "question": "Which Java collection preserves insertion order and allows duplicates?",
            "options": ["HashSet", "TreeSet", "ArrayList", "HashMap"],
            "correct": 2,
        },
        {
            "question": "The finally block:",
            "options": ["Only runs if no exception occurs", "Runs only when an exception is caught", "Always runs regardless of exception", "Terminates the program"],
            "correct": 2,
        },
        {
            "question": "Which annotation signals an intended method override?",
            "options": ["@Overload", "@Super", "@Override", "@Inherit"],
            "correct": 2,
        },
    ],
    "python": [
        {
            "question": "Which syntax correctly creates a list in Python?",
            "options": ["x = (1,2,3)", "x = [1,2,3]", "x = {1,2,3}", "x = <1,2,3>"],
            "correct": 1,
        },
        {
            "question": "Which keyword defines a function in Python?",
            "options": ["function", "func", "def", "define"],
            "correct": 2,
        },
        {
            "question": "The pip tool is used to:",
            "options": ["Compile Python code", "Install and manage Python packages", "Debug Python programs", "Format source files"],
            "correct": 1,
        },
        {
            "question": "Which Python type is mutable?",
            "options": ["tuple", "str", "list", "frozenset"],
            "correct": 2,
        },
        {
            "question": "What does type([]) return?",
            "options": ["<class 'array'>", "<class 'list'>", "<class 'tuple'>", "<class 'object'>"],
            "correct": 1,
        },
        {
            "question": "The first parameter of an instance method refers to:",
            "options": ["The class itself", "The current instance", "The parent class", "A global namespace"],
            "correct": 1,
        },
        {
            "question": "The standard library module for regular expressions is:",
            "options": ["regex", "regexp", "re", "pattern"],
            "correct": 2,
        },
        {
            "question": "A lambda expression in Python is:",
            "options": ["A named recursive function", "A small anonymous function defined inline", "A built-in class method", "A decorator"],
            "correct": 1,
        },
        {
            "question": "Which library is primarily used for tabular data manipulation?",
            "options": ["NumPy", "Pandas", "Matplotlib", "SciPy"],
            "correct": 1,
        },
        {
            "question": "The __init__ method is called:",
            "options": ["When the class is imported", "When a new instance is created", "When the instance is deleted", "When a class method is invoked"],
            "correct": 1,
        },
    ],
    "webdev": [
        {
            "question": "HTML stands for:",
            "options": ["HyperText Markup Language", "High-level Text Machine Language", "HyperText Management Language", "Hybrid Transfer Markup Language"],
            "correct": 0,
        },
        {
            "question": "Which CSS property sets the foreground color of text?",
            "options": ["font-color", "text-color", "color", "foreground-color"],
            "correct": 2,
        },
        {
            "question": "The DOM is:",
            "options": ["A database format", "A tree-structured representation of an HTML document", "A CSS layout algorithm", "A JavaScript runtime"],
            "correct": 1,
        },
        {
            "question": "Which HTTP method submits form data to a server?",
            "options": ["GET", "PUT", "POST", "DELETE"],
            "correct": 2,
        },
        {
            "question": "CSS Flexbox is designed for:",
            "options": ["Animating elements", "One-dimensional layout of items", "Defining color variables", "Media queries"],
            "correct": 1,
        },
        {
            "question": "Which framework introduced the virtual DOM concept?",
            "options": ["Angular", "Vue", "React", "Svelte"],
            "correct": 2,
        },
        {
            "question": "HTTPS differs from HTTP because it:",
            "options": ["Uses a different port only", "Encrypts data in transit using TLS", "Compresses responses automatically", "Only supports GET requests"],
            "correct": 1,
        },
        {
            "question": "Which HTML element links an external CSS stylesheet?",
            "options": ["<style>", "<css>", "<link>", "<script>"],
            "correct": 2,
        },
        {
            "question": "Which is valid arrow function syntax in JavaScript?",
            "options": ["function() =>", "=> function()", "const fn = (x) => x * 2", "fn -> x * 2"],
            "correct": 2,
        },
        {
            "question": "The CSS unit rem is relative to:",
            "options": ["The parent element font size", "The viewport width", "The root element font size", "The screen resolution"],
            "correct": 2,
        },
    ],
    "gk": [
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Venus", "Mars", "Jupiter", "Saturn"],
            "correct": 1,
        },
        {
            "question": "The chemical symbol Au represents:",
            "options": ["Silver", "Aluminium", "Gold", "Argon"],
            "correct": 2,
        },
        {
            "question": "The Mona Lisa was painted by:",
            "options": ["Michelangelo", "Raphael", "Leonardo da Vinci", "Caravaggio"],
            "correct": 2,
        },
        {
            "question": "The largest ocean on Earth is:",
            "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
            "correct": 3,
        },
        {
            "question": "World War II ended in:",
            "options": ["1943", "1944", "1945", "1946"],
            "correct": 2,
        },
        {
            "question": "The approximate speed of light in vacuum is:",
            "options": ["300,000 km/s", "150,000 km/s", "500,000 km/s", "1,000,000 km/s"],
            "correct": 0,
        },
        {
            "question": "The Great Barrier Reef is located off the coast of:",
            "options": ["Brazil", "Indonesia", "Philippines", "Australia"],
            "correct": 3,
        },
        {
            "question": "The smallest country by land area is:",
            "options": ["Monaco", "San Marino", "Vatican City", "Liechtenstein"],
            "correct": 2,
        },
        {
            "question": "The adult human body has approximately how many bones?",
            "options": ["186", "206", "226", "246"],
            "correct": 1,
        },
        {
            "question": "The special theory of relativity was published by:",
            "options": ["Isaac Newton", "Nikola Tesla", "Albert Einstein", "Max Planck"],
            "correct": 2,
        },
    ],
}
