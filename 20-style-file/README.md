# 20 · A 10-line file. AI builds in my style.

The reel: the same prompt sent to Claude twice. Alone, it guesses (a blue button). With the ten rules of `STYLE.md` pasted under it, it builds the green pill.

## The prompt (also in `prompt.txt`)

> One HTML file, no libraries: a sign-up button for my app, centered on the page.

## How it was made

- Two fresh Claude sessions (`claude -p`, each in its own empty folder, no earlier chat), one try each, on 2026-11-26.
- Run 1 got the prompt alone. Run 2 got the same prompt plus "Follow the rules in STYLE.md:" and the ten lines.
- `answer_without.txt` and `answer_with.txt` are the full answers as they came back. `without.html` and `with.html` are the HTML code blocks from those answers, unedited.
- In the reel the two buttons are screenshots of those two files in headless Chrome (3x).
- In its first answer the model wrote: "The blue colour is also a guess, since I don't know your app's branding."

## Use it

Copy `STYLE.md`, change the ten rules to your own colours and shapes, and paste it under any UI prompt (or keep it in your project so your AI tool reads it).
