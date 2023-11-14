

# AMF TOOLS Python Librairie

## Description

AMF TOOLS Python Librairie is a python librairie to control AMF products (RVMFS, RVMLP, SPM and LSPOne) with a serial connection protocole.

## Installation

### Requirements

- Python 3.6 or higher
- pyserial 3.4 or higher
- ftd2xx 1.1.2 or higher

currently only tested on Windows 11 with Python 3.11 an update will be made to test on other OS

### Installation with pip

```bash
pip install AMFTools
```

### Installation from source

```bash
git clone
cd AMFTools
python setup.py install
```
## License

This Librairie is proprietary software of **Advanced Microfluidics S.A**. It is distributed under a proprietary license.

This Librairie is free to use for Advanced Microfluidics SA customers. It is not free to use for non-customers of Advanced Microfluidics SA.

If you have any questions about the license, please contact Advanced Microfluidics SA : 
- Chem. de la Dent d'Oche 1A, 1024 Ecublens (Switzerland)
- +41 21 552 14 30
- info@amf.ch

## Usage

### Import

```python
import amfTools
```


## Class AMF(): 

### General Methods:

```python
__init__(self, product : Object, autoconect : bool = True, portnumber: int = None, syringeVolume : int = None, productAdress : int = 1, type : str = None, serialBaudrate : int = None) -> None

```
Initialize the AMF object. Either serialPort, serialNumber or a Device type object must be specified as product.


```python
connect(self, serialBaudrate : int = serialBaudrate, serialTimeout : float = serialTimeout) -> bool
```
Connect to the product. If the connection is successful, return True, otherwise return False.

```python
disconnect(self) -> None
```
Disconnect from the product

```python
send(self, command : str, integer : bool = False, force_aws : bool = False) -> None
```
Send a command to the product. If the command is successful, return the response of the product. If integer is True, the response will be converted to an integer. If force_aws is True, the product will be temporary set to wait for an answer even if it is set to not wait for an answer.

```python
receive(self, integer=False, full=False, float = False) -> str
```
Receive a line of response from the product. If integer is True, the response will be converted to an integer. If full is True, the response will be returned as is, without removing the first and last character. If float is True, the response will be converted to a float.

```python
prepareCommand(self, command : str, parameter : int = None) -> str
```
Prepare a command to be sent to the product. If the command needs a parameter, it must be specified. The parameter must be an integer.

```python
pullAndWait(self, homming_mode : bool = False) -> None
```
Wait until the valve and the pump are not busy.

### LIST OF SET FUNCTION


```python
setAdress(self, adress : int) -> None
```
Set the adress of the product. The adress must be between 1 and 9. (1 by default)

```python
setSyringeSize(self, size : int) -> None
```
Set the syringe size of the product. The size must be between 0 and 5000 ( $\mu l$ ). 

```python
setAnswerMode(self, mode : int) -> None
```
Set the answer mode of the product. The mode must be between 0 and 2. 0: synchronous, 1: Asynchronous, 2: same as asynchronous but add number of subcommand processed in its last answer

```python
setPortNumber(self, portnumber : int = portnumber) -> None
```
Set the port number of the product's valves.

```python
setSpeedVolume(self, speed : float, syringeVolume: int = syringeSize) -> int
```
Set the speed of the product. The speed must be positive. The syringe volume must be between 0 and 5000  ( $\mu l$ ).

```python
setSpeed(self, speed : int) -> None
```
Set the speed of the product. The speed must be between 0 and 6000 (pulse/sec).

```python
setSpeedCode(self, speed : int) -> None
```
Set the speed of the product with a code. The speed must be between 0 and 50.

```python
setAcelerationRate(self, rate : int) -> None
```
Set the aceleration rate of the product. The rate must be between 1 and 59590. 

```python
setDecelerationRate(self, rate : int) -> None
```
Set the deceleration rate of the product. The rate must be between 1 and 59590.

```python
setMicrostepResolution(self, argument : int) -> None
```
Set the microstep resolution of the product. ( 0: 0.01mm resolution/step, 1: 0.00125mm resolution/step )

```python
setSlowMode(self) -> None
```
Set the slow mode of the product.

