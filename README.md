# 5 Degrees of Wiki

This application is designed to either randomly retrieve or take the user's input for wikipedia pages and proceed to 
scrape the links within each article and traverse between them based on user input until they run out of turns or reach
their target page.

## 401d19 Midterm

### Authors: Dana Huffman, Falashade Greene, Gina Napier, Vinny Shipley, Jamall Malik

### Links & Resources

https://github.com/Team-five-code-fellows/Prep

https://en.wikipedia.org/wiki/Main_Page

### Setup

pip install -r requirements.txt

### Initialize

python3.10 -m venv .venv

python source .venv/activate/bin

python -m app.game

### Tests

tests are in tests/test_game.py

run with pytest