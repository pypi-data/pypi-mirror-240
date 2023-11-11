# tidydata

Here is a suggested installation guide in English, incorporating your requirements:

---

## Installation Guide

For a seamless installation of our package, which is tightly coupled with fixed versions of Python and its dependencies, we highly recommend setting up a Python virtual environment and using a version management tool. Our preferred tool for managing Python versions is Rye, which offers a straightforward and user-friendly interface for this purpose.

### Prerequisites

Before proceeding with the installation, ensure that you have Rye installed on your system. If you haven't installed Rye yet, please visit [Rye's Installation Guide](https://rye-up.com/guide/publish/#publish) for detailed instructions on how to set it up.

### Setting up a Python Virtual Environment

1. Open your terminal.
2. Create a new virtual environment by running:
   ```bash
   python -m venv myenv
   ```
   Replace `myenv` with your preferred name for the virtual environment.

3. Activate the virtual environment:
   - On macOS and Linux:
     ```bash
     source myenv/bin/activate
     ```
   - On Windows:
     ```bash
     myenv\Scripts\activate
     ```

### Installing the Fixed Version of Python

With Rye, you can install and manage multiple versions of Python easily. To install Python 3.11.5, which our package requires, follow these steps:

1. Add Python 3.11.5 to your Rye configuration:
   ```bash
   rye add python@3.11.5
   ```

2. Once the specific Python version is installed, you can switch to it using:
   ```bash
   rye use python@3.11.5
   ```

### Installing Our Package

After setting up the environment and the correct Python version, you can now install our package. Since our package has fully pinned dependencies, it's crucial to install the exact versions specified.

1. To install our package, simply run:
   ```bash
   pip install our-package-name
   ```

   Replace `our-package-name` with the actual name of our package.

2. If there are any additional dependencies or specific versions required, they should be listed in a `requirements.txt` file included with our package. Install them using:
   ```bash
   pip install -r requirements.txt
   ```

By following these steps, you can ensure that the correct Python version and dependencies are used, which is crucial for the proper functioning of our package.

---

Make sure to replace placeholder text like `our-package-name` with actual information relevant to your package. Additionally, you can provide a `requirements.txt` file if your package requires specific versions of dependencies.


