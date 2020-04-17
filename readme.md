# Runner
This scripts runs an _application_ with _optional parameters_ and tries to open a file, _filtered by extension_.


## Command line help
```
optional arguments:
  -h, --help            show this help message and exit
  -a APP, --application APP
                        Application that will be used to run the file.
  -o CMD_ARGS, --run-options CMD_ARGS
                        Arguments that will be used to run this application.
  -e EXT_FILTER, --ext-filter EXT_FILTER
                        File extension to filter your options. (Default: *)

```


## How does it work
The script will (recursively) look into the current working directory and tell the application 
to open the file (filtered by extension). 

If only one file with that extension exists, will open it automatically, but if there's more than one, 
the script will ask the user which file to open.


## Usage example
Opens the solution in the current directory using Visual Studio.
```shell script
python runner.py -a -a "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\IDE\devenv.exe" -e *.sln
```

## My use cases
```vs.bat```: opens a solution file using Visual Studio
```batch file
 @echo off
<path to script>\runner.py -a "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\IDE\devenv.exe" -e *.sln
```

```rider.bat```: opens a solution file using Rider (from Jetbrains)
```batch file
 @echo off
<path to script>\runner.py -a "C:\Users\<user>\AppData\Local\JetBrains\Toolbox\apps\Rider\ch-0\193.6494.48\bin\rider64.exe" -e *.sln
```

## Notes
I know there may be better ways to do it, but this is script works fine and it's flexible enough to help me 
automate a couple of actions. 
