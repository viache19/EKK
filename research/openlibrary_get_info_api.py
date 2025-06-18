import requests

# Look for books with a key world
query = "Survival First Aid"
url = f"https://openlibrary.org/search.json?q={query}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for i, book in enumerate(data["docs"][:7], 1):
        print(f"{i}. {book.get('title')} - {book.get('author_name', ['Unknown'])[0]}")
        print(f"   Year: {book.get('first_publish_year')}")
        print(f"   OpenLibrary ID: {book.get('key')}")
        print()
else:
    print("Error while connecting to OpenLibrary")
