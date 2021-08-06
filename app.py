from datetime import datetime, timedelta
import json

# Counting the overall delivered energy by subtraction start meter from stop meter
def Counting_overall_energy(meterStart, meterStop):
    try:
        return meterStop - meterStart
    except Exception as e:
        return str(e)

# Calculating the duration time from start meter to stop
def Calculate_duration(timeStampStart, timeStampStop):
    try:
        start = datetime.strptime(str(timeStampStart), "%Y-%m-%dT%H:%M:%SZ")
        stop = datetime.strptime(str(timeStampStop), "%Y-%m-%dT%H:%M:%SZ")

        # Get deltatime in seconds
        deltaTime = timedelta.total_seconds(stop-start)
        return float(deltaTime)
    except Exception as e:
        return str(e)

def Counting_energy_price(energyFee,overallEnergy):
    try:
        return float("{:.3f}".format((overallEnergy/1000) * energyFee))
    except Exception as e:
        return str(e)

def Counting_time_price(timeFee,durationTime):
    try:
        hoursTimeStamp = durationTime / 3600
        return float("{:.3f}".format(hoursTimeStamp * timeFee))
    except Exception as e:
        return str(e)

def Counting_transaction_price(transactionFee,transactions):
    try:
        return float("{:.3f}".format(transactions * transactionFee))
    except Exception as e:
        return str(e)

def Calculate_overall_price(energyOverallPrice,timeOverallPrice,transactionFee):
    try:
        return "{:.2f}".format(float(energyOverallPrice) + float(timeOverallPrice) + float(transactionFee))
    except Exception as e:
        return str(e)

def Charging_process_rate(data):
    try:
        meter = data['cdr']
        meter = meter.replace("\'", "\"")
        meter = json.loads(meter)
    except Exception as e:
        return str(e)

    try:
        rate = data['rate']
        rate = rate.replace("\'", "\"")
        rate = json.loads(rate)
    except Exception as e:
        return str(e)
    #rate = json.loads(rate)
    
    # Getting meter values retrieved from the electricity meter along with a timestamp are sent by the charging station to the CSM
    # Meters for StartTransaction
    # Meter value of the electricity meter when the charging process was started
    meterStart = meter['meterStart']
    # Timestamp (according to ISO 8601) when the charging process was started
    timeStampStart = meter['timestampStart']

    # Meters for StopTransaction
    # Meter value of the electricity meter when the charging process was stopped
    meterStop = meter['meterStop']
    # Timestamp (according to ISO 8601) when the charging process was stopped
    timeStampStop = meter['timestampStop']

    # Getting Rating values
    # Rate the charging process based on the energy consumed
    energyFee = rate['energy']
    # Rate the charging process based on its duration
    timeFee = rate['time']
    # Fees per charging process
    transactionFee = rate['transaction']

    # Counting the overall delivered energy
    overallEnergy = Counting_overall_energy(meterStart, meterStop)

    # Counting the duration time from start meter to stop
    durationTime = Calculate_duration(timeStampStart, timeStampStop)
    
    energyOverallPrice = Counting_energy_price(energyFee,overallEnergy)

    timeOverallPrice = Counting_time_price(timeFee,durationTime)

    transactionOverallPrice = Counting_transaction_price(transactionFee,len(meter))

    overallPrice = Calculate_overall_price(energyOverallPrice,timeOverallPrice,transactionFee)

    result = {'overall':overallPrice,
    'components':{'energy':energyOverallPrice,'time':timeOverallPrice,'transaction':transactionFee}}

    return result