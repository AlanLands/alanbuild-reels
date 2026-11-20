# 18 · 1 prompt. A 3D glass logo.

The reel: one prompt to Claude, one HTML file back, and that file is the turning glass badge you see.

## The prompt (all of it, also in `prompt.txt`)

> One HTML file, no libraries: the letters AB as a slowly turning 3D glass badge, deep green #1F4D12 and light green #7CC552 on a white page, under 80 lines.

## How it was made

- A fresh Claude agent (no earlier chat, no other files) got the prompt above, once.
- Its answer is `logo.html`, saved exactly as it came back: **first try, no edits**. 64 lines, no libraries, no imports, no images.
- The 3D is plain CSS: a stack of 14 thin layers pushed apart with `translateZ` for the thickness, a front and a back face, `perspective` on the page and one `rotateY` keyframe (14 s per turn). The glass is a translucent gradient, a white inner glow and a moving shine stripe.
- To put it in the reel, `logo.html` was opened unchanged in headless Chrome and screenshotted at fixed times (all CSS animations paused and set to each frame's time), then turned into a video.

## Try it

Open `logo.html` in any browser. That's it.

Known quirk we left in (first try means first try): when the back faces you, the letters show through the glass mirrored.
