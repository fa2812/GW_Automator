# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['GW Auto - GUI.py'],
    pathex=[],
    binaries=[],
    datas=[
	('C:\\Users\\Fawwaz.Azwar\\OneDrive - Last Mile\\Documents - OneDrive\\Python Scripts\\GW_Automator\\images', 'images'),
	('C:\\Users\\Fawwaz.Azwar\\OneDrive - Last Mile\\Documents - OneDrive\\Python Scripts\\GW_Automator\\Outputs', 'Outputs')
	],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='GW Automator & Macros',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='GW Automator & Macros',
)