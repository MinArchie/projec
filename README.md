
# 💊 Drug-Drug Interaction Prediction using Graph Neural Networks (GMPNN-CSNet)

**Authors:**  
Jaee Priyadarshan Kulkarni, R Keerthana Prasad, Sanskriti Tondihal, Swathi Kulkarni  
School of Computer Science and Engineering, RV University, Bangalore, India  
USN: 1RVU23CSE196, 1RVU23CSE363, 1RVU23CSE409, 1RVU22CSE492  

---

## 🧠 Project Overview

Drug-Drug Interaction (DDI) prediction is crucial in pharmacology and clinical settings to ensure safe and effective drug administration. This project presents a deep learning-based approach using a **Gated Message Passing Neural Network (GMPNN-CSNet)** to predict potential drug interactions. This project builds upon the original paper and code by [Nyambo et. all](https://academic.oup.com/bib/article/23/1/bbab441/6409692). By leveraging molecular graphs and relational features from the DrugBank database, our model identifies interaction types with high accuracy, utilizing graph neural network techniques and GPU acceleration.

---

## 📂 Project Structure

```
DDI-GNN-Prediction/
│
├── data/                     # Processed data, flods, and pos-neg-triplets raw data
├── extras/                   # Log files, graphing tools
├── datasets/                 # DrugBank Dataset
├── ddi_prediction.ipynb      # Entry point to train and evaluate the model
├── gmpnn_model_recovered.pt  # Saved model
└── README.md                 # Project documentation
```

---

## 🔬 Methodology

### 🔸 Dataset

- **Source**: [DrugBank Database](https://go.drugbank.com/)
- **Samples**: 191,808 drug-pairs
- **Labels**: 86 unique interaction types  
- **Preprocessing**:
  - SMILES → Molecular graph using RDKit
  - Nodes = Atoms (with atom-level features)
  - Edges = Bonds (with bond-type features)
  - Negative samples generated using corrupted molecule technique (Nyambo et al.)

### 🔸 Model Architecture

**GMPNN-CSNet** builds upon the Message Passing Neural Network framework with the following enhancements:

- LSTM-based hidden state update
- Multi-head Attention for message passing
- Edge-aware transformations (bond conditioning)
- Line-graph enhancement for bond representation
- Sigmoid-based final prediction with margin contrastive loss

---

## 🚀 How to Run

### ⚙️ Installation

```bash
git clone https://github.com/your-username/DDI-GNN-Prediction.git
cd DDI-Prediction
```

### ▶️ Train the Model

Run all ipynb cells


## 📈 Evaluation Metrics

We evaluate model performance using:

- **Accuracy**
- **Precision**
- **Recall**
- **F1-score**
- **Interpolated Precision (int-p)**
- **Average Precision (ap)**
- **ROC-AUC Score**

Example ROC-AUC: **0.92** (GPU-trained)

---

## 🧪 Results

- Model exhibits high accuracy and generalization across multiple data splits.
- GPU acceleration significantly enhances training efficiency and performance.
- GMPNN-CSNet surpasses traditional machine learning and basic GNN baselines.

---

## 📊 Visualizations

- Training Loss vs Epochs
- Molecule visulaziation 

---

## 💡 Key Takeaways

- Graph neural networks (GNNs) are powerful tools for drug discovery and DDI analysis.
- Molecular structure and bond-based features play a crucial role in capturing drug behavior.
- Relation-aware and edge-conditioned message passing significantly improves model robustness.

---

## 🤝 Acknowledgements

- Nyambo et al. for the original GMPNN model inspiration
- Dr. Shabbeer Basha S H from RV University
- RDKit for molecular graph extraction  
- DrugBank for dataset access  

---
