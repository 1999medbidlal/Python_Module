import sys

print("\nLOADING STATUS: Loading programs...")
print("\nChecking dependencies: ")
missing = []
try:
    package = 'pandas'
    import pandas as pd
    print(f"[OK] pandas ({pd.__version__}) - Data manipulation ready")
except ImportError:
    missing.append(package)
try:
    package = 'requests'
    import requests
    print(f"[OK] requests ({requests.__version__}) - Network access ready")
except ImportError:
    missing.append(package)
try:
    package = 'matplotlib'
    import matplotlib
    print(f"[OK] matplotlib({matplotlib.__version__}) - Visualization ready ")
    import matplotlib.pyplot as plt
except ImportError:
    missing.append(package)
try:
    package = 'numpy'
    import numpy
except ImportError:
    missing.append(package)

if len(missing):
    print(f"missing dependencies: {missing}")
    print("installation instructions: ")
    print("method1 : pip install -r requirements.txt")
    print("method2: poetry install")
    sys.exit(1)
url = "https://google.com"
print("\nAnalyzing Matrix data...")
names = ['Ahmed', 'ALI', 'SAMAR', 'MOHAMED', 'HAMZA']
data = {
    'name': numpy.random.choice(names, 1000),
    'age': numpy.random.randint(18, 60, 1000)
}
print("Processing 1000 data points...")
proc = pd.DataFrame(data)
print("Generating visualization...")
plt.bar(proc['name'], proc['age'], color='skyblue')
plt.xlabel('Name', fontsize=16, color='red')
plt.ylabel('Age', fontsize=16, color='blue')
plt.title("Loading Programs", fontsize=20, color='green')
plt.savefig("matrix_analysis.png")
print("\nAnalysis complete!")
print("Results saved to: matrix_analysis.png")
