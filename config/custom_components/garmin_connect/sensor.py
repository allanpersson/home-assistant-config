import json
import logging
import requests
import re
from datetime import date
from datetime import timedelta

import voluptuous as vol

"""Platform for sensor integration."""
from homeassistant.const import (ATTR_SECONDS, LENGTH_METERS, CONF_USERNAME, CONF_PASSWORD)
from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import PLATFORM_SCHEMA


log = logging.getLogger(__name__)


PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_USERNAME): cv.string,
    vol.Required(CONF_PASSWORD): cv.string
})

SCAN_INTERVAL = timedelta(minutes=10)

def setup_platform(hass, config, add_entities, discovery_info=None):
    UN = config.get(CONF_USERNAME)
    PW = config.get(CONF_PASSWORD)
    add_entities([Garmin_Connect(UN, PW)])
    #return True


class Garmin_Connect(Entity):
    
    base_url = 'https://connect.garmin.com'
    sso_url = 'https://sso.garmin.com/sso'
    modern = base_url + '/modern'
    signin = sso_url + '/signin'
    url = modern + '/proxy/usersummary-service/usersummary/daily/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; https://github.com/andrewcooke/choochoo)',
        'origin': 'https://sso.garmin.com'
    }
    
    def __init__(self, UN, PW):
        """Initialize the sensor."""
        
        self._r = requests.session()
        self._log_response = True
        self.UN = UN
        self.PW = PW
        self._state = None
        self._unit = 'steps'
        self.login(self.UN, self.PW)
        
        self._attrs = {}
        self._name = "steps"

    @property
    def name(self):
        """Return the name of the sensor."""
        return "garmin_" + self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return self._unit
    
    @property
    def device_state_attributes(self):
        """Return attributes for sensor."""
        if self._state is None or self._attrs is None:
            return None

        attributes = {
            'userProfileId': self._attrs['userProfileId'],
            'totalKilocalories': self._attrs['totalKilocalories'],
            'activeKilocalories': self._attrs['activeKilocalories'],
            'bmrKilocalories': self._attrs['bmrKilocalories'],
            'wellnessKilocalories': self._attrs['wellnessKilocalories'],
            'burnedKilocalories': self._attrs['burnedKilocalories'],
            'consumedKilocalories': self._attrs['consumedKilocalories'],
            'remainingKilocalories': self._attrs['remainingKilocalories'],
            'netCalorieGoal': self._attrs['netCalorieGoal'],
            'totalDistanceMeters': self._attrs['totalDistanceMeters'],
            'wellnessDistanceMeters': self._attrs['wellnessDistanceMeters'],
            'wellnessActiveKilocalories': self._attrs['wellnessActiveKilocalories'],
            'netRemainingKilocalories': self._attrs['netRemainingKilocalories'],
            'userDailySummaryId': self._attrs['userDailySummaryId'],
            'calendarDate': self._attrs['calendarDate'],
            'rule': self._attrs['rule'],
            'uuid': self._attrs['uuid'],
            'dailyStepGoal': self._attrs['dailyStepGoal'],
            'wellnessStartTimeGmt': self._attrs['wellnessStartTimeGmt'],
            'wellnessStartTimeLocal': self._attrs['wellnessStartTimeLocal'],
            'wellnessEndTimeGmt': self._attrs['wellnessEndTimeGmt'],
            'wellnessEndTimeLocal': self._attrs['wellnessEndTimeLocal'],
            'durationInMilliseconds': self._attrs['durationInMilliseconds'],
            'wellnessDescription': self._attrs['wellnessDescription'],
            'highlyActiveSeconds': self._attrs['highlyActiveSeconds'],
            'activeSeconds': self._attrs['activeSeconds'],
            'sedentarySeconds': self._attrs['sedentarySeconds'],
            'sleepingSeconds': self._attrs['sleepingSeconds'],
            'includesWellnessData': self._attrs['includesWellnessData'],
            'includesActivityData': self._attrs['includesActivityData'],
            'includesCalorieConsumedData': self._attrs['includesCalorieConsumedData'],
            'privacyProtected': self._attrs['privacyProtected'],
            'moderateIntensityMinutes': self._attrs['moderateIntensityMinutes'],
            'vigorousIntensityMinutes': self._attrs['vigorousIntensityMinutes'],
            'floorsAscendedInMeters': self._attrs['floorsAscendedInMeters'],
            'floorsDescendedInMeters': self._attrs['floorsDescendedInMeters'],
            'floorsAscended': self._attrs['floorsAscended'],
            'floorsDescended': self._attrs['floorsDescended'],
            'intensityMinutesGoal': self._attrs['intensityMinutesGoal'],
            'userFloorsAscendedGoal': self._attrs['userFloorsAscendedGoal'],
            'minHeartRate': self._attrs['minHeartRate'],
            'maxHeartRate': self._attrs['maxHeartRate'],
            'restingHeartRate': self._attrs['restingHeartRate'],
            'lastSevenDaysAvgRestingHeartRate': self._attrs['lastSevenDaysAvgRestingHeartRate'],
            'source': self._attrs['source'],
            'averageStressLevel': self._attrs['averageStressLevel'],
            'maxStressLevel': self._attrs['maxStressLevel'],
            'stressDuration': self._attrs['stressDuration'],
            'restStressDuration': self._attrs['restStressDuration'],
            'activityStressDuration': self._attrs['activityStressDuration'],
            'uncategorizedStressDuration': self._attrs['uncategorizedStressDuration'],
            'totalStressDuration': self._attrs['totalStressDuration'],
            'lowStressDuration': self._attrs['lowStressDuration'],
            'mediumStressDuration': self._attrs['mediumStressDuration'],
            'highStressDuration': self._attrs['highStressDuration'],
            'stressPercentage': self._attrs['stressPercentage'],
            'restStressPercentage': self._attrs['restStressPercentage'],
            'activityStressPercentage': self._attrs['activityStressPercentage'],
            'uncategorizedStressPercentage': self._attrs['uncategorizedStressPercentage'],
            'lowStressPercentage': self._attrs['lowStressPercentage'],
            'mediumStressPercentage': self._attrs['mediumStressPercentage'],
            'highStressPercentage': self._attrs['highStressPercentage'],
            'stressQualifier': self._attrs['stressQualifier'],
            'measurableAwakeDuration': self._attrs['measurableAwakeDuration'],
            'measurableAsleepDuration': self._attrs['measurableAsleepDuration'],
            'lastSyncTimestampGMT': self._attrs['lastSyncTimestampGMT'],
            'minAvgHeartRate': self._attrs['minAvgHeartRate'],
            'maxAvgHeartRate': self._attrs['maxAvgHeartRate'],
            'bodyBatteryChargedValue': self._attrs['bodyBatteryChargedValue'],
            'bodyBatteryDrainedValue': self._attrs['bodyBatteryDrainedValue'],
            'bodyBatteryHighestValue': self._attrs['bodyBatteryHighestValue'],
            'bodyBatteryLowestValue': self._attrs['bodyBatteryLowestValue'],
            'bodyBatteryMostRecentValue': self._attrs['bodyBatteryMostRecentValue'],
            'abnormalHeartRateAlertsCount': self._attrs['abnormalHeartRateAlertsCount'],
            'averageSpo2': self._attrs['averageSpo2'],
            'lowestSpo2': self._attrs['lowestSpo2'],
            'latestSpo2': self._attrs['latestSpo2'],
            'latestSpo2ReadingTimeGmt': self._attrs['latestSpo2ReadingTimeGmt'],
            'latestSpo2ReadingTimeLocal': self._attrs['latestSpo2ReadingTimeLocal'],
            'averageMonitoringEnvironmentAltitude': self._attrs['averageMonitoringEnvironmentAltitude']
        }
        
        if self._attrs['privacyProtected'] == True:
            self.login(self.UN, self.PW)
            

