import csv
import random

# Human-style templates
human_templates = [
    "I worked on a project where I {}.",
    "During my internship, I {}.",
    "In my experience, I {}.",
    "I usually approach problems by {}.",
    "I faced a challenge when I {}, but I solved it by {}.",
    "I improved my skills by {}.",
    "I collaborated with my team to {}.",
    "I learned {} while working on {}.",
    "I enjoy {} because it helps me {}.",
    "I built a system that {}."
]

human_actions = [
    "developed a web application",
    "fixed bugs in the system",
    "used Python for automation",
    "worked with APIs",
    "optimized performance",
    "learned new frameworks",
    "solved complex problems",
    "implemented new features",
    "debugged code efficiently",
    "improved system design"
]

# AI-style templates
ai_templates = [
    "Artificial intelligence is a field that {}.",
    "Machine learning is a method that {}.",
    "Python is a programming language that {}.",
    "Data science involves {}.",
    "Cloud computing allows {}.",
    "Cybersecurity focuses on {}.",
    "Software engineering is the discipline of {}.",
    "Big data refers to {}.",
    "Blockchain technology enables {}.",
    "Deep learning is a subset of AI that {}."
]

ai_definitions = [
    "enables machines to perform intelligent tasks",
    "analyzes data to make predictions",
    "supports multiple programming paradigms",
    "extracts insights from data",
    "provides scalable resources over the internet",
    "protects systems from cyber threats",
    "designs and develops software systems",
    "handles large volumes of data efficiently",
    "ensures secure transactions",
    "uses neural networks for learning"
]

# Generate dataset
rows = []

# Generate 100 human samples
for _ in range(100):
    template = random.choice(human_templates)
    action1 = random.choice(human_actions)
    action2 = random.choice(human_actions)

    text = template.format(action1, action2) if "{}" in template else template
    rows.append([text, 0])

# Generate 100 AI samples
for _ in range(100):
    template = random.choice(ai_templates)
    definition = random.choice(ai_definitions)

    text = template.format(definition)
    rows.append([text, 1])

# Save to CSV
with open("data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["text", "label"])
    writer.writerows(rows)

print("✅ Dataset generated with 200 samples!")