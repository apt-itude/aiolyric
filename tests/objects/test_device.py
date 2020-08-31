"""
Generated by generator/generator.py - 2020-08-31 14:06:02.854691
"""
from aiolyric.objects.device import AIOLyricDevice
from tests.responses.device_fixtrue import device_fixtrue_response

def test_device(device_fixtrue_response):
    obj = AIOLyricDevice(device_fixtrue_response)
    assert obj.displayedOutdoorHumidity == device_fixtrue_response['displayedOutdoorHumidity']
    assert obj.vacationHold.enabled == device_fixtrue_response['vacationHold']['enabled']
    assert obj.currentSchedulePeriod.day == device_fixtrue_response['currentSchedulePeriod']['day']
    assert obj.currentSchedulePeriod.period == device_fixtrue_response['currentSchedulePeriod']['period']
    assert obj.scheduleCapabilities.availableScheduleTypes[0] == device_fixtrue_response['scheduleCapabilities']['availableScheduleTypes'][0]
    assert obj.scheduleCapabilities.schedulableFan == device_fixtrue_response['scheduleCapabilities']['schedulableFan']
    assert obj.scheduleType.scheduleType == device_fixtrue_response['scheduleType']['scheduleType']
    assert obj.scheduleType.scheduleSubType == device_fixtrue_response['scheduleType']['scheduleSubType']
    assert obj.scheduleStatus == device_fixtrue_response['scheduleStatus']
    assert obj.allowedTimeIncrements == device_fixtrue_response['allowedTimeIncrements']
    assert obj.settings.hardwareSettings.brightness == device_fixtrue_response['settings']['hardwareSettings']['brightness']
    assert obj.settings.hardwareSettings.maxBrightness == device_fixtrue_response['settings']['hardwareSettings']['maxBrightness']
    assert obj.settings.temperatureMode.air == device_fixtrue_response['settings']['temperatureMode']['air']
    assert obj.settings.devicePairingEnabled == device_fixtrue_response['settings']['devicePairingEnabled']
    assert obj.deviceClass == device_fixtrue_response['deviceClass']
    assert obj.deviceType == device_fixtrue_response['deviceType']
    assert obj.deviceID == device_fixtrue_response['deviceID']
    assert obj.name == device_fixtrue_response['name']
    assert obj.isAlive == device_fixtrue_response['isAlive']
    assert obj.isUpgrading == device_fixtrue_response['isUpgrading']
    assert obj.isProvisioned == device_fixtrue_response['isProvisioned']
    assert obj.macID == device_fixtrue_response['macID']
    assert obj.service.mode == device_fixtrue_response['service']['mode']
    assert obj.deviceRegistrationDate == device_fixtrue_response['deviceRegistrationDate']
    assert obj.dataSyncStatus == device_fixtrue_response['dataSyncStatus']
    assert obj.units == device_fixtrue_response['units']
    assert obj.indoorTemperature == device_fixtrue_response['indoorTemperature']
    assert obj.outdoorTemperature == device_fixtrue_response['outdoorTemperature']
    assert obj.allowedModes[0] == device_fixtrue_response['allowedModes'][0]
    assert obj.deadband == device_fixtrue_response['deadband']
    assert obj.hasDualSetpointStatus == device_fixtrue_response['hasDualSetpointStatus']
    assert obj.minHeatSetpoint == device_fixtrue_response['minHeatSetpoint']
    assert obj.maxHeatSetpoint == device_fixtrue_response['maxHeatSetpoint']
    assert obj.minCoolSetpoint == device_fixtrue_response['minCoolSetpoint']
    assert obj.maxCoolSetpoint == device_fixtrue_response['maxCoolSetpoint']
    assert obj.changeableValues.mode == device_fixtrue_response['changeableValues']['mode']
    assert obj.changeableValues.heatSetpoint == device_fixtrue_response['changeableValues']['heatSetpoint']
    assert obj.changeableValues.coolSetpoint == device_fixtrue_response['changeableValues']['coolSetpoint']
    assert obj.changeableValues.thermostatSetpointStatus == device_fixtrue_response['changeableValues']['thermostatSetpointStatus']
    assert obj.changeableValues.nextPeriodTime == device_fixtrue_response['changeableValues']['nextPeriodTime']
    assert obj.changeableValues.heatCoolMode == device_fixtrue_response['changeableValues']['heatCoolMode']
    assert obj.changeableValues.endHeatSetpoint == device_fixtrue_response['changeableValues']['endHeatSetpoint']
    assert obj.changeableValues.endCoolSetpoint == device_fixtrue_response['changeableValues']['endCoolSetpoint']
    assert obj.operationStatus.mode == device_fixtrue_response['operationStatus']['mode']
    assert obj.operationStatus.fanRequest == device_fixtrue_response['operationStatus']['fanRequest']
    assert obj.operationStatus.circulationFanRequest == device_fixtrue_response['operationStatus']['circulationFanRequest']
    assert obj.deviceModel == device_fixtrue_response['deviceModel']