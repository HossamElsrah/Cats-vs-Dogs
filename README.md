<<<<<<< HEAD
# Cat vs Dog Classifier 🐱 vs 🐶  
**Best Model: Custom CNN (98% Train / 96% Val Accuracy)**  
*Outperformed VGG16 transfer learning (92% both)*  

---

## 🚀 **Streamlit Web App (Main Feature)**  

### **App Features**:  
- 🖼️ **Drag-and-drop** interface for model upload (.keras/.h5)  
- 🐶 **Instant prediction** with confidence percentage  
- 📱 **Mobile-responsive** design  
- 🔄 **Model switching** between Custom CNN and VGG16  

**App Screenshot**:  
![App Interface](https://github.com/HossamElsrah/Cats-vs-Dogs/blob/main/App%20Photo.png?raw=true)  

**Run locally**:  
```bash
streamlit run app.py -- --model custom  # Uses best model by default
```

---

## 🏆 Key Findings  
### Model Comparison  
| Model Type       | Train Accuracy | Val Accuracy | Parameters |  
|------------------|----------------|--------------|------------|  
| **Custom CNN** ✅ | 98%            | 96%          | ~1.2M      |  
| VGG16 FT         | 92%            | 92%          | ~15M       |  

**Why our CNN wins**:  
- 🎯 12x more efficient (1.2M vs 15M params)  
- ⚡ Faster inference (~15ms/image on CPU)  
- 📉 No overfitting (98→96 vs VGG16's 92→92)  

---

## 🛠️ Technical Details  
### Custom CNN Architecture  
```python
Sequential([
    Conv2D(32, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    .......
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')
])
```

### **App Components**:  
1. `app.py` - Main Streamlit interface  
2. `model_loader.py` - Handles model switching  
3. `utils/` - Image preprocessing pipelines  

---

## 🔄 Reproduce  
```bash
# 1. Get data
kaggle competitions download -c dogs-vs-cats

# 2. Train models
python train.py --model custom --epochs 50
python train.py --model vgg16 --epochs 30

# 3. Launch app
streamlit run app.py
```

> *"Our Custom CNN proves that task-specific architectures often outperform generic transfer learning."*

**Dataset**: [Dogs vs Cats](https://www.kaggle.com/c/dogs-vs-cats)  
```
=======
# Cats-vs-Dogs
>>>>>>> 68213e7bd3d39576734d1834970aac87678d8c76
