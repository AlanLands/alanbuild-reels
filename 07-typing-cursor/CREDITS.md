# Credits

## Voice, music and sound effects
- **Voiceover:** ElevenLabs premade voice "Chris" (`eleven_multilingual_v2`), one line per step.
- **Music + effects:** the same ElevenLabs-generated track and pops / whooshes / chime as posts 02-06, plus one soft click per typed letter, mixed to -14 LUFS.

## The effect
The five CSS lines on screen are the whole effect. In the reel, GSAP plays the same timing (1 s step-end blink, 2 s `steps(15)` width) so every rendered frame is deterministic. To use it on a site, paste the CSS on any monospace element.
