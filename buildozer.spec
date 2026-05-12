[app]
title = Sanzo Quiz Sans Faute
package.name = sanzoquizsansfaute
package.domain = org.example
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,wav
version = 1.0
requirements = python3,kivy,kivymd,numpy
orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b

[buildozer]
log_level = 2
warn_on_root=1 