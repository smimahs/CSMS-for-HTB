from datetime import datetime, timedelta

# Counting the overall delivered energy by subtraction start meter from stop meter
def Counting_overall_energy(meterStart, meterStop):
    try:
        return meterStop - meterStart
    except Exception as e:
        return e

# Calculating the duration time from start meter to stop
def Calculate_duration(timeStampStart, timeStampStop):
    try:
        timeStampStart = datetime.strptime(timeStampStart, "%Y-%m-%dT%H:%M:%SZ")
        d2timeStampStop = datetime.strptime(timeStampStop, "%Y-%m-%dT%H:%M:%SZ")

        # Get deltatime in seconds
        deltaTime = timedelta.total_seconds(timeStampStop-timeStampStart)
        return deltaTime
    except Exception as e:
        return e

def Counting_energy_price(energyFee,overallEnergy):
    try:
        return "{:,.3f}".format(overallEnergy * energyFee)
    except Exception as e:
        return e

def Counting_time_price(timeFee,durationTime):
    try:
        hoursTimeStamp = durationTime / 60.0
        return "{:,.3f}".format(hoursTimeStamp * timeFee)
    except Exception as e:
        return e

def Counting_transaction_price(transactionFee,transactions):
    try:
        return "{:,.3f}".format(transactions * transactionFee)
    except Exception as e:
        return e

def Calculate_overall_price(energyOverallPrice,timeOverallPrice,transactionFee):
    try:
        return "{:,.2f}".format(float(energyOverallPrice) + float(timeOverallPrice) + float(transactionFee))
    except Exception as e:
        return e

def Charging_process_rate(data):
    meter = data['crd']
    rate = data['rate']

    # Getting meter values retrieved from the electricity meter along with a timestamp are sent by the charging station to the CSM
    # Meters for StartTransaction
    # Meter value of the electricity meter when the charging process was started
    meterStart = meter['meterStart']
    # Timestamp (according to ISO 8601) when the charging process was started
    timeStampStart = meter['timeStampStart']

    # Meters for StopTransaction
    # Meter value of the electricity meter when the charging process was stopped
    meterStop = meter['meterStop']
    # Timestamp (according to ISO 8601) when the charging process was stopped
    timeStampStop = meter['timeStampStop']

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
