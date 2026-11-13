# Starting prompts

These are the prompts we type in the videos, in order. They're short and plain on purpose: you talk to your agent like a person, not like a programmer.

Copy them if you get stuck, but **say it your own way** if you like. Your agent understands what you mean.

> **Tip:** press **Shift+Tab** to switch modes. Steps 2 and 3 start in **plan mode**: your agent can read and plan, but it can't change anything until you approve.

---

## 1. Set up your agent

Start Claude Code in your project folder, then type:

```
Read seed.md. You're my MPC agent now. Set yourself up.
```

Your agent creates its folders, then asks you four questions. Answer in your own words, for example:

```
Call me Sam. I've done a little coding. Main points, please. Yes, my MPC is plugged in and on its normal screen.
```

It then checks your MPC's firmware version by itself and tells you what it found.

---

## 2. Get to know your MPC

Switch to **plan mode** (Shift+Tab), then type:

```
Let's get to know my MPC before we build anything. Read only. Study the user guide and the firmware updater in inputs (open the updater like a zip file, never run it), plus whatever you can safely see from the MPC over USB. A community project has already mapped a lot of this: https://github.com/open-mpc. Use it as a map, but check its claims against Akai's files and my device. Show me your plan first.
```

Read the plan. If it looks right, approve it. Your agent unpacks the firmware, studies it, and writes up what it learned.

---

## 3. Your first feature: your logo on the MPC

Pick **A** or **B**. Switch to **plan mode** first.

### A. Your logo
Drop your logo (a PNG or JPG) into your `inputs` folder, then type:

```
I put my logo in inputs. When I start my MPC with my card in, I want my logo on the screen for a few seconds, then the normal MPC starts like always. If I take the card out, it should be completely stock. Write up the spec first so I can approve it.
```

### B. Just text
No image needed. Type:

```
When I start my MPC with my card in, I want it to show "Hello World" on the screen for a few seconds, then the normal MPC starts like always. If I take the card out, it should be completely stock. Write up the spec first so I can approve it.
```

Your agent writes the spec (`features/01-.../scope.md`): what it will do, how, what could go wrong, and how you'll test it. **Read it before you approve.** Then it builds, and it tells you when it needs you at the MPC (for example, to enter SD Card mode so it can copy files to the card).

---

More prompts arrive with each new video.
