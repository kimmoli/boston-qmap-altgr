TARGET = boston-qmap-altgr
TEMPLATE = aux

qmap.files = boston.qmap
qmap.path = /usr/share/qt5/keymaps

INSTALLS = qmap

OTHER_FILES += \
    rpm/boston-qmap-altgr.spec \
    boston.qmap
