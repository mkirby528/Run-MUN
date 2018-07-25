from cx_Freeze import setup,Executable

exe=Executable(
     script="mun_app.py",
     base="Win32Gui",
     )

includefiles = ['config.json', 'ui_files/motion_options.ui', 'ui_files/delegate_view.ui',  'ui_files/speaker_view.ui','ui_files/mun_app_ui.ui']
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