##        if not self._include_offpeak:
##            attributes['offpeak_usage'] = self._attrs['usage_offpeak']

        return attributes
     
    def update(self):
        log.info('[GARMIN Connect] Updating data')
        response = self.get_stats()
        log.debug(response)
        self._attrs = response
        self._state = response["totalSteps"]

    # Python script to get Garmin Statistics
    # based on the work of Benjamin Blau - https://github.com/benniblau/GarminConnectActivityExport
    # 2019-08-31

    ### lean Python 3 script to export Garmin actitvities to JSON or CSV file
    ### based on code from Andre Cooke (https://github.com/andrewcooke) https://github.com/andrewcooke/choochoo/blob/master/ch2/fit/download/connect.py
    ### logic and data from https://github.com/tcgoetz/GarminDB/blob/master/download_garmin.py
    ###updated to the recent Garmin API specification
    ### added features to export JSON and CSV
    ### 2019-08-18

    def login(self, username, password):

        log.info('Connecting to Garmin Connect as %s' % username)

        params = {
            'webhost': self.base_url,
            'service': self.modern,
            'source': self.signin,
            'redirectAfterAccountLoginUrl': self.modern,
            'redirectAfterAccountCreationUrl': self.modern,
            'gauthHost': self.sso_url,
            'locale': 'en_US',
            'id': 'gauth-widget',
            'cssUrl': 'https://static.garmincdn.com/com.garmin.connect/ui/css/gauth-custom-v1.2-min.css',
            'clientId': 'GarminConnect',
            'rememberMeShown': 'true',
            'rememberMeChecked': 'false',
            'createAccountShown': 'true',
            'openCreateAccount': 'false',
            'usernameShown': 'false',
            'displayNameShown': 'false',
            'consumeServiceTicket': 'false',
            'initialFocus': 'true',
            'embedWidget': 'false',
            'generateExtraServiceTicket': 'false'
        }

        response = self._log_r(self._r.get(self.signin, headers=self.headers, params=params))
        response.raise_for_status()

        data = {
            'username': username,
            'password': password,
            'embed': 'true',
            'lt': 'e1s1',
            '_eventId': 'submit',
            'displayNameRequired': 'false'
        }

        response = self._log_r(self._r.post(self.signin, headers=self.headers, params=params, data=data))
        response.raise_for_status()

        response_url = re.search(r'"(https:[^"]+?ticket=[^"]+)"', response.text)
        if not response_url:
            log.debug(response.text)
            raise Exception('Could not find response URL')
        response_url = re.sub(r'\\', '', response_url.group(1))
        log.debug('Response URL: %s' % response_url)

        response = self._log_r(self._r.get(response_url))

        self.user_prefs = self.__get_json(response.text, 'VIEWER_USERPREFERENCES')
        self.display_name = self.user_prefs['displayName']
        self.social_profile = self.__get_json(response.text, 'VIEWER_SOCIAL_PROFILE')
        self.full_name = self.social_profile['fullName']
        response.raise_for_status()

    def _log_r(self, response):
        if self._log_response:
            log.debug('headers: %s' % response.headers)
            log.debug('reason: %s' % response.reason)
            log.debug('cookies: %s' % response.cookies)
            log.debug('history: %s' % response.history)
        return response


    def __get_json(self, page_html, key):
         found = re.search(key + r" = JSON.parse\(\"(.*)\"\);", page_html, re.M)
         if found:
             json_text = found.group(1).replace('\\"', '"')
             return json.loads(json_text)
        
    def get_stats(self): # retrieve stats
        today = str(date.today())
        getURL = self.url + self.display_name + '?' + 'calendarDate=' + today
        response = self._log_r(self._r.get(getURL, headers=self.headers))
        log.info('[GARMIN Connect] Retrieving GARMIN json data stream ') # from ' + getURL )
        response.raise_for_status()
        return(response.json())
