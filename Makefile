deps: requirements.txt
	@echo "Installing Dependencies"
	@pip install -r requirements.txt

build:
	@echo "Compiling the software"
	python -m PyInstaller --noconfirm --onefile --windowed  ".\calculadora2.py" --icon icone.ico

clean:
	@echo "Cleaning project directory"
	if exist "./build" rd /s /q build
	if exist "./dist" rd /s /q dist
	if exist "./calculadora2.spec" del calculadora2.spec

