import sys
from time import sleep
import time

def print_list():
    lines = [
        # delay same the song name MEYOU - วันนี้ปีที่แล้ว [OFFICIAL MV]

        ("ในวันนี้เมื่อปีที่แล้ว", 0.14),
        ("คือวันที่เรานั้นเลิกกัน", 0.1),
        ("ตอนนั้นฉันคิดว่ามันคงดีถ้าไม่มีเธอ", 0.16),
        ("แต่วันนี้ไม่มีอีกแล้ว", 0.15),
        ("และต่อให้ฉันขอร้อง เท่าไร", 0.15),
        ("เธอคงไม่กลับมาหา", 0.155),
        ("คนที่ไล่ให้เธอไป", 0.15),
    ]

# 30s

    delay = [0.6, 0.6, 0.9, 0.7, 0.8, 1, 0.4]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delay[i])
        print()

print_list()