import requests
from bs4 import BeautifulSoup

def print_secret_message(url):
    # 1. Fetch the content from the URL
    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching the URL: {e}")
        return

    # 2. Parse the HTML table
    soup = BeautifulSoup(response.text, 'html.parser')
    rows = soup.find_all('tr')
    
    data = []
    # Skip the header row (index 0)
    for row in rows[1:]:
        cols = row.find_all('td')
        if len(cols) == 3:
            try:
                # The table structure is usually: x-coord, character, y-coord
                x = int(cols[0].text.strip())
                char = cols[1].text.strip()
                y = int(cols[2].text.strip())
                data.append((x, y, char))
            except ValueError:
                # This skips rows that don't contain valid integers
                continue

    if not data:
        print("No valid coordinate data found at the URL.")
        return

    # 3. Determine the dimensions of the grid
    max_x = max(point[0] for point in data)
    max_y = max(point[1] for point in data)

    # 4. Initialize the grid with spaces
    # We use (max_y + 1) rows and (max_x + 1) columns
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # 5. Fill the grid with the characters
    for x, y, char in data:
        grid[y][x] = char

    # 6. Print the grid
    # Note: In this challenge, y=0 is typically the bottom row.
    # We print from max_y down to 0 to display it correctly.
    for r in range(max_y, -1, -1):
        print("".join(grid[r]))

# Usage
if __name__ == "__main__":
    url = input("Enter the URL containing the secret message table: ")
    print_secret_message(url)
 