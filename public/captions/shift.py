#!/usr/bin/python3

import sys
import re
from datetime import timedelta, datetime

def parse_timecode(time_str):
    # Handles negative time shifts
    negative = time_str.startswith('-')
    if negative:
        time_str = time_str[1:]  # Remove the negative sign for parsing

    # Parse time format "HH:MM:SS:FF"
    parts = time_str.split(':')
    if len(parts) != 4:
        raise ValueError("Time shift must be in the format HH:MM:SS:FF")
    hours, minutes, seconds, frames = map(int, parts)

    # Assuming 30 fps for frame calculation
    fps = 30
    total_seconds = hours * 3600 + minutes * 60 + seconds + frames / fps

    # Apply negative sign if necessary
    if negative:
        total_seconds = -total_seconds

    return timedelta(seconds=total_seconds)

def format_time(time_obj):
    # Format time to "HH:MM:SS.mmm"
    return time_obj.strftime("%H:%M:%S.") + f"{time_obj.microsecond // 1000:03d}"

def shift_time(line, delta):
    # Regex to find time patterns in VTT format "HH:MM:SS.mmm"
    time_pattern = r'(\d{2}:\d{2}:\d{2}\.\d{3})'
    times = re.findall(time_pattern, line)
    if times:
        # Shift both start and end times in the cue
        shifted_times = [format_time(datetime.strptime(t, "%H:%M:%S.%f") + delta) for t in times]
        return re.sub(time_pattern, lambda m: shifted_times.pop(0), line)
    return line

def adjust_vtt_timing(file_path, output_path, time_shift_str):
    # Calculate the timedelta from the custom time format
    delta = parse_timecode(time_shift_str)
    
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
  
    with open(output_path, 'w', encoding='utf-8') as file:
        for line in lines:
            new_line = shift_time(line, delta)
            file.write(new_line)

if __name__ == "__main__":
    # Command-line usage: python script.py input.vtt output.vtt "00:05:36:24"
    if len(sys.argv) != 4:
        print("Usage: python script.py <input_file> <output_file> <time_shift_in_HH:MM:SS:FF>")
        sys.exit(1)

    input_file, output_file, time_shift_str = sys.argv[1], sys.argv[2], sys.argv[3]
    adjust_vtt_timing(input_file, output_file, time_shift_str)

