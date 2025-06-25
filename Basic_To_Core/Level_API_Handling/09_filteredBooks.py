import requests
url = "https://api.freeapi.app/api/v1/public/books?page=1&limit=2&inc=kind%252Cid%252Cetag%252CvolumeInfo&query=tech"
def fetchBooks(page=1, limit=2):
    params = {"page": page, "limit": limit}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error occurred: {e}")
        return None

# Filter books where publisher is "Addison-Wesley Signature Series (Cohn)"
target_publisher = "Addison-Wesley Signature Series (Cohn)"

# Loop through first 3 pages
for page in range(1, 4):
    data = fetchBooks(page=page, limit=2)
    if data:
        books = data.get("data", {}).get("data", [])
        matching_books = [
            book for book in books 
            if book.get("volumeInfo", {}).get("publisher") == target_publisher
        ]

        print(f"\n--- Page {page} - Books from {target_publisher} ---")
        if not matching_books:
            print("No matching books found on this page.")
        else:
            for book in matching_books:
                title = book.get("volumeInfo", {}).get("title", "")
                authors = book.get("volumeInfo", {}).get("authors", [])
                print(f"Title: {title}, Author(s): {', '.join(authors)}")