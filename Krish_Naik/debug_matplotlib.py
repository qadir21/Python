#!/usr/bin/env python3

import sys
print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version}")
print(f"Python path: {sys.path[:3]}...")  # Show first 3 paths

try:
    import matplotlib
    print(f"✅ Matplotlib found! Version: {matplotlib.__version__}")
    print(f"Matplotlib location: {matplotlib.__file__}")
    
    import matplotlib.pyplot as plt
    print("✅ pyplot imported successfully!")
    
    # Simple test
    import numpy as np
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    
    plt.figure(figsize=(6, 4))
    plt.plot(x, y, 'bo-')
    plt.title('Simple Test Plot')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.savefig('debug_plot.png', dpi=100, bbox_inches='tight')
    print("✅ Plot created and saved as 'debug_plot.png'")
    plt.close()
    
except ImportError as e:
    print(f"❌ Import Error: {e}")
    print("Matplotlib is not installed in this Python environment")
except Exception as e:
    print(f"❌ Other Error: {e}")

print("\n" + "="*50)
print("If you see this message without errors above,")
print("then matplotlib is working correctly!")
print("="*50)
