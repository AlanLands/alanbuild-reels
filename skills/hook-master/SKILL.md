---
name: hook-master
description: Simulated audience test for a finished reel. Watches the video once with the `watch` skill, then sends 10 sub-agents, each a different human viewer persona (doomscroller, busy parent, designer, editor, skeptic, sound-off viewer...), to "scroll into" it and decide second by second whether they skip or keep watching. Ends with an analysis report (retention curve, skip points, actions, ranked fixes). Use when the user says "hook master", "/hook-master", "test this hook", "would people skip this", or wants a pre-post audience check on a video file or URL.
argument-hint: "<video-path-or-url> [character or niche]"
---

# Hook Master: 10 simulated viewers watch your reel

This is a SIMULATION, not real analytics. Say so in the report. For real numbers after posting, use your platform's insights.

## Step 1: watch once (main agent only)
Run the `watch` skill's script ONE time and keep the files so the agents can read them:

```bash
OUT=reports/hook_master/work/<slug>
python3 ~/.claude/skills/watch/scripts/watch.py "<source>" --out-dir "$OUT" --resolution 768
```

- Use 768px so on-screen text and captions are readable.
- For the first 3 seconds (where most skips happen), also run a dense pass: `--start 0 --end 3 --out-dir "$OUT/hook"` (2 fps).
- Save the printed transcript to `$OUT/transcript.txt`.
- Note the duration and the account's niche (who the reel is for).

Do not Read every frame yourself; the agents do the watching. Read just 2-3 frames to confirm the extraction worked.

## Step 2: send 10 persona agents in ONE message (parallel)
Spawn all 10 with the Agent tool in a single response, `subagent_type: general-purpose`, `model: sonnet` (10 agents x ~30 frames is expensive on the top model). Each prompt holds: the persona card below, the frame folder paths, the transcript path (EXCEPT persona 9, who gets no transcript and no audio), the video duration, the platform (Instagram Reels, 9:16, sound on by default), and the task + output format.

| # | Persona | Who they are and what makes them skip |
|---|---|---|
| 1 | **Doomscroller, 17** | Gen Z, thumb on the glass, decides in under 1 second. Skips anything slow, staged or "ad-like". Rewatches things that feel weird or funny. |
| 2 | **Busy parent, 38** | Scrolling on a lunch break, 20 spare seconds, tired. Stays only if the point is useful to their real life right now. |
| 3 | **Niche fan** | The exact target viewer of this account (e.g. a front-end dev for a coding page, a 55+ health-curious viewer for a wellness page). Already follows similar accounts; bored by advice they've heard before. |
| 4 | **AI skeptic, 30** | Hates fake-looking AI content. Hunts for warped hands, dead eyes, lip-sync drift, plastic skin. Skips (and maybe comments) the moment it looks AI, unless the content is good enough to forgive it. |
| 5 | **Graphic designer, 27** | Judges type, color, layout, text safe zones, captions covering the face, cluttered pills. Ugly or hard-to-read text makes them leave. |
| 6 | **Video editor, 33** | Judges pacing, dead air, cut timing, zoom, audio mix, music bed. Skips on a slow start or a sloppy cut. |
| 7 | **Retiree, 67** | Slower reader, watches with sound, likes warm and calm people, distrusts hype and fast talk. Shares good stuff to family. |
| 8 | **Hustle guy, 24** | Wants money/self-improvement value fast. Skips soft or vague openings, stays for a sharp contrarian claim. |
| 9 | **Sound-off viewer, 31** | On a train, phone muted. Sees ONLY the frames and on-screen text. If the captions and visuals don't carry the hook, they're gone. |
| 10 | **Rival creator, 29** | Makes content in the same niche. Watches to steal or judge; knows every hook trick. Notices clichés and asks "would I save this?" |

### Agent task (paste into each prompt)
> You are <persona card>. Stay in character: real human attention, real impatience, no politeness. You are scrolling Instagram Reels and this video appears.
> Read the hook frames first (`<OUT>/hook`), then the rest of the frames in time order (`<OUT>`), and the transcript (`<OUT>/transcript.txt`) unless you are the sound-off viewer.
> Decide, second by second, how much attention you give (0-10) and the exact second you would swipe away, if you would. If you'd stay, say whether you'd rewatch, like, comment, save, share, or follow.
> Be honest: most real viewers skip most reels. Don't invent things that aren't in the frames or transcript.
> Reply with ONLY this JSON:
> ```json
> {"persona": "", "skip_at_s": null, "why_skip_or_stay": "", "attention_per_second": [], "first_impression_0_1s": "", "best_moment": {"t": 0, "why": ""}, "worst_moment": {"t": 0, "why": ""}, "actions": {"rewatch": false, "like": false, "comment": false, "save": false, "share": false, "follow": false}, "comment_i_would_write": "", "one_fix": ""}
> ```
> `skip_at_s` = null means you watched to the end. `attention_per_second` has one number per second of video (stop at your skip second).

## Step 3: analysis report
When all 10 come back, build the report yourself (no extra agent). Save it to `reports/hook_master/YYYY-MM-DD_<slug>.md`:

1. **Verdict line**: hook score /100, 3-second hold %, completion %, ship / fix-then-ship / re-cut.
   - Hook score = average attention over 0-3s x 10, minus 10 per persona who skipped before 3s (floor 0).
2. **Retention curve**: % of the 10 still watching at each second (text table or ASCII bar per second).
3. **Skip map**: every skip second with who left and why; flag clusters (3+ skips within 1s = a problem moment).
4. **Persona table**: persona | skip at | attention avg | actions | their comment.
5. **What worked**: best moments named by 2+ personas.
6. **Ranked fixes**: merge the `one_fix` answers, rank by how many skips each would prevent, and mark which are local HyperFrames edits (text, trim, zoom, captions, music) vs. needing a new clip. Respect your own house rules (e.g. text safe zone, brand style).
7. **Predicted actions**: counts of rewatch / like / comment / save / share / follow out of 10.
8. Footer: "Simulated by 10 AI personas; real results vary. Check real numbers in your insights after posting."

Tell the user the report path, the verdict line, and the top 3 fixes. Delete `reports/hook_master/work/<slug>` unless they want to rerun.

## Rules
- Never post, edit or regenerate anything from this skill; it only reports. Fixes are suggestions for the user.
- One watch run, one round of 10 agents. Rerun only if the user asks (e.g. after a fix, to compare).
- If an agent returns bad JSON or no answer, use the other 9 and note it in the report.
