:: ----------------------------------------------------------------------
:: Jupyter / Lab Quick Start Batch Script
:: Atul Singh
:: www.datagenx.net
:: ----------------------------------------------------------------------


:: Got to your Code Directory
cd C:\learn\Git

:: Replace the value of below Arguement as per your Anaconda installation
:: My Anaconda Installation Location is - C:\tools\Anaconda3
:: My Phython Enviornment name is - pytorch
:: Use the "jupyter lab" command Or "jupyter notebook"

%windir%\System32\cmd.exe "/K C:\tools\Anaconda3\Scripts\activate.bat C:\tools\Anaconda3\envs\pytorch && jupyter lab"
