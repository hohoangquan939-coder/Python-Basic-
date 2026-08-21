
book = {
    "title": "AAAAA",
    "author": "Le Thi B",
    "year": 1998,
    "price ($)": 76
}

print(f"Ten sach: {book["title"]} - Tac gia: {book["author"]}")
book["price ($)"] *= 1.15
book["genre"] = "Comedy"

print(book.get("discount", "Khong co giam gia"))

for key, value in book.items():
    print(f"{key} : {value}")