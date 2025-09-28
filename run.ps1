# Temporär Execution Policy lockern
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

# Virtuelle Umgebung aktivieren
. .venv\Scripts\Activate.ps1

# Projekt installieren (editable)
pip install -e .

# Robot-Tests ausführen
# robot -d reports tests\test_swingset3_structure.robot
robot -d reports tests\WidgetsDemo.robot tests\Web_Caption.robot tests\Web_Label.robot tests\Web_Placeholder.robot tests\Web_Attribute.robot tests\Web_Focus.robot