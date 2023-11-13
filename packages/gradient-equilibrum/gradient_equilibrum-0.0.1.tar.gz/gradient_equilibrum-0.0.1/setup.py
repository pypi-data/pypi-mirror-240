# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ge']

package_data = \
{'': ['*']}

install_requires = \
['pytests', 'torch']

setup_kwargs = {
    'name': 'gradient-equilibrum',
    'version': '0.0.1',
    'description': 'Gradient Equillibrum - Pytorch',
    'long_description': '[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)\n\n# Gradient Equilibrum\nGradient Equilibrium is a numerical optimization technique used to find the point at which a function reaches its global middle. This is different from traditional gradient descent methods, which seek to minimize or maximize a function. Instead, Gradient Equilibrium tries to find the point where the function value is at its average or equilibrium.\n\n\n# Install\n`pip install gradient-equilibrum`\n\n# Usage\n```python\n\nimport torch\nimport torch.nn as nn\nfrom ge.main import GradientEquilibrum  # Import your optimizer class\n\n# Define a sample model\nclass SampleModel(nn.Module):\n    def __init__(self):\n        super(SampleModel, self).__init__()\n        self.fc = nn.Linear(10, 10)\n\n    def forward(self, x):\n        return self.fc(x)\n\n# Create a sample model and data\nmodel = SampleModel()\ndata = torch.randn(64, 10)\ntarget = torch.randn(64, 10)\nloss_fn = nn.MSELoss()\n\n# Initialize your GradientEquilibrum optimizer\noptimizer = GradientEquilibrum(model.parameters(), lr=0.01)\n\n# Training loop\nepochs = 100\nfor epoch in range(epochs):\n    # Zero the gradients\n    optimizer.zero_grad()\n\n    # Forward pass\n    output = model(data)\n\n    # Calculate the loss\n    loss = loss_fn(output, target)\n\n    # Backward pass\n    loss.backward()\n\n    # Update the model\'s parameters using the optimizer\n    optimizer.step()\n\n    # Print the loss for monitoring\n    print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item()}")\n\n# After training, you can use the trained model for inference\n\n```\n\n## **Why Gradient Equilibrium?**\n\nIn many real-world scenarios, it\'s not always about finding the minimum or maximum. Sometimes, we might be interested in finding a balance or an average. This is where Gradient Equilibrium comes into play. For example, in load balancing problems or in scenarios where resources need to be evenly distributed, finding an equilibrium point is more relevant than finding extremes.\n\n## **Algorithmic Pseudocode**\n\n```\nFunction GradientEquilibrium(Function f, float learning_rate, int max_iterations):\n\n    Initialize x = random value within the domain of f\n    Initialize previous_x = x + 1  // Just to ensure we enter the loop\n\n    For i = 1 to max_iterations and |previous_x - x| > small_value:\n        previous_x = x\n        \n        // Compute gradient of f at x\n        gradient = derivative(f, x)\n        \n        // Update x using gradient descent\n        x = x - learning_rate * gradient\n\n    End For\n\n    Return x\n\nEnd Function\n\nFunction derivative(Function f, float x):\n    delta_x = small_value\n    Return (f(x + delta_x) - f(x)) / delta_x\nEnd Function\n```\n\n\n**How does the Algorithm Work?**\n\nThe Gradient Equilibrium algorithm starts by initializing a random value within the domain of the function. This value serves as our starting point. \n\nDuring each iteration, we calculate the gradient or derivative of the function at the current point. The gradient gives us the direction of steepest ascent. Since we are looking for the equilibrium, we move against the gradient by a factor of the learning rate. This step is similar to the gradient descent method but with a different goal in mind.\n\nThe algorithm stops iterating when the change between the current value and the previous value is less than a small threshold or when the maximum number of iterations is reached.\n\n**Applications of Gradient Equilibrium**\n\n1. **Load Balancing**: In distributed systems, ensuring that each server or node handles an approximately equal share of requests is crucial. Gradient Equilibrium can be used to find the optimal distribution.\n\n2. **Resource Allocation**: Whether it\'s distributing funds, manpower, or any other resource, Gradient Equilibrium can help find the point where each division or department gets an average share.\n\n3. **Economic Models**: In economics, equilibrium points where supply meets demand are of great significance. Gradient Equilibrium can be applied to find such points in complex economic models.\n\n**Conclusion**\n\nGradient Equilibrium offers a fresh perspective on optimization problems. Instead of always seeking extremes, sometimes the middle ground or average is more relevant. With its straightforward approach and wide range of applications, Gradient Equilibrium is an essential tool for modern-day problem solvers.\n\n\n# License \nMIT\n',
    'author': 'Kye Gomez',
    'author_email': 'kye@apac.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kyegomez/GradientEquillibrum',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
