import subprocess
import re
import argparse
import os
import json

# Function to parse the duration argument
def parse_duration(duration_str):
    if duration_str is None:
        return None
    
    if type(duration_str) is not str:
        return duration_str
    
    if ':' in duration_str:
        parts = duration_str.split(':')
        parts = [int(part) for part in parts if part.isdigit()]
        if len(parts) == 3:
            hours, minutes, seconds = parts
            total_seconds = hours * 3600 + minutes * 60 + seconds
        elif len(parts) == 2:
            minutes, seconds = parts
            total_seconds = minutes * 60 + seconds
        elif len(parts) == 1:
            total_seconds = int(parts[0])
        else:
            raise ValueError("Invalid duration format. Please use 'HH:MM:SS', 'MM:SS', or 'SS'.")
    else:
        pattern = r'((?P<hours>\d+)h)?((?P<minutes>\d+)m)?((?P<seconds>\d+)s)?'
        match = re.match(pattern, duration_str)
        if not match:
            raise ValueError("Invalid duration format. Please use the format 'XXhXXmXXs'.")
        hours = match.group('hours')
        minutes = match.group('minutes')
        seconds = match.group('seconds')
        total_seconds = 0
        if hours:
            total_seconds += int(hours) * 3600
        if minutes:
            total_seconds += int(minutes) * 60
        if seconds:
            total_seconds += int(seconds)
    return total_seconds

def parse_intervals(intervals_str):
    # This function will try to correct the format if it's not a proper JSON
    try:
        # Try to directly load the JSON
        intervals = json.loads(intervals_str)
    except json.JSONDecodeError:
        # If it fails, try to fix missing quotes and handle MM:SS format
        # Match MM:SS and HH:MM:SS formats, and wrap them in quotes
        fixed_str = re.sub(r'(?<!:)(\b\d{1,2}:\d{2}\b)(?!:)', r'"\1"', intervals_str)
        fixed_str = re.sub(r'(\b\d{1,2}:\d{2}:\d{2}\b)', r'"\1"', fixed_str)
        intervals = json.loads(fixed_str)
    return intervals

# Function to change video playback speed
def change_playback_speed(input_path, output_path, target_duration_seconds, overwrite=False):
    # Calculate the video speed change
    result = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 
                             'format=duration', '-of', 
                             'default=noprint_wrappers=1:nokey=1', input_path],
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    original_duration = float(result.stdout)
    speed_factor = original_duration / target_duration_seconds
    setpts_value = f"PTS/{speed_factor}" if speed_factor >= 1.0 else f"{1/speed_factor}*PTS"

    # Construct the ffmpeg command
    cmd = ['ffmpeg', '-i', input_path]
    if overwrite:
        cmd.append('-y')
    cmd.extend(['-filter_complex', f"[0:v]setpts={setpts_value}[outv];[0:a]atempo={speed_factor}[outa]", '-map', '[outv]', '-map', '[outa]'])
    cmd.append(output_path)

    # Execute the ffmpeg command
    subprocess.run(cmd, check=True)

def invert_intervals(cut_intervals, total_duration):
    # Assuming cut_intervals is a list of tuples like [(start1, end1), (start2, end2), ...]
    # and that it's sorted by start times
    inverted_intervals = []
    previous_end = 0
    for start, end in cut_intervals:
        if previous_end < start:
            inverted_intervals.append((previous_end, start))
        previous_end = end
    if previous_end < total_duration:
        inverted_intervals.append((previous_end, total_duration))
    return inverted_intervals

