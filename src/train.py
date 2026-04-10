import numpy as np
from model import create_model

# Dummy dataset (for demo)
X = np.random.rand(20,128,128,3)
y = np.random.randint(0,2,20)

model = create_model()

model.fit(X, y, epochs=3)

print("Training complete")
