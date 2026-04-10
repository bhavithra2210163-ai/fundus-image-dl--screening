# fundus-image-dl--screening
Deep learning pipeline for disease screening using retinal fundus images
## 📊 Model Performance (Research Work)

### ROC Curve
![ROC Curve](results/roc_curve.png)

- AUC Score: ~0.87

### Confusion Matrix
![Confusion Matrix](results/confusion_matrix.png)

## 📈 Key Results
- Good classification performance on medical imaging dataset  
- Balanced detection of Normal and Thickened cases  
- Strong ROC-AUC indicating reliable model performance  

## Advanced Model Details
The full model was developed using:

- SE-ResNeXt50 architecture
- Feature extraction + classification pipeline
- Stratified train/validation/test split
- Clinical metadata integration (age, gender)
- Evaluation metrics: Accuracy, F1-score, ROC-AUC

Due to dataset and privacy constraints, the complete training pipeline is not included in this repository.

