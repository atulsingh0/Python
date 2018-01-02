

:: Listing Conda Details
conda info

:: Listing Conda Environment
conda info --envs
conda env list

:: Listing Installed Conda packages
conda list --show-channel-urls

:: Listing Specific environments packages
conda list -n <myenv>

:: Check if package is installed or not
conda list -n <myenv> <pkg>

:: Running Conda Navigator
anaconda-navigator

:: Updating Conda Navigator
conda update anaconda-navigator

:: Exporting Conda Environment file
call activate <myenv>
conda env export > env.y,ml

:: Removing Conda Envitonment
conda remove --name <env> --all 