#!/bin/csh

# Path for Madagascar installation directory
setenv RSFROOT /mnt/e/small_mada/madagascar-4.2

# Path for Madagascar source directory
setenv RSFSRC "/mnt/e/small_mada/madagascar-4.2"

# Path for Python packages
if ($?PYTHONPATH) then
setenv PYTHONPATH $RSFROOT/lib/python3.13/site-packages:${PYTHONPATH}
else
setenv PYTHONPATH $RSFROOT/lib/python3.13/site-packages
endif

# Path for Julia API
if ($?JULIA_LOAD_PATH) then
setenv JULIA_LOAD_PATH $RSFROOT/lib:${JULIA_LOAD_PATH}:
else
setenv JULIA_LOAD_PATH $RSFROOT/lib:
endif

# Path for binary data files part of RSF datasets
setenv DATAPATH /var/tmp/

# Path for manual pages
setenv MANPATH `manpath`:$RSFROOT/share/man

# Path for shared object files
if ($?LD_LIBRARY_PATH) then
setenv LD_LIBRARY_PATH $RSFROOT/lib:${LD_LIBRARY_PATH}
else
setenv LD_LIBRARY_PATH $RSFROOT/lib
endif

# Path for executables
set path = ($RSFROOT/bin $path)
