# In this dict the keys are the lanes, and the values are the list of lanes that a box has to pass
# through before reaching it.
box_paths = {"S001.M003.02.01": [], "S001.M003.02.02": [], "S001.M003.02.03": [],
             "S001.M004.01.01": ["S001.M007.01.03"], "S001.M004.01.02": ["S001.M007.01.01"],
             "S001.M004.02.01": ["S001.M007.01.04"], "S001.M004.02.02": ["S001.M007.01.02"],
             "S001.M004.03.01": ["S001.M007.02.03"], "S001.M004.03.02": ["S001.M007.02.01"],
             "S001.M004.04.01": ["S001.M007.02.04"], "S001.M004.04.02": ["S001.M007.02.02"],
             "S001.M005.01.01": ["S001.M003.02.03"], "S001.M005.01.02": ["S001.M003.02.03"],
             "S001.M005.01.03": ["S001.M003.02.01"],
             "S001.M005.02.01": ["S001.M003.02.03"], "S001.M005.02.02": ["S001.M003.02.03"],
             "S001.M005.03.01": ["S001.M003.02.03"], "S001.M005.03.02": ["S001.M003.02.03"],
             "S001.M005.03.03": ["S001.M003.02.02"],
             "S001.M005.04.01": ["S001.M003.02.03"], "S001.M005.04.02": ["S001.M003.02.03"],
             "S001.M006.01.01": ["S001.M007.01.04", "S001.M004.02.01"],
             "S001.M006.01.02": ["S001.M007.02.04", "S001.M004.04.01"],
             "S001.M006.01.03": ["S001.M007.02.03", "S001.M004.03.01"],
             "S001.M006.01.04": ["S001.M003.02.02", "S001.M005.03.03"],
             "S001.M006.01.05": ["S001.M007.01.03", "S001.M004.01.01"],
             "S001.M006.02.01": ["S001.M007.01.02", "S001.M004.02.02"],
             "S001.M006.02.02": ["S001.M007.02.02", "S001.M004.04.02"],
             "S001.M006.02.03": ["S001.M007.02.01", "S001.M004.03.02"],
             "S001.M006.02.04": ["S001.M003.02.01", "S001.M005.01.03"],
             "S001.M006.02.05": ["S001.M007.01.01", "S001.M004.01.02"],
             "S001.M007.01.01": [], "S001.M007.01.02": [], "S001.M007.01.03": [], "S001.M007.01.04": [],
             "S001.M007.02.01": [], "S001.M007.02.02": [], "S001.M007.02.03": [], "S001.M007.02.04": []}

# Define dicts of lanes for each inventory with the number of boxes they should contain:
Lager_Fertigung = {"S001.M003.02.01": 0, "S001.M003.02.02": 2, "S001.M003.02.03": 2}
SM_Lieferung = {"S001.M004.01.01": 3, "S001.M004.01.02": 4, "S001.M004.02.01": 4, "S001.M004.02.02": 3,
                "S001.M004.03.01": 3, "S001.M004.03.02": 4, "S001.M004.04.01": 4, "S001.M004.04.02": 3}
SM_Fertigung = {"S001.M005.01.01": 3, "S001.M005.01.02": 2, "S001.M005.01.03": 4,
                "S001.M005.02.01": 3, "S001.M005.02.02": 4,
                "S001.M005.03.01": 4, "S001.M005.03.02": 2, "S001.M005.03.03": 4,
                "S001.M005.04.01": 4, "S001.M005.04.02": 4}
SM_Montage = {"S001.M006.01.01": 2, "S001.M006.01.02": 3, "S001.M006.01.03": 3,
              "S001.M006.01.04": 2, "S001.M006.01.05": 3,
              "S001.M006.02.01": 2, "S001.M006.02.02": 2, "S001.M006.02.03": 2,
              "S001.M006.02.04": 3, "S001.M006.02.05": 2}
Zentral_Lager = {"S001.M007.01.01": 3, "S001.M007.01.02": 3, "S001.M007.01.03": 3, "S001.M007.01.04": 5,
                 "S001.M007.02.01": 3, "S001.M007.02.02": 5, "S001.M007.02.03": 2, "S001.M007.02.04": 3}


