# ZTR

<div align="center">

# 🍎 Bad Apple!! in CMD (ASCII Player)

An ultra-smooth, lightweight terminal-based ASCII video renderer built with Python and OpenCV.

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20CMD%20%7C%20Terminal-lightgrey.svg?style=for-the-badge&logo=windows-terminal&logoColor=white)](#)

<br/>

```text
       .---.
      /     \
     | () () |     "Ever on and on, I continue circling..."
      \  _  /
       '---'
```

</div>

---

## 📖 เกี่ยวกับโปรเจกต์ (Overview)

โปรแกรมแสดงผลแอนิเมชันระดับตำนาน **"Bad Apple!!"** บน **Windows Command Prompt (CMD)** หรือ Terminal ใดๆ ด้วยอักขระ ASCII Art แบบเรียลไทม์ 

### ✨ จุดเด่น (Features)
- 🚀 **Flicker-Free Rendering:** ใช้วิธี Reposition Cursor ด้วย ANSI escape code (`\033[H`) แทนการล้างหน้าจอด้วย `cls` ทำให้ภาพไม่กระพริบ
- 📐 **Auto Resizing:** ปรับขนาดภาพตามความกว้างและความสูงของหน้าจอ CMD อัตโนมัติ
- ⏱️ **Frame Timing Lock:** รักษา FPS ให้อิงตามวิดีโอต้นฉบับ ลื่นไหล ไม่เร่งสปีดเกินจริง
- 🔤 **Monochrome Contrast Palette:** เลือกชุดตัวอักษร ASCII ที่เกลี่ยน้ำหนักขาว-ดำ ได้คมชัดเป็นพิเศษสำหรับภาพเงา (Shadow Silhouette) ของ Bad Apple

---

## 🛠️ ความต้องการของระบบ (Prerequisites)

- **Python 3.8+**
- **pip** (Python package manager)
- วิดีโอไฟล์ `bad_apple.mp4`

---

## ⚡ เริ่มต้นใช้งาน (Quick Start)

### 1. โคลนหรือดาวน์โหลดโปรเจกต์
```cmd
git clone https://github.com/your-username/bad-apple-cmd.git
cd bad-apple-cmd
```

### 2. ติดตั้ง Dependencies
```cmd
pip install -r requirements.txt
```
*(หรือติดตั้งตรงๆ ผ่านคำสั่ง: `pip install opencv-python`)*

### 3. เตรียมไฟล์วิดีโอ
ดาวน์โหลดคลิป Bad Apple แล้วตั้งชื่อว่า `bad_apple.mp4` วางไว้ในโฟลเดอร์เดียวกันกับสคริปต์

### 4. รันโปรแกรม!
```cmd
python bad_apple.py
```

> **เคล็ดลับสำหรับภาพที่คมชัดที่สุดบน CMD:**
> - กดปุ่ม `F11` หรือขยายหน้าต่าง CMD ให้เต็มจอ (Maximize)
> - คลิกขวาแถบ Title bar ของ CMD -> เลือก **Properties** -> ไปที่แท็บ **Font**
> - เปลี่ยนฟอนต์เป็น **Consolas** หรือ **Lucida Console** และปรับขนาดลงเหลือประมาณ **8 - 10 pt**

---

## 📂 โครงสร้างโฟลเดอร์ (Project Structure)

```text
bad-apple-cmd/
├── bad_apple.py         # สคริปต์หลักสำหรับประมวลผลและเรนเดอร์ ASCII
├── bad_apple.mp4        # ไฟล์วิดีโอ (นำมาวางไว้ที่นี่)
├── requirements.txt     # ไลบรารีที่จำเป็น
└── README.md            # คู่มือการใช้งาน
```

---

## ⚙️ พารามิเตอร์และการปรับแต่ง (Customization)

### การเลือกไฟล์วิดีโออื่น
คุณสามารถรันไฟล์วิดีโออื่นหรือระบุ path ที่ต้องการได้โดยส่งเป็น argument:
```cmd
python bad_apple.py "C:\path\to\custom_video.mp4"
```

### ปรับชุดอักษร ASCII Palette
สามารถแก้ไขความละเอียดของระดับแสง (Grayscale) ได้ใน `bad_apple.py`:
```python
# ความคมชัดสูง (ไล่เฉด 10 ระดับ)
ASCII_CHARS = "  ..::--==++**##%%@@"

# แบบคมจัด ขาว-ดำ ล้วน (เน้น Silhouette)
ASCII_CHARS = "  @@"
```

---

## ⌨️ ปุ่มควบคุม (Controls)

| ปุ่ม | การทำงาน |
| :---: | :--- |
| `Ctrl + C` | ออกจากโปรแกรมและคืนค่า Cursor ตามปกติ |

---

## 📜 ลิขสิทธิ์ (License)

โปรเจกต์นี้เผยแพร่ภายใต้ลิขสิทธิ์ [MIT License](LICENSE) — สามารถนำไปพัฒนาต่อ ปรับแต่ง หรือศึกษาได้อย่างอิสระ!
