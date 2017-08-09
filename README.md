# bitlocker_filter
Get bit locker keys form AD then filter/format/sort

It filters, sorts and prints out the date and the recovery keys. 

I've found the core of the PowerShell script [here](https://ndswanson.wordpress.com/2014/10/20/get-bitlocker-recovery-from-active-directory-with-powershell/). I just modifed a bit. Thanks a mill!

It can also export the keys into a .csv file. (But I don't recommend that!)


# Usage
```
PS C:\Users\admin\PS> .\bitlocker.ps1
Enter hostname: WIN-123456

Date       Recovery Key
----       ------------
2017-08-08 111111-222222-333333-444444-555555-666666-777777-888888
2017-08-03 999999-000000-111111-222222-333333-444444-555555-666666
```

## Work in progress