def cut_video_sections(input_path, output_path, cut_intervals, overwrite=False):
    # Get the total duration of the video
    result = subprocess.run(['ffprobe', '-v', 'error', '-show_entries',
                             'format=duration', '-of',
                             'default=noprint_wrappers=1:nokey=1', input_path],
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    total_duration = float(result.stdout)

    # Parse the cut intervals to get start and end times in seconds
    # Parse the string intervals to seconds and sort them
    cut_intervals_seconds = [(parse_duration(start), parse_duration(end)) for start, end in cut_intervals]
    cut_intervals_sorted = sorted(cut_intervals_seconds, key=lambda x: x[0])

    # Invert intervals to get the parts we want to keep
    keep_intervals = invert_intervals(cut_intervals_sorted, total_duration)

    filter_complex = ''
    stream_specifiers = []
    # Loop over each keep interval and construct the filter_complex command
    for i, (start, end) in enumerate(keep_intervals):
        filter_complex += (
            f"[0:v]trim=start={start}:end={end},setpts=PTS-STARTPTS[v{i}];"
            f"[0:a]atrim=start={start}:end={end},asetpts=PTS-STARTPTS[a{i}];"
        )
        stream_specifiers.extend([f"[v{i}]", f"[a{i}]"])

    # Concatenate the video and audio pairs
    filter_complex += f"{''.join(stream_specifiers)}concat=n={len(keep_intervals)}:v=1:a=1[outv][outa]"

    cmd = ['ffmpeg', '-i', input_path]
    if overwrite:
        cmd.append('-y')
    cmd.extend(['-filter_complex', filter_complex, '-map', '[outv]', '-map', '[outa]'])
    cmd.append(output_path)

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print("FFmpeg command failed.")
        print(f"Return code: {e.returncode}")
        print(f"Output: {e.output.decode('utf-8')}")
        raise

def remove_silence(input_path, output_path, silence_threshold='-30dB', min_silence_duration=1, overwrite=False):
    cmd = [
        'ffmpeg', '-i', input_path, '-af',
        f'silencedetect=noise={silence_threshold}:d={min_silence_duration}', '-f', 'null', '-'
    ]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    silence_periods = re.findall(r'silence_start: (\d+\.\d+)|silence_end: (\d+\.\d+)', result.stderr)
    cut_intervals = []
    start_time = None  # Initialize start_time

    for start, end in silence_periods:
        if start:
            start_time = float(start)
        if end and start_time is not None:  # Ensure start_time is set before using it
            end_time = float(end)
            if end_time - start_time > min_silence_duration:
                # Adjust the start and end times
                adjusted_start = start_time + min_silence_duration / 2
                adjusted_end = end_time - min_silence_duration / 2
                cut_intervals.append((adjusted_start, adjusted_end))
            start_time = None  # Reset start_time for the next interval

    if cut_intervals:
        cut_video_sections(input_path, output_path, cut_intervals, overwrite)
    else:
        print("No silence detected or the silence duration is less than the minimum threshold.")



# Main function to process the command-line arguments
def main():
    parser = argparse.ArgumentParser(description='Process a video file by changing playback speed, cutting sections, or removing silence.')
    parser.add_argument('input', type=str, help='Input video file path')
    parser.add_argument('--output', type=str, default=None,
                        help='Output video file path. If not provided, a name is generated automatically.')
    parser.add_argument('--duration', type=str, default=None,
                        help='Target duration (format: XXhXXmXXs or HH:MM:SS).')
    parser.add_argument('--cut_intervals', type=str, default=None,
                        help='JSON string of time intervals to cut. Format: [[HH:MM:SS, HH:MM:SS], ...]')
    parser.add_argument('--remove_silence', action='store_true',
                        help='Remove silence from the video.')
    parser.add_argument('--min_silence_duration', type=float, default=1,
                        help='Minimum duration of silence to be removed (in seconds).')
    parser.add_argument('--overwrite', action='store_true',
                        help='Overwrite the output file.')

    args = parser.parse_args()

    if args.output:
        output_path = args.output
    else:
        file_root, file_ext = os.path.splitext(args.input)
        version_match = re.search(r'(_adjusted\d*)$', file_root)
        if version_match:
            version_str = version_match.group(0)
            version_num = int(version_str[len('_adjusted'):]) if version_str[len('_adjusted'):] else 0
            new_version_num = version_num + 1
            new_file_root = file_root[:file_root.find(version_str)] + f'_adjusted{new_version_num}'
        else:
            new_file_root = f"{file_root}_adjusted1"
        output_path = f"{new_file_root}{file_ext}"

    if args.remove_silence:
        remove_silence(args.input, output_path, min_silence_duration=args.min_silence_duration, overwrite=args.overwrite)
    elif args.cut_intervals:
        cut_intervals = parse_intervals(args.cut_intervals)
        cut_video_sections(args.input, output_path, cut_intervals, args.overwrite)
    elif args.duration:
        target_duration_seconds = parse_duration(args.duration)
        change_playback_speed(args.input, output_path, target_duration_seconds, args.overwrite)

if __name__ == '__main__':
    main()