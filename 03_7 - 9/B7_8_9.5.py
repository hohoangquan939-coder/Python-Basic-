
students = [
    {   "name": "Ho Hoang Quan",
        "score": 8.5,},

    { "name": 'Nguyen Van An',
      "score": 9.2},

    { 'name': 'Le Thi Binh',
      'score': 4.5}
]

with open('students.txt','w') as f:
    for i in students:
        f.write(f"{i['name']} - {i['score']}\n")

with open('students.txt','r') as f:
    content = f.read()
    print(content)