def generate_kafka_messages(lane, number_of_boxes, file):
    path_size = len(box_paths[lane])
    # For each prior lane, we require a put event followed by a pick event
    for prior_lane in box_paths[lane]:
        for i in range(number_of_boxes):
            # Write all put events into the lane
            file.write('[29/Oct/2023 0' + str(1 + box_paths[lane].index(prior_lane)) + f':00:0{i}] "DEBUG" ' +
                       '"ils_event_consumer" "KAFKA | RECEIVED | ' +
                       '[topic=organisation_events_1091c573-df2b-44e3-8755-64c8a09cebcc] | ' +
                       '[content={"header":{"traceId":"54b850b1-b646-4ef8-b8d6-817a3dc319bc",' +
                       '"id":"625505b6-24c8-4326-a96d-4ef5ffde3511",' +
                       '"organisationId":"b6c197fa-c1d2-43ec-930f-57daf8c7aa9b",' +
                       '"timestamp":"2023-10-13T14:23:47.355603218Z"},"body":{"action":{"carrier":{"laneAddress":"' +
                       prior_lane + '","carrierActionType":"CARRIER_ACTION_PUT","locationType":"LOCATION_SECONDARY",' +
                       '"carrierId":"9502b9cf-1833-a7cd-b3a6-646e05e26239","currentCount":2}}}}]"')
            file.write("\n")

        for i in range(number_of_boxes):
            # Write all pick events from the lane
            file.write('[29/Oct/2023 0' + str(1 + box_paths[lane].index(prior_lane)) + f':30:0{i}] "DEBUG" ' +
                       '"ils_event_consumer" "KAFKA | RECEIVED | ' +
                       '[topic=organisation_events_1091c573-df2b-44e3-8755-64c8a09cebcc] | ' +
                       '[content={"header":{"traceId":"54b850b1-b646-4ef8-b8d6-817a3dc319bc",' +
                       '"id":"625505b6-24c8-4326-a96d-4ef5ffde3511",' +
                       '"organisationId":"b6c197fa-c1d2-43ec-930f-57daf8c7aa9b",' +
                       '"timestamp":"2023-10-13T14:23:47.355603218Z"},"body":{"action":{"carrier":{"laneAddress":"' +
                       prior_lane + '","carrierActionType":"CARRIER_ACTION_PICK","locationType":"LOCATION_SECONDARY",' +
                       '"carrierId":"9502b9cf-1833-a7cd-b3a6-646e05e26239","currentCount":2}}}}]"')
            file.write("\n")

    # Conclude with all put events at the destination lane
    for i in range(number_of_boxes):
        file.write('[29/Oct/2023 0' + str(1 + path_size) + f':00:0{i}] "DEBUG" ' +
                   '"ils_event_consumer" "KAFKA | RECEIVED | ' +
                   '[topic=organisation_events_1091c573-df2b-44e3-8755-64c8a09cebcc] | ' +
                   '[content={"header":{"traceId":"54b850b1-b646-4ef8-b8d6-817a3dc319bc",' +
                   '"id":"625505b6-24c8-4326-a96d-4ef5ffde3511",' +
                   '"organisationId":"b6c197fa-c1d2-43ec-930f-57daf8c7aa9b",' +
                   '"timestamp":"2023-10-13T14:23:47.355603218Z"},"body":{"action":{"carrier":{"laneAddress":"' +
                   lane + '","carrierActionType":"CARRIER_ACTION_PUT","locationType":"LOCATION_SECONDARY",' +
                   '"carrierId":"9502b9cf-1833-a7cd-b3a6-646e05e26239","currentCount":2}}}}]"')
        file.write("\n")


# Create the file
with open("initialize_inventory.txt", "w") as file:
    # Initialize Montage first (3-lane-long paths)
    for lane in SM_Montage:
        generate_kafka_messages(lane, SM_Montage[lane], file)
    # Initialize SM_Lieferung and SM_Fertigung (2-lane-long paths)
    for lane in SM_Lieferung:
        generate_kafka_messages(lane, SM_Lieferung[lane], file)
    for lane in SM_Fertigung:
        generate_kafka_messages(lane, SM_Fertigung[lane], file)
    # Initialize Lager_Fertigung and Zentral_Lager (1-lane-long paths)
    for lane in Lager_Fertigung:
        generate_kafka_messages(lane, Lager_Fertigung[lane], file)
    for lane in Zentral_Lager:
        generate_kafka_messages(lane, Zentral_Lager[lane], file)

print("Done.")
