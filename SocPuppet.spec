# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['SocPuppet.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['html', 'shodan', 'requests', 'ipwhois', 'gpt4all', 'unfurl', 'win32com', 'tkinter', 'tkinter.filedialog', 'extract_msg', 'sys', 'alive_progress', 'grapheme'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='SocPuppet',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='SocPuppet',
)