```python
setFastMode(self) -> None
```
Set the fast mode of the product.

```python
setPumpStrenghAndHome(self, strengh : int, block : bool = True) -> None
```
Set the pump strengh and home the pump. The strengh must be between 0 and 3. If block is True, the function will wait until the pump is not busy.

```python
setPlungerForce(self, force : int) -> None
```
Set the plunger force of the product. The force must be between 0 and 3.

```python
setNoAwser(self) -> None
```
Set the product to not wait for an answer. (if the product is set to not wait for an answer, it will not send any answer even if you force it with force_aws parameters)


### LIST OF GET FUNCTION

```python
getSerialPort(self, serialNumber : str = serialNumber) -> str
```
Find the serial port of the product with the specified serial number

```python
getSerialNumber(self, serialPort = serialPort) -> str
```
Get the serial number of the product

```python
getType(self) -> None
```
Autoset the type of the product (SPM, RVMFS or RVMLP)
 
```python
getPortNumber(self) -> int
```
Get the number of port of the product's valve

```python
getCurrentStatus(self) -> str
```
Get the current status of the product

```python
getValvePosition(self) -> int
```
Get the valve position of the product

```python
getRealPlungerPosition(self) -> int:
```
Get the real plunger position of the product

```python
getPlungerPosition(self) -> int
```
Get the plunger position of the product

```python
getNumberValveMovements(self) -> int
```
Get the number of valve movements of the product

```python
getNumberValveMovementsSinceLastReport(self) -> int
```
Get the number of valve movements since last report of the product

```python
getSpeedMode(self) -> str
```
Get the speed mode of the product

```python
getFirmwareChecksum(self) -> str
```
Get the firmware checksum of the product

```python
getFirmwareVersion(self) -> str
```
Get the firmware version of the product

```python
getValveAdress(self) -> int
```
Get the valve adress of the product

```python
getValveConfiguration(self) -> int
```
Get the valve configuration of the product

```python
getMicrostepResolution(self) -> int
```
Get the microstep resolution of the product

```python
getPlungerCurrent(self) -> int
```
Get the plunger current of the product

```python
getAnswerMode(self) -> str
```
Get the answer mode of the product

```python
getAcceleration(self) -> int
```
Get the acceleration of the product

```python
getDeceleration(self) -> int
```
Get the deceleration of the product

```python
getSuplyVoltage(self) -> float
```
Get the suply voltage of the product

```python
getUniqueID(self) -> str
```
Get the unique ID of the product

```python
getValveStatus(self) -> int
```
Get the valve status of the product

```python
getPumpStatus(self) -> int
```
Get the pump status of the product

```python
getHomeStatus(self) -> bool
```
Get the home status of the product (False: not homed, True: homed)

```python
getDeviceInformation(self) -> object
```
Get all the information of the product

### GLOBAL ACTION FUNCTION

```python
checkValveStatus(self) -> None
```
Check the valve status of the product

```python
checkPumpStatus(self) -> None
```
Check the pump status of the product

```python
sendBrute(self, command : str, blocked : bool = True, force_aws : bool = False) -> None
```
Send a command to the product. If blocked is True, the function will wait until the product is not busy. If force_aws is True, the function will ask for an answer even if the product is set to not wait for an answer.

```python
internalReset(self) -> None
```
Reset the product

```python
executeLastCommand(self) -> None
```
Execute the last command of the product

```python
delay(self, delay : int) -> None
```
Delay the product. The delay must be positive.

```python
home(self, block= True) -> None
```
Home the product. If block is True, the function will wait until the product is not busy.

```python
valveShortestPath(self, target: int, enforced : bool = False, block : bool = True) -> None
```
Move the valve to the target port with the shortest path. The target must be between 1 and the number of port of the product. If enforced is True, the valve will move to the target port with the shortest path even if it is not the shortest path. If block is True, the function will wait until the product is not busy.

```python	
valveIncrementalMoov(self, target: int, enforced : bool = False, block : bool = True) -> None
```
Move the valve to the target port with an incremental moov. The target must be between 1 and the number of port of the product. If enforced is True, the valve will move even if they are already on the target point (1 complete rotation). If block is True, the function will wait until the product is not busy.

