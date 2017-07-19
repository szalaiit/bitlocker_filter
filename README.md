# bitlocker_filter
Get bit locker keys form AD then filter/format

I've found the PowerShell script [here](https://ndswanson.wordpress.com/2014/10/20/get-bitlocker-recovery-from-active-directory-with-powershell/). Thanks a mill!

The PS script exports the keys into a .csv file.

My python cript reads/filters the bitlocker.csv file and writes into a new output.csv file.
