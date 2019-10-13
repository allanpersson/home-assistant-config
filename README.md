# Pepe's Home Assistant Config
This is my [Home Assistant](https://github.com/home-assistant) configuration for inspiration.


![Image](https://github.com/allanpersson/home-assistant-config/blob/master/www/images/themes/material_dark_theme_custom_preview.png)
The theme on the image is [Material Dark Theme - Pepe Version](https://github.com/allanpersson/home-assistant-config/blob/master/themes/material_dark_theme_custom.yaml) with some minor tweaks made by me like rounded corners, color changes etc.

## Lovelace card configuration
Add the following code to your lovelace configuration, and insert your own entities.

```yaml
# Example "stue" lovelace view
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

# Device list
List of all the devices i use on [Home Assistant](https://github.com/home-assistant), and information about if i have automations build around the device.

| Brand | Model | Automations |
| --------- | ----------- | ----------- |
| Google | Home | Yes |
| Google | Home Hub | Yes |
| Google | Home Mini | Yes |
| Huawei | Mediapad T3 | ? |
| Ikea | Fyrtur | Yes |
| Raspberry | Pi Zero W | ? |
| Xiaomi | Dafang | ? |
| Xiaomi | Roborock S50 | Yes |

Updating! The list is incomplete...


# Credits
Thanks to [Frenck](https://github.com/frenck) for config inspiration, and for your hard work and effort to the [Home Assistant](https://github.com/home-assistant) community.

# Contact
Fell free to follow and/or contact me on:
[Facebook](http://facebook.com/marathonpepe) │ [Instagram](http://instagram.com/marathonpepe) │ [Twitter](http://twitter.com/marathonpepe) │ [Website](http://marathonpepe.dk)

# Support
This body runs on coffee and you can <a href="https://www.buymeacoffee.com/marathonpepe" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
