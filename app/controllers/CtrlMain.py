from app.database.mysqlConn import mysqlConn
import os
import json
import time

class CtrlMain:
    config = json.load( open('./config.json'))
    auth = config['auth']
    
    conn = mysqlConn(config["database"])

    def snowflake(self):
        # Get current timestamp
        if "snowflake" in os.environ:
            last_timestamp = int(os.environ["snowflake"])
        else:
            last_timestamp = -1 
        timestamp = int(time.time() * 1000) - self.config["snowflake"]["EPOCH"]
        
        # Handle clock drift by waiting until the next millisecond
        if timestamp < last_timestamp:
            time.sleep((last_timestamp - timestamp) / 1000.0)
            timestamp = int(time.time() * 1000) - self.config["snowflake"]["EPOCH"]
        
        # Reset sequence if we moved to a new millisecond
        if timestamp == last_timestamp:
            sequence = (sequence + 1) % (1 << self.config["snowflake"]["SEQUENCE_BITS"])
            if sequence == 0:
                # Wait until the next millisecond
                while timestamp <= last_timestamp:
                    timestamp = int(time.time() * 1000) - self.config["snowflake"]["EPOCH"]
        else:
            sequence = 0
        
        os.environ["snowflake"] = str(timestamp)
        
        # Generate Snowflake ID
        snowflake_id = (timestamp << (self.config["snowflake"]["NODE_ID_BITS"] + self.config["snowflake"]["SEQUENCE_BITS"])) | (self.config["snowflake"]["SERVER"] << self.config["snowflake"]["SEQUENCE_BITS"]) | sequence
        return hex(snowflake_id)[2:]

    def kerberos(self,id):
        path = self.auth["path"]
        #validar base de datos
        if (os.path.exists(path+"/"+str(id)+".json")):
            return True
        else:
            return False