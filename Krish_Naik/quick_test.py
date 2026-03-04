# Quick matplotlib test
import sys
print(f"Python path: {sys.executable}")
print(f"Python version: {sys.version}")

try:
    import matplotlib
    print(f"✅ Matplotlib version: {matplotlib.__version__}")
    print(f"Matplotlib location: {matplotlib.__file__}")
    
    import matplotlib.pyplot as plt
    print("✅ matplotlib.pyplot imported successfully!")
    
except ImportError as e:
    print(f"❌ Error: {e}")
    
# List all available packages
import pkg_resources
installed_packages = [d.project_name for d in pkg_resources.working_set]
matplotlib_found = 'matplotlib' in installed_packages
print(f"Matplotlib in installed packages: {matplotlib_found}")
