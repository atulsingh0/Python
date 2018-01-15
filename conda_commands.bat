

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
conda list -n <myenv> <pkg_name>

:: Running Conda Navigator
anaconda-navigator

:: Updating Conda Navigator
conda update anaconda-navigator

:: Exporting Conda Environment file
call activate <myenv>
conda env export > env.yml

:: Removing Conda Envitonment
conda remove --name <myenv> --all 

:: Install pkg
conda install <pkg>

:: Install pkg from specific channel
conda install <pkg> -c  <chaneel>  # such as conda-forge

:: Install pkg for specific env
conda install --name <env> <pkg>

