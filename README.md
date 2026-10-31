# AlanBuild reels

The source code of the [@alan.build](https://www.instagram.com/alan.build/) Instagram reels. Every reel is an HTML page
that [HyperFrames](https://hyperframes.heygen.com) renders frame by frame into a 1080×1920 MP4. There's no video editor:
the motion is a paused [GSAP](https://gsap.com) timeline, the look is plain CSS, and the sound is a mixed track of
real recorded sounds.

| Folder | Reel | Length |
|---|---|---|
| [`intro/`](intro) | "A new beginning": word roller, liquid-glass profile card, finger tap on Follow, end card | 11.4 s |
| [`02-this-reel-is-html/`](02-this-reel-is-html) | "This reel is 264 lines of HTML": the intro's own code scrolling next to the intro | 13.7 s |

## Render one

You need Node 18+ and Chrome or Chromium (HyperFrames drives a headless browser).

```bash
cd intro
npm run render          # writes an MP4 (npx downloads the pinned hyperframes CLI on first run)
npm run dev             # live preview in the browser while you edit
npm run check           # lint, layout and contrast checks
```

## How a reel is built

- **`index.html` is the whole film.** Each scene is a `div` with `class="clip"`, `data-start` and `data-duration`
  in seconds.
- **One paused GSAP timeline drives all the motion.** It's registered on `window.__timelines["main"]`, and
  HyperFrames seeks it frame by frame, so every render comes out identical.
- **The ideas the reels point at:**
  - **Liquid glass** is the `.lq` class (lines 36-45 of `intro/index.html`): a frosted
    `backdrop-filter`, a bright rim, inset highlights, and a sheen that moves on a `--sx` custom property.
  - **The word roller** is a 6-line `forEach` (lines 201-206) that steps a stack of words onto the beat.
  - **The finger tap** is 4 lines (248-251): the hand slides in, presses, lifts and leaves.
- **Sound** is one pre-mixed `assets/soundtrack.wav` under an `<audio>` tag, every effect placed on the frame
  where its action happens and the music cut at bar lines so its drop lands on the reveal.

## Fonts

The published reels use San Francisco, but Apple's licence doesn't allow redistributing it. This repo uses **Inter**
and **JetBrains Mono** instead. Both are open-source and bundled with HyperFrames, so the renders here look slightly
different from the posted reels. The line counts quoted in the reels still match (the SF `@font-face` lines became
one-line comments).

## Credits and licence

- **Code:** MIT (see [`LICENSE`](LICENSE)).
- **Music and sound effects:** `intro/` uses real recordings from Freesound.org (CC0 / CC BY, listed in its
  `CREDITS.md`; CC BY sounds need that credit if you reuse them). `02-this-reel-is-html/` uses music and effects
  generated with ElevenLabs (see its `CREDITS.md`).
- **Brand:** the AlanBuild name and the AB logo aren't licensed for reuse.

Made with code + AI by AlanBuild. Follow [@alan.build](https://www.instagram.com/alan.build/) for the next build.
