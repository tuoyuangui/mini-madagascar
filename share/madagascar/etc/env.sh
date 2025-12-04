#!/bin/sh

# Path for Madagascar installation directory
export RSFROOT=/mnt/e/small_mada/madagascar-4.2

# Path for Madagascar source directory
export RSFSRC="/mnt/e/small_mada/madagascar-4.2"

# Path for Python packages
if [ -n "$PYTHONPATH" ]; then
export PYTHONPATH=$RSFROOT/lib/python3.13/site-packages:${PYTHONPATH}
else
export PYTHONPATH=$RSFROOT/lib/python3.13/site-packages
fi

# Path for Julia API
if [ -n "$JULIA_LOAD_PATH" ]; then
export JULIA_LOAD_PATH=$RSFROOT/lib:${JULIA_LOAD_PATH}:
else
export JULIA_LOAD_PATH=$RSFROOT/lib:
fi

# Path for binary data files part of RSF datasets
export DATAPATH=/var/tmp/

# Path for manual pages
unset MANPATH
export MANPATH=`manpath`:$RSFROOT/share/man

# Path for shared object files
if [ -n "$LD_LIBRARY_PATH" ]; then
export LD_LIBRARY_PATH=$RSFROOT/lib:${LD_LIBRARY_PATH}
else
export LD_LIBRARY_PATH=$RSFROOT/lib
fi

# Path for executables
export PATH=$RSFROOT/bin:$PATH
