# POLYBOT Tools
This is a collection of tools that run on PolyBot.

External Temp Sensor - measure, save, publish on MQTT  and dweet from 1-wire temp sensor

a 10 min record is kept by appending to a file named "poly_temp.txt"
The Error count is a poormans version fo detecting problems with your internet connection.  it trips when the dweet API call fails.

poly_temp.py is the basic form of measure, save, dweet
poly_temp_mqqt.py adds the mqtt publishing capability. all servers hard coded in to the scripts.  future update would be a config file.  But, this is just a 'collection' of tools. :)
