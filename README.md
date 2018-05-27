# README
[How to set udev rules permanently](https://answers.ros.org/question/224028/permanently-set-permissions-for-devttyacm0-port-using-udev/)

/etc/udev/rules.d/01-sensor.rules:
```
SUBSYSTEMS=="usb", ATTRS{idVendor}=="0483", ATTRS{idProduct}=="5740", GROUP="users", MODE="0666", SYMLINK+="sens_acm", ENV{ID_MM_DEVICE_IGNORE}="1"
```