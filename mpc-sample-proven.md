# What StemBred's agent has proven on the MPC Sample

> **Learner:** put this file in your `inputs` folder. It's what our agent learned the hard way, so yours doesn't start from zero.
> **Agent:** every item here is **reported by StemBred**: proven on StemBred's own MPC Sample on firmware **1.3.0.12**. Treat it as a strong lead, not as proof on *this* learner's device. Label it "reported" until it works here, then upgrade it to "proven on the device".

## Running code from the SD card (autorun)
1. The **MPC app itself** (not Linux startup) reads an `autorun` folder at the root of the SD card when it starts, and runs the script listed in `autorun/autorun.json` with `sh`, as root.
2. `autorun.json` format (one script, no files):
   ```json
   {"value0": {"scripts": [{"path": "autorun.sh", "askQuestion": false,
     "message": "", "yesButtonText": "Yes", "noButtonText": "No"}], "files": []}}
   ```
3. **Use `"askQuestion": false`.** With `true`, startup can hang at a 0.0% loading bar or a black screen.
4. `autorun/autorun.check` must hold the lowercase hex **SHA-256** of: the bytes of `autorun.json` + the bytes of `autorun.sh` + the text `f7bed1c9-7e90-4731-9194-c996666b4331`, with no newline at the end. Method published by the community (`tools/check_autorun.py` in https://github.com/orrpunk-art/mpc-sample-root-ssh; that repo has no licence, so write your own code and credit the method). Any edit to the JSON or the script means a new check file.
5. Save `autorun.sh` with **LF** line endings (not Windows CRLF).
6. **Run once per boot.** The card is re-read when SD Card Access mode ends, which runs the script again. Use a marker file in `/run` (cleared at every reboot) and exit if it exists.

## Drawing on the screen
7. The screen is **320 × 240**, 32 bits per pixel, at `/dev/fb0`. A full frame is 320 × 240 × 4 = 307,200 bytes, with no padding.
8. The pixel order is **B, G, R, X** (blue first). Swap red and blue when you convert an image, or gold shows up cyan.
9. The working sequence in `autorun.sh`:
   - set a `trap` that **always** runs `systemctl start ac50.service` on exit, so the MPC app comes back even if something fails
   - `systemctl stop ac50.service` (the MPC app stops drawing)
   - **wake the screen:** `echo 1 > /sys/class/graphics/fb0/blank; echo 0 > /sys/class/graphics/fb0/blank`. Without this, the screen stays black.
   - `cat logo.raw > /dev/fb0`
   - `sleep 3`, then exit (the trap restarts the app)
10. `az0x-splashctl` exists in the firmware, but it failed from autorun on 1.3.0.12 (exit 1 for every image format). Its service is probably gone by then. Use `/dev/fb0` instead.

## Working with the card efficiently
11. Every card round trip costs the learner several button presses and a reboot. **Learn as much as you can per trip:** batch your on-device checks into one script, and have it write a log to the card.
12. Card out, power on = completely stock. Our changes live only on the card.
