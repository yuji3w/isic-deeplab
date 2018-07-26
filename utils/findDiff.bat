for %%i IN (*.py) do (
   diff %%i "D:\tensorflow-models-master-2018-5\research\deeplab-7-22-2018\utils\%%i"
   pause
)

for %%i IN (*.sh) do (
   diff %%i "D:\tensorflow-models-master-2018-5\research\deeplab-7-22-2018\utils\%%i"
   pause
)

pause