window
python -m nuitka --mingw64 --standalone --windows-disable-console --onefile --include-data-dir=ui=ui --enable-plugin=pyside2 --nofollow-imports --output-dir=out --remove-output main.py

linux
python -m nuitka --static-libpython=no --standalone --onefile --include-data-dir=ui=ui --enable-plugin=pyside2 --nofollow-imports --output-dir=out --remove-output main.py

mac
python -m nuitka --static-libpython=no --standalone --macos-create-app-bundle --onefile --include-data-dir=ui=ui --enable-plugin=pyside2 --nofollow-imports --output-dir=out --remove-output main.py
