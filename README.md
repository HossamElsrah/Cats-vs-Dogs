# 🐱 vs 🐶 Cats vs Dogs Classifier  
**Best Model: VGG16 Fine-Tuned (100% Train / 98% Val Accuracy)**  
*Outperformed our Custom CNN (98% Train / 96% Val)*  

---

## 🚀 **Streamlit Web App (Main Feature)**  

### **App Features**:  
- 🖼️ **Drag-and-drop** interface for model upload (.keras/.h5)  
- 🐶 **Instant prediction** with confidence percentage  
- 📱 **Mobile-responsive** design  
- 🔄 **Model switching** between VGG16 (default) and Custom CNN  

**App Screenshot**:  
![App Interface](https://github.com/HossamElsrah/Cats-vs-Dogs/blob/main/App%20Photo.png?raw=true)  

**Run locally**:  
```bash
streamlit run app.py  # Uses VGG16 by default (best model)
```

---

## 🏆 Key Findings  
### Model Comparison  
| Model Type       | Train Accuracy | Val Accuracy | Parameters |  
|------------------|----------------|--------------|------------|  
| **VGG16 FT** ✅  | 100%           | 98%          | ~15M       |  
| Custom CNN       | 98%            | 96%          | ~1.2M      |  

**Why VGG16 Wins**:  
- 🎯 **Perfect training accuracy** (100% vs 98%)  
- 🏆 **Better generalization** (98% val vs 96%)  
- 🧠 **Transfer learning power** despite more parameters  

---

## 🛠️ Technical Details  
### VGG16 Fine-Tuned Architecture  
```python
Sequential([
    VGG16(weights='imagenet', include_top=False),
    Flatten(),
    Dense(512, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')
])
```

### **Optimization Secrets**:  
1. Unfrozen last 10 layers for fine-tuning  
2. Used RMSprop with learning rate 1e-5  
3. Added aggressive dropout (0.5)  

---

## 🔄 Reproduce  
```bash
# 1. Get data
kaggle competitions download -c dogs-vs-cats

# 2. Train VGG16 (best model)
python train.py --model vgg16 --epochs 50

# 3. Launch app
streamlit run app.py
```

> *"After careful tuning, our VGG16 model achieved perfect training accuracy while maintaining excellent generalization - a rare and impressive result!"*

**Dataset**: [Dogs vs Cats](https://www.kaggle.com/c/dogs-vs-cats)  

=======
