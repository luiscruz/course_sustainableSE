---
Authors: Jan-Hendrik Schneider, Daniel Chou Rainho, Filip Gunnarsson
Title: "Comparing Video Codecs on Energy Consumption"
Date: 01/03/2024
---

## 1. Introduction

Video content is everywhere, be it through powering streaming, video conferencing, or social media. At its foundation lies video codecs—technologies that compress and decompress video files for efficient internet transmission.

Traditionally, discussions about video codecs focus on compression efficiency: their ability to minimize file sizes without degrading quality. However, an equally important aspect is their energy efficiency.

The environmental footprint of digital media consumption cannot be overlooked. As the demand for higher quality video content grows, so does the computational load required to encode and decode these videos, leading to increased energy consumption. This research not only contributes to a deeper understanding of codec efficiency but also highlights the importance of choosing the right technology for reducing the carbon footprint of our digital activities.

We investigate the performance of 3 major codecs—`H264/AVC`, `H265/HEVC`, and `AV1` in terms of their energy demands. Our findings aim to guide content creators, streaming services, and eco-conscious individuals in selecting codecs that balance efficiency with environmental impact.

The replication package of the experiments can be found [here](https://github.com/JellyAge/video_codec_power_comparison).

## 2. Background

**What is a Video Codec?**

A video codec, which stands for "compressor-decompressor," is a software or hardware tool designed to compress (encode) and decompress (decode) digital video. The purpose of a codec is to reduce the file size of video data to make storage and transmission more efficient, without significantly compromising the quality of the video. [(Source)](https://corp.kaltura.com/blog/video-codec/)

**What Makes Them Different?**

Video codecs differ in several key aspects, including their compression algorithms, efficiency, compatibility, and licensing requirements. For example, `H.264/AVC` is known for its broad compatibility and balance between compression efficiency and quality. `H.265/HEVC` offers improved compression rates compared to `H.264/AVC`, allowing for higher quality videos at similar file sizes, but it is more computationally intensive. [(Source)](https://corp.kaltura.com/blog/video-codec/)

**Role of Hardware Acceleration**

Hardware acceleration refers to the use of specialized hardware components within a computer or device to perform certain tasks more efficiently than is possible in software running on a general-purpose CPU. For video codecs, hardware acceleration can significantly reduce the processing power required to encode or decode video, thereby reducing energy consumption. The availability and effectiveness of hardware acceleration depends on the codec and the hardware itself. [(Source)](https://universal-blue.org/guide/codecs/)

**What is bitrate?**

Bitrate refers to the amount of data processed over a given period, typically measured in bits per second (bps). In the context of video files, it quantifies the amount of data encoded for each second of video, directly influencing the file's size and quality. A higher bitrate means more data is stored for each second of video, generally resulting in better image and sound quality but also larger file sizes. Conversely, a lower bitrate reduces file size at the cost of quality, potentially leading to pixelation or other artifacts in the video. [(Source)](https://restream.io/blog/what-is-video-bitrate/)

**What are container formats?**

Unlike codecs, which determine how video and audio data are compressed and decompressed, container formats define how this data, along with metadata such as subtitles, chapters, and information about the file itself, is stored and organized within a file. [(Source)](https://www.techsmith.com/blog/video-file-formats/)

## 3. Methodology

### 3.1 Objective of the Study
The primary objective of this study is to compare the energy efficiency of three widely used video codecs: `H.264/AVC`, `H.265/HEVC`, and `AV1`.

Through this comparison, we aim to provide insights into the most sustainable choices for video encoding in various hardware configurations.

The settings were selected to maintain a high decoding load while still delivering consistent quality across all codecs, thereby increasing the impact of decoding compared to background tasks.

Furthermore, we evaluated the effects of hardware acceleration, as our preliminary results indicated that it has a significant impact on the outcomes.


### 3.2 Selection of Codecs
`H.264/AVC` was chosen because it is one of the most widely adapted video codes and is commonly used for various applications.

We also evaluate its successor `H265/HEVC`, which uses more complex compression algorithms, with the main goal of reducing file size without compromising video quality.

Finally, we also evaluate the `AV1` codec, which is the successor of the `VP9` codec and has similar compression performance as `H265/HEVC`, but unlike it has a royalty-free licensing model.

### 3.3 Selection of Video Player

In the context of our study on the energy efficiency of different video codecs, the choice of the video player software is critical. VLC Media Player was selected for several reasons, making it an ideal tool for our experiment. 

VLC is one of the most popular and widely used open-source multimedia players. VLC's ability to support a wide range of codecs, including `H.264/AVC`, `H.265/HEVC`, and `AV1`, without the need for additional codec packs, makes it highly relevant to our study. It allows us to conduct a fair and comprehensive comparison of the energy efficiency of these codecs under conditions that mimic real-world usage scenarios.

Its advanced features, such as hardware acceleration support, further enable us to explore the impact of this technology on video playback energy consumption. By using VLC, we align our experiment with the software that consumers are likely to use in their daily lives, thereby enhancing the practical relevance of our findings to the broader community.

### 3.4 Video Source and Specifications

For our testing framework, we chose the [Big Buck Bunny](http://distribution.bbb3d.renderfarming.net/video/mp4/bbb_sunflower_2160p_60fps_normal.mp4) video, an open-source project by the Blender Foundation. This video is often used for video playback tests due to its open source license and various available resolutions and frame rates.

We specifically selected the highest available resolution of 2160p at 60 fps to amplify the measurable differences between codecs.

Such settings can increase the decoding load, which in turn can lead to higher absolute differences in codecs energy consumption. The source video was originally encoded with a bitrate of 8000 kbits in `H.264/AVC` .

For our purposes, we increased the bitrate to 12,000 kbits to increase the decoding load and to compensate for the potential loss of quality caused by using the medium quality settings for encoding.

A higher quality setting would generally increase the quality of the video without increasing the bitrate, but would significantly increase the encoding time and thus delay our experiments.

For the bitrate of the `AVC` and `HEVC` code, we relied on the following [study](https://doi.org/10.1007/978-3-030-27202-9_14), which concluded that `AV1` and `HEVC` have about 60% lower bitrate at 2160p resolution while delivering similar video quality.
So we set the bitrate for the `AV1` and `H.265/HEVC` variants of the video to 4,800 kbits.

### 3.5 Video Conversion Process

For the conversion of video we used [Handbrake](https://handbrake.fr/), an open source video converter, which supports all tested video codecs. The source video was converted into three separate files, each using a different video codec while maintaining consistent container format, resolution, frame rate, and audio settings.

| Codec | Bitrate | Framerate | Resolution |Encoding Preset| Audio | File Size
|-----------|-----|-----|---------|-------|---------|----|
| H.264/AVC | 12,000 kBit/s | 60 FpS | 3840 x 2160 |medium|160 kBit/s AAC stereo | 87MB
| H.H65/HEVC| 4,800 kBits/s | 60 FpS | 3840 x 2160 |medium|160 kBit/s AAC stereo | 32.7MB
| AV1 | 4,800 kBits/s | 60 FpS | 3840 x 2160 |6|160 kBit/s AAC stereo | 35.7MB


### 3.6 Experiment Setup

System Specifications:

| Component | CPU | RAM | Storage | Operating System |
|-----------|-----|-----|---------|------------------|
| **Specification** | AMD Ryzen 5700U 8-Core, Max Clock Speed 4300 MHz | 16 GB, 3200 MHz | KBG40ZNV1T02 KIOXIA, NVME-SSD, 1 TB | Microsoft Windows 11 Home, 64-bit, Version 23H2 |

In preparation for the energy consumption experiment, we did the following to ensure a controlled environment and reliable results:
- All non-essential applications were closed.
- Non-required hardware peripherals were disconnected.
- Unnecessary services running on the system were terminated.
- The screen brightness was set to maximum.
- A CPU-intensive task, specifically calculating the Fibonacci sequence, was executed for 5 minutes as a warm-up to stabilize the CPU temperature.
- The experiment was conducted in a room with stable temperature.
- WiFi connectivity was disabled to prevent network activity from influencing the measurements.


### 3.7 Measurement Scripts
The `warmup.ps1` script calculates Fibonacci numbers for a duration of 5 minutes, starting with the 15th Fibonacci number.

The `test.ps1` script automates the process of measuring energy consumption for video playback using different codecs, using [EnergyBridge](https://github.com/tdurieux/EnergiBridge) and VLC Media Player. It executes 30 measurements for each of the three video codecs (`AV1`, `H.264`, `H.265`), randomly shuffling the test order to minimize bias. Each video is played in full screen without audio for a duration of 1 minute, with a pause of 1 minute between tests to stabilize the system.


## 4. Results
The experiment conducted shows that the power consumption varies only slightly between the different codecs, but the difference between hardware-accelerated decoding and non-accelerated decoding is quite significant.

First of all, it should be noted that the CPU of the hardware used does not support `AV1` hardware acceleration, so we don't have results for `AV1` with hardware acceleration.

The lowest power consumption was measured with accelerated `H.264/AVC` with an average power consumption of $4.06 W$. The second lowest result with an approximately 6 % higher power consumption was $4.30 W$.

The difference with and without hardware acceleration is generally much higher. Disabling hardware acceleration for `H264/AVC` increases the power consumption by 238% to $13.72 W$, and for `H265/HEVC` by 222% to $13.87 W$.

The difference between the encodings without acceleration is smaller again. `H264/AVC` is again the most efficient in this category, consuming $13.72 W$, followed by `H265/HEVC`, which consumes only 1% more power at $13.87 W$. Finally, `AV1` consumes $14.09 W$, which is 2.6% more than `H264/AVC` without hardware acceleration and 247% more than `H264/AVC` with hardware acceleration.

![compare_all](https://hackmd.io/_uploads/HJXLe5Jap.svg)

![distribution_without_acceleration](https://hackmd.io/_uploads/rkUOl9yT6.svg)

![distribution_hwaccel](https://hackmd.io/_uploads/ByTKx91p6.svg)

### Statistical Tests

Given the above visualisations, it is important to determine whether if the observed differences are statistically significant or could have occurred by chance. This testing will provide us with objective and quantifiable evidence to support or refute the observations from our above visualisations. 

We followed a 4 step procedure to perform these tests:

1. Check the normality of the power consumption data using the Shapiro-Wilk test for each combination of codec and hardware acceleration.
2. If the data is normally distributed, check for equal variances using Levene's test.
3. Depending on the outcomes of these tests, either perform an ANOVA test or a non-parametric Kruskal-Wallis test.
4. If the ANOVA or Kruskal-Wallis test shows significant differences, conduct post hoc tests to identify where those differences lie.

With this said, we get the following as we use the general rule of thumb which is that if the p-value is less than the chosen alpha level (usually $0.05$), then the null hypothesis of normality is rejected, indicating that the data is not normally distributed.

- `AV1` without hardware acceleration: p-value $= 0.0335$, suggesting that the power consumption data for this group is not normally distributed.
- `H264` without hardware acceleration: p-value $= 0.8309$, suggesting that the power consumption data for this group is normally distributed.
- `H264` with hardware acceleration: p-value $= 0.0013$, suggesting that the power consumption data for this group is not normally distributed.
- `H265` without hardware acceleration: p-value $= 0.0004$, suggesting that the power consumption data for this group is not normally distributed.
- `H265` with hardware acceleration: p-value $\approx 0$, suggesting that the power consumption data for this group is not normally distributed.

Given that only `H264` without hardware acceleration suggests it is normally  distributed, we continue on with using non-parametric tests for the statistical analysis. This means we perform the non-parametric Kuskall-Wallis  H-test to determine if there are significant differences in power consumption among the different codec groups and hardware acceleration. 

The Kruskal-Wallis H-test yielded a p-value $\approx 2.21 \times 10^{-27}$, significantly below the alpha of $0.05$. Indicating that there is a significant difference in power consumption between the different codec and hardware acceleration statuses.

Since this test only indicate that there are differences, we want to know where, so we performed a post hoc analysis for the given data. We continue with pairwise Mann-Whitney U tests for this analysis. 


| Comparison                    | P-Value                |
|-------------------------------|------------------------|
| (AV1, False) vs (H264, False) | 2.5263629217472197e-10 |
| (AV1, False) vs (H264, True)  | 3.019859359162157e-11  |
| (AV1, False) vs (H265, False) | 5.092196223484032e-08  |
| (AV1, False) vs (H265, True)  | 3.019859359162157e-11  |
| (H264, False) vs (H264, True) | 6.680905866173482e-11  |
| (H264, False) vs (H265, False)| 0.00027972315726719634 |
| (H264, False) vs (H265, True) | 6.680905866173482e-11  |
| (H264, True) vs (H265, False) | 3.019859359162157e-11  |
| (H264, True) vs (H265, True)  | 6.5182731281236696e-09 |
| (H265, False) vs (H265, True) | 3.019859359162157e-11  |

With each pair of group compared, we found the following interesting:

- `AV1` (without hardware acceleration) compared with all other groups (`H264` and `H265`, with and without hardware acceleration) showed statistically significant differences, with all adjusted p-values being well below the $0.05$ threshold.
- `H264` with hardware acceleration compared with `H265` without hardware acceleration also showed a significant difference.
- `H264` with and without hardware acceleration showed significant differences.
- `H265` with and without hardware acceleration showed significant differences.


## 5. Limitations

**Limited video playback time**

In our experiment, the video was played for only one minute for each setting. Due to the relatively short playback time, the processing overhead of opening and closing the video player could have some impact on power consumption.

**Single video**

The experiment was performed on a single example video (Big Buck Bunny) with a single resolution, bitrate and frame rate. Results may vary depending on the content of the video as well as the resolution, frame rate and bit rate. In general, lower resolution, frame rate or bit rate will result in lower power consumption, regardless of the codec. This would probably reduce the absolute difference in power consumption.

**One hardware configuration**

As our results show, the chosen hardware plays a significant role. The difference in energy consumption with and without hardware acceleration is significantly higher than the difference between different codecs. Therefore, depending on which codecs are natively supported, the energy consumption can vary drastically. And since the experiment was run on a PC without hardware-accelerated `AV1` encoding, we don't have any results on what the power consumption would be for `AV1` with hardware acceleration.

## 6. Conclusion

Our study reveals significant insights on the energy consumption of `H.264/AVC`, `H.265/HEVC`, and `AV1` codecs, especially highlighting the importance of hardware acceleration for energy efficiency. Hardware-accelerated `H.264/AVC` emerged as the most energy-efficient, consuming only $4.06 W$, a stark contrast to its non-accelerated form at $13.72 W$. Similarly, `H.265/HEVC` benefits from acceleration, with power consumption dropping from $13.87 W$ to $4.30 W$. `AV1`, lacking hardware acceleration support in our tests, showed the highest energy use at $14.09 W$. However, the difference between the codecs themselves is relatively small, with changes all in the single-digit percentage range. This means that it is important to select the codec depending on the hardware support of the devices used. However, as long as the codec is supported, switching to a more complex codec such as `H265/HEVC` is probably a good decision, since a small increase in power consumption of a few percent can result in a significant reduction in bitrate of up to 60%. This, in turn, reduces the amount of storage required for data transfer. These findings underscore the significant environmental benefits of choosing the right codec with hardware in mind, which can lead to significant energy savings and a reduced carbon footprint for digital video delivery.

However, our study is limited by its focus on a single system and video sample, indicating a need for broader research. Future work should examine a wider range of hardware and video types to fully understand the implications of codec selection on energy consumption and environmental impact. This study emphasizes the critical role of codec and hardware compatibility in achieving energy-efficient video streaming, a consideration that is increasingly vital in an era of growing digital video consumption.
