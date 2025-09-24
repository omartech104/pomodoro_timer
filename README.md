# Pomodoro Timer ⏲️

A simple Python-based **Pomodoro Timer** for Linux users.  
It helps you stay productive by following the **Pomodoro Technique**:  
- **25 minutes** of focused work  
- **5 minutes** of short break  
- After 4 cycles, take a **15–30 minute long break**  

---

## Features
- Runs in the **terminal**  
- Sends Linux **desktop notifications** (`notify-send`)  
- Customizable work and break durations  
- Lightweight and dependency-free (except `notify-send`)  

---

## Requirements
- Python 3.7+  
- Linux system with `notify-send` available (usually part of `libnotify-bin`)  

Install `notify-send` if missing:  
```bash
sudo apt install libnotify-bin   # Debian/Ubuntu
sudo dnf install libnotify       # Fedora
sudo pacman -S libnotify         # Arch

