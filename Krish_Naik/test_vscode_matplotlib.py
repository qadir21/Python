# Test file for VS Code matplotlib
# Run this in VS Code to verify matplotlib works

print("🔍 Testing matplotlib import...")

try:
    import matplotlib.pyplot as plt
    print("✅ matplotlib.pyplot imported successfully!")
    
    # Also test the original way you were importing
    import matplotlib as mpl
    print("✅ matplotlib (as mpl) imported successfully!")
    
    # Create a simple test plot
    import numpy as np
    x = np.linspace(0, 10, 50)
    y = np.sin(x)
    
    plt.figure(figsize=(8, 4))
    plt.plot(x, y, 'b-', label='sin(x)')
    plt.title('VS Code Matplotlib Test')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Save the plot
    plt.savefig('vscode_test_plot.png')
    print("📊 Plot saved as 'vscode_test_plot.png'")
    
    print("🎉 All tests passed! Matplotlib is working in VS Code.")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("📝 VS Code is still using the wrong Python interpreter.")
    print("🔧 Please follow the steps to select the correct interpreter.")
