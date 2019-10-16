[![Last commit][img-last-commit]][link-repo]
[![Price][img-price]][link-license]
[![License][img-license]][link-license]
[![Home Assistant version][img-ha-version]][link-ha-version]
[![Hass.io][img-hassio]][link-hassio]
<a href="https://www.buymeacoffee.com/marathonpepe" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 10px !important;width: 40px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>


<h1 align="center">
  🏰<br/>Home Assistant configuration</sub></sup>
</h1>
<h2 align="center">
 ...for making my life easier... Hopefully 🙈<br/> <sup><sub>by <a href="http://marathonpepe.dk">Allan Persson</a> 😈</sub></sup>
</h2>


## Table of contents 📑
1. **[Overview](#overview-)**\
    [Code](#code-) | [Description](#description-) | [PRs](#prs-) | [Screenshots](#screenshots-) | [Theme](#theme-)
2. **[Devices](#devices-)**\
    [Cameras](#cameras) | [Climate](#climate) | [Covers](#covers) | [Fans](#fans) | [Hardware](#hardware) | [Lights](#lights) | [Locks](#locks) | [Mediaplayers](#mediaplayers) | [Sensors](#sensors) | [Smoke Detectors](#smokedetectors) | [Switches](#switches) | [Vacuums](#vacuums)
3. **[Lovelace Configuration](#Lovelace-configuration-)**\
    [Camera View](#camera-view-) | [Vacuum Card](#vacuum-card-)
4. **[Credits](#credits-)**
5. **[Contact](#contact-)**
6. **[Support](#support-)**



## Overview 📇
⚠ ***Documentation is currently work in progress*** ⚠ 


## Code ⌨
Let me be clear from the start; I'm not a great coder in any way!
I don't feel the excitement from putting some code together, but i have the higest respect and admiration for people who finds joy in it and are good at it. **You make my life easier ❤️**

So you might experience my code is 'ugly' and you are probably right, i find joy in making things work as i want it to. In coding there is frontend and backend coders, i'm the **userfriendliness and comfort guy** 😛



## Description 📜
Configuration for [Home Assistant](https://home-assistant.io/) running [Hass.io](https://home-assistant.io/hassio/) on a [INTEL® NUC KIT NUC8I3BEK](https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dm570.l1313%26_nkw%3DINTEL%2BNUC8I3BEK%2B%26_sacat%3D0&campid=5338610312&toolid=20008) for a two bedroom apartment (66m2).

I use `packages "configuration"` introduced by [Frenck](https://github.com/frenck/). 

That means my [configuration.yaml](https://github.com/allanpersson/home-assistant-config/blob/master/configuration.yaml) points to the folder [integrations](https://github.com/allanpersson/home-assistant-config/tree/master/integrations), and the files in my [integrations](https://github.com/allanpersson/home-assistant-config/tree/master/integrations) folder is pointing to the [entities](https://github.com/allanpersson/home-assistant-config/tree/master/entities) folder where every entity has it's own file sorted by type.



## PRs 📝
You are more than welcome to submit PRs to my repo. This repo and documentation is "quite big" to keep up to date but i try my best! 
Your help is much appreciated on my code, broken links, typos etc.



## Screenshots 📷
![Image](https://github.com/allanpersson/home-assistant-config/blob/master/www/images/themes/material_dark_theme_custom_preview.png)



## Theme 🌅
The theme i use (screenshot images) is [Material Dark Theme](https://github.com/allanpersson/home-assistant-config/blob/master/themes/material_dark_theme_custom.yaml) with some minor tweaks made by me like rounded corners, color changes etc.

**Automations:**
- [Default theme](https://github.com/allanpersson/home-assistant-config/blob/master/automations/system/default_theme.yaml)



## Devices 🌅
<a name="devices"></a>
<div align="center">
  <h4>
    <a href="https://github.com/allanpersson/home-assistant-config#cameras">
      Cameras
    </a>
    <span> | </span>
    <a href="https://github.com/allanpersson/home-assistant-config#climate">
      Climate
    </a>
    <span> | </span>
    <a href="https://github.com/allanpersson/home-assistant-config#covers">
      Covers
    </a>
    <span> | </span>
    <a href="https://github.com/allanpersson/home-assistant-config#fans">
      Fans
    </a>
    <span> | </span>
    <a href="https://github.com/allanpersson/home-assistant-config#hardware">
      Hardware
    </a>
    <span> | </span>
    <a href="https://github.com/allanpersson/home-assistant-config#lights">
      Lights
    </a>
    <span> | </span>
    <a href="https://github.com/allanpersson/home-assistant-config#locks">
      Locks
    </a>
    <span> | </span>
    <a href="https://github.com/allanpersson/home-assistant-config#mediaplayers">
      Mediaplayers
    </a>
    <span> | </span>
    <a href="https://github.com/allanpersson/home-assistant-config#sensors">
      Sensors
    </a>
    <span> | </span>
    <a href="https://github.com/allanpersson/home-assistant-config#smokedetectors">
      Smoke Detectors
    </a>
    <span> | </span>
    <a href="https://github.com/allanpersson/home-assistant-config#switches">
      Switches
    </a>
    <span> | </span>
    <a href="https://github.com/allanpersson/home-assistant-config#vacuums">
      Vacuums
    </a>
  </h4>
</div>



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

I don't have any [Automations](https://github.com/allanpersson/home-assistant-config/tree/master/automations) for my camera entities. So far i haven't found any use case for any automations, but feel free to inspire me with some ideas.

**Automations:**
<details>
  <summary>None... But feel free to suggest some cool automations for me</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/automations/>
  None... But feel free to suggest some cool automations for me - /automations/</a><br>
<p></details>

</td></tr>



<tr><td colspan="4">

Below configuration on the different cameras. 

**Configuration:**
<details>
  <summary>Huawei Mediapad T3 10</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/entities/cameras/sovevarelset.yaml>
  Huawei Mediapad T3 10 - Wallpanel</a><br>
<p></details>
<details>
  <summary>Local File</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/entities/cameras/gangen.yaml>
  Local file - Local image as camera</a><br>
<p></details>
<details>
  <summary>Raspberry Pi Zero W</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/entities/cameras/hoveddor.yaml>
  Raspberry Pi Zero W - MotionEyeOS</a><br>
<p></details>
<details>
  <summary>Xiaomi Dafang</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/entities/cameras/kokkenet.yaml>
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

I use alot of [Automations](https://github.com/allanpersson/home-assistant-config/tree/master/automations) for controlling my thermostats for best comfort and saving most energy.

**Automations:**
<details>
  <summary>Entity update</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/automations/system/entity_update/climate_update.yaml>
  Entity update (Climate) - /automations/system/entity_update/climate_update.yaml</a><br>
<p></details>
<details>
  <summary>Away mode</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/automations/areas/helehuset/climate/climate_auto_away.yaml>
  Away mode - /automations/areas/helehuset/climate/climate_auto_away.yaml</a><br>
<p></details>
<details>
  <summary>Home mode</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/automations/areas/helehuset/climate/climate_auto_home.yaml>
  Home mode - /automations/areas/helehuset/climate/climate_auto_home.yaml</a><br>
<p></details>
<details>
  <summary>Auto off</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/automations/areas/helehuset/climate/climate_auto_off.yaml>
  Auto off - /automations/areas/helehuset/climate/climate_auto_off.yaml</a><br>
<p></details>
<details>
  <summary>Sleep mode (Night)</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/automations/areas/helehuset/climate/climate_auto_sleep.yaml>
  Sleep mode (Night) - /automations/areas/helehuset/climate/climate_auto_sleep.yaml</a><br>
<p></details>
<details>
  <summary>Windows closed</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/automations/areas/helehuset/climate/climate_close_windows.yaml>
  Windows closed - /automations/areas/helehuset/climate/climate_close_windows.yaml</a><br>
<p></details>
<details>
  <summary>Windows open</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/automations/areas/helehuset/climate/climate_open_windows.yaml>
  Windows open - /automations/areas/helehuset/climate/climate_open_windows.yaml</a><br>
<p></details>

</td></tr>



<tr><td colspan="4">

Below configuration on my radiator thermostats. It's possible to use the Tado cloud service in [Home Assistant](https://home-assistant.io/) which i have done until i changed to the new option with homekit in [Home Assistant](https://home-assistant.io/).

**Configuration:**
<details>
  <summary>Homekit documentation</summary><p align="center">
  <a href=https://www.home-assistant.io/integrations/homekit_controller/>
  Homekit - Documentation</a><br>
<p></details>
<details>
  <summary>Template Sensors (Climate)</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/entities/sensors/template/climate_template.yaml>
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

I use some [Automations](https://github.com/allanpersson/home-assistant-config/tree/master/automations) for my covers, but in future i'm gonna look more into cool cover automations, maybe a "naked sensor" that rolls down the covers if your naked...

**Automations:**
<details>
  <summary>Roll down when mediaplayer (Kodi) is playing</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/automations/areas/stuen/cover_kodi.yaml>
  Roll down when mediaplayer (Kodi) is playing - /automations/areas/stuen/cover_kodi.yaml</a><br>
<p></details>
<details>
  <summary>Roll down when sunny and room is getting hot</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/automations/areas/stuen/cover_sunny.yaml>
  Roll down when sunny and room is getting hot - /automations/areas/stuen/cover_sunny.yaml</a><br>
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

I use scripts to trigger my cover automations.

**Scripts:**
<details>
  <summary>Cover 0% open</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/scripts/cover_stuen_0_percent_open.yaml>
  Cover 0% open - /scripts/cover_stuen_0_percent_open.yaml</a><br>
<p></details>
<details>
  <summary>Cover 10% open</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/scripts/cover_stuen_10_percent_open.yaml>
  Cover 10% open - /scripts/cover_stuen_10_percent_open.yaml</a><br>
<p></details>
<details>
  <summary>Cover 50% open</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/scripts/cover_stuen_50_percent_open.yaml>
  Cover 50% open - /scripts/cover_stuen_50_percent_open.yaml</a><br>
<p></details>
<details>
  <summary>Cover 100% open</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/scripts/cover_stuen_100_percent_open.yaml>
  Cover 100% open - /scripts/cover_stuen_100_percent_open.yaml</a><br>
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

I have alot of [Automations](https://github.com/allanpersson/home-assistant-config/tree/master/automations) for my lights. Actually i almost never manually or with voice activate my lights. 

**Automations:**
<details>
  <summary>Lights on (Day)</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/automations/areas/kokkenet/kokken_lights_on_day.yaml>
  Lights on (Day) - /automations/areas/kokkenet/kokken_lights_on_day.yaml</a><br>
<p></details>
<details>
  <summary>Lights off (Day)</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/automations/areas/kokkenet/kokken_lights_off_day.yaml>
  Lights off (Day) - /automations/areas/kokkenet/kokken_lights_off_day.yaml</a><br>
<p></details>
<details>
  <summary>Lights on (Night)</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/automations/areas/kokkenet/kokken_lights_on_night.yaml>
  Lights on (Night) - /automations/areas/kokkenet/kokken_lights_on_night.yaml</a><br>
<p></details>
<details>
  <summary>Lights off (Night)</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/automations/areas/kokkenet/kokken_lights_off_night.yaml>
  Lights off (Night) - /automations/areas/kokkenet/kokken_lights_off_night.yaml</a><br>
<p></details>
<details>
  <summary>Lights on when lux is low, door is closed and mediaplayer is playing</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/automations/areas/stuen/stuen_androidtv_lights_on.yaml>
  Lights on when lux is low, door is closed and mediaplayer is playing - /automations/areas/stuen/stuen_androidtv_lights_on.yaml</a><br>
<p></details>
<details>
  <summary>Lights off when mediaplayer is turned off at bedtime</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/automations/areas/stuen/stuen_androidtv_lights_off.yaml>
  Lights off when mediaplayer is turned off at bedtime - /automations/areas/stuen/stuen_androidtv_lights_off.yaml</a><br>
<p></details>
<details>
  <summary>Turn off all lights and mediaplayer when not home</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/automations/areas/helehuset/leaving_home_turn_off.yaml>
  Turn off all lights and mediaplayer when not home - /automations/areas/helehuset/leaving_home_turn_off.yaml</a><br>
<p></details>

</td></tr>






<tr><td colspan="4">

Below configuration for my lights. 

**Configuration:**
<details>
  <summary>Yeelight</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/integrations/yeelight.yaml>
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
I don't have any [Automations](https://github.com/allanpersson/home-assistant-config/tree/master/automations) for my Danalock because i have the bluetooth only version.

**Automations:**
<details>
  <summary>None... But feel free to to suggest some for me</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/automations/>
  None... But feel free to to suggest some for me - /automations/</a><br>
<p></details>

</td></tr>



<tr><td colspan="4">

Below configuration of my locks.

**Configuration:**
<details>
  <summary>None... But would love to get my lock in Home Assistant</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/entities/>
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

I use my mediaplayers in many of my [Automations](https://github.com/allanpersson/home-assistant-config/tree/master/automations) because in my use case it often define what i'm doing. I also use my mediaplayers alot for playing music and podcasts, so the volume sync is fantastic for not being annoyed with different volume level around the appartment.

**Automations:**
<details>
  <summary>Google Home volume sync</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/tree/master/automations/areas/helehuset/media_players_volume_sync>
  Google Home volume sync - /automations/areas/helehuset/media_players_volume_sync</a><br>
<p></details>
<details>
<summary>Auto light on in livingroom when lux is low and mediaplayer is 'on'</summary><p align="center">
<a href=https://github.com/allanpersson/home-assistant-config/blob/master/automations/areas/stuen/stuen_androidtv_lights_on.yaml>
Auto light on in livingroom when lux is low and mediaplayer is 'on' - /automations/areas/stuen/stuen_androidtv_lights_on.yaml</a><br>
<p></details>
<details>
<summary>Roll down Ikea Fyrtur cover when Kodi is 'on'.</summary><p align="center">
<a href=https://github.com/allanpersson/home-assistant-config/blob/master/automations/areas/stuen/cover_kodi.yaml>
Roll down Ikea Fyrtur cover when Kodi is 'on' - /automations/areas/stuen/cover_kodi.yaml</a><br>
<p></details>
<details>
<summary>Play radio in bathroom when having guests</summary><p align="center">
<a href=https://github.com/allanpersson/home-assistant-config/blob/master/automations/areas/badevarelset/bad_radio_on_guests.yaml>
Play radio in bathroom when having guests - /automations/areas/badevarelset/bad_radio_on_guests.yaml</a><br>
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

I don't have any [Automations](https://github.com/allanpersson/home-assistant-config/tree/master/automations) for my smoke detectors yet. I want to consult with a friend of mine who is firefighter to make sure the automation(s) i safe, to make sure i don't choose a color of light that makes it impossible to get out in case of fire... 

**Automations:**
<details>
  <summary>None.... Yet</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/automations/>
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

#### Vacuums <a name="vacuums" href="https://github.com/allanpersson/home-assistant-config#devices"><img align="right" border="0" src="https://cdn.pixabay.com/photo/2016/09/05/10/50/app-1646212_960_720.png" width="20" ></a>
</td></tr>
<tr><td align="center">

[Xiaomi Roborock S50](https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dp2380057.m570.l1313.TR11.TRC1.A0.H0.Xxiaomi%2Broborock%2Bs50.TRS0%26_nkw%3Dxiaomi%2Broborock%2Bs50%26_sacat%3D0&campid=5338610312&toolid=20008)
</td></tr>

</td><td align="center"><a href="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dp2380057.m570.l1313.TR11.TRC1.A0.H0.Xxiaomi%2Broborock%2Bs50.TRS0%26_nkw%3Dxiaomi%2Broborock%2Bs50%26_sacat%3D0&campid=5338610312&toolid=20008" target="_blank"><img border="0" src="https://sc02.alicdn.com/kf/HTB11hAzm0fJ8KJjy0Feq6xKEXXaQ/Global-Version-XIAOMI-Roborock-S50-MI-Robot.jpg_350x350.jpg" ></a><img src="https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dp2380057.m570.l1313.TR11.TRC1.A0.H0.Xxiaomi%2Broborock%2Bs50.TRS0%26_nkw%3Dxiaomi%2Broborock%2Bs50%26_sacat%3D0&campid=5338610312&toolid=20008" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></a>

<tr><td colspan="4">

I have alot of [Automations](https://github.com/allanpersson/home-assistant-config/tree/master/automations) for my vacuum to help me keep my appartment clean, which can be tricky with a labrador retriever. And of course some for comfort as well. 

**Automations:**
<details>
  <summary>Autoclean every 3.5 hours after last finish</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/automations/areas/stuen/vacuum_autoclean.yaml>
  Autoclean every 3.5 hours after last finish - /automations/areas/stuen/vacuum_autoclean.yaml</a><br>
<p></details>
<details>
<summary>Set home mode if home</summary><p align="center">
<a href=https://github.com/allanpersson/home-assistant-config/blob/master/automations/areas/stuen/vacuum_home.yaml>
Set home mode if home - /automations/areas/stuen/vacuum_home.yaml</a><br>
<p></details>
<details>
<summary>Set away mode if away</summary><p align="center">
<a href=https://github.com/allanpersson/home-assistant-config/blob/master/automations/areas/stuen/vacuum_away.yaml>
Set away mode if away - /automations/areas/stuen/vacuum_away.yaml</a><br>
<p></details>
<details>
<summary>Return to dock when child is going to bed</summary><p align="center">
<a href=https://github.com/allanpersson/home-assistant-config/blob/master/automations/areas/stuen/vacuum_ea_sleep.yaml>
Return to dock when child is going to bed - /automations/areas/stuen/vacuum_ea_sleep.yaml</a><br>
<p></details>

</td></tr>

<tr><td colspan="4">
  
  
I have some [Scripts](https://github.com/allanpersson/home-assistant-config/tree/master/scripts) for my vacuum, which i use for zoned clean up or trigger sleep mode when i go to bed late. 

**Scripts:**
<details>
  <summary>Goodnight script turn off autoclean for 9 hours</summary><p align="center">
  <a href=https://github.com/allanpersson/home-assistant-config/blob/master/scripts/godnat_vacuum_off.yaml>
  Goodnight script turn off autoclean for 9 hours - /scripts/godnat_vacuum_off.yaml</a><br>
<p></details>
<details>
<summary>Zoned clean up (Livingroom)</summary><p align="center">
<a href=https://github.com/allanpersson/home-assistant-config/blob/master/scripts/vacuum_zone_stuen.yaml>
Zoned clean up (Livingroom) - /scripts/vacuum_zone_stuen.yaml</a><br>
<p></details>

</td></tr>

<tr><td colspan="4">

</table>
</p>



## Lovelace Configuration 🌅
Add the following code to your lovelace configuration, and insert your own entities.

## Camera View 🌅
```yaml
# Example "stue" camera lovelace view
aspect_ratio: 16x11
camera_image: camera.stuen
entities:
  - group.stuen_windows
  - light.stuen
  - binary_sensor.motion_stuen
  - climate.stuen
  - sensor.stuen_temperature
  - sensor.motion_stuen_2
  - sensor.stuen_humidity
  - binary_sensor.fire_stuen
title: Stue
type: picture-glance
```

## Vacuum Card 🌅
```yaml
# Example Xiaomi Roborock vacuum card
cards:
  - aspect_ratio: 16x9
    elements:
      - entity: vacuum.james
        icon: 'mdi:bell-ring'
        style:
          color: '#3090C7'
          left: 80%
          top: 90%
        tap_action:
          action: call-service
          entity: vacuum.james
          service: vacuum.locate
        type: icon
      - entity: vacuum.james
        icon: 'mdi:crosshairs'
        style:
          color: '#3090C7'
          left: 65%
          top: 90%
        tap_action:
          action: call-service
          entity: vacuum.james
          service: vacuum.clean_spot
        type: icon
      - entity: vacuum.james
        icon: 'mdi:home'
        style:
          color: '#3090C7'
          left: 50%
          top: 90%
        tap_action:
          action: call-service
          entity: vacuum.james
          service: vacuum.return_to_base
        type: icon
      - entity: vacuum.james
        icon: 'mdi:stop'
        style:
          color: '#3090C7'
          left: 35%
          top: 90%
        tap_action:
          action: call-service
          entity: vacuum.james
          service: vacuum.stop
        type: icon
      - entity: vacuum.james
        icon: 'mdi:play'
        style:
          color: '#3090C7'
          left: 20%
          top: 90%
        tap_action:
          action: call-service
          entity: vacuum.james
          service: vacuum.start
        type: icon
      - entity: sensor.vacuum_operation
        style:
          background-color: '#3090C7'
          border-color: 'rgb(34, 154, 210)'
          border-radius: 20px
          color: 'rgb(255, 255, 255)'
          font-family: Trebuchet MS
          font-size: 70%
          font-weight: bold
          left: 1%
          pointer-events: none
          top: 20%
          transform: 'translate(0%,-50%)'
        type: state-label
      - entity: sensor.vacuum_accessories
        style:
          background-color: '#3090C7'
          border-color: 'rgb(34, 154, 210)'
          border-radius: 20px
          color: 'rgb(255, 255, 255)'
          font-family: Trebuchet MS
          font-size: 70%
          font-weight: bold
          pointer-events: none
          right: 1%
          top: 20%
          transform: 'translate(0%,-50%)'
        type: state-label
      - entity: vacuum.james
        icon: 'mdi:robot-vacuum'
        style:
          background-color: '#cccccc'
          border-color: 'rgb(34, 154, 210)'
          border-radius: 80px
          color: 'rgb(255, 255, 255)'
          font-family: Trebuchet MS
          font-size: 150%
          font-weight: bold
          left: 45%
          top: 10%
          transform: 'translate(0%,-50%)'
        tap_action:
          action: more-info
          entity: vacuum.james
        type: icon
      - entity: sensor.vacuum_cleanmainbrush
        style:
          border-color: 'rgb(34, 154, 210)'
          border-right-style: solid
          color: '#ffffff'
          font-family: Trebuchet MS
          font-size: 76%
          font-weight: bold
          pointer-events: none
          right: 1%
          top: 35%
          transform: 'translate(0%,-50%)'
        type: state-label
      - entity: sensor.vacuum_cleansidebrush
        style:
          border-color: 'rgb(34, 154, 210)'
          border-right-style: solid
          color: '#ffffff'
          font-family: Trebuchet MS
          font-size: 76%
          font-weight: bold
          pointer-events: none
          right: 1%
          top: 45%
          transform: 'translate(0%,-50%)'
        type: state-label
      - entity: sensor.vacuum_cleanfilter
        style:
          border-color: 'rgb(34, 154, 210)'
          border-right-style: solid
          color: '#ffffff'
          font-family: Trebuchet MS
          font-size: 76%
          font-weight: bold
          opacity: 0.8
          pointer-events: none
          right: 1%
          top: 55%
          transform: 'translate(0%,-50%)'
        type: state-label
      - entity: sensor.vacuum_sensordirtyleft
        style:
          border-color: 'rgb(34, 154, 210)'
          border-right-style: solid
          color: '#ffffff'
          font-family: Trebuchet MS
          font-size: 76%
          font-weight: bold
          pointer-events: none
          right: 1%
          top: 65%
          transform: 'translate(0%,-50%)'
        type: state-label
      - entity: vacuum.james
        style:
          border-color: '#3090C7'
          border-left-style: solid
          color: '#ffffff'
          font-family: Trebuchet MS
          font-size: 76%
          font-weight: bold
          left: 1%
          pointer-events: none
          top: 35%
          transform: 'translate(0%,-50%)'
        type: state-label
      - entity: sensor.vacuum_status
        style:
          border-color: '#3090C7'
          border-left-style: solid
          color: '#ffffff'
          font-family: Trebuchet MS
          font-size: 76%
          font-weight: bold
          left: 1%
          pointer-events: none
          top: 45%
          transform: 'translate(0%,-50%)'
        type: state-label
      - entity: sensor.vacuum_battery
        style:
          border-color: 'rgb(34, 154, 210)'
          border-left-style: solid
          color: '#ffffff'
          font-family: Trebuchet MS
          font-size: 75%
          font-weight: bold
          left: 1%
          pointer-events: none
          top: 55%
          transform: 'translate(0%,-50%)'
        type: state-label
      - entity: sensor.vacuum_fan_speed
        style:
          border-color: 'rgb(34, 154, 210)'
          border-left-style: solid
          color: '#ffffff'
          font-family: Trebuchet MS
          font-size: 75%
          font-weight: bold
          left: 1%
          pointer-events: none
          top: 65%
          transform: 'translate(0%,-50%)'
        type: state-label
      - entity: sensor.vacuum_cleaned_area
        prefix: 'Area:'
        style:
          color: '#84a6ba'
          font-family: Trebuchet MS
          font-size: 80%
          font-weight: bold
          left: 31%
          pointer-events: none
          top: 79%
          transform: 'translate(0%,-50%)'
        type: state-label
      - entity: sensor.vacuum_cleaning_time
        prefix: 'Time:'
        style:
          color: '#84a6ba'
          font-family: Trebuchet MS
          font-size: 80%
          font-weight: bold
          left: 51%
          pointer-events: none
          top: 79%
          transform: 'translate(0%,-50%)'
        type: state-label
    image: /local/images/things/vacuum1.jpg
    type: picture-elements
type: 'custom:vertical-stack-in-card'
```



# Credits ✋
Thanks to:
- [Ccostan](https://github.com/CCOSTAN/) for documentation inspiration.
- [Frenck](https://github.com/frenck/) for config inspiration, and for your hard work and effort to the [Home Assistant](https://github.com/home-assistant) community.
- [Renemarc](https://github.com/renemarc/) for documentation inspiration.



# Contact 📮
Fell free to follow and/or contact me on:
[Facebook](http://facebook.com/marathonpepe) │ [Instagram](http://instagram.com/marathonpepe) │ [Twitter](http://twitter.com/marathonpepe) │ [Website](http://marathonpepe.dk)



# Support 🙏
This body runs on coffee and you can <a href="https://www.buymeacoffee.com/marathonpepe" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>



[img-ha-version]:https://img.shields.io/badge/Home_Assistant-0.100.2-53c1f1.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDEuMS8vRU4iICJodHRwOi8vd3d3LnczLm9yZy9HcmFwaGljcy9TVkcvMS4xL0RURC9zdmcxMS5kdGQiPjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxLjgsMTNIMjBWMjFIMTNWMTcuNjdMMTUuNzksMTQuODhMMTYuNSwxNUMxNy42NiwxNSAxOC42LDE0LjA2IDE4LjYsMTIuOUMxOC42LDExLjc0IDE3LjY2LDEwLjggMTYuNSwxMC44QTIuMSwyLjEgMCAwLDAgMTQuNCwxMi45TDE0LjUsMTMuNjFMMTMsMTUuMTNWOS42NUMxMy42Niw5LjI5IDE0LjEsOC42IDE0LjEsNy44QTIuMSwyLjEgMCAwLDAgMTIsNS43QTIuMSwyLjEgMCAwLDAgOS45LDcuOEM5LjksOC42IDEwLjM0LDkuMjkgMTEsOS42NVYxNS4xM0w5LjUsMTMuNjFMOS42LDEyLjlBMi4xLDIuMSAwIDAsMCA3LjUsMTAuOEEyLjEsMi4xIDAgMCwwIDUuNCwxMi45QTIuMSwyLjEgMCAwLDAgNy41LDE1TDguMjEsMTQuODhMMTEsMTcuNjdWMjFINFYxM0gyLjI1QzEuODMsMTMgMS40MiwxMyAxLjQyLDEyLjc5QzEuNDMsMTIuNTcgMS44NSwxMi4xNSAyLjI4LDExLjcyTDExLDNDMTEuMzMsMi42NyAxMS42NywyLjMzIDEyLDIuMzNDMTIuMzMsMi4zMyAxMi42NywyLjY3IDEzLDNMMTcsN1Y2SDE5VjlMMjEuNzgsMTEuNzhDMjIuMTgsMTIuMTggMjIuNTksMTIuNTkgMjIuNiwxMi44QzIyLjYsMTMgMjIuMiwxMyAyMS44LDEzTTcuNSwxMkEwLjksMC45IDAgMCwxIDguNCwxMi45QTAuOSwwLjkgMCAwLDEgNy41LDEzLjhBMC45LDAuOSAwIDAsMSA2LjYsMTIuOUEwLjksMC45IDAgMCwxIDcuNSwxMk0xNi41LDEyQzE3LDEyIDE3LjQsMTIuNCAxNy40LDEyLjlDMTcuNCwxMy40IDE3LDEzLjggMTYuNSwxMy44QTAuOSwwLjkgMCAwLDEgMTUuNiwxMi45QTAuOSwwLjkgMCAwLDEgMTYuNSwxMk0xMiw2LjlDMTIuNSw2LjkgMTIuOSw3LjMgMTIuOSw3LjhDMTIuOSw4LjMgMTIuNSw4LjcgMTIsOC43QzExLjUsOC43IDExLjEsOC4zIDExLjEsNy44QzExLjEsNy4zIDExLjUsNi45IDEyLDYuOVoiIGZpbGw9IiNmZmZmZmYiIC8+PC9zdmc+Cg==&maxAge=21600
[img-hassio]:https://img.shields.io/badge/config_for-Hass.io-53c1f1.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDEuMS8vRU4iICJodHRwOi8vd3d3LnczLm9yZy9HcmFwaGljcy9TVkcvMS4xL0RURC9zdmcxMS5kdGQiPjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEyLDE1LjVBMy41LDMuNSAwIDAsMSA4LjUsMTJBMy41LDMuNSAwIDAsMSAxMiw4LjVBMy41LDMuNSAwIDAsMSAxNS41LDEyQTMuNSwzLjUgMCAwLDEgMTIsMTUuNU0xOS40MywxMi45N0MxOS40NywxMi42NSAxOS41LDEyLjMzIDE5LjUsMTJDMTkuNSwxMS42NyAxOS40NywxMS4zNCAxOS40MywxMUwyMS41NCw5LjM3QzIxLjczLDkuMjIgMjEuNzgsOC45NSAyMS42Niw4LjczTDE5LjY2LDUuMjdDMTkuNTQsNS4wNSAxOS4yNyw0Ljk2IDE5LjA1LDUuMDVMMTYuNTYsNi4wNUMxNi4wNCw1LjY2IDE1LjUsNS4zMiAxNC44Nyw1LjA3TDE0LjUsMi40MkMxNC40NiwyLjE4IDE0LjI1LDIgMTQsMkgxMEM5Ljc1LDIgOS41NCwyLjE4IDkuNSwyLjQyTDkuMTMsNS4wN0M4LjUsNS4zMiA3Ljk2LDUuNjYgNy40NCw2LjA1TDQuOTUsNS4wNUM0LjczLDQuOTYgNC40Niw1LjA1IDQuMzQsNS4yN0wyLjM0LDguNzNDMi4yMSw4Ljk1IDIuMjcsOS4yMiAyLjQ2LDkuMzdMNC41NywxMUM0LjUzLDExLjM0IDQuNSwxMS42NyA0LjUsMTJDNC41LDEyLjMzIDQuNTMsMTIuNjUgNC41NywxMi45N0wyLjQ2LDE0LjYzQzIuMjcsMTQuNzggMi4yMSwxNS4wNSAyLjM0LDE1LjI3TDQuMzQsMTguNzNDNC40NiwxOC45NSA0LjczLDE5LjAzIDQuOTUsMTguOTVMNy40NCwxNy45NEM3Ljk2LDE4LjM0IDguNSwxOC42OCA5LjEzLDE4LjkzTDkuNSwyMS41OEM5LjU0LDIxLjgyIDkuNzUsMjIgMTAsMjJIMTRDMTQuMjUsMjIgMTQuNDYsMjEuODIgMTQuNSwyMS41OEwxNC44NywxOC45M0MxNS41LDE4LjY3IDE2LjA0LDE4LjM0IDE2LjU2LDE3Ljk0TDE5LjA1LDE4Ljk1QzE5LjI3LDE5LjAzIDE5LjU0LDE4Ljk1IDE5LjY2LDE4LjczTDIxLjY2LDE1LjI3QzIxLjc4LDE1LjA1IDIxLjczLDE0Ljc4IDIxLjU0LDE0LjYzTDE5LjQzLDEyLjk3WiIgZmlsbD0iI2ZmZmZmZiIgLz48L3N2Zz4K&maxAge=86400
[img-last-commit]:https://img.shields.io/github/last-commit/allanpersson/home-assistant-config/master
[img-license]:https://img.shields.io/github/license/allanpersson/home-assistant-config
[img-price]:https://img.shields.io/badge/price-FREE-53c1f1.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDEuMS8vRU4iICJodHRwOi8vd3d3LnczLm9yZy9HcmFwaGljcy9TVkcvMS4xL0RURC9zdmcxMS5kdGQiPjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTcsMTVIOUM5LDE2LjA4IDEwLjM3LDE3IDEyLDE3QzEzLjYzLDE3IDE1LDE2LjA4IDE1LDE1QzE1LDEzLjkgMTMuOTYsMTMuNSAxMS43NiwxMi45N0M5LjY0LDEyLjQ0IDcsMTEuNzggNyw5QzcsNy4yMSA4LjQ3LDUuNjkgMTAuNSw1LjE4VjNIMTMuNVY1LjE4QzE1LjUzLDUuNjkgMTcsNy4yMSAxNyw5SDE1QzE1LDcuOTIgMTMuNjMsNyAxMiw3QzEwLjM3LDcgOSw3LjkyIDksOUM5LDEwLjEgMTAuMDQsMTAuNSAxMi4yNCwxMS4wM0MxNC4zNiwxMS41NiAxNywxMi4yMiAxNywxNUMxNywxNi43OSAxNS41MywxOC4zMSAxMy41LDE4LjgyVjIxSDEwLjVWMTguODJDOC40NywxOC4zMSA3LDE2Ljc5IDcsMTVaIiBmaWxsPSIjZmZmIiAvPjwvc3ZnPgo=&maxAge=86400
[img-release]:https://img.shields.io/github/release/allanpersson/home-assistant-config/all.svg?logo=github&logoColor=white&maxAge=21600
[link-board]:https://github.com/allanpersson/home-assistant-config/projects/1
[link-ha-version]:https://github.com/home-assistant/home-assistant/tree/0.100.2
[link-hassio]:https://home-assistant.io/hassio/
[link-issues]:https://github.com/allanpersson/home-assistant-config/issues
[link-license]:https://github.com/allanpersson/home-assistant-config/blob/master/LICENSE.txt
[link-repo]:https://github.com/allanpersson/home-assistant-config
