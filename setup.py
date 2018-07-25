from cx_Freeze import setup,Executable

exe=Executable(
     script="mun_app.py",
     base="Win32Gui",
     )

includefiles = ['config.json', '/motion_options.ui', '/delegate_view.ui',  '/speaker_view.ui','/mun_app_ui.ui']
excludes = []
includes = []
packages = []

setup(
    name = 'MUN App',
    version = '0.1',
    description = 'An app for model un chairs',
    options = {'build_exe': {'includes':includes,'excludes':excludes,'packages':packages,'include_files':includefiles}}, 
    executables = [exe]
)