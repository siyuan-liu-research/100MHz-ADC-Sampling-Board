# 100MHz-ADC-Sampling-Board

100MHz High-Speed ADC Sampling Board (Including 3.3V-1.8V Voltage Conversion Board) | Hardware Design + FPGA Firmware Development + Open-Source Performance Test Script | 2025 Undergraduate Innovation Practice Training Program Project, National Astronomical Observatories, Chinese Academy of Sciences

## Project Overview

This project is a **100MSps, 8-bit, dual-channel** high-speed ADC sampling system, consisting of a core ADC sampling board and a supporting 3.3V-1.8V voltage conversion board. It is designed specifically for high-speed analog signal digital acquisition and is ultimately connected to the AXKU041 FPGA development board for signal acquisition and processing.

The system completes the conversion and level adaptation from analog to digital signals through a standard signal link. The hardware design is completed based on JLC EDA, and the FPGA firmware is developed based on Vivado 2024.2. All hardware design files (schematic diagrams, PCBs, BOMs), FPGA firmware code, and performance test scripts are fully open-sourced for academic research and non-commercial educational purposes only.

## Physical Display

## Project Background

This project is an approved project of the **2025 Undergraduate Innovation Practice Training Program of the National Astronomical Observatories, Chinese Academy of Sciences**, and is developed relying on the Pulsar and Gravitational Physics Research Group - BAO of the National Astronomical Observatories.

### Funding Source

The project R&D funding is jointly provided by **Shenzhen JLC Technology Group Co., Ltd.** and the **Pulsar and Gravitational Physics Research Group (BAO) of the National Astronomical Observatories, Chinese Academy of Sciences**.

## Hardware Design

All hardware design files are stored in the `hardware/` directory, which is divided into two subdirectories to manage the design files of the ADC sampling board and the voltage conversion board. All are drawn with **JLC EDA**, including complete schematic diagrams, PCB layouts, and Bill of Materials (BOM):

### 1. Core ADC Sampling Board (`hardware/ADC_Sampling_Board/`)

#### Signal Acquisition Link (SMA Input → FMC Output)

`SMA signal source termination` → Signal buffering/conditioning (AD8065ARZ) → Single-ended to differential conversion (AD8132ARZ, ADC front-end adaptation) → ADC analog-to-digital conversion (AD9288BSTZ-100, 100MSps+8bit + dual-channel) → FMC interface digital signal output (3.3V level)

#### Core Components

- Signal conditioning op-amp: AD8065ARZ
- Single-ended to differential chip: AD8132ARZ
- Analog-to-digital conversion chip: AD9288BSTZ-100 (100MSps, 8bit, dual-channel)

### 2. Voltage Conversion Board (`hardware/Voltage_Conversion_Board/`)

#### Core Function

Realizes **3.3V→1.8V** digital signal level conversion to complete the level matching between the ADC sampling board and the AXKU041 FPGA development board. The inter-board connection is realized through the FMC interface throughout.

#### Core Components

- Level conversion chip: SN74LVC8T245

### 3. Inter-Board/HHardware Connection Relationship

ADC Sampling Board ↔ Voltage Conversion Board (FMC interface) ↔ AXKU041 FPGA Development Board (FMC interface), forming a complete high-speed signal acquisition link.

## Firmware Development

Firmware code and programming files are stored in the `firmware/` directory, which is the FPGA acquisition firmware adapted for AXKU041. It is developed entirely based on **Xilinx Vivado 2024.2**, including Vivado project source code, project configuration files, and directly programmable bitstream files.

## Quick Start

### 1. Hardware Connection

Complete the hardware assembly in the following order, all connected directly through the FMC interface:

`10MHz analog signal source` → Connect to the SMA input port of the ADC sampling board → ADC sampling board FMC port ↔ Voltage conversion board FMC port → Another FMC port of the voltage conversion board ↔ AXKU041 FPGA development board FMC port

### 2. Firmware Programming

Open Xilinx Vivado 2024.2 and program the bitstream file in the `firmware/` directory into the AXKU041 FPGA development board through the software.

### 3. Signal Acquisition and Data Capture

Power on all hardware. After the programming is completed, the AXKU041 FPGA will automatically start signal acquisition and complete the digital conversion of the 10MHz analog signal. Then capture the acquired data through Vivado, the steps are as follows:

Open the ILA (Integrated Logic Analyzer) debugging interface of Vivado 2024.2, trigger the acquisition of the digital signal data after ADC sampling, and export the captured data to a **CSV format file**.

### 4. Circuit Board Performance Testing and Phenomenon Viewing

This project provides a Python automated analysis script (stored in the `test/` directory). The script can automatically parse the CSV data exported by ILA, complete the conversion from hexadecimal data to int16 format, and visually present the test phenomena through **time-domain waveforms + frequency-domain spectrograms** to intuitively verify the validity of the sampled signal. The specific operation steps are as follows:

1. Put the CSV format sampling data file exported from the Vivado ILA interface into the `test/` directory of the repository;
2. Open the terminal/command line, enter the `test/` directory, and execute the Python script running command (the CSV file name needs to be passed as a parameter). The command format:
```
python script_file_name.py sampling_data.csv
```
3. After the script runs, it will automatically complete data parsing, **draw and pop up the time-domain waveform diagram and normalized frequency-domain spectrogram of each channel in real time**, and generate a PNG format visualization result file with the same name in the `test/` directory (CSV file name + .png). The integrity of the sampled signal can be intuitively analyzed through the waveform/spectrum to complete the circuit board performance verification.

## Repository Directory Structure

```
100MHz High-Speed ADC Sampling Board/
├── images/          # Project images: hardware physical drawings, test-related drawings, etc.
├── hardware/        # Hardware design main directory
│   ├── ADC_Sampling_Board/  # ADC sampling board: schematic diagrams, PCBs, BOMs
│   └── Voltage_Conversion_Board/ # Voltage conversion board: schematic diagrams, PCBs, BOMs
├── firmware/        # FPGA firmware: source code, Vivado project files, programmable bitstream files
├── test/            # Performance testing: Python analysis scripts
├── LICENSE          # Open-source license (MIT + academic use restrictions)
└── README.md        # Project description document (this document)
```

## Contact Information

If you have any questions, suggestions or want to communicate in depth about the project, please contact me via email:
siyuan.liu.research@outlook.com

## Acknowledgments

1. 2025 Undergraduate Innovation Practice Training Program, National Astronomical Observatories, Chinese Academy of Sciences
2. Pulsar and Gravitational Physics Research Group - BAO, National Astronomical Observatories, Chinese Academy of Sciences
3. Shenzhen JLC Technology Group Co., Ltd.
