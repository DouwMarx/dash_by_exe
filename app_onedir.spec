# -*- mode: python ; coding: utf-8 -*-
# This is a specification file for compiling the application into a single folder

block_cipher = None


a = Analysis(['server.py'],
             pathex=['C:\\Users\\douwm\\repos\\dash_by_exe'],
             binaries=[],
             datas=[
                  ('C:/Users/douwm/Anaconda3/envs/dash_by_exe/Lib/site-packages/dash_core_components','dash_core_components'),
                  ('C:/Users/douwm/Anaconda3/envs/dash_by_exe/Lib/site-packages/dash_html_components',
                  'dash_html_components'),
                  ('C:/Users/douwm/Anaconda3/envs/dash_by_exe/Lib/site-packages/dash_bootstrap_components','dash_bootstrap_components'),
                  ('C:/Users/douwm/Anaconda3/envs/dash_by_exe/Lib/site-packages/plotly',
                  'plotly'),
                  ('C:/Users/douwm/Anaconda3/envs/dash_by_exe/Lib/site-packages/dash_renderer',
                  'dash_renderer'),
                  ('C:/Users/douwm/Anaconda3/envs/dash_by_exe/Lib/site-packages/dash',
                  'dash'),
                  ('C:/Users/douwm/repos/dash_by_exe/assets','assets'),
                  ('C:/Users/douwm/repos/dash_by_exe/data','data'),
                  ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='launch_app',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          icon = 'assets/icon.ico',
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='app')
