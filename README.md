# Brain Tumor Identification System

## Overview
The prevalence of brain tumors underscores the urgent need for advanced diagnostic tools in the medical field. With approximately 11,700 individuals affected each year and a sobering 5-year survival rate of just 34% for men and 36% for women, the significance of early detection cannot be overstated. In response to this pressing healthcare challenge, I developed a project which can provide a user-friendly, ready-to-use brain tumor segmentation system utilizing the U-Net architecture.
## Key Features
- **High Accuracy**: Achieves an impressive accuracy of 99%, ensuring reliable identification of brain tumors.
- **Robust Performance**: Boasts a recall of 93% and a precision of 94%, highlighting the system's effectiveness in accurately pinpointing tumor regions.
- **Advanced Metrics**: Demonstrates a Dice coefficient of 94% and an Intersection over Union (IoU) of 89%, indicating remarkable precision in delineating tumor boundaries.

## Performance Metrics
- **Accuracy**: 99%
- **Recall**: 93%
- **Precision**: 94%
- **Dice Coefficient**: 94%
- **Intersection over Union (IoU)**: 89%
## Dataset Used
The dataset used for training and testing this model is from [Kaggle](https://www.kaggle.com/datasets/mateuszbuda/lgg-mri-segmentation). This dataset is well-known in the field of medical imaging and provides comprehensive MRI scans for brain tumor segmentation tasks.

## How to Use
1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/brain-tumor-identification-system.git
    cd brain-tumor-identification-system
    ```

2. **Install the Requirements**
    ```bash
    pip install -r requirements.txt
    ```

3. **Execute the Python File**
    ```bash
    python hello.py
    ```

4. **Use the Test MRI Image**
    - Test the system using the MRI images provided in the `test images` folder.
