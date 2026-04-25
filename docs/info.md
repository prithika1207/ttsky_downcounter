<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

# Down Counter (TinyTapeout Project)

## 🧠 What it does
This project is an 8-bit down counter.  
It decreases its value by 1 on every clock cycle when enabled.

When the counter reaches 0, it wraps around to 255 and continues counting down.

---

## ⚙️ Inputs

- **clk** → Clock signal (drives counting)
- **rst_n** → Active-low reset (sets counter to 0)
- **ena** → Enable signal (1 = count, 0 = hold)
- **ui_in / uio_in** → Not used in this design

---

## 📤 Outputs

- **uo_out[7:0]** → Current counter value (8-bit output)
- **uio_out / uio_oe** → Not used

---

## 🔄 Working

On every rising clock edge:
- If reset = 0 → counter = 0
- If enable = 1 → counter = counter - 1

---

## 📊 Example behavior


## How to test


---

## 🧪 Testing

The design is tested using cocotb:
- Clock is generated in the testbench
- Output is checked each cycle
- Verifies correct decrement and wrap-around

---

## 📌 Summary

A simple 8-bit digital down counter suitable for learning basic sequential logic and TinyTapeout design flow.
## External hardware

No exteral hardware
