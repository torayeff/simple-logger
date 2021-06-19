from Logger import Logger


if __name__ == "__main__":
    weightLogger = Logger(id="some_id_1", category="Health")
    
    weightLogger.log({
        "weight": 75.30
    })

    weightLogger.log({
        "weight": 75.10
    })

    weightLogger.log({
        "weight": 75.00
    })

    weightLogger.log({
        "weight": 74.75
    })

    # save
    weightLogger.save()

    # you can also save directly
    # this might be inefficient for big data logging
    # but safe for ensuring persistency
    weightLogger.log({
        "weight": 74.20
    }, save=True)

    # PhD logger
    phdLogger = Logger(id="my_awesome_id2", category="PhD")
    phdLogger.log({
        "activity": "Reading papers",
        "duration": "45min"
    })
    phdLogger.log({
        "activity": "Lab Experiment",
        "duration": "120mins"
    })
    phdLogger.save()