<h1 align="center">
  🏰<br/>Home Assistant configuration for making my life easier... Hopefully 🙈<br/> <sup><sub>by <a href="http://marathonpepe.dk">Allan Persson</a> 😈</sub></sup>
</h1>

[![Price][img-price]][link-license]
[![License][img-license]][link-license]
[![Home Assistant version][img-ha-version]][link-ha-version]
[![Hass.io][img-hassio]][link-hassio]
<a href="https://www.buymeacoffee.com/marathonpepe" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 10px !important;width: 40px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

Configuration for [Home Assistant](https://home-assistant.io/) running [Hass.io](https://home-assistant.io/hassio/) on a [INTEL® NUC KIT NUC8I3BEK](https://www.intel.com/content/www/us/en/products/boards-kits/nuc/kits/nuc8i3bek.html) for a two bedroom apartment (66m2).

![Image](https://github.com/allanpersson/home-assistant-config/blob/master/www/images/themes/material_dark_theme_custom_preview.png)
The theme on the image is [Material Dark Theme - Pepe Version](https://github.com/allanpersson/home-assistant-config/blob/master/themes/material_dark_theme_custom.yaml) with some minor tweaks made by me like rounded corners, color changes etc.

# Devices & Automations

<a name="devices"></a>
<div align="center">
  <h4>
    <a href="https://github.com/allanpersson/home-assistant-config#climate">
      Climate
    </a>
    <span> | </span>
    <a href="https://github.com/allanpersson/home-assistant-config#lights">
      Lights
    </a>
    <span> | </span>
    <a href="https://github.com/allanpersson/home-assistant-config#mediaplayers">
      Mediaplayers
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


#### Mediaplayers <a name="mediaplayers" href="https://github.com/allanpersson/Home-AssistantConfig#devices"><img align="right" border="0" src="https://cdn.pixabay.com/photo/2016/09/05/10/50/app-1646212_960_720.png" width="20" ></a>
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

</td><td align="center"><img border="0" <img align="center" border="0" src="https://lh3.googleusercontent.com/igThvoKwToXtZOfTANWbgp2ZoLnPBV2KDt9oJuaK419yIHQIo24eIcsCbgWcnfwlFjs=w1000" width="140" ></a>
</td><td align="center"><img border="0" <img align="center" border="0" src="https://azcd.harveynorman.com.au/media/catalog/product/cache/21/image/992x558/9df78eab33525d08d6e5fb8d27136e95/g/h/ghh-rc2.jpg" width="140" ></a>
</td><td align="center"><img border="0" <img align="center" border="0" src="https://www.mytrendyphone.dk/images2/Google-Home-Mini-Smart-Speaker-Chalk-11052018-04-p.jpg" width="140" ></a>
</td><td align="center"><img border="0" <img align="center" border="0" src="https://cdn.webshopapp.com/shops/76048/files/220339352/harman-kardon-citation-300.jpg" width="140" ></a>

<tr><td colspan="4">

</td></tr>
<tr><td align="center">

[Huawei Mediapad T3 10](https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_osacat%3D0%26_odkw%3Dxiaomi%2Bmi%2Bbox%2Bs%26_from%3DR40%26_trksid%3Dp2334524.m570.l1313.TR11.TRC1.A0.H0.Xhuawei%2Bmediapad%2Bt3.TRS0%26_nkw%3Dhuawei%2Bmediapad%2Bt3%26_sacat%3D0&campid=5338610312&toolid=20008)
</td><td align="center">

[Xiaomi Mi Box S](https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_osacat%3D0%26_odkw%3DHarman%2BKardon%2BCitation%2B300%26_from%3DR40%26_trksid%3Dp2334524.m570.l1313.TR12.TRC2.A0.H0.Xxiaomi%2Bmi%2Bbox%2Bs.TRS0%26_nkw%3Dxiaomi%2Bmi%2Bbox%2Bs%26_sacat%3D0&campid=5338610312&toolid=20008)
</td></tr>

</td><td align="center"><img border="0" <img align="center" border="0" src="https://consumer-img.huawei.com/content/dam/huawei-cbg-site/cee-nordics/dk/mkt/pdp/tablets/mediapad-t3-10/mediapad-t3-10-dimage-0212-original.jpg" width="140" ></a>
</td><td align="center"><img border="0" <img align="center" border="0" src="https://upload.wikimedia.org/wikipedia/commons/d/d1/Xiaomi_Mi_Box_S.jpg" width="140" ></a>

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
<summary>Roll down Ikea Fyrtur when Kodi is 'on'.</summary><p align="center">
<a href=https://github.com/allanpersson/home-assistant-config/blob/master/automations/areas/stuen/cover_kodi.yaml>
Roll down Ikea Fyrtur when Kodi is 'on' - /automations/areas/stuen/cover_kodi.yaml</a><br>
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


#### Vacuums <a name="vacuums" href="https://github.com/allanpersson/Home-AssistantConfig#devices"><img align="right" border="0" src="https://cdn.pixabay.com/photo/2016/09/05/10/50/app-1646212_960_720.png" width="20" ></a>
</td></tr>
<tr><td align="center">

[Xiaomi Roborock S50](https://rover.ebay.com/rover/1/710-53481-19255-0/1?mpre=https%3A%2F%2Fwww.ebay.co.uk%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dp2380057.m570.l1313.TR11.TRC1.A0.H0.Xxiaomi%2Broborock%2Bs50.TRS0%26_nkw%3Dxiaomi%2Broborock%2Bs50%26_sacat%3D0&campid=5338610312&toolid=20008)
</td></tr>

</td><td align="center"><img border="0" <img align="center" border="0" src="https://sc02.alicdn.com/kf/HTB11hAzm0fJ8KJjy0Feq6xKEXXaQ/Global-Version-XIAOMI-Roborock-S50-MI-Robot.jpg_350x350.jpg" width="140" ></a>

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

</table>
</p>

## Lovelace card configuration
Add the following code to your lovelace configuration, and insert your own entities.

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

# Credits
Thanks to:
- [Ccostan](https://github.com/CCOSTAN/) for documentation inspiration.
- [Frenck](https://github.com/frenck/) for config inspiration, and for your hard work and effort to the [Home Assistant](https://github.com/home-assistant) community.
- [Renemarc](https://github.com/renemarc/) for documentation inspiration.

# Contact
Fell free to follow and/or contact me on:
[Facebook](http://facebook.com/marathonpepe) │ [Instagram](http://instagram.com/marathonpepe) │ [Twitter](http://twitter.com/marathonpepe) │ [Website](http://marathonpepe.dk)

# Support
This body runs on coffee and you can <a href="https://www.buymeacoffee.com/marathonpepe" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>


[img-ha-version]:https://img.shields.io/badge/Home_Assistant-0.100.2-53c1f1.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDEuMS8vRU4iICJodHRwOi8vd3d3LnczLm9yZy9HcmFwaGljcy9TVkcvMS4xL0RURC9zdmcxMS5kdGQiPjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxLjgsMTNIMjBWMjFIMTNWMTcuNjdMMTUuNzksMTQuODhMMTYuNSwxNUMxNy42NiwxNSAxOC42LDE0LjA2IDE4LjYsMTIuOUMxOC42LDExLjc0IDE3LjY2LDEwLjggMTYuNSwxMC44QTIuMSwyLjEgMCAwLDAgMTQuNCwxMi45TDE0LjUsMTMuNjFMMTMsMTUuMTNWOS42NUMxMy42Niw5LjI5IDE0LjEsOC42IDE0LjEsNy44QTIuMSwyLjEgMCAwLDAgMTIsNS43QTIuMSwyLjEgMCAwLDAgOS45LDcuOEM5LjksOC42IDEwLjM0LDkuMjkgMTEsOS42NVYxNS4xM0w5LjUsMTMuNjFMOS42LDEyLjlBMi4xLDIuMSAwIDAsMCA3LjUsMTAuOEEyLjEsMi4xIDAgMCwwIDUuNCwxMi45QTIuMSwyLjEgMCAwLDAgNy41LDE1TDguMjEsMTQuODhMMTEsMTcuNjdWMjFINFYxM0gyLjI1QzEuODMsMTMgMS40MiwxMyAxLjQyLDEyLjc5QzEuNDMsMTIuNTcgMS44NSwxMi4xNSAyLjI4LDExLjcyTDExLDNDMTEuMzMsMi42NyAxMS42NywyLjMzIDEyLDIuMzNDMTIuMzMsMi4zMyAxMi42NywyLjY3IDEzLDNMMTcsN1Y2SDE5VjlMMjEuNzgsMTEuNzhDMjIuMTgsMTIuMTggMjIuNTksMTIuNTkgMjIuNiwxMi44QzIyLjYsMTMgMjIuMiwxMyAyMS44LDEzTTcuNSwxMkEwLjksMC45IDAgMCwxIDguNCwxMi45QTAuOSwwLjkgMCAwLDEgNy41LDEzLjhBMC45LDAuOSAwIDAsMSA2LjYsMTIuOUEwLjksMC45IDAgMCwxIDcuNSwxMk0xNi41LDEyQzE3LDEyIDE3LjQsMTIuNCAxNy40LDEyLjlDMTcuNCwxMy40IDE3LDEzLjggMTYuNSwxMy44QTAuOSwwLjkgMCAwLDEgMTUuNiwxMi45QTAuOSwwLjkgMCAwLDEgMTYuNSwxMk0xMiw2LjlDMTIuNSw2LjkgMTIuOSw3LjMgMTIuOSw3LjhDMTIuOSw4LjMgMTIuNSw4LjcgMTIsOC43QzExLjUsOC43IDExLjEsOC4zIDExLjEsNy44QzExLjEsNy4zIDExLjUsNi45IDEyLDYuOVoiIGZpbGw9IiNmZmZmZmYiIC8+PC9zdmc+Cg==&maxAge=21600
[img-hassio]:https://img.shields.io/badge/config_for-Hass.io-53c1f1.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDEuMS8vRU4iICJodHRwOi8vd3d3LnczLm9yZy9HcmFwaGljcy9TVkcvMS4xL0RURC9zdmcxMS5kdGQiPjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEyLDE1LjVBMy41LDMuNSAwIDAsMSA4LjUsMTJBMy41LDMuNSAwIDAsMSAxMiw4LjVBMy41LDMuNSAwIDAsMSAxNS41LDEyQTMuNSwzLjUgMCAwLDEgMTIsMTUuNU0xOS40MywxMi45N0MxOS40NywxMi42NSAxOS41LDEyLjMzIDE5LjUsMTJDMTkuNSwxMS42NyAxOS40NywxMS4zNCAxOS40MywxMUwyMS41NCw5LjM3QzIxLjczLDkuMjIgMjEuNzgsOC45NSAyMS42Niw4LjczTDE5LjY2LDUuMjdDMTkuNTQsNS4wNSAxOS4yNyw0Ljk2IDE5LjA1LDUuMDVMMTYuNTYsNi4wNUMxNi4wNCw1LjY2IDE1LjUsNS4zMiAxNC44Nyw1LjA3TDE0LjUsMi40MkMxNC40NiwyLjE4IDE0LjI1LDIgMTQsMkgxMEM5Ljc1LDIgOS41NCwyLjE4IDkuNSwyLjQyTDkuMTMsNS4wN0M4LjUsNS4zMiA3Ljk2LDUuNjYgNy40NCw2LjA1TDQuOTUsNS4wNUM0LjczLDQuOTYgNC40Niw1LjA1IDQuMzQsNS4yN0wyLjM0LDguNzNDMi4yMSw4Ljk1IDIuMjcsOS4yMiAyLjQ2LDkuMzdMNC41NywxMUM0LjUzLDExLjM0IDQuNSwxMS42NyA0LjUsMTJDNC41LDEyLjMzIDQuNTMsMTIuNjUgNC41NywxMi45N0wyLjQ2LDE0LjYzQzIuMjcsMTQuNzggMi4yMSwxNS4wNSAyLjM0LDE1LjI3TDQuMzQsMTguNzNDNC40NiwxOC45NSA0LjczLDE5LjAzIDQuOTUsMTguOTVMNy40NCwxNy45NEM3Ljk2LDE4LjM0IDguNSwxOC42OCA5LjEzLDE4LjkzTDkuNSwyMS41OEM5LjU0LDIxLjgyIDkuNzUsMjIgMTAsMjJIMTRDMTQuMjUsMjIgMTQuNDYsMjEuODIgMTQuNSwyMS41OEwxNC44NywxOC45M0MxNS41LDE4LjY3IDE2LjA0LDE4LjM0IDE2LjU2LDE3Ljk0TDE5LjA1LDE4Ljk1QzE5LjI3LDE5LjAzIDE5LjU0LDE4Ljk1IDE5LjY2LDE4LjczTDIxLjY2LDE1LjI3QzIxLjc4LDE1LjA1IDIxLjczLDE0Ljc4IDIxLjU0LDE0LjYzTDE5LjQzLDEyLjk3WiIgZmlsbD0iI2ZmZmZmZiIgLz48L3N2Zz4K&maxAge=86400
[img-license]:https://img.shields.io/github/license/allanpersson/home-assistant-config.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDEuMS8vRU4iICJodHRwOi8vd3d3LnczLm9yZy9HcmFwaGljcy9TVkcvMS4xL0RURC9zdmcxMS5kdGQiPjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE3LjgsMjBDMTcuNCwyMS4yIDE2LjMsMjIgMTUsMjJINUMzLjMsMjIgMiwyMC43IDIsMTlWMThINUwxNC4yLDE4QzE0LjYsMTkuMiAxNS43LDIwIDE3LDIwSDE3LjhNMTksMkMyMC43LDIgMjIsMy4zIDIyLDVWNkgyMFY1QzIwLDQuNCAxOS42LDQgMTksNEMxOC40LDQgMTgsNC40IDE4LDVWMThIMTdDMTYuNCwxOCAxNiwxNy42IDE2LDE3VjE2SDVWNUM1LDMuMyA2LjMsMiA4LDJIMTlNOCw2VjhIMTVWNkg4TTgsMTBWMTJIMTRWMTBIOFoiIGZpbGw9IiNmZmZmZmYiIC8+PC9zdmc+Cg==&maxAge=86400
[img-price]:https://img.shields.io/badge/price-FREE-53c1f1.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDEuMS8vRU4iICJodHRwOi8vd3d3LnczLm9yZy9HcmFwaGljcy9TVkcvMS4xL0RURC9zdmcxMS5kdGQiPjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTcsMTVIOUM5LDE2LjA4IDEwLjM3LDE3IDEyLDE3QzEzLjYzLDE3IDE1LDE2LjA4IDE1LDE1QzE1LDEzLjkgMTMuOTYsMTMuNSAxMS43NiwxMi45N0M5LjY0LDEyLjQ0IDcsMTEuNzggNyw5QzcsNy4yMSA4LjQ3LDUuNjkgMTAuNSw1LjE4VjNIMTMuNVY1LjE4QzE1LjUzLDUuNjkgMTcsNy4yMSAxNyw5SDE1QzE1LDcuOTIgMTMuNjMsNyAxMiw3QzEwLjM3LDcgOSw3LjkyIDksOUM5LDEwLjEgMTAuMDQsMTAuNSAxMi4yNCwxMS4wM0MxNC4zNiwxMS41NiAxNywxMi4yMiAxNywxNUMxNywxNi43OSAxNS41MywxOC4zMSAxMy41LDE4LjgyVjIxSDEwLjVWMTguODJDOC40NywxOC4zMSA3LDE2Ljc5IDcsMTVaIiBmaWxsPSIjZmZmIiAvPjwvc3ZnPgo=&maxAge=86400
[img-release]:https://img.shields.io/github/release/allanpersson/home-assistant-config/all.svg?logo=github&logoColor=white&maxAge=21600
[link-board]:https://github.com/allanpersson/home-assistant-config/projects/1
[link-ha-version]:https://github.com/home-assistant/home-assistant/tree/0.100.2
[link-hassio]:https://home-assistant.io/hassio/
[link-issues]:https://github.com/allanpersson/home-assistant-config/issues
[link-license]:LICENSE.txt
