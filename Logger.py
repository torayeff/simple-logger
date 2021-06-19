import json
import time
import os


class Logger:
    def __init__(self, id, category):
        self.logId = id
        self.category = category
        self.fName = f"logs/log-{self.logId}-{self.category}.json"
        self.logData = []

    def log(self, info, save=False):
        """Logs info."""
        timestamp = time.time()
        self.logData.append(
            {
                "id": f"{self.logId}-{self.category}-{timestamp}",
                "timestamp": timestamp,
                "info": info,
            }
        )

        if save:
            self.save()

    def save(self):
        # create logs directory if not exists
        if not os.path.exists("logs"):
            os.mkdir("logs")
            
        # check whether file already exists
        if not os.path.exists(self.fName):
            with open(self.fName, "w") as f:
                json.dump(self.logData, f, indent="\t")
        else:
            # this part can be and should be improved
            # for handling large logs

            with open(self.fName, "r") as f:
                # read previously stored data
                allData = json.load(f)

            allData.extend(self.logData)
            with open(self.fName, "w") as f:
                json.dump(allData, f, indent="\t")
