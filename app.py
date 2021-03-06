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

# Calculating the total energy price from start meter to stop based on energeFee
def Counting_energy_price(energyFee,overallEnergy):
    try:
        # convert Wh to kWh
        return float("{:.3f}".format((overallEnergy/1000) * energyFee))
    except Exception as e:
        return str(e)

# Calculating the total time price from start meter to stop based on timeFee
def Counting_time_price(timeFee,durationTime):
    try:
        # convert second to hour
        hoursTimeStamp = durationTime / 3600
        return float("{:.3f}".format(hoursTimeStamp * timeFee))
    except Exception as e:
        return str(e)

# Calculating the total transaction price from start meter to stop based on transactionFee
def Counting_transaction_price(transactionFee,transactions):
    try:
        return float("{:.3f}".format(transactions * transactionFee))
    except Exception as e:
        return str(e)

# Calculating the overall price from start meter to stop based on Fees
def Calculate_overall_price(energyOverallPrice,timeOverallPrice,transactionFee):
    try:
        return float("{:.2f}".format(float(energyOverallPrice) + float(timeOverallPrice) + float(transactionFee)))
    except Exception as e:
        return str(e)

def Charging_process_rate(data):
    # Getting meter values retrieved from the electricity meter along with a timestamp are sent by the charging station to the CSM
    try:
        meter = data['cdr']
        # convert string to json
        meter = meter.replace("\'", "\"")
        meter = json.loads(meter)
    except Exception as e:
        return str("The input value in incorrect")
    
    # Meters for StartTransaction
    # Meter value of the electricity meter when the charging process was started
    meterStart = float(meter['meterStart'])
    # Timestamp (according to ISO 8601) when the charging process was started
    timeStampStart = meter['timestampStart']

    # Meters for StopTransaction
    # Meter value of the electricity meter when the charging process was stopped
    meterStop = float(meter['meterStop'])
    # Timestamp (according to ISO 8601) when the charging process was stopped
    timeStampStop = meter['timestampStop']

    # Getting Rating values
    try:
        rate = data['rate']
        # convert string to json
        rate = rate.replace("\'", "\"")
        rate = json.loads(rate)
    except Exception as e:
        return str("The input value in incorrect")

    # Rate the charging process based on the energy consumed
    energyFee = float(rate['energy'])
    # Rate the charging process based on its duration
    timeFee = float(rate['time'])
    # Fees per charging process
    transactionFee = float(rate['transaction'])

    # Counting the overall delivered energy
    overallEnergy = Counting_overall_energy(meterStart, meterStop)

    # Counting the duration time from start meter to stop
    durationTime = Calculate_duration(timeStampStart, timeStampStop)
    
    # Calculate energy overall price based on energy fee and overall energy
    energyOverallPrice = Counting_energy_price(energyFee,overallEnergy)

    # Calculate time overall price based on time fee and duration time
    timeOverallPrice = Counting_time_price(timeFee,durationTime)

    # Calculate transaction overall price based on transaction fee and transaction counts
    transactionOverallPrice = Counting_transaction_price(transactionFee,len(meter))

    # Sum of energy, time, and transaction price
    overallPrice = Calculate_overall_price(energyOverallPrice,timeOverallPrice,transactionFee)

    # Send correct result form to server
    result = {'overall':overallPrice,
    'components':{'energy':energyOverallPrice,'time':timeOverallPrice,'transaction':transactionFee}}

    return result