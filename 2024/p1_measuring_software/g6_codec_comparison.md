## Video Preparation Process for Codec Comparison

The experiment aims to compare the energy efficiency of playing videos encoded with H.264, H.265 (HEVC), and AV1 codecs. The source video used for this purpose was obtained from the official Blender website:

- **Source Video**: [Big Buck Bunny](https://download.blender.org/peach/bigbuckbunny_movies/big_buck_bunny_720p_h264.mov)
- **Video Specifications**: 720p resolution, .MOV container, encoded in H.264 codec.

### Video Conversion Process

Using FFmpeg, the source video was converted into three separate files, each using a different video codec while maintaining consistent container format, resolution, frame rate, and audio settings.

1. **H.264 Encoding**

    ```bash
    ffmpeg -i input.mov -c:v libx264 -preset medium -crf 23 -c:a aac -b:a 128k output_h264.mp4
    ```

2. **H.265 (HEVC) Encoding**

    ```bash
    ffmpeg -i input.mov -c:v libx265 -preset medium -crf 28 -c:a aac -b:a 128k output_h265.mp4
    ```

3. **AV1 Encoding**

    ```bash
    ffmpeg -i input.mov -c:v libaom-av1 -crf 30 -b:v 0 -cpu-used 4 -c:a aac -b:a 128k output_av1.mp4
    ```

In preparation for the energy consumption experiment, we did the following to ensure a controlled environment and reliable results:
- All non-essential applications were closed.
- Non-required hardware peripherals were disconnected.
- Unnecessary services running on the system were terminated.
- The screen brightness was set to maximum.
- A CPU-intensive task, specifically calculating the Fibonacci sequence, was executed for 5 minutes as a warm-up to stabilize the CPU temperature.
- The experiment was conducted in a room with stable temperature.
- WiFi connectivity was disabled to prevent network activity from influencing the measurements.

The `warmup.ps1` script calculates Fibonacci numbers for a duration of 5 minutes, starting with the 15th Fibonacci number.

The `test.ps1` script automates the process of measuring energy consumption for video playback using different codecs, using EnergyBridge and VLC Media Player. It executes 30 measurements for each of the three video codecs (AV1, H.264, H.265), randomly shuffling the test order to minimize bias. Each video is played in full screen without audio for a duration of 1 minute, with a pause of 1 minute between tests to stabilize the system.
## System Specifications

### CPU
- **Model**: AMD Ryzen 9 3900X 12-Core Processor
- **Manufacturer**: AuthenticAMD
- **Cores**: 12
- **Max Clock Speed**: 3800 MHz

### GPU
- **Model**: NVIDIA GeForce RTX 3060 Ti
- **Adapter RAM**: 4293918720 bytes (Approx. 4.29 GB)
- **Driver Version**: 31.0.15.4633

### RAM
- **Total Capacity**: 34359738368 bytes (Approx. 32 GB across 4 sticks)
- **Speed**: 2133 MHz

### Storage
- **Model**: Samsung SSD 980 500GB
- **Type**: Fixed hard disk media
- **Capacity**: 500105249280 bytes (Approx. 500 GB)

### Operating System
- **OS**: Microsoft Windows 10 Home
- **Architecture**: 64-bit
- **Version**: 10.0.19045
