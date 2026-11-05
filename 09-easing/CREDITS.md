# Credits

## Voice, music and sound effects
- **Voiceover:** ElevenLabs premade voice "Chris" (`eleven_multilingual_v2`), one line per beat.
- **Music:** a new ElevenLabs-generated smooth lo-fi house bed (117 BPM, G minor), used only in this reel.
- **Effects:** the same ElevenLabs pops / whooshes / clicks / chime as posts 06-08, mixed to -14 LUFS.

## The effect
One line of CSS: `transition: transform .8s cubic-bezier(.16, 1, .3, 1);` (easeOutExpo: fast start, soft landing).
In the reel the three pills are driven by GSAP using a real cubic-bezier solver as the ease, so each lane moves exactly
like its CSS timing function (`linear`, `ease-out`, `cubic-bezier(.16,1,.3,1)`), and every rendered frame is deterministic.
