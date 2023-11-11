# VideoClipper

VideoClipper is a command-line utility for video editing, including adjusting playback speed and cutting specific sections from videos. It utilizes FFmpeg to provide a robust set of features that are accessible via a simple command-line interface.

## Features

- **Adjust Playback Speed**: Modify the speed of your video to reach a desired duration.
- **Cut Specific Sections**: Remove unwanted parts from your video by specifying start and end times.

## Prerequisites

- FFmpeg must be installed on your system.
- Python 3.6 or higher.

## Installation

To install VideoClipper, run the following command:

```bash
pip install videoclipper
```

## Usage

Here's a quick example of how to use VideoClipper:

```bash
videocliper input_video.mp4 --cut_intervals "[[00:01:00, 00:02:00], [00:03:30, 00:04:30]]"
videocliper input_video.mp4 --duration "1h20m30s"
```

Parameters:
- `input`: Path to the input video file.
- `--duration`: Target duration (format: XXhXXmXXs or HH:MM:SS). Omit to maintain original duration.
- `--cut_intervals`: JSON string of time intervals to cut (format: [[HH:MM:SS, HH:MM:SS], ...]).
- `--overwrite`: Flag to allow overwriting of the output file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [FFmpeg](https://ffmpeg.org/) for providing the underlying video processing capabilities.

Project Repository: [https://github.com/fuzihaofzh/videoclipper](https://github.com/fuzihaofzh/videoclipper)
