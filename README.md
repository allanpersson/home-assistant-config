# Home Assistant configuration 🏰

...for making my and others life easier... Hopefully 🙈\
by **[Allan Persson][allanpersson]**

[![Home Assistant version][img-ha-version]][link-ha-version] [![Home Assistant Android version][img-ha-android-version]][link-ha-android-version]  [![Hass.io][img-hassio]][link-hassio] [![Price][img-price]][link-license]\
[![Last commit][img-last-commit]][link-repo] [![Issues][img-issues]][issues] [![License][img-license]][link-license]\
[![Buy me a coffee][img-buymeacoffee]][buymeacoffee]

# Table of contents 📑

1. **[Overview](#overview-)**\
    [Code](#code-) | [Description](#description-) | [PRs](#prs-) | [Screenshots](#screenshots-) | [Theme](#theme-)
2. **[Devices](#devices-)**\
    [Cameras](#cameras) | [Climate](#climate) | [Covers](#covers) | [Fans](#fans) | [Hardware](#hardware) | [Lights](#lights) | [Locks](#locks) | [Mediaplayers](#mediaplayers) | [Sensors](#sensors) | [Smoke Detectors](#smokedetectors) | [Switches](#switches) | [Vacuums](#vacuums)
3. **[Lovelace Configuration](#Lovelace-configuration-)**\
    [Camera Card](#camera-card) | [Speedtest Card](#speedtest-card) | [Vacuum Card](#vacuum-card)
4. **[Addons](#addons-)**\
    [Adguard Home](#adguard-home)
5. **[Seasons](#seasons-)**\
    [Halloween](#halloween-)
6. **[Credits](#credits-)**\
     [Ccostan](#ccostan) | [Frenck](#frenck) | [Renemarc](#renemarc)
7. **[Contact](#contact-)**
8. **[Support](#support-)**\
     [Affiliate Links](#affiliate-links-) | [Buy me a coffee](#buy-me-a-coffee-)

# Overview 📇

⚠ This repo contains [affiliate links](#affiliate-links-) from [Aliexpress][aliexpress] & [Ebay][ebay] that [support](#support-) my work! ⚠

## Code ⌨

Let me be clear from the start; I'm not a great coder in any way!
I don't feel the excitement from putting some code together, but i have the higest respect and admiration for people who finds joy in it and are good at it. **You make my life easier ❤️**

So you might experience my code is 'ugly' and you are probably right, i find joy in making things work as i want it to. In coding there is frontend and backend coders, i'm the **userfriendliness and comfort guy** 😛

Actual [issues][issues].

## Description 📜

Configuration for [Home Assistant][home-assistant] running [Hass.io][hassio] on a [INTEL® NUC KIT NUC8I3BEK][intelnuc] for a two bedroom apartment (66 m2).

I use `packages "configuration"` introduced by [Frenck][frenck].

That means my [configuration.yaml][configuration-yaml] points to the folder [integrations][integrations], and the files in my [integrations][integrations] folder is pointing to the [entities][entities] etc. folder where every entity has it's own file sorted by type.

Watch this video to learn more: [How I structure my Home Assistant configuration - By Frenck](https://www.youtube.com/watch?v=lndeybw21PY) or take a deeper look at my configuration.

## PRs 📝

You are more than welcome to submit PRs to my repo. This repo and documentation is "quite big" to keep up to date but i try my best!
Your help is much appreciated on my code, broken links, typos etc.

If you want to help take a look at the [issues][issues] section.

## Screenshots 📷

**Laptop:**
![Image](https://github.com/allanpersson/home-assistant-config/blob/master/config/www/images/themes/material_dark_theme_custom_laptop_frontpage.png)
![Image](https://github.com/allanpersson/home-assistant-config/blob/master/config/www/images/themes/material_dark_theme_custom_camera_description.jpeg)
![Image](https://github.com/allanpersson/home-assistant-config/blob/master/config/www/images/themes/material_dark_theme_custom_laptop_system.jpeg)

**Tablet:**
![Image](https://github.com/allanpersson/home-assistant-config/blob/master/config/www/images/themes/material_dark_theme_custom_tablet.jpeg)

**Mobile:**
![Image](https://github.com/allanpersson/home-assistant-config/blob/master/config/www/images/themes/material_dark_theme_custom_mobile.jpg)

## Theme 🖼️

The [theme][theme] i use ([screenshots](https://github.com/allanpersson/home-assistant-config#screenshots-)) is my take on [Material Dark Theme "Pepe Version"][theme] with some minor tweaks like rounded corners, color changes etc.

**Automations:**

- [Default theme](https://github.com/allanpersson/home-assistant-config/blob/master/config/automations/system/default_theme.yaml)

# Devices 📱

[Cameras](#cameras) | [Climate](#climate) | [Covers](#covers) | [Fans](#fans) | [Hardware](#hardware) | [Lights](#lights) | [Locks](#locks) | [Mediaplayers](#mediaplayers) | [Sensors](#sensors) | [Smoke Detectors](#smokedetectors) | [Switches](#switches) | [Vacuums](#vacuums)

<table align="center" border="0">
<tr><td colspan="4">

#### Cameras <a name="cameras" href="https://github.com/allanpersson/home-assistant-config#devices"><img align="right" border="0" src="https://cdn.pixabay.com/photo/2016/09/05/10/50/app-1646212_960_720.png" width="20" ></a>
</td></tr>
<tr><td align="center">

[Huawei Mediapad T3 10](https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_osacat%3D0%26_odkw%3Dxiaomi%2Bmi%2Bbox%2Bs%26_from%3DR40%26_trksid%3Dp2334524.m570.l1313.TR11.TRC1.A0.H0.Xhuawei%2Bmediapad%2Bt3.TRS0%26_nkw%3Dhuawei%2Bmediapad%2Bt3%26_sacat%3D0&campid=5338610312&toolid=20008)
</td><td align="center">
  
[Raspberry Pi 5MP](https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_odkw%3Draspberry%2Bpi%2Bzero%2Bw%2Bcamera%2B5mp%26_osacat%3D0%26_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3Draspberry%2Bpi%2Bzero%2Bw%2Bcamera%2B5mp%26_sacat%3D0&campid=5338610312&toolid=20008)
</td><td align="center">

[Xiaomi Dafang](https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dp2380057.m570.l1313.TR1.TRC0.A0.H0.Xxiaomi%2Bdafang.TRS0%26_nkw%3Dxiaomi%2Bdafang%26_sacat%3D0&campid=5338610312&toolid=20008)
</td></tr>

</td><td align="center"><a href="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_osacat%3D0%26_odkw%3Dxiaomi%2Bmi%2Bbox%2Bs%26_from%3DR40%26_trksid%3Dp2334524.m570.l1313.TR11.TRC1.A0.H0.Xhuawei%2Bmediapad%2Bt3.TRS0%26_nkw%3Dhuawei%2Bmediapad%2Bt3%26_sacat%3D0&campid=5338610312&toolid=20008" target="_blank"><img border="0" src="https://consumer-img.huawei.com/content/dam/huawei-cbg-site/cee-nordics/dk/mkt/pdp/tablets/mediapad-t3-10/mediapad-t3-10-dimage-0212-original.jpg" ></a><img src="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_osacat%3D0%26_odkw%3Dxiaomi%2Bmi%2Bbox%2Bs%26_from%3DR40%26_trksid%3Dp2334524.m570.l1313.TR11.TRC1.A0.H0.Xhuawei%2Bmediapad%2Bt3.TRS0%26_nkw%3Dhuawei%2Bmediapad%2Bt3%26_sacat%3D0&campid=5338610312&toolid=20008" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></a>

</td><td align="center"><a href="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_odkw%3Draspberry%2Bpi%2Bzero%2Bw%2Bcamera%2B5mp%26_osacat%3D0%26_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3Draspberry%2Bpi%2Bzero%2Bw%2Bcamera%2B5mp%26_sacat%3D0&campid=5338610312&toolid=20008" target="_blank"><img border="0" src="https://ae01.alicdn.com/kf/HTB1C.WoLpXXXXXwXXXXq6xXFXXXu/free-shipping-raspberry-pi-camera-5mp-pixels-RASPBERRY-PI-2-CAMERA.jpg" ></a><img src="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_odkw%3Draspberry%2Bpi%2Bzero%2Bw%2Bcamera%2B5mp%26_osacat%3D0%26_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3Draspberry%2Bpi%2Bzero%2Bw%2Bcamera%2B5mp%26_sacat%3D0&campid=5338610312&toolid=20008" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></a>

</td><td align="center"><a href="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dp2380057.m570.l1313.TR1.TRC0.A0.H0.Xxiaomi%2Bdafang.TRS0%26_nkw%3Dxiaomi%2Bdafang%26_sacat%3D0&campid=5338610312&toolid=20008" target="_blank"><img border="0" src="https://github.com/EliasKotlyar/Xiaomi-Dafang-Hacks/raw/master/dafang.png" ></a><img src="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dp2380057.m570.l1313.TR1.TRC0.A0.H0.Xxiaomi%2Bdafang.TRS0%26_nkw%3Dxiaomi%2Bdafang%26_sacat%3D0&campid=5338610312&toolid=20008" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></a>

<tr><td colspan="4">

Below list of accessories i use with my cameras.

**Accessories:**
<details>
  <summary>ZeroView</summary><p align="center">
  <a href=https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_osacat%3D0%26_odkw%3Draspberry%2Bpi%2Bzero%2Bw%2Bcamera%2B5mp%26_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3Dzeroview%26_sacat%3D0&campid=5338610312&toolid=20008>
  ZeroView - Window mount for Pi Zero W + Camera</a><br>
<p></details>

</td></tr>

<tr><td colspan="4">

I don't have any [Automations][automations] for my camera entities. So far i haven't found any use case for any [Automations][automations], but feel free to inspire me with some ideas.

**Automations:**
<details>
  <summary>None... But feel free to suggest some cool automations for me</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/config/config/automations/>
  None... But feel free to suggest some cool automations for me - /config/automations/</a><br>
<p></details>

</td></tr>

<tr><td colspan="4">

Below configuration on the different cameras.

**Configuration:**
<details>
  <summary>Huawei Mediapad T3 10</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/config/entities/cameras/sovevarelset.yaml>
  Huawei Mediapad T3 10 - Wallpanel</a><br>
<p></details>
<details>
  <summary>Local File</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/config/entities/cameras/gangen.yaml>
  Local file - Local image as camera</a><br>
<p></details>
<details>
  <summary>Raspberry Pi Zero W</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/config/entities/cameras/hoveddor.yaml>
  Raspberry Pi Zero W - MotionEyeOS</a><br>
<p></details>
<details>
  <summary>Xiaomi Dafang</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/config/entities/cameras/kokkenet.yaml>
  Xiaomi Dafang - Dafang Hacks</a><br>
<p></details>

</td></tr>

<tr><td colspan="4">

I don't use any NVR for my cameras. They just stream and disappears...

**NVR:**
<details>
  <summary>None... But feel free to suggest NVR</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/>
  None... But feel free to suggest NVR - /</a><br>
<p></details>

</td></tr>

<tr><td colspan="4">
  
Below you can find list of the software i'm using with my cameras.

**Software:**
<details>
  <summary>Dafang Hacks</summary><p align="center">
  <a href=https://github.com/EliasKotlyar/Xiaomi-Dafang-Hacks>
  Dafang Hacks - Alternative OS for Xiaomi Dafang</a><br>
<p></details>
<details>
  <summary>Local File</summary><p align="center">
  <a href=https://www.home-assistant.io/integrations/local_file/>
  Home Assistant Local File - Used for still image in my lovelace view ("Fake" camera view)</a><br>
<p></details>
<details>
  <summary>MotionEyeOS</summary><p align="center">
  <a href=https://github.com/ccrisan/motioneyeos/wiki>
  MotionEyeOS - OS for Raspberry Pi Zero W + Camera</a><br>
<p></details>
<details>
  <summary>Wallpanel</summary><p align="center">
  <a href=https://thanksmister.com/wallpanel-android/>
  Wallpanel - Dashboard, camera, motionsensor etc. for Android</a><br>
<p></details>

</td></tr>

<tr><td colspan="4">

</table>
</p>

<table align="center" border="0">
<tr><td colspan="4">

#### Climate <a name="climate" href="https://github.com/allanpersson/home-assistant-config#devices"><img align="right" border="0" src="https://cdn.pixabay.com/photo/2016/09/05/10/50/app-1646212_960_720.png" width="20" ></a>
</td></tr>
<tr><td align="center">

[Tado Smart Radiator Thermostat V3+](https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3Dtado%26_sacat%3D0&campid=5338610312&toolid=20008)
</td></tr>

</td><td align="center"><a href="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3Dtado%26_sacat%3D0&campid=5338610312&toolid=20008" target="_blank"><img border="0" src="https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/HMNR2?wid=1144&hei=1144&fmt=jpeg&qlt=95&op_usm=0.5,0.5&.v=1543598077883" ></a><img src="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3Dtado%26_sacat%3D0&campid=5338610312&toolid=20008" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></a>

<tr><td colspan="4">

I use alot of [Automations][automations] for controlling my thermostats for best comfort and saving most energy.

**Automations:**
<details>
  <summary>Entity update</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/config/automations/system/entity_update/climate_update.yaml>
  Entity update (Climate) - /config/automations/system/entity_update/climate_update.yaml</a><br>
<p></details>
<details>
  <summary>Away mode</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/config/automations/areas/helehuset/climate/climate_auto_away.yaml>
  Away mode - /config/automations/areas/helehuset/climate/climate_auto_away.yaml</a><br>
<p></details>
<details>
  <summary>Home mode</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/config/automations/areas/helehuset/climate/climate_auto_home.yaml>
  Home mode - /config/automations/areas/helehuset/climate/climate_auto_home.yaml</a><br>
<p></details>
<details>
  <summary>Auto off</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/config/automations/areas/helehuset/climate/climate_auto_off.yaml>
  Auto off - /config/automations/areas/helehuset/climate/climate_auto_off.yaml</a><br>
<p></details>
<details>
  <summary>Sleep mode (Night)</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/config/automations/areas/helehuset/climate/climate_auto_sleep.yaml>
  Sleep mode (Night) - /config/automations/areas/helehuset/climate/climate_auto_sleep.yaml</a><br>
<p></details>
<details>
  <summary>Windows closed</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/config/automations/areas/helehuset/climate/climate_close_windows.yaml>
  Windows closed - /config/automations/areas/helehuset/climate/climate_close_windows.yaml</a><br>
<p></details>
<details>
  <summary>Windows open</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/config/automations/areas/helehuset/climate/climate_open_windows.yaml>
  Windows open - /config/automations/areas/helehuset/climate/climate_open_windows.yaml</a><br>
<p></details>

</td></tr>

<tr><td colspan="4">

Below configuration on my radiator thermostats. It's possible to use the Tado cloud service in [Home Assistant][home-assistant] which i have done until i changed to the new option with homekit in [Home Assistant][home-assistant].

**Configuration:**
<details>
  <summary>Homekit documentation</summary><p align="center">
  <a href=https://www.home-assistant.io/integrations/homekit_controller/>
  Homekit - Documentation</a><br>
<p></details>
<details>
  <summary>Template Sensors (Climate)</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/config/entities/sensors/template/climate_template.yaml>
  Template sensors - Climate</a><br>
<p></details>

</td></tr>

<tr><td colspan="4">

</table>
</p>

<table align="center" border="0">
<tr><td colspan="4">
  
#### Covers <a name="covers" href="https://github.com/allanpersson/home-assistant-config#devices"><img align="right" border="0" src="https://cdn.pixabay.com/photo/2016/09/05/10/50/app-1646212_960_720.png" width="20" ></a>
</td></tr>
<tr><td align="center">

[Ikea Fyrtur](https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3Dikea%2Bfyrtur%26_sacat%3D0&campid=5338610312&toolid=20008)
</td></tr>

</td><td align="center"><a href="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3Dikea%2Bfyrtur%26_sacat%3D0&campid=5338610312&toolid=20008" target="_blank"><img border="0" src="https://www.ikea.com/PIAimages/0595179_PE675959_S5.JPG" ></a><img src="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3Dikea%2Bfyrtur%26_sacat%3D0&campid=5338610312&toolid=20008" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></a>

<tr><td colspan="4">

I use some [Automations][automations] for my covers, but in future i'm gonna look more into cool cover automations, maybe a "naked sensor" that rolls down the covers if your naked...

**Automations:**
<details>
  <summary>Roll down when mediaplayer (Kodi) is playing</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/config/automations/areas/stuen/cover_kodi.yaml>
  Roll down when mediaplayer (Kodi) is playing - /config/automations/areas/stuen/cover_kodi.yaml</a><br>
<p></details>
<details>
  <summary>Roll down when sunny and room is getting hot</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/config/automations/areas/stuen/cover_sunny.yaml>
  Roll down when sunny and room is getting hot - /config/automations/areas/stuen/cover_sunny.yaml</a><br>
<p></details>

</td></tr>

<tr><td colspan="4">

Below information on the gateway(s) im using for my covers. 

**Gateway:**
<details>
  <summary>Conbee II</summary><p align="center">
  <a href=https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3DConBee%2BII%26_sacat%3D0&campid=5338610312&toolid=20008>
  Conbee II - Deconz</a><br>
<p></details>

</td></tr>

<tr><td colspan="4">

I use [Scripts][scripts] to trigger my cover automations.

**Scripts:**
<details>
  <summary>Cover 0% open</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/config/scripts/cover_stuen_0_percent_open.yaml>
  Cover 0% open - /config/scripts/cover_stuen_0_percent_open.yaml</a><br>
<p></details>
<details>
  <summary>Cover 10% open</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/config/scripts/cover_stuen_10_percent_open.yaml>
  Cover 10% open - /config/scripts/cover_stuen_10_percent_open.yaml</a><br>
<p></details>
<details>
  <summary>Cover 50% open</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/config/scripts/cover_stuen_50_percent_open.yaml>
  Cover 50% open - /config/scripts/cover_stuen_50_percent_open.yaml</a><br>
<p></details>
<details>
  <summary>Cover 100% open</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/config/scripts/cover_stuen_100_percent_open.yaml>
  Cover 100% open - /config/scripts/cover_stuen_100_percent_open.yaml</a><br>
<p></details>

</td></tr>

<tr><td colspan="4">

Below some videos i have found useful myself. 

**Videos:**
<details>
  <summary>IKEA FYRTUR smart blinds unboxing and teardown</summary><p align="center">
  <a href=https://www.youtube.com/watch?v=tfJn6oNGF74>
  IKEA FYRTUR smart blinds unboxing and teardown - DIY techie</a><br>
<p></details>
<details>
  <summary>IKEA FYRTUR smart blinds hands-on installation guide + noise and speed test</summary><p align="center">
  <a href=https://www.youtube.com/watch?v=RqW6bVfrHNQ&t=57s>
  IKEA FYRTUR smart blinds hands-on installation guide + noise and speed test - DIY techie</a><br>
<p></details>
<details>
  <summary>IKEA SMART BLINDS cut to size - how to make them fit your window</summary><p align="center">
  <a href=https://www.youtube.com/watch?v=PL6LPZZoFlo>
  IKEA SMART BLINDS cut to size, how to make them fit your window - DIY techie</a><br>
<p></details>
<details>
  <summary>IKEA smart blinds with Google Assistant & IKEA app - No HomeKit or Alexa</summary><p align="center">
  <a href=https://www.youtube.com/watch?v=pe0WhThL3Eo>
  IKEA smart blinds with Google Assistant & IKEA app, No HomeKit or Alexa - DIY techie</a><br>
<p></details>
<details>
  <summary>HomeKit support for IKEA FYRTUR SMART BLINDS via Homebridge</summary><p align="center">
  <a href=https://www.youtube.com/watch?v=1l4-mtsb66A>
  HomeKit support for IKEA FYRTUR SMART BLINDS via Homebridge - DIY techie</a><br>
<p></details>

</td></tr>

</table>
</p>

<table align="center" border="0">
<tr><td colspan="4">
  
<table align="center" border="0">
<tr><td colspan="4">


#### Fans <a name="fans" href="https://github.com/allanpersson/home-assistant-config#devices"><img align="right" border="0" src="https://cdn.pixabay.com/photo/2016/09/05/10/50/app-1646212_960_720.png" width="20" ></a>
</td></tr>
<tr><td align="center">

[Table fan](https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_osacat%3D0%26_odkw%3Dfan%26_from%3DR40%26_trksid%3Dp2334524.m570.l1313.TR11.TRC1.A0.H0.Xtable%2Bfan.TRS0%26_nkw%3Dtable%2Bfan%26_sacat%3D0&campid=5338610312&toolid=20008)
</td></tr>

</td><td align="center"><a href="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_osacat%3D0%26_odkw%3Dfan%26_from%3DR40%26_trksid%3Dp2334524.m570.l1313.TR11.TRC1.A0.H0.Xtable%2Bfan.TRS0%26_nkw%3Dtable%2Bfan%26_sacat%3D0&campid=5338610312&toolid=20008" target="_blank"><img border="0" src="http://c1.peakpx.com/wallpaper/858/711/797/white-fan-objects-hardwood-wallpaper-preview.jpg" ></a><img src="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_osacat%3D0%26_odkw%3Dfan%26_from%3DR40%26_trksid%3Dp2334524.m570.l1313.TR11.TRC1.A0.H0.Xtable%2Bfan.TRS0%26_nkw%3Dtable%2Bfan%26_sacat%3D0&campid=5338610312&toolid=20008" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></a>

<tr><td colspan="4">

I don't have any [Automations][automations] for my fan(s) at the moment.

**Automations:**
<details>
  <summary>None.... Yet</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/config/automations/>
  None.... Yet</a><br>
<p></details>

</td></tr>

<tr><td colspan="4">
  
Below you can find information about my configuration.

**Configuration:**
<details>
  <summary>Fan entity (Generic_Thermostat)</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/config/entities/climate/born_fan.yaml>
  Fan entity (Generic_Thermostat)</a><br>
<p></details>

</td></tr>

<tr><td colspan="4">

</table>
</p>

<table align="center" border="0">
<tr><td colspan="4">
  
#### Hardware <a name="hardware" href="https://github.com/allanpersson/home-assistant-config#devices"><img align="right" border="0" src="https://cdn.pixabay.com/photo/2016/09/05/10/50/app-1646212_960_720.png" width="20" ></a>
</td></tr>
<tr><td align="center">

[ConBee II](https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3DConBee%2BII%26_sacat%3D0&campid=5338610312&toolid=20008)
</td><td align="center">

[INTEL® NUC KIT NUC8I3BEK](https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3DINTEL%2BNUC8I3BEK%2B%26_sacat%3D0&campid=5338610312&toolid=20008)
</td><td align="center">

[Raspberry Pi Zero W](https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dp2380057.m570.l1313.TR8.TRC2.A0.H0.XRaspberry%2BPi%2BZero%2BW.TRS0%26_nkw%3DRaspberry%2BPi%2BZero%2BW%26_sacat%3D0&campid=5338610312&toolid=20008)
</td></tr>

</td><td align="center"><a href="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3DConBee%2BII%26_sacat%3D0&campid=5338610312&toolid=20008" target="_blank"><img border="0" src="https://shop.dresden-elektronik.de/media/catalog/product/cache/3/image/9df78eab33525d08d6e5fb8d27136e95/f/r/freigestellt.png" ></a><img src="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3DConBee%2BII%26_sacat%3D0&campid=5338610312&toolid=20008" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></a>

</td><td align="center"><a href="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3DINTEL%2BNUC8I3BEK%2B%26_sacat%3D0&campid=5338610312&toolid=20008" target="_blank"><img border="0" src="https://www.intel.com/content/dam/products/hero/foreground/nuc8-i5i3-bek-front-angle.png.rendition.intel.web.978.550.png" ></a><img src="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3DINTEL%2BNUC8I3BEK%2B%26_sacat%3D0&campid=5338610312&toolid=20008" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></a>

</td><td align="center"><a href="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dp2380057.m570.l1313.TR8.TRC2.A0.H0.XRaspberry%2BPi%2BZero%2BW.TRS0%26_nkw%3DRaspberry%2BPi%2BZero%2BW%26_sacat%3D0&campid=5338610312&toolid=20008" target="_blank"><img border="0" src="https://cdn.shopify.com/s/files/1/0176/3274/products/raspberry-pi-zero-wireless-front_1024x1024.jpg?v=1542643550" ></a><img src="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dp2380057.m570.l1313.TR8.TRC2.A0.H0.XRaspberry%2BPi%2BZero%2BW.TRS0%26_nkw%3DRaspberry%2BPi%2BZero%2BW%26_sacat%3D0&campid=5338610312&toolid=20008" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></a>

<tr><td colspan="4">

Below information on the software used on/with my hardware.

**Software:**
<details>
  <summary>Deconz</summary><p align="center">
  <a href=https://www.home-assistant.io/integrations/deconz/>
  Deconz - Controlling Zigbee network</a><br>
<p></details>
<details>
  <summary>Hass.io</summary><p align="center">
  <a href=https://www.home-assistant.io/getting-started/>
  Hass.io - Flashed with etcher direct on the SSD</a><br>
<p></details>
<details>
  <summary>MotionEyeOS</summary><p align="center">
  <a href=https://github.com/ccrisan/motioneyeos/wiki>
  MotionEyeOS - OS for Raspberry Pi Zero W + Camera</a><br>
<p></details>

</td></tr>

<tr><td colspan="4">

</table>
</p>

<table align="center" border="0">
<tr><td colspan="4">


#### Lights <a name="lights" href="https://github.com/allanpersson/home-assistant-config#devices"><img align="right" border="0" src="https://cdn.pixabay.com/photo/2016/09/05/10/50/app-1646212_960_720.png" width="20" ></a>
</td></tr>
<tr><td align="center">

[Ikea Trådfri LED 600 lm](https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3Dikea%2Btr%25C3%25A5dfri%2Bled%26_sacat%3D0&campid=5338610312&toolid=20008)
</td><td align="center">

[Innr](https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_osacat%3D0%26_odkw%3Dyeelight%2Blightstrip%2Bplus%26_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3Dinnr%2Bbulb%26_sacat%3D0&campid=5338610312&toolid=20008)
</td><td align="center">
  
[Philips Hue](https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_osacat%3D0%26_odkw%3Dikea%2Btr%25C3%25A5dfri%2Bled%26_from%3DR40%26_trksid%3Dp2334524.m570.l1313.TR10.TRC2.A0.H0.Xphilips%2Bhue%2Bbulb.TRS0%26_nkw%3Dphilips%2Bhue%2Bbulb%26_sacat%3D0&campid=5338610312&toolid=20008)
</td><td align="center">

[Xiaomi Yeelight Lightstrip Plus](https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_osacat%3D0%26_odkw%3Dphilips%2Bhue%2Bbulb%26_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3Dyeelight%2Blightstrip%2Bplus%26_sacat%3D0&campid=5338610312&toolid=20008)
</td></tr>

</td><td align="center"><a href="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3Dikea%2Btr%25C3%25A5dfri%2Bled%26_sacat%3D0&campid=5338610312&toolid=20008" target="_blank"><img border="0" src="https://www.ikea.com/PIAimages/0653803_PE708096_S5.JPG?f=s" ></a><img src="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3Dikea%2Btr%25C3%25A5dfri%2Bled%26_sacat%3D0&campid=5338610312&toolid=20008" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></a>

</td><td align="center"><a href="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_osacat%3D0%26_odkw%3Dyeelight%2Blightstrip%2Bplus%26_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3Dinnr%2Bbulb%26_sacat%3D0&campid=5338610312&toolid=20008" target="_blank"><img border="0" src="https://cdn.shopify.com/s/files/1/0066/8149/3559/products/rb165_bulb_3d_1_700x700.jpg?v=1556780428" ></a><img src="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_osacat%3D0%26_odkw%3Dyeelight%2Blightstrip%2Bplus%26_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3Dinnr%2Bbulb%26_sacat%3D0&campid=5338610312&toolid=20008" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></a>

</td><td align="center"><a href="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_osacat%3D0%26_odkw%3Dikea%2Btr%25C3%25A5dfri%2Bled%26_from%3DR40%26_trksid%3Dp2334524.m570.l1313.TR10.TRC2.A0.H0.Xphilips%2Bhue%2Bbulb.TRS0%26_nkw%3Dphilips%2Bhue%2Bbulb%26_sacat%3D0&campid=5338610312&toolid=20008" target="_blank"><img border="0" src="https://brain-images-ssl.cdn.dixons.com/6/3/10160336/u_10160336.jpg" ></a><img src="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_osacat%3D0%26_odkw%3Dikea%2Btr%25C3%25A5dfri%2Bled%26_from%3DR40%26_trksid%3Dp2334524.m570.l1313.TR10.TRC2.A0.H0.Xphilips%2Bhue%2Bbulb.TRS0%26_nkw%3Dphilips%2Bhue%2Bbulb%26_sacat%3D0&campid=5338610312&toolid=20008" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></a>

</td><td align="center"><a href="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_osacat%3D0%26_odkw%3Dphilips%2Bhue%2Bbulb%26_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3Dyeelight%2Blightstrip%2Bplus%26_sacat%3D0&campid=5338610312&toolid=20008" target="_blank"><img border="0" src="https://xiaomi-store.cz/4226/xiaomi-yeelight-lightstrip-plus-extension.jpg" ></a><img src="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_osacat%3D0%26_odkw%3Dphilips%2Bhue%2Bbulb%26_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3Dyeelight%2Blightstrip%2Bplus%26_sacat%3D0&campid=5338610312&toolid=20008" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></a>

<tr><td colspan="4">

I have alot of [Automations][automations] for my lights. Actually i almost never manually or with voice activate my lights.

**Automations:**
<details>
  <summary>Lights on (Day)</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/config/automations/areas/kokkenet/kokken_lights_on_day.yaml>
  Lights on (Day) - /config/automations/areas/kokkenet/kokken_lights_on_day.yaml</a><br>
<p></details>
<details>
  <summary>Lights off (Day)</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/config/automations/areas/kokkenet/kokken_lights_off_day.yaml>
  Lights off (Day) - /config/automations/areas/kokkenet/kokken_lights_off_day.yaml</a><br>
<p></details>
<details>
  <summary>Lights on (Night)</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/config/automations/areas/kokkenet/kokken_lights_on_night.yaml>
  Lights on (Night) - /config/automations/areas/kokkenet/kokken_lights_on_night.yaml</a><br>
<p></details>
<details>
  <summary>Lights off (Night)</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/config/automations/areas/kokkenet/kokken_lights_off_night.yaml>
  Lights off (Night) - /config/automations/areas/kokkenet/kokken_lights_off_night.yaml</a><br>
<p></details>
<details>
  <summary>Lights on when lux is low, door is closed and mediaplayer is playing</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/config/automations/areas/stuen/stuen_androidtv_lights_on.yaml>
  Lights on when lux is low, door is closed and mediaplayer is playing - /config/automations/areas/stuen/stuen_androidtv_lights_on.yaml</a><br>
<p></details>
<details>
  <summary>Lights off when mediaplayer is turned off at bedtime</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/config/automations/areas/stuen/stuen_androidtv_lights_off.yaml>
  Lights off when mediaplayer is turned off at bedtime - /config/automations/areas/stuen/stuen_androidtv_lights_off.yaml</a><br>
<p></details>
<details>
  <summary>Turn off all lights and mediaplayer when not home</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/config/automations/areas/helehuset/leaving_home_turn_off.yaml>
  Turn off all lights and mediaplayer when not home - /config/automations/areas/helehuset/leaving_home_turn_off.yaml</a><br>
<p></details>

</td></tr>

<tr><td colspan="4">

Below configuration for my lights.

**Configuration:**
<details>
  <summary>Yeelight</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/config/integrations/yeelight.yaml>
  Yeelight</a><br>
<p></details>

</td></tr>

<tr><td colspan="4">
  
Below you can find information about my gateway and software used to control my lights.

**Gateway & Software:**
<details>
  <summary>Conbee II</summary><p align="center">
  <a href=https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3DConBee%2BII%26_sacat%3D0&campid=5338610312&toolid=20008>
  Conbee II - Deconz</a><br>
<p></details>
<details>
  <summary>Deconz</summary><p align="center">
  <a href=https://www.home-assistant.io/integrations/deconz/>
  Deconz - Controlling Zigbee network</a><br>
<p></details>

</td></tr>

<tr><td colspan="4">

</table>
</p>

<table align="center" border="0">
<tr><td colspan="4">

#### Locks <a name="locks" href="https://github.com/allanpersson/home-assistant-config#devices"><img align="right" border="0" src="https://cdn.pixabay.com/photo/2016/09/05/10/50/app-1646212_960_720.png" width="20" ></a>
</td></tr>
<tr><td align="center">

[Danalock V3](https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dp2380057.m570.l1313.TR11.TRC1.A0.H0.Xdanalock.TRS0%26_nkw%3Ddanalock%26_sacat%3D0&campid=5338610312&toolid=20008)
</td></tr>

</td><td align="center"><a href="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dp2380057.m570.l1313.TR11.TRC1.A0.H0.Xdanalock.TRS0%26_nkw%3Ddanalock%26_sacat%3D0&campid=5338610312&toolid=20008" target="_blank"><img border="0" src="https://images-na.ssl-images-amazon.com/images/I/71I1QvjAVIL._SL1500_.jpg" ></a><img src="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dp2380057.m570.l1313.TR11.TRC1.A0.H0.Xdanalock.TRS0%26_nkw%3Ddanalock%26_sacat%3D0&campid=5338610312&toolid=20008" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></a>


<tr><td colspan="4">

⚠️ ***I strongly advise you NOT to buy any Danalock products. The software is not working, and they don't take it serious and keeps deleting their social media profiles to make the company look better!*** ⚠️
<br><br>
I don't have any [Automations][automations] for my Danalock because i have the bluetooth only version.

**Automations:**
<details>
  <summary>None... But feel free to to suggest some for me</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/config/automations/>
  None... But feel free to to suggest some for me - /config/automations/</a><br>
<p></details>

</td></tr>

<tr><td colspan="4">

Below configuration of my locks.

**Configuration:**
<details>
  <summary>None... But would love to get my lock in Home Assistant</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/config/entities/>
  None... But would love to get my lock in Home Assistant</a><br>
<p></details>

</td></tr>

<tr><td colspan="4">

</table>
</p>

<table align="center" border="0">
<tr><td colspan="4">

#### Mediaplayers <a name="mediaplayers" href="https://github.com/allanpersson/home-assistant-config#devices"><img align="right" border="0" src="https://cdn.pixabay.com/photo/2016/09/05/10/50/app-1646212_960_720.png" width="20" ></a>
</td></tr>
<tr><td align="center">

[Google Home](https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3FBrand%3DGoogle%26LH_All%3D1%26_osacat%3D0%26_odkw%3Dgoogle%2Bhome%2Bmini%26rt%3Dnc%26_dcat%3D184435%26_from%3DR40%26_trksid%3Dp2334524.m570.l1313.TR10.TRC0.A0.H0.Xgoogle%2Bhome.TRS0%26_nkw%3Dgoogle%2Bhome%26_sacat%3D0&campid=5338610312&toolid=20008)
</td><td align="center">

[Google Home Hub](https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3FBrand%3DGoogle%26LH_All%3D1%26_osacat%3D0%26_odkw%3Dgoogle%2Bhome%26_dcat%3D184435%26rt%3Dnc%26_from%3DR40%26_trksid%3Dp2334524.m570.l1313.TR10.TRC0.A0.H0.Xgoogle%2Bhome%2Bhub.TRS0%26_nkw%3Dgoogle%2Bhome%2Bhub%26_sacat%3D0&campid=5338610312&toolid=20008)
</td><td align="center">

[Google Home Mini](https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_nkw%3Dgoogle%2Bhome%2Bmini%26_sacat%3D0%26Brand%3DGoogle%26_dcat%3D184435%26rt%3Dnc%26LH_All%3D1&campid=5338610312&toolid=20008)
</td><td align="center">

[Harman Kardon Citation 300](https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3FBrand%3DGoogle%26LH_All%3D1%26_osacat%3D0%26_odkw%3Dgoogle%2Bhome%2Bhub%26rt%3Dnc%26_dcat%3D184435%26_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3DHarman%2BKardon%2BCitation%2B300%26_sacat%3D0&campid=5338610312&toolid=20008)
</td></tr>

</td><td align="center"><a href="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3FBrand%3DGoogle%26LH_All%3D1%26_osacat%3D0%26_odkw%3Dgoogle%2Bhome%2Bmini%26rt%3Dnc%26_dcat%3D184435%26_from%3DR40%26_trksid%3Dp2334524.m570.l1313.TR10.TRC0.A0.H0.Xgoogle%2Bhome.TRS0%26_nkw%3Dgoogle%2Bhome%26_sacat%3D0&campid=5338610312&toolid=20008" target="_blank"><img border="0" src="https://lh3.googleusercontent.com/igThvoKwToXtZOfTANWbgp2ZoLnPBV2KDt9oJuaK419yIHQIo24eIcsCbgWcnfwlFjs=w1000" ></a><img src="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3FBrand%3DGoogle%26LH_All%3D1%26_osacat%3D0%26_odkw%3Dgoogle%2Bhome%2Bmini%26rt%3Dnc%26_dcat%3D184435%26_from%3DR40%26_trksid%3Dp2334524.m570.l1313.TR10.TRC0.A0.H0.Xgoogle%2Bhome.TRS0%26_nkw%3Dgoogle%2Bhome%26_sacat%3D0&campid=5338610312&toolid=20008" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></a>

</td><td align="center"><a href="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3FBrand%3DGoogle%26LH_All%3D1%26_osacat%3D0%26_odkw%3Dgoogle%2Bhome%26_dcat%3D184435%26rt%3Dnc%26_from%3DR40%26_trksid%3Dp2334524.m570.l1313.TR10.TRC0.A0.H0.Xgoogle%2Bhome%2Bhub.TRS0%26_nkw%3Dgoogle%2Bhome%2Bhub%26_sacat%3D0&campid=5338610312&toolid=20008" target="_blank"><img border="0" src="https://azcd.harveynorman.com.au/media/catalog/product/cache/21/image/992x558/9df78eab33525d08d6e5fb8d27136e95/g/h/ghh-rc2.jpg" ></a><img src="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3FBrand%3DGoogle%26LH_All%3D1%26_osacat%3D0%26_odkw%3Dgoogle%2Bhome%26_dcat%3D184435%26rt%3Dnc%26_from%3DR40%26_trksid%3Dp2334524.m570.l1313.TR10.TRC0.A0.H0.Xgoogle%2Bhome%2Bhub.TRS0%26_nkw%3Dgoogle%2Bhome%2Bhub%26_sacat%3D0&campid=5338610312&toolid=20008" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></a>

</td><td align="center"><a href="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_nkw%3Dgoogle%2Bhome%2Bmini%26_sacat%3D0%26Brand%3DGoogle%26_dcat%3D184435%26rt%3Dnc%26LH_All%3D1&campid=5338610312&toolid=20008" target="_blank"><img border="0" src="https://www.mytrendyphone.dk/images2/Google-Home-Mini-Smart-Speaker-Chalk-11052018-04-p.jpg" ></a><img src="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_nkw%3Dgoogle%2Bhome%2Bmini%26_sacat%3D0%26Brand%3DGoogle%26_dcat%3D184435%26rt%3Dnc%26LH_All%3D1&campid=5338610312&toolid=20008" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></a>

</td><td align="center"><a href="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3FBrand%3DGoogle%26LH_All%3D1%26_osacat%3D0%26_odkw%3Dgoogle%2Bhome%2Bhub%26rt%3Dnc%26_dcat%3D184435%26_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3DHarman%2BKardon%2BCitation%2B300%26_sacat%3D0&campid=5338610312&toolid=20008" target="_blank"><img border="0" src="https://cdn.webshopapp.com/shops/76048/files/220339352/harman-kardon-citation-300.jpg" ></a><img src="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3FBrand%3DGoogle%26LH_All%3D1%26_osacat%3D0%26_odkw%3Dgoogle%2Bhome%2Bhub%26rt%3Dnc%26_dcat%3D184435%26_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3DHarman%2BKardon%2BCitation%2B300%26_sacat%3D0&campid=5338610312&toolid=20008" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></a>

<tr><td colspan="4">

</td></tr>
<tr><td align="center">

[Huawei Mediapad T3 10](https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_osacat%3D0%26_odkw%3Dxiaomi%2Bmi%2Bbox%2Bs%26_from%3DR40%26_trksid%3Dp2334524.m570.l1313.TR11.TRC1.A0.H0.Xhuawei%2Bmediapad%2Bt3.TRS0%26_nkw%3Dhuawei%2Bmediapad%2Bt3%26_sacat%3D0&campid=5338610312&toolid=20008)
</td><td align="center">

[Xiaomi Mi Box S](https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_osacat%3D0%26_odkw%3DHarman%2BKardon%2BCitation%2B300%26_from%3DR40%26_trksid%3Dp2334524.m570.l1313.TR12.TRC2.A0.H0.Xxiaomi%2Bmi%2Bbox%2Bs.TRS0%26_nkw%3Dxiaomi%2Bmi%2Bbox%2Bs%26_sacat%3D0&campid=5338610312&toolid=20008)
</td></tr>

</td><td align="center"><a href="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_osacat%3D0%26_odkw%3Dxiaomi%2Bmi%2Bbox%2Bs%26_from%3DR40%26_trksid%3Dp2334524.m570.l1313.TR11.TRC1.A0.H0.Xhuawei%2Bmediapad%2Bt3.TRS0%26_nkw%3Dhuawei%2Bmediapad%2Bt3%26_sacat%3D0&campid=5338610312&toolid=20008" target="_blank"><img border="0" src="https://consumer-img.huawei.com/content/dam/huawei-cbg-site/cee-nordics/dk/mkt/pdp/tablets/mediapad-t3-10/mediapad-t3-10-dimage-0212-original.jpg" ></a><img src="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_osacat%3D0%26_odkw%3Dxiaomi%2Bmi%2Bbox%2Bs%26_from%3DR40%26_trksid%3Dp2334524.m570.l1313.TR11.TRC1.A0.H0.Xhuawei%2Bmediapad%2Bt3.TRS0%26_nkw%3Dhuawei%2Bmediapad%2Bt3%26_sacat%3D0&campid=5338610312&toolid=20008" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></a>

</td><td align="center"><a href="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_osacat%3D0%26_odkw%3DHarman%2BKardon%2BCitation%2B300%26_from%3DR40%26_trksid%3Dp2334524.m570.l1313.TR12.TRC2.A0.H0.Xxiaomi%2Bmi%2Bbox%2Bs.TRS0%26_nkw%3Dxiaomi%2Bmi%2Bbox%2Bs%26_sacat%3D0&campid=5338610312&toolid=20008" target="_blank"><img border="0" src="https://upload.wikimedia.org/wikipedia/commons/d/d1/Xiaomi_Mi_Box_S.jpg" ></a><img src="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_osacat%3D0%26_odkw%3DHarman%2BKardon%2BCitation%2B300%26_from%3DR40%26_trksid%3Dp2334524.m570.l1313.TR12.TRC2.A0.H0.Xxiaomi%2Bmi%2Bbox%2Bs.TRS0%26_nkw%3Dxiaomi%2Bmi%2Bbox%2Bs%26_sacat%3D0&campid=5338610312&toolid=20008" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></a>

<tr><td colspan="4">

I use my mediaplayers in many of my [Automations][automations] because in my use case it often define what i'm doing. I also use my mediaplayers alot for playing music and podcasts, so the volume sync is fantastic for not being annoyed with different volume level around the appartment.

**Automations:**
<details>
  <summary>Google Home volume sync</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/tree/master/config/automations/areas/helehuset/media_players_volume_sync>
  Google Home volume sync - /config/automations/areas/helehuset/media_players_volume_sync</a><br>
<p></details>
<details>
<summary>Auto light on in livingroom when lux is low and mediaplayer is 'on'</summary><p align="center">
<a href=https://github.com/allanpersson/home-assistant-config/blob/master/config/automations/areas/stuen/stuen_androidtv_lights_on.yaml>
Auto light on in livingroom when lux is low and mediaplayer is 'on' - /config/automations/areas/stuen/stuen_androidtv_lights_on.yaml</a><br>
<p></details>
<details>
<summary>Roll down Ikea Fyrtur cover when Kodi is 'on'.</summary><p align="center">
<a href=https://github.com/allanpersson/home-assistant-config/blob/master/config/automations/areas/stuen/cover_kodi.yaml>
Roll down Ikea Fyrtur cover when Kodi is 'on' - /config/automations/areas/stuen/cover_kodi.yaml</a><br>
<p></details>
<details>
<summary>Play radio in bathroom when having guests</summary><p align="center">
<a href=https://github.com/allanpersson/home-assistant-config/blob/master/config/automations/areas/badevarelset/bad_guests.yaml>
Play radio in bathroom when having guests - /config/automations/areas/badevarelset/bad_guests.yaml</a><br>
<p></details>

</td></tr>

<tr><td colspan="4">

</table>
</p>

<table align="center" border="0">
<tr><td colspan="4">

#### Sensors <a name="sensors" href="https://github.com/allanpersson/home-assistant-config#devices"><img align="right" border="0" src="https://cdn.pixabay.com/photo/2016/09/05/10/50/app-1646212_960_720.png" width="20" ></a>
</td></tr>
<tr><td align="center">

[Xiaomi BLE Temperature and Humidity sensor](https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_osacat%3D0%26_odkw%3Dxiaomi%2Bdoor%2Bwindow%2Bsensor%26_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3Dxiaomi%2Bble%2Btemperature%2Bsensor%26_sacat%3D0&campid=5338610312&toolid=20008)
</td><td align="center">

[Xiaomi ZigBee Temperature and Humidity sensor](https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_osacat%3D0%26_odkw%3Dxiaomi%2Bble%2Btemperature%2Bsensor%26_from%3DR40%26_trksid%3Dp2334524.m570.l1313.TR3.TRC2.A0.H0.Xxiaomi%2Btemperature%2Bsensor.TRS0%26_nkw%3Dxiaomi%2Btemperature%2Bsensor%26_sacat%3D0&campid=5338610312&toolid=20008)
</td><td align="center">

[Xiaomi Door and Window sensor](https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_osacat%3D0%26_odkw%3Dikea%2Btr%25C3%25A5dfri%2Bsmart%2Bplug%26_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3Dxiaomi%2Bdoor%2Bwindow%2Bsensor%26_sacat%3D0&campid=5338610312&toolid=20008)
</td></tr>


</td><td align="center"><a href="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_osacat%3D0%26_odkw%3Dxiaomi%2Bdoor%2Bwindow%2Bsensor%26_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3Dxiaomi%2Bble%2Btemperature%2Bsensor%26_sacat%3D0&campid=5338610312&toolid=20008" target="_blank"><img border="0" src="https://images-na.ssl-images-amazon.com/images/I/510hPhIkOPL._SX425_.jpg" ></a><img src="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_osacat%3D0%26_odkw%3Dxiaomi%2Bdoor%2Bwindow%2Bsensor%26_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3Dxiaomi%2Bble%2Btemperature%2Bsensor%26_sacat%3D0&campid=5338610312&toolid=20008" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></a>

</td><td align="center"><a href="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_osacat%3D0%26_odkw%3Dxiaomi%2Bble%2Btemperature%2Bsensor%26_from%3DR40%26_trksid%3Dp2334524.m570.l1313.TR3.TRC2.A0.H0.Xxiaomi%2Btemperature%2Bsensor.TRS0%26_nkw%3Dxiaomi%2Btemperature%2Bsensor%26_sacat%3D0&campid=5338610312&toolid=20008" target="_blank"><img border="0" src="https://images-na.ssl-images-amazon.com/images/I/31kV-Vk90NL._SX466_.jpg" ></a><img src="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_osacat%3D0%26_odkw%3Dxiaomi%2Bble%2Btemperature%2Bsensor%26_from%3DR40%26_trksid%3Dp2334524.m570.l1313.TR3.TRC2.A0.H0.Xxiaomi%2Btemperature%2Bsensor.TRS0%26_nkw%3Dxiaomi%2Btemperature%2Bsensor%26_sacat%3D0&campid=5338610312&toolid=20008" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></a>

</td><td align="center"><a href="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_osacat%3D0%26_odkw%3Dikea%2Btr%25C3%25A5dfri%2Bsmart%2Bplug%26_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3Dxiaomi%2Bdoor%2Bwindow%2Bsensor%26_sacat%3D0&campid=5338610312&toolid=20008" target="_blank"><img border="0" src="https://i.ebayimg.com/images/g/i88AAOSwnG1dTOpH/s-l640.jpg" ></a><img src="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_osacat%3D0%26_odkw%3Dikea%2Btr%25C3%25A5dfri%2Bsmart%2Bplug%26_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3Dxiaomi%2Bdoor%2Bwindow%2Bsensor%26_sacat%3D0&campid=5338610312&toolid=20008" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></a>

<tr><td colspan="4">

I have alot of [Automations][automations] involving my sensors. Most of them is about comfort, but one of them is about safety inspired by the Disappearance of Madeleine McCann case. The one called [Opening door notification](https://github.com/allanpersson/home-assistant-config/blob/master/config/automations/notifications/hoved_notification.yaml) which give me a instant notification if door opens on my phone and smartwatch, so i can react if my childrens or mine safety is in danger.

**Automations:**
<details>
  <summary>Opening door notification</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/config/automations/notifications/hoved_notification.yaml>
  Opening door notification - /config/automations/notifications/hoved_notification.yaml</a><br>
<p></details>
<details>
  <summary>Climate automations</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config#climate>
  Climate automations - Climate section</a><br>
<p></details>
<details>
  <summary>Cover automations</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config#covers>
  Cover automations - Cover section</a><br>
<p></details>
<details>
  <summary>Lights automations</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config#lights>
  Lights automations - Lights section</a><br>
<p></details>
<details>
  <summary>Mediaplayers automations</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config#mediaplayers>
  Mediaplayers automations - Mediaplayers section</a><br>
<p></details>
<details>
  <summary>Switches automations</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config#switches>
  Switches automations - Switches section</a><br>
<p></details>
<details>
  <summary>Vacuums automations</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config#vacuums>
  Vacuums automations - Vacuums section</a><br>
<p></details>

</td></tr>

<tr><td colspan="4">

</table>
</p>

<table align="center" border="0">
<tr><td colspan="4">

#### Smoke Detectors <a name="smokedetectors" href="https://github.com/allanpersson/home-assistant-config#devices"><img align="right" border="0" src="https://cdn.pixabay.com/photo/2016/09/05/10/50/app-1646212_960_720.png" width="20" ></a>
</td></tr>
<tr><td align="center">

[Xiaomi Mijia Honeywell](https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dp2380057.m570.l1313.TR12.TRC2.A0.H0.Xxiaomi%2Bhoneywell.TRS0%26_nkw%3Dxiaomi%2Bhoneywell%26_sacat%3D0&campid=5338610312&toolid=20008)
</td></tr>


</td><td align="center"><a href="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dp2380057.m570.l1313.TR12.TRC2.A0.H0.Xxiaomi%2Bhoneywell.TRS0%26_nkw%3Dxiaomi%2Bhoneywell%26_sacat%3D0&campid=5338610312&toolid=20008" target="_blank"><img border="0" src="https://images-na.ssl-images-amazon.com/images/I/61y8pOxMJLL._SX425_.jpg" ></a><img src="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dp2380057.m570.l1313.TR12.TRC2.A0.H0.Xxiaomi%2Bhoneywell.TRS0%26_nkw%3Dxiaomi%2Bhoneywell%26_sacat%3D0&campid=5338610312&toolid=20008" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></a>

<tr><td colspan="4">

I don't have any [Automations][automations] for my smoke detectors yet. I want to consult with a friend of mine who is firefighter to make sure the automation(s) i safe, to make sure i don't choose a color of light that makes it impossible to get out in case of fire... 

**Automations:**
<details>
  <summary>None.... Yet</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/config/automations/>
  None.... Yet</a><br>
<p></details>

</td></tr>

<tr><td colspan="4">
  
Below you can find information about my gateway and software used to control my smoke detectors.

**Gateway & Software:**
<details>
  <summary>Conbee II</summary><p align="center">
  <a href=https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3DConBee%2BII%26_sacat%3D0&campid=5338610312&toolid=20008>
  Conbee II - Deconz</a><br>
<p></details>
<details>
  <summary>Deconz</summary><p align="center">
  <a href=https://www.home-assistant.io/integrations/deconz/>
  Deconz - Controlling Zigbee network</a><br>
<p></details>

</td></tr>

<tr><td colspan="4">

</table>
</p>

<table align="center" border="0">
<tr><td colspan="4">

#### Switches <a name="switches" href="https://github.com/allanpersson/home-assistant-config#devices"><img align="right" border="0" src="https://cdn.pixabay.com/photo/2016/09/05/10/50/app-1646212_960_720.png" width="20" ></a>
</td></tr>
<tr><td align="center">

[Ikea Trådfri smart plug](https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_osacat%3D0%26_odkw%3Dtable%2Bfan%26_from%3DR40%26_trksid%3Dp2334524.m570.l1313.TR11.TRC1.A0.H0.Xikea%2Btr%25C3%25A5dfri%2Bsmart%2Bplug.TRS0%26_nkw%3Dikea%2Btr%25C3%25A5dfri%2Bsmart%2Bplug%26_sacat%3D0&campid=5338610312&toolid=20008)
</td></tr>

</td><td align="center"><a href="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_osacat%3D0%26_odkw%3Dtable%2Bfan%26_from%3DR40%26_trksid%3Dp2334524.m570.l1313.TR11.TRC1.A0.H0.Xikea%2Btr%25C3%25A5dfri%2Bsmart%2Bplug.TRS0%26_nkw%3Dikea%2Btr%25C3%25A5dfri%2Bsmart%2Bplug%26_sacat%3D0&campid=5338610312&toolid=20008" target="_blank"><img border="0" src="https://www.ikea.com/PIAimages/0515582_PE640306_S5.JPG?f=s" ></a><img src="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_osacat%3D0%26_odkw%3Dtable%2Bfan%26_from%3DR40%26_trksid%3Dp2334524.m570.l1313.TR11.TRC1.A0.H0.Xikea%2Btr%25C3%25A5dfri%2Bsmart%2Bplug.TRS0%26_nkw%3Dikea%2Btr%25C3%25A5dfri%2Bsmart%2Bplug%26_sacat%3D0&campid=5338610312&toolid=20008" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></a>

<tr><td colspan="4">

I don't have any real [Automations][automations] for my switches(s) at the moment. Exept making sure they are on at start up.

**Automations:**
<details>
  <summary>Start on start up</summary><p align="center">
  <a href=hhttps://github.com/allanpersson/home-assistant-config/blob/master/config/automations/system/start_on_startup.yaml>
  Start on start up - /config/automations/system/start_on_startup.yaml</a><br>
<p></details>

</td></tr>

<tr><td colspan="4">
  
Below you can find information about my configuration.

**Configuration:**
<details>
  <summary>Fan controlling (Generic_Thermostat)</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/#fans>
  Fan controlling (Generic_Thermostat)</a><br>
<p></details>

</td></tr>

<tr><td colspan="4">
  
Below you can find information about my gateway and software used to control my switches.

**Gateway & Software:**
<details>
  <summary>Conbee II</summary><p align="center">
  <a href=https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3DConBee%2BII%26_sacat%3D0&campid=5338610312&toolid=20008>
  Conbee II - Deconz</a><br>
<p></details>
<details>
  <summary>Deconz</summary><p align="center">
  <a href=https://www.home-assistant.io/integrations/deconz/>
  Deconz - Controlling Zigbee network</a><br>
<p></details>

</td></tr>

<tr><td colspan="4">

</table>
</p>

<table align="center" border="0">
<tr><td colspan="4">

# Vacuums

| [Xiaomi Roborock S50][xiaomiroborocks50] |
| ------------- |
| [![Xiaomi Roborock S50][img-xiaomiroborocks50]][xiaomiroborocks50] |

## Vacuums automations

I have alot of [Automations][automations] for my vacuum to help me keep my appartment clean, which can be tricky with a labrador retriever. And of course some for comfort as well.

| Name | Location |
| ------------- | ------------- |
| [Autoclean every 3.5 hours after last finish](https://github.com/allanpersson/home-assistant-config/blob/master/config/automations/areas/stuen/vacuum_autoclean.yaml) | /config/automations/areas/stuen/vacuum_autoclean.yaml |
| [Set home mode if home](https://github.com/allanpersson/home-assistant-config/blob/master/config/automations/areas/stuen/vacuum_home.yaml) | /config/automations/areas/stuen/vacuum_home.yaml |
| [Set away mode if away](https://github.com/allanpersson/home-assistant-config/blob/master/config/automations/areas/stuen/vacuum_away.yaml) | /config/automations/areas/stuen/vacuum_away.yaml |
| [Return to dock when child is going to bed](https://github.com/allanpersson/home-assistant-config/blob/master/config/automations/areas/stuen/vacuum_ea_sleep.yaml) | /config/automations/areas/stuen/vacuum_ea_sleep.yaml |

## Vacuums scripts

I have some [Scripts][scripts] for my vacuum, which i use for zoned clean up or trigger sleep mode when i go to bed late.

| Name | Location |
| ------------- | ------------- |
| [Goodnight script turn off autoclean for x hours](https://github.com/allanpersson/home-assistant-config/blob/master/config/scripts/godnat_vacuum_off.yaml) | /config/scripts/godnat_vacuum_off.yaml |
| [Zoned clean up (Livingroom)](https://github.com/allanpersson/home-assistant-config/blob/master/config/scripts/vacuum_zone_stuen.yaml) | /config/scripts/vacuum_zone_stuen.yaml |

# Lovelace Configuration ⚓

Add the following code to your lovelace configuration, and insert your own entities.

## Camera Card

Here you can find the lovelace code for [Camera card][cameracard]

## Speedtest Card

![Image](https://github.com/allanpersson/home-assistant-config/blob/master/config/www/images/themes/speedtestcard.jpg)

Here you can find the lovelace code for [Speedtest card][speedtestcard]

Requirements:

- [Mini Graph Card][minigraphcard]
- [Speedtest integration][speedtestintegration]

## Vacuum Card

Here you can find the lovelace code for [Vacuum card][vacuumcard]

# Addons 🔥

[Home Assistant][home-assistant] have an amazing [community][home-assistant-community] helping each other and building one amazing addon after another. So browse through the following places to find awesome stuff for your installation:

- Official [Home Assistant][home-assistant] website.
- [Home Assistant Community][home-assistant-community] forum.
- [Community Hass.io Add-on][hassio-addons] store by [Frenck][frenck].

Below you can find short description about some of the addons and plugins i use.

## Adguard Home

[Adguard Home][adguard-home-addon] is network-wide ads & trackers blocking DNS server.

# Seasons 🎅

Below you can find links to seasons [automations][automations] and [scrips][scripts] i use.

## Halloween 🎃

For halloween i use these:

- [Halloween automations][halloween-automations].
- [Halloween scripts][halloween-scripts].

[![Halloween video](http://img.youtube.com/vi/1hgWB6LhkBo/0.jpg)](https://www.youtube.com/watch?v=1hgWB6LhkBo "Halloween automation")

# Credits 💕

Thanks to:

## Ccostan

- [Ccostan][ccostan] for documentation inspiration.

## Frenck (Franck Nijhof)

- [Frenck][frenck] for config inspiration, and for learning me 95% of all my [Home Assistant][home-assistant] knowledge. And for your hard work and effort to the [Home Assistant][home-assistant] community you are the champ!

## Renemarc

- [Renemarc][renemarc] for documentation inspiration.

# Contact 📮

Fell free to contact me on one of the following places. And i would be happy if you follow me as well.

| [Facebook][facebook] | [Instagram][instagram] | [Twitter][twitter] | [Website][website] |
| ------------- | ------------- | ------------- | ------------- |

# Support 👍

This body runs on coffee and you can send a little love to me in the following way(s).

## Affiliate Links 🤝

By using my product links in this repo i get a small commision, and you are supporting me and encourage me to keep spending time keeping it up to date.
Affiliate partners: [Aliexpress][aliexpress] & [Ebay][ebay]

## Buy me a coffee ☕

[![Buy me a coffee][img-buymeacoffee]][buymeacoffee]

[aliexpress]: http://s.click.aliexpress.com/e/l8H1V6jQ
[allanpersson]: http://allanpersson.dk
[adguard-home-addon]: https://github.com/hassio-addons/addon-adguard-home
[automations]: https://github.com/allanpersson/home-assistant-config/tree/master/config/automations
[buymeacoffee]: https://www.buymeacoffee.com/marathonpepe
[cameracard]: https://github.com/allanpersson/home-assistant-config/blob/master/config/www/lovelace_cards/camera_card.yaml
[ccostan]: https://github.com/CCOSTAN/
[configuration-yaml]: https://github.com/allanpersson/home-assistant-config/blob/master/config/configuration.yaml
[ebay]: http://rover.ebay.com/rover/1/710-53481-19255-0/1?ff3=4&pub=5575546327&toolid=10001&campid=5338610312&customid=&mpre=http%3A%2F%2Febay.co.uk
[entities]: https://github.com/allanpersson/home-assistant-config/tree/master/config/entities
[facebook]: http://facebook.com/marathonpepe
[frenck]: http://frenck.dev
[halloween-automations]: https://github.com/allanpersson/home-assistant-config/tree/master/config/automations/seasons/halloween
[halloween-scripts]: https://github.com/allanpersson/home-assistant-config/tree/master/config/scripts/halloween
[hassio]: https://home-assistant.io/hassio/
[hassio-addons]: https://github.com/hassio-addons
[home-assistant]: https://home-assistant.io
[home-assistant-community]: https://community.home-assistant.io

[img-buymeacoffee]: https://www.buymeacoffee.com/assets/img/guidelines/download-assets-sm-2.svg

[img-ha-version]:https://img.shields.io/badge/Home_Assistant-0.104.1-53c1f1.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDEuMS8vRU4iICJodHRwOi8vd3d3LnczLm9yZy9HcmFwaGljcy9TVkcvMS4xL0RURC9zdmcxMS5kdGQiPjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxLjgsMTNIMjBWMjFIMTNWMTcuNjdMMTUuNzksMTQuODhMMTYuNSwxNUMxNy42NiwxNSAxOC42LDE0LjA2IDE4LjYsMTIuOUMxOC42LDExLjc0IDE3LjY2LDEwLjggMTYuNSwxMC44QTIuMSwyLjEgMCAwLDAgMTQuNCwxMi45TDE0LjUsMTMuNjFMMTMsMTUuMTNWOS42NUMxMy42Niw5LjI5IDE0LjEsOC42IDE0LjEsNy44QTIuMSwyLjEgMCAwLDAgMTIsNS43QTIuMSwyLjEgMCAwLDAgOS45LDcuOEM5LjksOC42IDEwLjM0LDkuMjkgMTEsOS42NVYxNS4xM0w5LjUsMTMuNjFMOS42LDEyLjlBMi4xLDIuMSAwIDAsMCA3LjUsMTAuOEEyLjEsMi4xIDAgMCwwIDUuNCwxMi45QTIuMSwyLjEgMCAwLDAgNy41LDE1TDguMjEsMTQuODhMMTEsMTcuNjdWMjFINFYxM0gyLjI1QzEuODMsMTMgMS40MiwxMyAxLjQyLDEyLjc5QzEuNDMsMTIuNTcgMS44NSwxMi4xNSAyLjI4LDExLjcyTDExLDNDMTEuMzMsMi42NyAxMS42NywyLjMzIDEyLDIuMzNDMTIuMzMsMi4zMyAxMi42NywyLjY3IDEzLDNMMTcsN1Y2SDE5VjlMMjEuNzgsMTEuNzhDMjIuMTgsMTIuMTggMjIuNTksMTIuNTkgMjIuNiwxMi44QzIyLjYsMTMgMjIuMiwxMyAyMS44LDEzTTcuNSwxMkEwLjksMC45IDAgMCwxIDguNCwxMi45QTAuOSwwLjkgMCAwLDEgNy41LDEzLjhBMC45LDAuOSAwIDAsMSA2LjYsMTIuOUEwLjksMC45IDAgMCwxIDcuNSwxMk0xNi41LDEyQzE3LDEyIDE3LjQsMTIuNCAxNy40LDEyLjlDMTcuNCwxMy40IDE3LDEzLjggMTYuNSwxMy44QTAuOSwwLjkgMCAwLDEgMTUuNiwxMi45QTAuOSwwLjkgMCAwLDEgMTYuNSwxMk0xMiw2LjlDMTIuNSw2LjkgMTIuOSw3LjMgMTIuOSw3LjhDMTIuOSw4LjMgMTIuNSw4LjcgMTIsOC43QzExLjUsOC43IDExLjEsOC4zIDExLjEsNy44QzExLjEsNy4zIDExLjUsNi45IDEyLDYuOVoiIGZpbGw9IiNmZmZmZmYiIC8+PC9zdmc+Cg==&maxAge=21600

[img-ha-android-version]:https://img.shields.io/badge/Home_Assistant_Android-Latest_Beta-53c1f1.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDEuMS8vRU4iICJodHRwOi8vd3d3LnczLm9yZy9HcmFwaGljcy9TVkcvMS4xL0RURC9zdmcxMS5kdGQiPjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxLjgsMTNIMjBWMjFIMTNWMTcuNjdMMTUuNzksMTQuODhMMTYuNSwxNUMxNy42NiwxNSAxOC42LDE0LjA2IDE4LjYsMTIuOUMxOC42LDExLjc0IDE3LjY2LDEwLjggMTYuNSwxMC44QTIuMSwyLjEgMCAwLDAgMTQuNCwxMi45TDE0LjUsMTMuNjFMMTMsMTUuMTNWOS42NUMxMy42Niw5LjI5IDE0LjEsOC42IDE0LjEsNy44QTIuMSwyLjEgMCAwLDAgMTIsNS43QTIuMSwyLjEgMCAwLDAgOS45LDcuOEM5LjksOC42IDEwLjM0LDkuMjkgMTEsOS42NVYxNS4xM0w5LjUsMTMuNjFMOS42LDEyLjlBMi4xLDIuMSAwIDAsMCA3LjUsMTAuOEEyLjEsMi4xIDAgMCwwIDUuNCwxMi45QTIuMSwyLjEgMCAwLDAgNy41LDE1TDguMjEsMTQuODhMMTEsMTcuNjdWMjFINFYxM0gyLjI1QzEuODMsMTMgMS40MiwxMyAxLjQyLDEyLjc5QzEuNDMsMTIuNTcgMS44NSwxMi4xNSAyLjI4LDExLjcyTDExLDNDMTEuMzMsMi42NyAxMS42NywyLjMzIDEyLDIuMzNDMTIuMzMsMi4zMyAxMi42NywyLjY3IDEzLDNMMTcsN1Y2SDE5VjlMMjEuNzgsMTEuNzhDMjIuMTgsMTIuMTggMjIuNTksMTIuNTkgMjIuNiwxMi44QzIyLjYsMTMgMjIuMiwxMyAyMS44LDEzTTcuNSwxMkEwLjksMC45IDAgMCwxIDguNCwxMi45QTAuOSwwLjkgMCAwLDEgNy41LDEzLjhBMC45LDAuOSAwIDAsMSA2LjYsMTIuOUEwLjksMC45IDAgMCwxIDcuNSwxMk0xNi41LDEyQzE3LDEyIDE3LjQsMTIuNCAxNy40LDEyLjlDMTcuNCwxMy40IDE3LDEzLjggMTYuNSwxMy44QTAuOSwwLjkgMCAwLDEgMTUuNiwxMi45QTAuOSwwLjkgMCAwLDEgMTYuNSwxMk0xMiw2LjlDMTIuNSw2LjkgMTIuOSw3LjMgMTIuOSw3LjhDMTIuOSw4LjMgMTIuNSw4LjcgMTIsOC43QzExLjUsOC43IDExLjEsOC4zIDExLjEsNy44QzExLjEsNy4zIDExLjUsNi45IDEyLDYuOVoiIGZpbGw9IiNmZmZmZmYiIC8+PC9zdmc+Cg==&maxAge=21600

[img-hassio]:https://img.shields.io/badge/config_for-Hass.io-53c1f1.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDEuMS8vRU4iICJodHRwOi8vd3d3LnczLm9yZy9HcmFwaGljcy9TVkcvMS4xL0RURC9zdmcxMS5kdGQiPjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEyLDE1LjVBMy41LDMuNSAwIDAsMSA4LjUsMTJBMy41LDMuNSAwIDAsMSAxMiw4LjVBMy41LDMuNSAwIDAsMSAxNS41LDEyQTMuNSwzLjUgMCAwLDEgMTIsMTUuNU0xOS40MywxMi45N0MxOS40NywxMi42NSAxOS41LDEyLjMzIDE5LjUsMTJDMTkuNSwxMS42NyAxOS40NywxMS4zNCAxOS40MywxMUwyMS41NCw5LjM3QzIxLjczLDkuMjIgMjEuNzgsOC45NSAyMS42Niw4LjczTDE5LjY2LDUuMjdDMTkuNTQsNS4wNSAxOS4yNyw0Ljk2IDE5LjA1LDUuMDVMMTYuNTYsNi4wNUMxNi4wNCw1LjY2IDE1LjUsNS4zMiAxNC44Nyw1LjA3TDE0LjUsMi40MkMxNC40NiwyLjE4IDE0LjI1LDIgMTQsMkgxMEM5Ljc1LDIgOS41NCwyLjE4IDkuNSwyLjQyTDkuMTMsNS4wN0M4LjUsNS4zMiA3Ljk2LDUuNjYgNy40NCw2LjA1TDQuOTUsNS4wNUM0LjczLDQuOTYgNC40Niw1LjA1IDQuMzQsNS4yN0wyLjM0LDguNzNDMi4yMSw4Ljk1IDIuMjcsOS4yMiAyLjQ2LDkuMzdMNC41NywxMUM0LjUzLDExLjM0IDQuNSwxMS42NyA0LjUsMTJDNC41LDEyLjMzIDQuNTMsMTIuNjUgNC41NywxMi45N0wyLjQ2LDE0LjYzQzIuMjcsMTQuNzggMi4yMSwxNS4wNSAyLjM0LDE1LjI3TDQuMzQsMTguNzNDNC40NiwxOC45NSA0LjczLDE5LjAzIDQuOTUsMTguOTVMNy40NCwxNy45NEM3Ljk2LDE4LjM0IDguNSwxOC42OCA5LjEzLDE4LjkzTDkuNSwyMS41OEM5LjU0LDIxLjgyIDkuNzUsMjIgMTAsMjJIMTRDMTQuMjUsMjIgMTQuNDYsMjEuODIgMTQuNSwyMS41OEwxNC44NywxOC45M0MxNS41LDE4LjY3IDE2LjA0LDE4LjM0IDE2LjU2LDE3Ljk0TDE5LjA1LDE4Ljk1QzE5LjI3LDE5LjAzIDE5LjU0LDE4Ljk1IDE5LjY2LDE4LjczTDIxLjY2LDE1LjI3QzIxLjc4LDE1LjA1IDIxLjczLDE0Ljc4IDIxLjU0LDE0LjYzTDE5LjQzLDEyLjk3WiIgZmlsbD0iI2ZmZmZmZiIgLz48L3N2Zz4K&maxAge=86400

[img-issues]: https://img.shields.io/github/issues/allanpersson/home-assistant-config
[img-last-commit]: https://img.shields.io/github/last-commit/allanpersson/home-assistant-config/master
[img-license]: https://img.shields.io/github/license/allanpersson/home-assistant-config

[img-price]:https://img.shields.io/badge/price-FREE-53c1f1.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDEuMS8vRU4iICJodHRwOi8vd3d3LnczLm9yZy9HcmFwaGljcy9TVkcvMS4xL0RURC9zdmcxMS5kdGQiPjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTcsMTVIOUM5LDE2LjA4IDEwLjM3LDE3IDEyLDE3QzEzLjYzLDE3IDE1LDE2LjA4IDE1LDE1QzE1LDEzLjkgMTMuOTYsMTMuNSAxMS43NiwxMi45N0M5LjY0LDEyLjQ0IDcsMTEuNzggNyw5QzcsNy4yMSA4LjQ3LDUuNjkgMTAuNSw1LjE4VjNIMTMuNVY1LjE4QzE1LjUzLDUuNjkgMTcsNy4yMSAxNyw5SDE1QzE1LDcuOTIgMTMuNjMsNyAxMiw3QzEwLjM3LDcgOSw3LjkyIDksOUM5LDEwLjEgMTAuMDQsMTAuNSAxMi4yNCwxMS4wM0MxNC4zNiwxMS41NiAxNywxMi4yMiAxNywxNUMxNywxNi43OSAxNS41MywxOC4zMSAxMy41LDE4LjgyVjIxSDEwLjVWMTguODJDOC40NywxOC4zMSA3LDE2Ljc5IDcsMTVaIiBmaWxsPSIjZmZmIiAvPjwvc3ZnPgo=&maxAge=86400

[img-release]: https://img.shields.io/github/release/allanpersson/home-assistant-config/all.svg?logo=github&logoColor=white&maxAge=21600

[img-xiaomiroborocks50]: https://sc02.alicdn.com/kf/HTB11hAzm0fJ8KJjy0Feq6xKEXXaQ/Global-Version-XIAOMI-Roborock-S50-MI-Robot.jpg_350x350.jpg
[instagram]: http://instagram.com/marathonpepe
[integrations]: https://github.com/allanpersson/home-assistant-config/tree/master/config/integrations
[intelnuc]: https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3DINTEL%2BNUC8I3BEK%2B%26_sacat%3D0&campid=5338610312&toolid=20008
[issues]: https://github.com/allanpersson/home-assistant-config/issues
[link-board]: https://github.com/allanpersson/home-assistant-config/projects/1
[link-ha-version]: https://github.com/home-assistant/home-assistant/tree/0.104.1
[link-ha-android-version]: https://github.com/home-assistant/home-assistant-android
[link-hassio]: https://home-assistant.io/hassio/
[link-issues]: https://github.com/allanpersson/home-assistant-config/issues
[link-license]: https://github.com/allanpersson/home-assistant-config/blob/master/LICENSE.txt
[link-repo]: https://github.com/allanpersson/home-assistant-config
[minigraphcard]: https://github.com/kalkih/mini-graph-card
[renemarc]: https://github.com/renemarc/
[scripts]: https://github.com/allanpersson/home-assistant-config/tree/master/config/scripts
[speedtestcard]: https://github.com/allanpersson/home-assistant-config/blob/master/config/www/lovelace_cards/speedtest_card.yaml
[speedtestintegration]: https://www.home-assistant.io/integrations/speedtestdotnet/
[theme]: https://github.com/allanpersson/home-assistant-config/blob/master/config/themes/material_dark_theme_custom.yam
[twitter]: http://twitter.com/marathonpepe
[vacuumcard]: https://github.com/allanpersson/home-assistant-config/blob/master/config/www/lovelace_cards/vacuum_card.yaml
[website]: http://marathonpepe.dk
[xiaomiroborocks50]: https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dp2380057.m570.l1313.TR11.TRC1.A0.H0.Xxiaomi%2Broborock%2Bs50.TRS0%26_nkw%3Dxiaomi%2Broborock%2Bs50%26_sacat%3D0&campid=5338610312&toolid=20008