```python
valveClockwiseMoov(self, target: int, enforced : bool = False, block : bool = True) -> None
```
Move the valve to the target port with an incremental moov. The target must be between 1 and the number of port of the product. If enforced is True, the valve will move even if they are already on the target point (1 complete rotation). If block is True, the function will wait until the product is not busy.

```python
valveDecrementalMoov(self, target: int, enforced : bool = False, block : bool = True) -> None
```
Move the valve to the target port with a decremental moov. The target must be between 1 and the number of port of the product. If enforced is True, the valve will move even if they are already on the target point (1 complete rotation). If block is True, the function will wait until the product is not busy.

```python
valveCounterClockwiseMoov(self, target: int, enforced : bool = False, block : bool = True) -> None
```
Move the valve to the target port with a decremental moov. The target must be between 1 and the number of port of the product. If enforced is True, the valve will move even if they are already on the target point (1 complete rotation). If block is True, the function will wait until the product is not busy.

```python
valveMoov(self, target: int, mode:int = 0, enforced = False, block : bool = True) -> None
```
Move the valve to the target port. The target must be between 1 and the number of port of the product. The mode must be between 0 and 2. 0: ShortestPath, 1: IncrementalMoov, 2: DecrementalMoov. If enforced is True, the valve will move even if they are already on the target point (1 complete rotation). If block is True, the function will wait until the product is not busy.

```python
hardStop(self) -> None
```
Stop the product (imediate stop of the valve and the pump)

```python
powerOff(self) -> None
```
Power off the product

### PUMP ACTION FUNCTION

```python
pumpAbsolutePosition(self, position : int, block : bool = True) -> None
```
Move the pump to the specified position. The position must be between 0 and 3000 (or 24000). If block is True, the function will wait until the product is not busy.

```python
pump(self, position : int, block : bool = True)
```
Move the pump to the specified position. The position must be between 0 and 3000 (or 24000). If block is True, the function will wait until the product is not busy.

```python
pumpVolume(self, volume : int, syringeVolume: int = syringeSize, block : bool = True) -> None
```
Move the pump to the specified volume. The volume must be between 0 and 5000 ( $\mu l$ ). If syringeVolume is specified, it will be used as the syringe volume. If block is True, the function will wait until the product is not busy.

```python
pumpRelativePickup(self, position : int, block : bool = True) -> None
```
Move the pump to the specified relative position. The position must be between 0 and 3000 (or 24000). If block is True, the function will wait until the product is not busy.

```python
pumpPickup(self, position : int, block : bool = True)
```
Move the pump to the specified relative position. The position must be between 0 and 3000 (or 24000). If block is True, the function will wait until the product is not busy.

```python
pumpPickupVolume(self, volume : int, syringeVolume: int = syringeSize, block : bool = True) -> None
```
Move the pump to the specified relative volume. The volume must be between 0 and 5000 ( $\mu l$ ). If syringeVolume is specified, it will be used as the syringe volume. If block is True, the function will wait until the product is not busy.

```python
pumpRelativeDispense(self, position : int, block : bool = True) -> None
```
Move the pump to the specified relative position. The position must be between 0 and 3000 (or 24000). If block is True, the function will wait until the product is not busy.

```python
pumpDispense(self, position : int, block : bool = True)
```
Move the pump to the specified relative position. The position must be between 0 and 3000 (or 24000). If block is True, the function will wait until the product is not busy.

```python
pumpDispenseVolume(self, volume : int, syringeVolume: int = syringeSize, block : bool = True) -> None
```
Move the pump to the specified relative volume. The volume must be between 0 and 5000 ( $\mu l$ ). If syringeVolume is specified, it will be used as the syringe volume. If block is True, the function will wait until the product is not busy.

## Class Device():

### Atributes:
```python	
SerialNumber : str = None
ComPort : str = None
DeviceType : str = None
```

str method return exemple : 
"Device RVMFS on port com3 with serial number P201-O0000xxxx"

## Class utile():
```python
getProductList(specified_type = None) -> list:
```
Return a list of Device object. If specified_type is specified, only the Device object with the specified type will be returned.