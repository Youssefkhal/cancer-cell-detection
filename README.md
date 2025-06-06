# Cancer Cell Detection with YOLOv5 🧬🩺

This project demonstrates the use of **YOLOv5** for detecting **cancer cells** in breast radiology images using a custom-trained deep learning model.



---

## 🧠 Overview

I trained a YOLOv5 model to detect cancer cells using a small medical image dataset. The model was trained for **20 epochs** due to **limited hardware resources**.

- **Model:** YOLOv5 (custom trained)
- **Framework:** PyTorch + Flask
- **Application:** Cancer cell detection from microscopy images
- **Training duration:** 20 epochs  
- **Performance:**  
  - precision of 64.5%

Despite limitations, this project is a step toward applying AI in **medical imaging and diagnostics**.

---


https://github.com/user-attachments/assets/e1a7b25f-1d96-45e4-93f3-4d54fc7caf6e



![image](https://github.com/user-attachments/assets/1026b32d-8852-4f0b-a2e7-c19d55ffc915)

![image](https://github.com/user-attachments/assets/5686eec6-a75d-4ade-bb6d-c47b3d884f4b)

![image](https://github.com/user-attachments/assets/1e1a981f-50f0-4aff-9736-3b4fb1d81a60)


## 📂 Project Structure

```bash
.
├── app.py                # Flask backend to upload & run detection
├── templates/
│   └── index.html        # Frontend interface
├── uploads/              # Uploaded images (auto-created)
├── results/              # Detected result images (auto-created)
├── best.pt               # Trained YOLOv5 model weights
└── README.md
