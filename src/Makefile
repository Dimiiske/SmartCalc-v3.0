test:
	cd model && gcc -shared -fPIC -o libcalc.so s21_calc.c && pytest-3 tests.py && cd ..

prepare:
	bash prepare.sh

install:
	cd model && gcc -shared -fPIC -o libcalc.so s21_calc.c && cd ..
	python3 install.py build && ./build/exe.linux-x86_64-3.10/main

uninstall:
	rm -rf build
