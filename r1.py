# PRACTICAL 1 - Raspberry Pi Hardware Preparation and Installation
# File: practical_1_raspberry_pi_installation_steps.py

# =========================
# HARDWARE REQUIRED
# =========================
# 1. Raspberry Pi 3 Model B
# 2. MicroSD card (16GB or above)
# 3. SD card reader
# 4. 5V Micro USB power adapter
# 5. HDMI cable + monitor
# 6. USB keyboard and mouse
# 7. Internet connection (Wi-Fi / Ethernet)

# =========================
# INSTALLATION STEPS
# =========================
# Step 1: Download Raspberry Pi Imager on your PC
# Step 2: Insert MicroSD card into card reader
# Step 3: Open Raspberry Pi Imager
# Step 4: Select Raspberry Pi OS
# Step 5: Select the SD card
# Step 6: Click WRITE to flash the OS
# Step 7: Insert SD card into Raspberry Pi
# Step 8: Connect HDMI, keyboard, mouse, and power supply
# Step 9: Boot Raspberry Pi and complete setup

# =========================
# STATIC IP CONFIGURATION
# =========================
# Open terminal and run:
# sudo nano /etc/dhcpcd.conf
# Add:
# interface eth0
# static ip_address=192.168.2.20/24
# static routers=192.168.2.1
# static domain_name_servers=8.8.8.8
# Save and reboot Raspberry Pi

# =========================
# REMOTE ACCESS SETTINGS
# =========================
# Enable VNC:
# Menu -> Preferences -> Raspberry Pi Configuration -> Interfaces -> Enable VNC
# Install VNC Viewer on laptop and connect using Pi IP

# Enable SSH:
# Menu -> Preferences -> Raspberry Pi Configuration -> Interfaces -> Enable SSH
# Connect using:
# ssh pi@192.168.2.20

# Practical 1 completed