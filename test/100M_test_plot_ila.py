import csv
import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fin_str = sys.argv[1]
# fin_str = "/home/fxzjshm/Documents/pulsar/rfsoc/GRALIC_4t4r/rf_test/iladata.csv"
print("Reading file ", fin_str)

df = pd.read_csv(fin_str, skiprows=[1])

channel_data = {}

target_cols = [col for col in df.columns if "data_sync" in col]

if not target_cols:
    print("The column 'data_sync' was not found in the CSV file")
    sys.exit(1)

for col_name in target_cols:
    clean_name = col_name.split('[')[0]
    channel_vals = df[col_name].values
    channel_data[clean_name] = channel_vals

num_channels = len(channel_data)
fig, axes = plt.subplots(num_channels, 2, figsize=(16, 4 * num_channels))
fig.suptitle(f"Channel Data Analysis - 10MHz Signal(-3dBa) | 100M Sampling | UNSIGNED 8bit - {fin_str}", fontsize=14, fontweight='bold')

for i, (ch_name, data) in enumerate(channel_data.items()):
    ax_time = axes[i][0]
    ax_freq = axes[i][1]

    ax_time.plot(data, color='#1f77b4', linestyle='-', linewidth=1.2, label=ch_name)
    ax_time.set_title(f"{ch_name} - Time Domain", fontsize=12, fontweight='bold')
    ax_time.set_xlabel("Sample Index", fontsize=10)
    ax_time.set_ylabel("UNSIGNED Value (0-255)", fontsize=10)
    ax_time.set_ylim(0, 255)
    ax_time.grid(True, alpha=0.3)
    ax_time.legend(loc='upper right')

    fft_result = np.fft.rfft(data)
    fft_result[0] = 0

    sample_rate_Hz = 100 * 10 ** 6
    freqs_Hz = np.fft.rfftfreq(len(data), d=1 / sample_rate_Hz)
    freqs_MHz = freqs_Hz / 10 ** 6

    intensity = np.abs(fft_result) ** 2
    intensity_dB = 10 * np.log10(intensity + 1e-6)

    ax_freq.plot(freqs_MHz, intensity_dB, color='#ff7f0e', linestyle='-', linewidth=1.2)
    ax_freq.axvline(x=10, color='#d62728', linestyle='--', linewidth=1.5, label='10MHz Signal')
    ax_freq.set_title(f"{ch_name} - Frequency Spectrum (max={np.max(intensity_dB):.2f}dB)", fontsize=12)
    ax_freq.set_xlabel(f"Frequency (MHz) | 100M Sampling | Nyquist: 50MHz", fontsize=10)
    ax_freq.set_ylabel("Intensity (dB)", fontsize=10)
    ax_freq.set_xlim(0, 50)
    ax_freq.grid(True, alpha=0.3)
    ax_freq.legend(loc='upper right')

plt.tight_layout()
save_path = fin_str.replace('.csv', '_analysis.png')
plt.savefig(save_path, dpi=300, bbox_inches='tight')
plt.show()

print(f"The image has been saved to: {save_path}")
print(f"Number of channels: {num_channels} | Total number of data samples: {len(df)}")