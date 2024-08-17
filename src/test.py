from src.main import JTF
import json

with open("../example.jtf", "r", encoding="utf-8") as file:
    data = file.read()

JTF.parse(json.loads(data))

print("Test successful!")
