@setlocal
@cd /d "%~dp0"
@chdir

python main.py --config default.ini
@REM "venv/Scripts/python.exe" main.py --config default.ini