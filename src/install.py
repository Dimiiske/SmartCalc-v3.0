from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["PIL", "matplotlib"],
    "include_files": []
}

setup(
    name="SmartCalc_v3",
    version="0.1",
    description="My Application",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py")]
)
