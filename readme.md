# Plotly Dash, hello word example, locally hosted by waitress, compiled into an .exe with Pyinstaller.
Set up to include data for dashboard, including and image in the dashboard and setting the .exe icon.

[Dash example](https://dash.plotly.com/layout)

[Pyinstaller](https://www.pyinstaller.org/)

## After cloning repository install the packages required
`pip install -r requirements.txt`

## Edit file paths for your system
Set the paths in `app_onedir.spec` under `pathex` and `datas` to be suitable for your system.

## To create exe
run `pyinstaller app_onedir.spec` in terminal.
The application is written to the dist folder. Double click the `launch_app.exe` to run the dashboard locally.

## Note
Using app_onedir.spec creates a folder with exe inside. It is possible to create a single .exe with pyinstaller using the appropriate configuration in the .spec, but it is slow to open. 

### Useful links 

`pkg_resources.DistributionNotFound: The 'flask-compress' distribution was not found and is required by the application
[3400] Failed to execute script app`
Use code from SO answer to do monkey patch.
Change correct version number. See fix in utils folder.
Run pip show flask-compress to get version number.

`FileNotFoundError: [Errno 2] No such file or directory: 'C:\Users\douwm\AppData\Local\Temp\_MEI63602\dash_core_components\package-info.
    json'    [6304] Failed to execute script app`
https://community.plotly.com/t/pyinstaller-error-when-executing-plotly-dash-exec-file/34126/10
answer by schan: Have to add path of dash_core_components and other to .spec file
Make a app.spec and specify the path of the packages


`https://stackoverflow.com/questions/56758159/attributeerror-frozenimporter-object-has-no-attribute-filename`
Debug should be False in app.py when not debugging (Production)

`To serve the app with waitress`
https://community.plotly.com/t/can-i-use-dash-plotly-in-production-environment/13541/5
http://127.0.0.1:8080/ % Go this when running server script

`To go to the url automatically when running the exe, we let sleep and then open with web broweser as recommended:`
https://stackoverflow.com/a/60957363/13372470

`Include an assets file for dash`
https://stackoverflow.com/questions/51264169/pyinstaller-add-folder-with-images-in-exe-file/51266275
Make sure the path in .spec file is correct for system

`Delete things in app folder until app does not work to reduce size
see reduce_file_size.txt for files that could be removed`

`To add an icon to the exe`
See spec file in exe section

`onefile.spec is slow, rather use onedir and then hide the files that the user wil not interact with.`

`For ofline running, first download the css file you want to use and put it in assets
https://stackpath.bootstrapcdn.com/bootswatch/4.5.2/darkly/bootstrap.min.css  (for example)`
