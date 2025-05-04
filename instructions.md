### Thoughtful Robotic Automation Factory

This repository contains a Python implementation for sorting packages into the correct stack based on their volume and mass.

---

### Objective

The goal is to dispatch packages to the appropriate stack using the following rules:

- **Bulky**: A package is bulky if its volume (Width x Height x Length) is ≥ 1,000,000 cm³ or any dimension is ≥ 150 cm.
- **Heavy**: A package is heavy if its mass is ≥ 20 kg.

#### Stacks:
- **STANDARD**: Packages that are neither bulky nor heavy.
- **SPECIAL**: Packages that are either bulky or heavy.
- **REJECTED**: Packages that are both bulky and heavy.

---

### How to Run

1. **Run the Program**:
   ```bash
   python main.py
   ```

2. **Run Tests**:
   ```bash
   python -m unittest test_main.py
   ```

---

### Setup

1. **Check Python Installation**:
   Ensure Python 3.6 or higher is installed:
   ```bash
   python3 --version
   ```

2. **Install Dependencies**:
   If required, install dependencies using:
   ```bash
   pip install -r requirements.txt
   ```

3. **Virtual Environment (Optional)**:
   - Create a virtual environment:
     ```bash
     python3 -m venv venv
     ```
   - Activate it:
     ```bash
     source venv/bin/activate
     ```
   - Deactivate it:
     ```bash
     deactivate
     ```
